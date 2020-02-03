from flask import Flask, request, jsonify, render_template
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.
from club import Club
from club_encoder import ClubEncoder
from user import User
from json import *
from analytics import *

import matplotlib
matplotlib.use('agg') # stops conflict between matplotlib creating new windows and flask

app = Flask(__name__)        

unencoded_clubs_list = []
clubs_html = get_clubs(soupify(get_clubs_html()))

for club in range(0, len(clubs_html)):
    unencoded_club = Club(get_club_name(clubs_html[club]), 
                          get_club_tags(clubs_html[club]), 
                          get_club_description(clubs_html[club]))
    unencoded_clubs_list.append(unencoded_club)
    
def encode_clubs():
    """
    Updates the encoding of the club for the /api/clubs. Only needed because of the favorite count
    """
    
    encoded_clubs_list = []
    for club in unencoded_clubs_list:
        encoded_club = ClubEncoder().encode(club)
        encoded_clubs_list.append(encoded_club)
    return encoded_clubs_list

encoded_clubs_list = encode_clubs()

user_list = []
jen = User('Jen', [unencoded_clubs_list[3], unencoded_clubs_list[9]])
bob = User('Bob', [unencoded_clubs_list[10], unencoded_clubs_list[2]])
joe = User('Joe', [])
sam = User('Sam', [unencoded_clubs_list[10], unencoded_clubs_list[2], unencoded_clubs_list[3], unencoded_clubs_list[9]])
user_list.append(jen)
user_list.append(bob)
user_list.append(joe)
user_list.append(sam)

@app.route('/')
def main():
    """
    The opening page. Nothing is done here.
    """
    
    return "Welcome to Penn Club Review!"

@app.route('/api')
def api():
    """
    Introduction to the API.
    """
    
    return "Welcome to the Penn Club Review API!."

@app.route('/api/clubs', methods = ['GET', 'POST'])
def clubs():
    """
    The page that allows the addition of a new club and the view of all of the clubs.
    
    The new club form is presented and the user either chooses not to add a new club, or enters
    the data for a new club. If the former happens, the POST method just shows the clubs in JSON
    format using jsonify. If the latter happens, a new club is added to the master list of clubs
    and then the clubs are shown in the same way as before.
    
    Returns:
    --------
    jsonify(encoded_clubs_list)
        The JSON format view of the clubs
    """
    
    if request.method == 'POST':
        new_club_name = request.form.get('new_club_name')
        if new_club_name == '':
            encoded_clubs_list = encode_clubs()
            return jsonify(encoded_clubs_list)
        new_club_tags = request.form.get('new_club_tags')
        new_club_tags = new_club_tags.splitlines()
        new_club_descr = request.form.get('new_club_descr')
        unencoded_club = Club(new_club_name, 
                              new_club_tags, 
                              new_club_descr)
        unencoded_clubs_list.append(unencoded_club)
        encoded_clubs_list = encode_clubs()
        return jsonify(encoded_clubs_list)
            
    return render_template('new_club.html')

@app.route('/api/user/<username>', methods = ['GET'])
def user(username):
    """
    The page that allows for view of a user's data.
    
    The function uses the username defined in the address (<username>) to find
    and show the user's data in a form defined by user_profile.html. If the user
    does not exist, an error message is shown. 
    
    Returns:
    --------
    "No Such Error"
        The error message
        
    render_template(user_profile.html)
        The html view of the user's information
    """
    desired_user = None
    for user in range(0, len(user_list)):
        if username == user_list[user].get_user_name():
            desired_user = user_list[user]
    if desired_user == None:
        return "No Such User"
    user_name = desired_user.get_user_name()
    user_clubs = desired_user.get_user_clubs()
    user_clubs_string = []
    for club in range(0, len(user_clubs)):
        user_clubs_string.append(user_clubs[club].__str__())
    return render_template('user_profile.html', user_name=user_name, user_clubs=user_clubs_string)
    
@app.route('/api/favorite', methods = ['GET', 'POST'])
def favorite():
    """
    The page that allows for a user to favorite a club.
    
    The favorite form is presented and upon entry of "good" data, a club is favorited
    by the user and the boolean list in that user is updated. A success message is also
    presented. If there is an error, an error message is returned. 
    
    Returns:
    --------
    "Favorited!"
        The success message
        
    "There was an error."
        The error message
    """
    
    if request.method == 'POST':
        user = request.form.get('user')
        club = request.form.get('club')
        for users in user_list:
            if users.get_user_name() == user:
                for clubs in unencoded_clubs_list:
                    if clubs.get_name() == club:
                        clubs.increase()
                        encoded_clubs_list = encode_clubs()
                        if clubs in users.get_user_clubs():
                            index = users.get_user_clubs().index(clubs)
                            users.get_fav_list()[index] = True
                            return "Favorited!"
        return "There was an error."
                                 
    return render_template('favorite_form.html')

@app.route('/api/analytics', methods = ['GET', 'POST'])
def analytics():
    """"
    This page provides desired graphs and analytics regarding information about clubs and users
    using matplotlib and numpy.
    
    Functions are defined in analytics.py
    
    Returns:
    --------
    
    
    """
    if request.method == 'POST':
        if 'club_tags' in request.form:
            return club_tags(unencoded_clubs_list)
                     
        elif 'clubs_per_user' in request.form:
            return clubs_per_user(user_list)
                
    return render_template('analytics_form.html')
    

    
if __name__ == '__main__':
    app.run()
