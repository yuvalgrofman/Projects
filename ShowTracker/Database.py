import sqlite3
from Show import Show
import os


class Database:
    '''Database'''

    def __init__(self, filename):
        try:         
            self.createDatabase(filename)
        except: 
            print("An error has occurred")

    def createDatabase(self, filename):

        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()

    def createShowTable(self):
        try: 
            self.cursor.execute("""CREATE TABLE shows (
                name text, 
                numSeasons int, 
                numEpisodes int, 
                releaseDate text, 
                isAiring int,
                nextEpisodeReleaseDate text,
                nextEpName text)  
                    """)
            self.conn.commit()

        except (sqlite3.OperationalError):
            print("Table Already exists")

    def addShowByInstance(self, show):

        self.cursor.execute("INSERT INTO shows VALUES (:name, :numSeasons, :numEpisodes, :releaseDate, :isAiring, :nextEpisodeReleaseDate, :nextEpName)",
                            {'name' : show.name, 'numSeasons' : show.numSeasons, 'numEpisodes' : show.numEpisodes, 'releaseDate' : show.releaseDate,
                             'isAiring' : show.isAiring, 'nextEpisodeReleaseDate' : show.nextEpisodeReleaseDate, 'nextEpName' : show.nextEpName})

        self.conn.commit()

    def addShow(self, name, isTv, api_key):
        show = Show(name, isTv, api_key)
        self.addShowByInstance(show)


    def updateShow(self, show):
        show.updateData()
        with self.conn:
            self.cursor.execute("""UPDATE shows SET nextEpisodeReleaseDate = :nextEpisodeReleaseDate, isAiring = :isAiring, nextEpName = :nextEpName 
                            WHERE name = :name AND releaseDate = :releaseDate""", 
                            {'nextEpisodeReleaseDate' : show.nextEpisodeReleaseDate, 'isAiring' : show.isAiring, 'name' : show.name, 'releaseDate' : show.releaseDate, 'nextEpName' : show.nextEpName})

    def deleteShowByInstance(self, show):
        self.cursor.execute("DELETE FROM shows WHERE name = :name AND numEpisodes = :numEpisodes AND releaseDate = :releaseDate", {'name' : show.name, 'numEpisodes' : show.numEpisodes, 'releaseDate' : show.releaseDate})
        self.conn.commit()

    def clearDatabase(self):
        self.cursor.execute("DELETE FROM shows")
        self.conn.commit()

    def deleteShow(self, name, isTv, api_key):
        show = Show(name, isTv, api_key) 
        self.deleteShowByInstance(show)

    def getShowsByInstance(self, show):
        self.cursor.execute("SELECT DISTINCT * FROM shows WHERE name=:name", {'name' : show.name})
        return self.cursor.fetchall()

    def getShowsByName(self, name):
        self.cursor.execute("SELECT DISTINCT * FROM shows WHERE name=:name", {'name' : name})
        return self.cursor.fetchall()

    def getShowsByDate(self, nextEpisodeReleaseDate):
        self.cursor.execute("SELECT DISTINCT * FROM shows WHERE nextEpisodeReleaseDate=:nextEpisodeReleaseDate AND isAiring=1", {'nextEpisodeReleaseDate' : nextEpisodeReleaseDate})
        return self.cursor.fetchall()

    def getAllShows(self):
        self.cursor.execute("SELECT DISTINCT * FROM shows")
        return self.cursor.fetchall()


def main():
    myApiKey = os.environ.get('SHOW_APIKEY')
    showsDatabase = Database("shows")
    showsDatabase.createShowTable()
    showsDatabase.clearDatabase()
    showOne = Show("My Hero Academia", 'tv', myApiKey)
    showsDatabase.addShowByInstance(showOne)
    print(showsDatabase.getAllShows())

if __name__ == '__main__': 
    main()