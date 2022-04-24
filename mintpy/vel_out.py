#%%
import os
import numpy as np
import matplotlib.pyplot as plt
from mintpy.objects import ifgramStack
from mintpy.utils import plot as pp, utils as ut
from mintpy import view, plot_network
from mintpy.unwrap_error_phase_closure import plot_num_triplet_with_nonzero_integer_ambiguity

# %%
dirs = '/home/jasmine/JasmineShare/kanger/mintpy/'
os.chdir(dirs)
#%%
view.main('geo/geo_velocity.h5 velocity -v -0.5 0.5 --noverbose -c BlueWhiteOrangeRed'.split())
#view.main('velocityERA5.h5 --notick --noaxis --noverbose'.split())

# %%
