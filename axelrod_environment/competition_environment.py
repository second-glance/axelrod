# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:17:05 2017

@author: clem
"""

from competitor import *
import numpy as np

class axelrod_environment:
    """
    The competition_environment class host a competition
    
    Static Properties
    -----------------
    None
        
    Properties
    ----------
    algos: set
        Set conatining all competitor instances involved in the competition
    n_round: int
        Number of rounds
    """
    
    def __init__(self,n_round = 200):
        """
        Parameters
        ----------
        n_round: int
            Numer of rounds for a single fight
        """
        self.algos = {}
        self.n_round = n_round
        #Switch scores
        self.score_table = {(True,True): [3,3], (True,False): [0,5], (False,True): [5,0], (False,False): [1,1]}
   
    def add_algo(self,author,name,algo):
        """
        Add an algorithm by instanciating a new competitor_algorithm and adding it to the algos dictionary.
        
        Parameters
        ----------
        author: str
            Author of the algorithm
        name: str
            Name of the algorithm
        algo: function (bool list -> bool list -> bool)
            Function that takes two list of bool as an input and returns a boolean value
            
        Returns
        -------
        None
        
        Exceptions
        ----------
        * An attempt to add an algorithm with a name that has already provided for another competitor will result in an Exception
        """
        if name in self.algos.keys():
            raise Exception("An algorithm named {} is already present in the competition. Please find an other name".format(name))
        self.algos[name] = competitor_algorithm(author,name,algo)
    
    def _update_scores(self,algo1,algo2,dec_alg1,dec_alg2):
        """
        Update the score of two competitors at the end of a fight
        
        Parameters
        ----------
        algo1, algo2: competitor
            Competitor instances that just finished a fight
        dec_alg1, dec_alg2: bool list
            Decisions taken by the algorithm during the fight
            
        Returns
        -------
        None
        
        Side Effects
        ------------
        algo1.score and algo2.score are both updated by adding their respective number of points
        """
        get_round_scores = lambda d1, d2: self.score_table[(d1,d2)]
        scores = np.sum(map(get_round_scores,dec_alg1,dec_alg2),axis=0)
        algo1.update_score(scores[0])
        algo2.update_score(scores[1])
    
    def _compete(self,algo1,algo2):
        """
        Make two competitor instances fighting
        
        Parameters
        ----------
        algo1, algo2: competitor
            competitor instances involved in the fight
        
        Returns
        -------
        None
        """
        dec1 = []
        dec2 = []
        for i in range(self.n_round):
            dec1.append(algo1(dec1,dec2))
            dec2.append(algo2(dec2,dec1))
        self._update_scores(algo1,algo2,dec1,dec2)
        
    def _output_scores(self):
        """
        Return a sorted list (by total score) of competitor instance
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type: competitor list
            List of competitors sorted by score (highest to lowest)
        """
        return sorted(self.algos.values(),key = lambda x: x.score ,reverse = True)
        
    def full_competition(self):
        """
        Makes competitor fight against each other
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type: competitor list
            List of competitor sorted by score (highest to lowest)
        """
        ks = self.algos.keys()
        for i,name in enumerate(self.algos):
            for j in range(i):
                self._compete(self.algos[name],self.algos[ks[j]])
        return self._output_scores()
    
    