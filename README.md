# Penn Labs Server Challenge

## Documentation
Fill out this section as you complete the challenge!

## Installation
1. Click the green "use this template" button to make your own copy of this repository, and clone it. 
2. Change directory into the cloned repository.
3. Install `pipenv`
   * `brew install pipenv` if you're on a Mac with [`homebrew`](https://brew.sh/) installed.
   * `pip install --user --upgrade pipenv` for most other machines.
4. Install packages using `pipenv install`.

## Developing
***More specific workings of functions are available in DocString format. Do help(<desired>) to get more information***
1. Had to run `pipenv shell` to activate environment. 
2. Use `pipenv run index.py` to run the project.
3. Follow the instructions [here](https://www.notion.so/pennlabs/Server-Challenge-Spring-20-5a14bc18fb2f44ba90a61ba86b6fc426).
4. Document your work in this `README.md` file.
5. Looked into BeautifulSoup -> pulls information from HTML and XML files
6. Created Club class, as I believe storing the club objects in memory is the best option. Having all of the clubs locally allows for faster iteration through the clubs. I see them as the most "primitive" type of data here, as every other data structure uses or groups clubs.
7. Began implementing functions in scraper.py
  - Needed to import requests
  - Created helper function `check_len` to avoid repeating if statements. See `help(check_len)`.
8. Tested Club object creation and worked as desired.
9. Created User class, and as I chose to keep the clubs in-memory, I believe it is best to keep any users in-memory as well. The user is contains a list of clubs, where I see every entry just pointing to an already in-memory club. My implementation uses iteration and lists heavily. Traversing the list and iterating would take longer if the data needed to be read from a JSON file and updated after.
10. I created the master list of clubs `unencoded_clubs_list` in `index.py` and defined a function `encode_clubs()`. This function encodes all of the clubs, which allows me to update the data in view after the unencoded version with direct access to the attributes of each club has been changed.
11. I defined the class `ClubEncoder` which is a child of `JSONEncoder` and creates returns an encoded version of the club.
12. Created an HTML template `new_club.html` which presents the user with a form with options to either see all of the clubs or add a new club and then see all of the clubs (including the new one).
13. Created GET and POST methods of `/api/clubs`. The GET method first shows the `new_club.html` template and then either shows all of the clubs using `jsonify` or adds a new club and shows the clubs using `jsonify`.
14. Created the GET method of `/api/username/<username>` and created another HTML template `user_profile.html`. The template presents the user with the information of the person entered in `<username>`. If that user does not exist, "No Such User" is shown instead.
15. Created the GET and POST methods of `/api/favorite` and created another HTML template `favorite_form.html`. This template presents the user with a form that requires a valid user name, and the name of the club that the user wants to favorite. If an error occurs, "There was an error." is returned, and if not, the club's favorite count is increased by 1, the `/api/clubs` data is updated, and "Favorited!" is displayed.
  - Favorite Logic
    - New `int` attribute in Club class.
    - Each user now gets a list of bools as long as their clubs list.
      - `False` is not favorited, `True` is favorited
    - Each call to a club goes through the `user_list` and counts the number of `true`s
    - Updated club representation in `/api/clubs`
16. Created the start of the analytics page, which has GET and POST methods. This is the personal feature I am implementing using `matplitlib` and `numpy`. I have the most programming experience in data science, so I see it as the best way to show some of my skillset.
17. 

TODO
  - Need to add catches for edge cases in user add, remove, and searching stuff
  
## Submitting
Follow the instructions at on the Technical Challenge page for submission.

## Installing Additional Packages
Use any tools you think are relevant to the challenge! To install additional packages 
run `pipenv install <package_name>` within the directory. Make sure to document your additions.
- Installed requests 
- Installed JSON
