# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:04:20 2017

@author: clem
"""

from competition_environment import *
from competitor import *
from dummy_algo import *

ce = axelrod_environment(200)

ce.add_algo("Clem","La balance",la_balance)
ce.add_algo("Melc","La balance, le retour",la_balance)
ce.add_algo("Clem","Yes Man!",yes_man)
ce.add_algo("Mecreant","Generous Tit for tat","generous_tit_for_tat","r")
ce.full_competition()
x = ce._output_scores()
for alg in x:
    print "{} - {}".format(alg.name,alg.score)