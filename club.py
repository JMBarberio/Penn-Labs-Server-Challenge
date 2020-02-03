from json import *

class Club:
    """
    The class representing each club
    
    Attributes:
    -----------
    name : str
        The name of the club
    category : list
        The tags associated with the club
    descr : str
        The description of the club
    """
    
    def __init__(self, name, category, descr):
        self.__name = name
        self.__category = category
        self.__descr = descr
        self.__fav = 0
        
    
    def get_name(self):
        """
        Gets the name of the club
        
        Returns:
        --------
        str
            The name of the club
        """
        
        return self.__name
    
    def set_name(self, new_name):
        """
        Sets the name of the club
        
        Arugments:
        ----------
        new_name : str
            The new name of the club
        """
        
        self.__name = new_name
        
    def get_category(self):
        """
        Gets the category(s) of the club
        
        Returns: 
        --------
        list
            The category(s) of the club
        """
        
        return self.__category
        
    def set_category(self, new_cat):
        """
        Sets the category(s) of the club
        
        Arguments:
        ----------
        new_cat : list
            The new category(s)
        """
        
        self.__category = new_cat
    
    def get_descr(self):
        """
        Gets the club description
        
        Returns:
        --------
        str
            The club description
        """
        
        return self.__descr
    
    def set_descr(self, new_descr):
        """
        Sets the club description
        
        Arguments:
        ----------
        new_descr : str
            The new club description
        """
        
        self.__descr = new_descr
    
    def get_fav(self):
        """
        Gets the current number of favorites
        
        Returns:
        --------
        int
            The current favorite count of the club
        """
        
        return self.__fav
    
    def increase(self):
        """
        Increases the current number of favorites by 1
        """
        
        self.__fav = self.__fav + 1
        
    def decrease(self):
        """
        Decreases the current number of favorites by 1
        """
        
        self.__fav = self.__fav - 1
        
    def __str__(self):
        """
        Override to output club in following form (as of Part 1)
        
        Name: <name>
        Tags: <tags>
        Description <description>
        
        Returns:
        --------
        str
            The desired string representation of a club
        """
        
        return 'Name: {}\nTags: {}\nDescription: {}'.format(self.__name, self.__category, self.__descr)