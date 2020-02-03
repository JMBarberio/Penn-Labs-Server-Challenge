class User():
    """
    The user class that contains user information.
    
    Attributes:
    -----------
    name : str
        The name of the user.
        
    clubs : list
        The list of the clubs that the user is in
    
    fav_list : list
        The bool list of whether or not a club has been favorited
    """
    
    def __init__(self, name, clubs):
        self.__name = name
        self.__clubs = clubs
        self.__fav_list = []
        for club in range(0, len(clubs)):
            self.__fav_list.append(False)
            
    def get_user_name(self):
        """
        Getter for the club name
        
        Returns:
        --------
        str
            The club name
        """
        
        return self.__name
    
    def set_user_name(self, new_name):
        """
        Setter for the club name
        
        Arguements:
        -----------
        new_name : str
            The new user name
        """
        
        self.__name = new_name
        
    def get_user_clubs(self):
        """
        Getter for the list of clubs
        
        Returns:
        --------
        list
            The list of clubs
        """
        
        return self.__clubs
        
    def get_fav_list(self):
        """
        Getter for the favorite list
        
        Returns:
        --------
        list 
            The bool list of favorites
        """
        
        return self.__fav_list
        
    def add(self, new_club):
        """
        Adds a new club to the club list
        
        Arguements:
        -----------
        new_club : Club 
            The new club to be added
            
        TODO: add throws for club not found
        """
        
        self.__clubs.append(new_club)
        self.__fav_list.append(false)
        
    def remove(self, club):
        """
        Removes a club from the club list if the club is in the current list
        Pops the boolean from the bool list at the corresponding index
        If the corresponding bool was True, the favorite count for that club is decreased
        
        Arguments:
        ----------
        club : Club 
            The club to be removed 
            
        Throws:
        -------
        
        """
        try:
            index = self.__clubs.index(club)
            if self.__fav_list[index] == True:
                club.decrease() 
            self.__clubs.remove(club)
            self.__fav_list.pop(index)
        except ValueError:
            raise e 