import media
import fresh_tomatoes


def get_movie_list():
    # Movies included in the website and attributes for each
    thor_ragnarok = media.Movie(
        "Thor: Ragnarok",
        "Thor has to prevent the all-powerful Hela from destroying Asgard.",
        ("https://upload.wikimedia.org/wikipedia/"
         "en/7/7d/Thor_Ragnarok_poster.jpg"),
        "https://www.youtube.com/watch?v=ue80QwXMRHg")
    spiderman_homecoming = media.Movie(
        "Spider-Man: Homecoming",
        ("Peter Parker tries to balance high school life with being "
         "Spider-Man."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/f/f9/Spider-Man_Homecoming_poster.jpg"),
        "https://www.youtube.com/watch?v=rk-dF1lIbIg")
    avengers_infinity_war = media.Movie(
        "Avengers: Infinity War",
        ("The Avengers unite to battle their most powerful enemy yet "
         "- the evil Thanos."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/4/4d/Avengers_Infinity_War_poster.jpg"),
        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
    captain_america_civil_war = media.Movie(
        "Captain America: Civil War",
        ("When the actions of the Avengers lead to collateral damage, "
         "an all-out feud among the superheroes ensues."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/5/53/Captain_America_Civil_War_poster.jpg"),
        "https://www.youtube.com/watch?v=dKrVegVI0Us")
    black_panther = media.Movie(
        "Black Panther",
        ("T'Challa, the king of Wakanda, must release the full power "
         "of Black Panther to protect his kingdom."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/0/0c/Black_Panther_film_poster.jpg"),
        "https://www.youtube.com/watch?v=xjDjIWPwcPU")
    antman_and_the_wasp = media.Movie(
        "Ant-Man and the Wasp",
        ("Lang must once again don the Ant-Man suit and "
         "fight alongside the Wasp."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/2/2c/Ant-Man_and_the_Wasp_poster.jpg"),
        "https://www.youtube.com/watch?v=UUkn-enk2RU")

    # Make a list of all movies in the website
    movies = [thor_ragnarok,
              spiderman_homecoming,
              avengers_infinity_war,
              captain_america_civil_war,
              black_panther,
              antman_and_the_wasp]

    return movies


def main():
    # Get all the movie data for the website
    movies = get_movie_list()

    # Create and display the webpage
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    main()
