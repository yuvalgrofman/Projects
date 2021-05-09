from Show import Show 
from Database import Database
import DatabaseWatch
import os

myApiKey = os.environ.get('SHOW_APIKEY')

def getShowsFromUser():
    return input("Which shows do you watch? (Write a \",\" between each show)").split(',')

def main():

    shows = getShowsFromUser()
    showDB = Database("shows")
    showDB.clearDatabase()

    for show in shows:
        showDB.addShow(show, 'tv', myApiKey)
   
    print(showDB.getAllShows())
    DatabaseWatch.startWatch("shows", "17:11")

if __name__ == '__main__': 
    main()