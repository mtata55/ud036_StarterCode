import media #file with class definition
import requests #for fetching API data
import json #for parsing API data
import fresh_tomatoes #for creating html


favorite_movies=['the godfather part II','the matrix','saw','ocean\'s eleven',
 'requiem for a dream', 'pulp fiction','inglourious basterds','school of rock','fight club',
 '12 angry men','the usual suspects','the silence of the lambs','the social network','phone booth'] # list of favorite movies by common search terms

movie_list = []
for movie in favorite_movies: 
	r = requests.get('http://www.omdbapi.com/?t='+movie+'&apikey=481969a1') #search for movie data using API
	parser = json.loads(r.text) #convert json into parseable form	
	#extract values for title, plot, poster and imdb ID
	title = parser['Title'] 
	poster_image_url = parser['Poster']
	imdbID = parser['imdbID']
	#new url request for youtube API to get trailer
	r2 = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&q='+movie+'trailer&type=video&maxResults=1&key=AIzaSyBgfyS7nzEk8SzFtg62nkITtH7dVTcXfoA') 
	parser2 = json.loads(r2.text)
	trailer_youtube_id = parser2['items'][0]['id']['videoId'] #extract youtube video id
	trailer_youtube_url = 'https://www.youtube.com/watch?v='+trailer_youtube_id
	
	movie_object = media.Movie(title, poster_image_url, trailer_youtube_url) #create movie object and append to list
	movie_list.append(movie_object)
	print(movie_object.title)

fresh_tomatoes.open_movies_page(movie_list)


