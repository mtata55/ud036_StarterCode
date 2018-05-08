import media  # file with class definition
import requests  # for fetching API data
import json  # for parsing API data
import fresh_tomatoes  # for creating html

# list of favorite movies by common search terms
favorite_movies = ['the godfather part II', 'the matrix', 'saw',
                   'ocean\'s eleven', 'requiem for a dream',
                   'pulp fiction', 'inglourious basterds',
                   'school of rock', 'fight club',
                   '12 angry men', 'the usual suspects',
                   'the silence of the lambs',
                   'the social network', 'phone booth']

# added print statement to clarify waiting time
print('Please wait, movie data is being called through API\'s...')
print('The browser window will open automatically when the website is ready')

movie_list = []

for movie in favorite_movies:
    # search for movie data using API
    r = requests.get('http://www.omdbapi.com/?t='+movie+'&apikey=481969a1')
    parser = json.loads(r.text)  # convert json into parseable form
    # extract values for title, plot, poster and imdb ID
    title = parser['Title']
    poster_image_url = parser['Poster']
    imdbID = parser['imdbID']
    # new url request for youtube API to get trailer
    r2 = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&q=' +
                      movie +
                      'trailer&type=video&maxResults=1&key=AIzaSyBgfyS7nzEk8SzFtg62nkITtH7dVTcXfoA')
    parser2 = json.loads(r2.text)
    # extract youtube video id
    trailer_youtube_id = parser2['items'][0]['id']['videoId']
    trailer_youtube_url = 'https://www.youtube.com/watch?v='+trailer_youtube_id

    # create movie object and append to list
    movie_object = media.Movie(title, poster_image_url, trailer_youtube_url)
    movie_list.append(movie_object)
    # print(movie_object.title) #commented out testing code

print('Website Generated!')  # print when loop complete and list generated
fresh_tomatoes.open_movies_page(movie_list)
