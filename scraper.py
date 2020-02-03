from bs4 import BeautifulSoup
import requests

def get_html(url):
    """
    Retrieve the HTML from the website at `url`
    
    Attributes:
    -----------
    url : str
        The url of the desired page
        
    Returns:
    --------
    Response
        The html of the page
    """    
    
    return requests.get(url)

def get_clubs_html():
    """
    Get the HTML of online clubs with Penn.
    
    Returns:
    --------
    Response
        The html of the page with the clubs at Penn
    """
    
    url = 'https://ocwp.apps.pennlabs.org'
    return get_html(url).text

def soupify(html):
    """
    Load HTML into BeautifulSoup so we can extract data more easily

    Note that for the rest of these functions, whenever we refer to a "soup", we're refering
    to an HTML document or snippet which has been parsed and loaded into BeautifulSoup so that
    we can query what's inside of it with BeautifulSoup.
    """
    return BeautifulSoup(html, "html.parser") 


def get_elements_with_class(soup, elt, cls):
    """
    Returns a list of elements of type "elt" with the class attribute "cls" in the
    HTML contained in the soup argument.

    For example, get_elements_with_class(soup, 'a', 'navbar') will return all links
    with the class "navbar". 

    Important to know that each element in the list is itself a soup which can be
    queried with the BeautifulSoup API. It's turtles all the way down!
    """ 
    return soup.findAll(elt, {'class': cls})

def get_clubs(soup):
    """
    This function should return a list of soups which each correspond to the html
    for a single club.
    
    Arguments:
    ----------
    soup : BeautifulSoup
        The html for the url
    
    Returns:
    --------
    list
        A list of soups for each club
    """
    
    return get_elements_with_class(soup, 'div', 'box')

def get_club_name(club):
    """
    Returns the string of the name of a club, when given a soup containing the data for a single club.

    We've implemented this method for you to demonstrate how to use the functions provided.
    """
    elts = get_elements_with_class(club, 'strong', 'club-name')
    return check_len(elts, 0)

def get_club_description(club):
    """
    Extract club description from a soup of 
    """
    
    elts = get_elements_with_class(club, 'em', '')
    return check_len(elts, 0)

def get_club_tags(club):
    """
    Get the tag labels for all tags associated with a single club.
    """
    
    elts = get_elements_with_class(club, 'span', 'tag is-info is-rounded')
    tags_list = []
    for tags in range(0, len(elts)):
        tags_list.append(check_len(elts, tags))
    return tags_list

def check_len(elts, index):
    """
    Length checker to avoid code redundancy
    
    Arguments:
    ----------
    elts : list
        The list of soups
    
    index : int
        The index value of elts
    
    Returns:
    --------
    str 
        Either the text associated with the soup, or an empty string.
    """
    
    if len(elts) < 1:
        return ''
    return elts[index].text
