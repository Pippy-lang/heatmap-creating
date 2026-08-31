import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

file_path = input('Paste your file path:')
data = pd.read_excel(file_path,index_col = 0)
data1 = data.values


fig = plt.figure(figsize = (14,8), dpi = 200)
ax = fig.subplots()
im = ax.imshow(data1, cmap = 'plasma')
ax.set_xlabel('protein', fontsize = 20)
ax.set_ylabel('uniprot index', fontsize = 20)
idx = data.index
columns = data.columns
ax.set_xticks(ticks = np.arange(len(columns)), labels = columns, fontsize = 20)
ax.set_yticks(ticks = np.arange(len(idx)), labels = idx, fontsize = 20)
for i in range(len(columns)):
    for j in range(len(idx)):
        ax.text(i,j,data1[j,i], fontsize = 20, ha = 'center', va = 'center', rotation = 45)
color_bar = plt.colorbar(im, ax = ax)
title = input('enter a name for color bar:')
color_bar.ax.set_title(title, fontsize = 20)
plt.show()