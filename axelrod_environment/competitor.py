# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:19:28 2017

@author: clem
"""

import subprocess

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
        
    def begin_match(self):
        pass
        
    def __call__(self,self_decision,other_decision):
        """
        Shorcut for self.algo(x,y)
        """
        return self.algo(self_decision,other_decision)
        
class r_competitor_algorithm(competitor_algorithm):
    
    def __init__(self,author,name,algo):
        competitor_algorithm.__init__(self,author,name,algo + ".r")
        
    def begin_match(self):
        self.subprocess = subprocess.Popen(['Rscript', 'r_wrapper.r', 'generous_tit_for_tat.r'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        
        
    
    def __call__(self,self_decision,other_decision):
        #args = [self.algo]
        args = [x.__str__().lower() for x in self_decision]
        args = args + [ x.__str__().lower() for x in other_decision]
        print(args)
        self.subprocess.stdin.write('T,T,T,F,F|T,T,F,T,F\n')
        self.subprocess.stdout.
        cmd = ['Rscript','r_wrapper.r'] + args
        answer = subprocess.check_output(cmd, universal_newlines=True)
        if(answer == 'TRUE'):
            res = True
        elif answer == 'FALSE':
            res = False
        else:
            raise Exception("Not a good answer")
        return res