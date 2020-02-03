from flask import Response

import matplotlib.pyplot as plt 
import matplotlib.axes as ax
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
from club import Club
from user import User
import io

"""
The file that houses the analytics functions
"""

def club_tags(unencoded_clubs_list):
    club_dict = {}
    for clubs in unencoded_clubs_list:
        for tag in clubs.get_category():
            if tag in club_dict:
                club_dict[tag] = club_dict[tag] + 1
            else: 
                club_dict[tag] = 1
    x = np.zeros(len(club_dict))
    index_counter = 0
    for tag in club_dict:
        x[index_counter] = club_dict.get(tag)
        index_counter = index_counter + 1
    
    fig = plt.figure()   
    ax = fig.add_subplot()
    bar = ax.bar(np.arange(len(club_dict)), x)
    labels = club_dict.keys()
    ax.set_xticks(np.arange(len(club_dict)))
    ax.set_xticklabels(labels, rotation='45', ha='right')
    ax.set_xlabel('Club Tags')
    ax.set_ylabel('Number of Occurrances')
    ax.set_title('Number of Club Tag Occurrances')
    for rect in bar:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
  
    plt.tight_layout()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png') 


def clubs_per_user(user_list):
    user_club_dict = {}
    for user in user_list:
        name = user.get_user_name()
        user_club_dict[name] = len(user.get_user_clubs())
    
    x = np.zeros(len(user_club_dict))
    index_counter = 0
    for user in user_club_dict:
        x[index_counter] = user_club_dict.get(user)
        index_counter = index_counter + 1
        
    fig = plt.figure()    
    ax = fig.add_subplot()
    bar = ax.bar(np.arange(len(user_club_dict)), x)
    labels = user_club_dict.keys()
    ax.set_xticks(np.arange(len(user_club_dict)))
    ax.set_xticklabels(labels, rotation='45', ha='right')
    ax.set_xlabel('User Name')
    ax.set_ylabel('Number of Clubs')
    ax.set_title('Number of Clubs per User')
    for rect in bar:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    plt.tight_layout()                
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')         

    