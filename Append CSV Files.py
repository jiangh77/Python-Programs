# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 00:39:25 2021

Append CSV Files

@author: jiang
"""

import pandas as pd

df1 = pd.read_csv("C:/Coinsquare/CSV Examples/alessa_csx_entity_master.csv")
df2 = pd.read_csv("C:/Coinsquare/CSV Examples/alessa_csc_entity_master_1.csv")
df3 = pd.read_csv("C:/Coinsquare/CSV Examples/alessa_csc_entity_master_2.csv")

frames = [df1, df2, df3]

result = pd.concat(frames)
result.to_csv("C:/Coinsquare/CSV Examples/Combine_1_alessa_entity_master.csv")

# This section produces a file with 1 index column at the first column, but no extra columns at the end

#%%

import pandas as pd

df1 = pd.read_csv("C:/Coinsquare/CSV Examples/alessa_csx_entity_master.csv")
df2 = pd.read_csv("C:/Coinsquare/CSV Examples/alessa_csc_entity_master_1.csv")
df3 = pd.read_csv("C:/Coinsquare/CSV Examples/alessa_csc_entity_master_2.csv")

frames = [df1, df2, df3]

result = pd.concat(frames)
result.to_csv("C:/Coinsquare/CSV Examples/Combine_2_alessa_entity_master.csv", index = False)

# This section produces a file with no index column at the start and no extra column at the end