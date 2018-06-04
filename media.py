import webbrowser


class Movie():
    """Stored details and actions that can be performed for each movie"""

    def __init__(self, title, storyline, poster_image, trailer_video):
        """Initializes movie object properties

        Args:
            title (str): Movie title
            storyline (str): Synopsis of the movie
            poster_image (str): Link to an image of the movie poster
            trailer_video (str): Link to a youtube trailer video
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_video

    def show_trailer(self):
        """Bring up and play the trailer in a new window"""
        webbrowser.open(self.trailer_video)
