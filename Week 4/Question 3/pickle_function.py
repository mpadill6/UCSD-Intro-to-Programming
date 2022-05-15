# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:09:39 2020

@author: mpadilla
"""
import pickle
#pickle function
teams={'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners'} #baseball team dictionary

filename='teams' #Create filename for resulting file
fhandle=open(filename,'wb') #Create filehandle

pickle.dump(teams,fhandle) #pickle dump
fhandle.close()
#Unpickle section
pickle_in=open(filename,'rb')
example_dict=pickle.load(pickle_in)

print(example_dict)