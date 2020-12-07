
#-*- coding: iso-8859-1 -*-
'''
Created on Dec 3, 2020

@author: ronny
'''

#-*- coding: iso-8859-1 -*-
import glassdoor_scraping as gs
import pandas as pd
import cython
path = "C:/Users/ronny/OneDrive/Dokumente/Software/chromedriver_win32/chromedriver.exe"

df = gs.get_jobs('data_scientist', 15, False, path, 3)
df.to_csv('glassdoor_jobs2.csv', index=False)
