import requests
import os

# myApiKey = os.environ.get('SHOW_APIKEY')

class Show:
    '''Class that represents a show which will be stored in a Database 
        Class Variables: 
        
        name,
        NumSeasons,
        NumEpisodes, 
        ReleaseDate, 
        isAiring, 
        NextEpisodesReleaseDate, 
        (Maybe more)
    
    '''


    def __init__(self, *args):

        if len(args) == 3:
            name = args[0]
            isShowOrMovie = args[1]
            api_key = args[2]

            self.name = name 
            self.name.replace(" ", "+")
            self.isShowOrMovie = isShowOrMovie
            self.api_key = api_key

            self.releaseDate = None
            self.numSeasons = None
            self.numEpisodes = None
            self.nextEpisodeReleaseDate = None
            self.isAiring = None

            self.getData()
            
        else: 
            self.name = args[0]
            self.numSeasons = args[1]
            self.numEpisodes = args[2]
            self.releaseDate = args[3]
            self.isAiring = args[4]
            self.nextEpisodeReleaseDate = args[5]




    def getData(self, numInResult = 0):

        self.id = requests.get(("https://api.themoviedb.org/3/search/{isShowOrMovie}?api_key={api_key}&language=en-US&query={name}").format(isShowOrMovie = self.isShowOrMovie, api_key = self.api_key, name = self.name)).json()['results'][numInResult]['id']
        self.data = requests.get(('https://api.themoviedb.org/3/tv/{id}?api_key={api_key}&language=en-US').format(id = self.id, api_key = self.api_key)).json() 

        self.numSeasons = self.data["number_of_seasons"]
        self.numEpisodes = self.data["number_of_episodes"]
        self.releaseDate = self.data["first_air_date"]

        self.getNextAiringEpisode()

        if self.isAiring == False: 
            self.nextEpisodeReleaseDate = ""
            return self.data 

        self.nextEpName = self.nextEp["name"]
        self.nextEpisodeReleaseDate = self.nextEp["air_date"] 

        return self.data

    def getNextAiringEpisode(self): 

        if not self.data["next_episode_to_air"] == None: 
            self.nextEp = self.data["next_episode_to_air"]
            self.isAiring = True

            return self.nextEp

        self.isAiring = False
        return None

    def updateData(self):
        self.data = requests.get(('https://api.themoviedb.org/3/tv/{id}?api_key={api_key}&language=en-US').format(id = self.id, api_key = self.api_key)).json() 
        self.getNextAiringEpisode()

        if self.isAiring == False: 
            self.nextEpisodeReleaseDate = ""
            return self.data 

        self.nextEpisodeReleaseDate = self.nextEp["air_date"] 
        self.nextEpName = self.nextEp["name"] 