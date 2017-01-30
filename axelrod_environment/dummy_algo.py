# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:01:34 2017

@author: clem
"""

from rpy2.robjects.vectors import BoolVector
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage as rsignature

r_yes_man_sign = rsignature('r_yes_man <- function(x,y){T}','r_yes_man')
r_yes_man = lambda x,y: r_yes_man_sign.r_yes_man(x,y)[0]
la_balance = lambda x,y: False
yes_man = lambda x,y: True
def idk(x,y):
    if len(x) == 0:
        return True
    else:
        if x[len(x)-1]:
            return False
        else:
            return True
            
shubik_str = """shubik = function(p, o) {
	round <- length(p)+1
	if(round == 1) {
		res <- TRUE
	} else {
		n <- max(1, sum(p & !o))
		d <- tail(which(!o), 1)
		punish <- ifelse(length(d) == 0, FALSE, round <= d+n)
		res <- tail(o, 1) & !punish
	}
	return(res)
} """

r_shubik_sign = rsignature(shubik_str,'shubik')
r_shubik = lambda x, y: r_shubik_sign.shubik(BoolVector(x),BoolVector(y))[0]