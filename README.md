# Movie Trailer Website

The Movie Trailer Website program dynamically creates a website from a list of movies that includes box art imagery, trailer and movie details. The web page produced allows users to browse, search for movies and watch trailers.

## Installation

1. Install **python 3.6.3**.
2. Clone the github repository [movie-trailer-website](https://github.com/czar3985/movie-trailer-website).
```
$ git clone https://github.com/czar3985/movie-trailer-website
```
3. The necessary files needed to the run the program are:
```
base_page.html
entertainment_center.py
fresh_tomatoes.css
fresh_tomatoes.js
fresh_tomatoes.py
media.py
movie_list.py
```
4. Run the python script _entertainment_center.py_. The following resource gives more information on how to run python scripts: [How to Run a Python Script via a File or the Shell](https://www.pythoncentral.io/execute-python-script-file-shell/).

## Usage

After the script is run for the first time, the html file _fresh_tomatoes.html_ is generated and can be used for browsing movies. You can open the generated html file using any browser.

Click on each movie to view the movie's storyline and play a youtube trailer.

The search function in the navigation bar can filter the results based on the searched text.

## Release Notes

The starter code contained the module for defining the base html file and for opening a modal for the trailer.

Major changes to the starter code:
- Addition of the Movie class, data for the movies and code for initiating the creation of the web page using the movie data
- Moved the base html, scripts and styling to different files for readability and easier modification and maintenance.
- Supported Bootstrap 4 and JQuery 3.3.1
- Showed title and storyline with the trailer
- Addition of the Search functionality

## Issues

There is a known compatibility issue with the cancel search feature in the Search text field for other browsers. It currently only works in Chrome. 

In _fresh_tomatoes.css_:
```CSS
input[type="search"]::-webkit-search-cancel-button {
    -webkit-appearance: searchfield-cancel-button;
}
```
Also, after a search is performed, clearing the search input field does not automatically reload the page. The Search button has to be pressed again.

## Acknowledgments

- [Udacity](https://www.udacity.com/) for the forked code. Starter code repository is in [here](https://github.com/udacity/ud036_StarterCode).
- [A. Wolff](https://stackoverflow.com/users/1414562/a-wolff) for the JQuery code of the search function. See the stackoverflow answer [here](https://stackoverflow.com/questions/16986497/jquery-hide-all-divs-except-for-the-divs-i-search-for/16987520#16987520).