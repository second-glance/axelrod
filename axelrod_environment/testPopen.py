# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:31:30 2017

@author: clem
"""

import subprocess

p = subprocess.Popen(['Rscript', 'r_wrapper.r', 'generous_tit_for_tat.r'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
p.stdin.write('T,T,T,F,F|T,T,F,T,F\n')