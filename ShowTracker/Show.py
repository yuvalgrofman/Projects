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
        """
            Takes either 3 arguments and sets variables according to external database or
            Takes all arguments

        Raises:
            TypeError: raises if the length of the parameters is not 3 or 6 
        """

        if len(args) == 3:
            name = args[0]
            isShowOrMovie = args[1]
            api_key = args[2]

            self.name = name.lower()
            self.name.replace(" ", "+")
            self.isShowOrMovie = isShowOrMovie
            self.api_key = api_key

            self.releaseDate = None
            self.numSeasons = None
            self.numEpisodes = None
            self.nextEpisodeReleaseDate = None
            self.isAiring = None

            self.getData()
            assert self.data != None
            
        elif len(args) == 6: 
            self.name = args[0]
            self.numSeasons = args[1]
            self.numEpisodes = args[2]
            self.releaseDate = args[3]
            self.isAiring = args[4]
            self.nextEpisodeReleaseDate = args[5]

        else: 
            raise TypeError("The input must either be of length 3 and include (string) name, (bool) isShowOrMovie, (string) Api_Key or of length 6 and include name, numSeasons, numEpisodes, ReleaseDate, (bool) isAiring, nextEpisodeReleaseDate")




    def getData(self, numInResult = 0):
        """
            sets all the necessary about the show 
            ie: name, numSeasons/Episodes, release date, if the shows is airing 
                if so next Episodes name and release date

        Args:
            numInResult (int, optional): If there are multiple results in the online show database it will take the one which is #numInResult (starting count in 0) . Defaults to 0.

        Raises:
            Exception: If there are no results will throw an Exception 

        Returns:
            JSON: The a json encoded response sent by the online database containing info about the show 
        """

        try: 

            self.id = requests.get(("https://api.themoviedb.org/3/search/{isShowOrMovie}?api_key={api_key}&language=en-US&query={name}").format(isShowOrMovie = self.isShowOrMovie, api_key = self.api_key, name = self.name)).json()['results'][numInResult]['id']

        except IndexError or KeyError: 
            raise Exception("No Results For Name " + str(self.name)) 

        self.data = requests.get(('https://api.themoviedb.org/3/tv/{id}?api_key={api_key}&language=en-US').format(id = self.id, api_key = self.api_key)).json() 

        self.numSeasons = self.data["number_of_seasons"]
        self.numEpisodes = self.data["number_of_episodes"]
        self.releaseDate = self.data["first_air_date"]

        self.getNextAiringEpisode()

        if self.isAiring == 'No': 
            self.nextEpisodeReleaseDate = "None"
            self.nextEpName = "None"
            return self.data 

        self.nextEpName = self.nextEp["name"]
        
        if (self.nextEpName == ""):
            self.nextEpName = "Not Yet Released"

        self.nextEpisodeReleaseDate = self.nextEp["air_date"] 

        return self.data

    def getNextAiringEpisode(self): 
        """
                Generates the data about the next airing episode if there is one 
                if not sets variables accordingly

        Returns:
            JSON: which contains data about next episodes to be released if there isn't one returns None  
        """

        if not self.data["next_episode_to_air"] == None: 
            self.nextEp = self.data["next_episode_to_air"]
            self.isAiring = 'Yes'

            return self.nextEp

        self.isAiring = 'No'
        return None

    def updateData(self):
        """
            Updates the data about the show. EVERYTHING

        Returns:
            None
        """
        self.data = requests.get(('https://api.themoviedb.org/3/tv/{id}?api_key={api_key}&language=en-US').format(id = self.id, api_key = self.api_key)).json() 
        self.getNextAiringEpisode()

        if self.isAiring == 'No': 
            self.nextEpisodeReleaseDate = ""
            return self.data 

        self.nextEpisodeReleaseDate = self.nextEp["air_date"] 
        self.nextEpName = self.nextEp["name"] 

