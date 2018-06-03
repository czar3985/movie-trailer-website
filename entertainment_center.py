import movie_list
import fresh_tomatoes


def main():
    # Get all the movie data for the website
    movies = movie_list.get_content()

    # Create and display the webpage
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    main()
