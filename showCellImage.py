# Plot the slices of the cell image
# Author : Arijit Dutta
# Last modified : 28-03-2022

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

filename = 'MMD-5_32.npy' # Only .npy files supported

d = np.load(filename, allow_pickle=True, fix_imports=True)

shape = np.shape(d)
print(shape)

L = int(shape[0])

fig, ax = plt.subplots(4,8, sharex=True, sharey=True, figsize=(16,8))
for i in range(L):
		row = int(i%4)
		col = int(i/4)
		A = d[:,:,i,0]
		im = ax[row,col].imshow(A, origin='lower', extent=[1, 32, 1, 32], norm=colors.Normalize(vmin=0, vmax=1, clip=True))
		cbar = fig.colorbar(im, ax=ax[row,col], fraction=0.045, location='top', pad=0.01)
		cbar.ax.tick_params(labelsize=12)

		ax[row,col].tick_params(direction='in', labelsize=14, color='white')

fig.tight_layout()
plt.show()
