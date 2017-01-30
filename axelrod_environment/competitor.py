# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:19:28 2017

@author: clem
"""

class competitor_algorithm(object):
    """
    Description
    -----------
    Store the characteristics of a competitor. This class implement a __call__ method
    
    Main Attributes
    ---------------
    author: str
        Author of the algorithm
    name: str
        Name of the algorithm
    algo: function (bool list -> bool list -> bool)
        Function to compete in the Axelrod competition
    score: int
        Score of the instance
        
    Main Methods
    ------------
    update_score: None
        Update the score of the instance
        
    Examples
    --------
    >>> comp = competitor_algorithm("John Doe", "My super algorithm",lambda x,y: True)
    >>> comp([True,True],[False,False])
    True
    >>> #This is equivalent to:
    >>> comp.algo([True,True],[False,False])
    True
    >>> comp.update_score(5)
    >>> print(comp.score)
    5
    """
    def __init__(self,author,name,algo):
        """
        Parameters
        ----------
        author: str
            Author of the algorithm
        name: str
            Name of the algorithm
        algo: function (bool list -> bool list -> bool)
            Function to compete in the Axelrod competition
        score: int
            Score of the instance
        """
        self.author = author
        self.name = name
        self.algo = algo
        self.score = 0

    
    def update_score(self,add_score):
        """
        Update the score of the competitor by adding the add_score value
        
        Parameters
        ----------
        add_score: int
            Value to add to the current score
        
        Returns
        -------
        None
        """
        self.score = self.score + add_score
        
    def __call__(self,self_decision,other_decision):
        """
        Shorcut for self.algo(x,y)
        """
        return self.algo(self_decision,other_decision)
        
class r_competitor_algorithm(competitor_algorithm):    
    
    def __call__(self,self_decision,other_decision):
        return 