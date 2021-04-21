import requests
import json



HOST_NAME = "imdb8.p.rapidapi.com"
API_KEY = "1a0ac83834mshc4bf97497c9d5a6p1a373ejsn14e832e9607e"

def __init__(self, year):
    
    HOST_NAME = "imdb8.p.rapidapi.com"
    API_KEY = "1a0ac83834mshc4bf97497c9d5a6p1a373ejsn14e832e9607e"

def get_movie_id(movie_name):
    '''
    Gets the id of a movie which can be used to get info from IMDB rapidAPI about that movie
    
    Parameters:
                movie_name(String): The name of a movie
    Returns:
    
    String
            The id of a movie used in IMDB api (eg. 'tt1049413')
                    
    '''
    url = "https://imdb8.p.rapidapi.com/title/find"
    
    querystring = {"q":movie_name}
    
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    data = data["results"][0]["id"]
    return(data[7:-1])

#print(get_movie_id("Up"))
#/title/tt0110912/


def get_plot_overview(movie_id):
    '''
    Gets the plot overview of a movie from IMDB rapidAPI 
    
    Parameters:
                movie_id(String): The id of a movie
    Returns:
    
    String
            The plot overview of a movie 
                    
    '''
    url = "https://imdb8.p.rapidapi.com/title/get-overview-details"
    # get the id of given movie
    #movie_id = get_movie_id(movie_id)
    querystring = {"tconst":movie_id,"currentCountry":"US"}

    #print(movie_id)
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    plot_overview = response.json()
    #print(plot_overview)
    plot_overview = plot_overview["plotSummary"]["text"]
    return (plot_overview)

#print(get_plot_overview("tt0110912"))

def get_top_100():
    '''
    Gets the top 100 IMDB movies from IMDB rapidAPI 
    
    Parameters:
                None
    Returns:
    
    List
            A list of 1oo strings of movie id's  
                    
    '''
    url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"
    
    querystring = {"purchaseCountry":"US","homeCountry":"US","currentCountry":"US"}
    
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    top_100_id = []
    for i in response:
        top_100_id.append(i[7:-1])
    return(top_100_id)
    
#print(get_top_100())

def get_short_plot(movie_id):
    '''
    Gets the plot overview of a movie from IMDB rapidAPI 
    
    Parameters:
                movie_id(String): The id of a movie
    Returns:
    
    String
            A short plot overview of a movie 
                    
    '''
    url = "https://imdb8.p.rapidapi.com/title/get-plots"
    
    querystring = {"tconst":movie_id}
    
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    plot = response["plots"][0]["text"]
    return(plot)
    
#print(get_short_plot("tt0110912"))

def get_medium_plot(movie_id):
    '''
    Gets the plot overview of a movie from IMDB rapidAPI 
    
    Parameters:
                movie_id(String): The id of a movie
    Returns:
    
    String
            A short plot overview of a movie 
                    
    '''
    url = "https://imdb8.p.rapidapi.com/title/get-plots"
   
    querystring = {"tconst":movie_id}
   
    headers = {
       'x-rapidapi-host': HOST_NAME,
       'x-rapidapi-key': API_KEY
       }
   
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    plot = response["plots"][1]["text"]
    return(plot)
   
#print(get_medium_plot("tt0110912"))
#
#def get_long_plot(movie_id):
#    url = "https://imdb8.p.rapidapi.com/title/get-plots"
#    
#    querystring = {"tconst":movie_id}
#    
#    headers = {
#        'x-rapidapi-host': HOST_NAME,
#        'x-rapidapi-key': API_KEY
#        }
#    
#    response = requests.request("GET", url, headers=headers, params=querystring)
#    response = response.json()
#    plot = response["plots"][2]["text"]
#    return(plot)
#    
#print(get_long_plot("tt0110912"))

def get_movie_year(movie_id):
    '''
    Gets the year of release of a movie from IMDB rapidAPI 
    
    Parameters:
                movie_id(String): The id of a movie
    Returns:
    
    Integer
            The year of a movie
                    
    '''
    url = "https://imdb8.p.rapidapi.com/title/get-details"

    querystring = {"tconst":movie_id}
    
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    movie_year = response["year"]
    
    return(movie_year)

#print(get_movie_year("tt0110912"))


def get_movie_title(movie_id):
    '''
    Gets the title of a movie from IMDB rapidAPI from it's ID
    
    Parameters:
                movie_id(String): The id of a movie
    Returns:
    
    String
            The title of a movie
                    
    '''
    
    url = "https://imdb8.p.rapidapi.com/title/get-details"

    querystring = {"tconst":movie_id}
    
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    movie_title = response["title"]
    
    return(movie_title)

#print(get_movie_title("tt0110912"))

def get_movie_details(movie_id):
    '''
    Gets all details of a movie from IMDB rapidAPI from it's ID
    
    Parameters:
                movie_id(String): The id of a movie
    Returns:
    
    JSON
            JSON list containing movie title, id, image URL, image width, running time in minutes, title, title type and year
                    
    '''
    url = "https://imdb8.p.rapidapi.com/title/get-details"

    querystring = {"tconst":movie_id}
    
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    movie_details = response.json()
    #movie_title = response["title"]
    
    return(movie_details)
    
#print(get_movie_details("tt0110912"))

def get_running_time(movie_id):
    '''
    Gets the running time of a movie from IMDB rapidAPI from it's ID
    
    Parameters:
                movie_id(String): The id of a movie
    Returns:
    
    String
            The running time in minutes of a movie
                    
    '''
    
    url = "https://imdb8.p.rapidapi.com/title/get-details"

    querystring = {"tconst":movie_id}
    
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    movie_running_time = response["runningTimeInMinutes"]
    
    return(movie_running_time)

#print(get_running_time("tt0110912"))

def get_poster_url(movie_id):
    '''
    Gets the URL which contains the poster of a movie from IMDB rapidAPI from it's ID
    
    Parameters:
                movie_id(String): The id of a movie
    Returns:
    
    String
            The URL of a movie poster
                    
    '''
    url = "https://imdb8.p.rapidapi.com/title/get-details"

    querystring = {"tconst":movie_id}
    
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    poster_url = response["image"]["url"]
    
    return(poster_url)

#print(get_poster_url("tt0110912"))


##NOT WORKING!!!
def get_actor_pic_url(actor_id):
    '''
    Gets the URL of an actor from IMDB rapidAPI from it's ID
    
    Parameters:
                actor_id(String): The id of an actor
    Returns:
    
    String
            The URL of a picture of an actor
                    
    '''
    url = "https://imdb8.p.rapidapi.com/actors/get-bio"

    querystring = {"nconst":actor_id}
    
    headers = {
        'x-rapidapi-host': HOST_NAME,
        'x-rapidapi-key': API_KEY
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    actor_pic_url = response["image"]["url"]
    
    return(actor_pic_url)

#print(get_actor_pic_url("nm0001667"))
