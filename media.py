class Movie(object):
    """Class Movie for storing data and methods applicable to
     movies for movie trailer website.

     Attributes:
        title (str): Movie title

        poster_image_url (str): URL of the movie poster used for
        website images

        trailer_youtube_url (str): URL of the movie trailer
        on YouTube
     """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
