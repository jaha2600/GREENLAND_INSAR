#%%
import numpy as np
import pandas as pd
import rasterio
from affine import Affine

dat = pd.read_table("/home/jasmine/JasmineShare/kanger/mintpy_summit/dis_vel.csv", sep=" ,", header=True, dtype=float, low_memory=False)
xmin = dat[0].min()
xmax = dat[0].max()
ymin = dat[1].min()
ymax = dat[1].max()
dx = dat[0].drop_duplicates().sort_values().diff().median()
dy = dat[1].drop_duplicates().sort_values().diff().median()
xv = pd.Series(np.arange(xmin, xmax + dx, dx))
yv = pd.Series(np.arange(ymin, ymax + dy, dy)[::-1])
xi = pd.Series(xv.index.values, index=xv)
yi = pd.Series(yv.index.values, index=yv)
nodata = -9999.
zv = np.ones((len(yi), len(xi)), np.float32) * nodata
zv[yi[dat[1]].values, xi[dat[0]].values] = dat[2]
#%%
# register geotransform based on upper-left corner
transform = Affine(dx, 0, xmin, 0, -dy, ymax) * Affine.translation(-0.5, -0.5)
with rasterio.open("file.tif", "w", "GTiff", len(xi), len(yi), 1, "EPSG:????",
                   transform, rasterio.float32, nodata) as ds:
    ds.write(zv.astype(np.float32), 1)