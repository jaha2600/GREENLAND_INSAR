#%%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from mpl_toolkits.basemap import basemap

# %%
filename = 'file.csv'
readcsv = pd.read_csv(filename)

#%%
lat = readcsv.latitude
lon = readcsv.longitude
east = readcsv.East
north = readcsv.North

#%% check components to get the right things (stephanies email)

