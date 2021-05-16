import sqlite3
from time import thread_time
from tkinter import ttk
from tkinter import *
from Show import Show 
from Database import Database
import os
from DatabaseWatch import *
from tkinter import messagebox as msg
from functools import partial
import _thread
from random import randint
from ttkthemes import *

class ShowsGui:
    '''ShowsGui

        This class is a GUI which accesses a database, 
        Allows it to  

    '''

    def __init__(self, databaseName = 'shows.db'):

        self.myApiKey = os.environ.get('SHOW_APIKEY')
        self.databaseRecords = None 

        self.name = databaseName

        # themes = ['adapta', 'aquativo', 'arc', 'black', 'blue', 'breeze', 'clearlooks', 'elegance', 'equilux', 'itft1', 'keramik', 'kroc', 'plastik', 'radiance', 'scidblue','scidgreen', 'scidgrey', 'scidmint', 'scidpink','scidpurple', 'scidsand', 'smog', 'ubuntu', 'winxpblue', 'yaru']
        # self.theme = themes[randint(0, len(themes) - 1)]
        # print(self.theme)

        self.theme = 'arc'

        self.frame = ThemedTk(theme = self.theme)
        self.frame.title("My Shows Database")
        self.frame.geometry("315x170")

        # self.style = ttk.Style() 
        # print(self.style.theme_names())
        # self.style.theme_use(self.theme)

        self.frame.style = ttk.Style()
        self.frame.style.configure('TButton', background = 'red')
        self.frame.style.configure('TButton', foreground = 'grey')

        self.database = Database(databaseName)
        self.createGui()    

        msg.showinfo("Explanation", "Add each show you watch to this database.\nIt will send you an email on a daily basis that contains info, \non which shows air today or tommorrow. \nTo see whats in the Database click show Records")

        self.startWatch()

    def startGui(self):
        self.frame.mainloop()

    def createGui(self):

        #Create name entry
        self.showNameEntry = ttk.Entry(self.frame, width = 30)
        self.showNameEntry.grid(row = 0, column = 1)

        #Create label for Entry
        self.showNameLabel = ttk.Label(self.frame, text = "Enter Show")
        self.showNameLabel.grid(row = 0, column = 0)
        
        #Create submit button 
        self.submitButton = ttk.Button(self.frame, text = "Add Show", command = self.addShow)
        self.submitButton.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 104)

        #Create query button 
        self.queryButton = ttk.Button(self.frame, text = "Show Records", command = self.showRecords)
        self.queryButton.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 98)
        
        #Create send reminder button 
        self.sendReminderButton = ttk.Button(self.frame, text = 'Send Reminder', command = self.sendReminder)
        self.sendReminderButton.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 96)
        

    def sendReminder(self):
        checkDatabase(self.database)

    def startWatch(self):
        _thread.start_new_thread(startWatch, (self.name, '12:01'))


    def addShow(self):

        try: 

            self.database.addShow(self.showNameEntry.get(), 'tv', self.myApiKey)
            
        except: 
            msg.showinfo(title = 'No results', message = 'No Results Found')
            
        self.showNameEntry.delete(0,END)

        if self.databaseRecords != None: 
            self.refreshShowRecords()

    def showRecords(self):

        self.databaseRecords = ThemedTk(theme = self.theme)
        self.databaseRecords.geometry("650x200") 

        # self.databaseRecords.style = ttk.Style()
        # self.databaseRecords.style.configure('TButton', background = 'red')
        # self.databaseRecords.style.configure('TButton', foreground = 'grey')

        self.refreshShowRecords()

        self.databaseRecords.mainloop()

    def refreshShowRecords(self):

        for widget in self.databaseRecords.winfo_children():
            widget.destroy()

        columns = self.database.getColumnNames()
        shows = self.database.getAllShows()

        colNum = 0

        for column in columns:
            widget = ttk.Entry(self.databaseRecords, width = 10, foreground = 'black')
            widget.grid(row = 0, column = colNum + 1)
            widget.insert(END, column)
            widget.configure(state = 'readonly')
            colNum += 1

        widget = ttk.Button(self.databaseRecords,text = 'Clear Database', width = 10, command = self.clearDatabase)
        widget.grid(row = 0, column = colNum + 1)
            
        row = 1 # row value inside the loop 

        for show in shows: 
            for col in range(len(show) + 2):

                if col == 0:
                    widget = ttk.Entry(self.databaseRecords, width=3, foreground = 'grey') 
                    widget.grid(row = row, column = col) 
                    widget.insert(END, str(row))
                    widget.configure(state = 'readonly')

                elif col < len(show) + 1:
                    widget = ttk.Entry(self.databaseRecords, width=10, foreground='blue') 
                    widget.grid(row = row, column = col) 
                    widget.insert(END, str(show[col - 1]))
                    widget.configure(state = 'readonly')
                
                else: 
                    widget = ttk.Button(self.databaseRecords, text='Del Row',command = partial(self.removeShow, show[0])) 
                    widget.grid(row = row, column = col)

            row = row + 1

        self.databaseRecords.mainloop()


    def removeShow(self, name):

        shouldDel = msg.askyesno("Delete ?","Delete " + str(name) + '?' , icon = 'warning' , default = 'no')

        if shouldDel: # True if yes button is clicked

            self.database.deleteShow(name, 'tv', self.myApiKey)

            self.refreshShowRecords()
    
    def clearDatabase(self):
        shouldDel = msg.askyesno("Delete ?","Delete ALL?", icon = 'warning' , default = 'no')

        if shouldDel: # True if yes button is clicked

            self.database.clearDatabase()
            self.refreshShowRecords()


def main():
    gui = ShowsGui('showsOne')
    gui.startGui()

if __name__ == '__main__':
    main()