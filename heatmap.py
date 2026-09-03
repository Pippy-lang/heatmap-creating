import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
file_path = input('enter the file path: ')
data = pd.read_excel(file_path, index_col = 0)
data1 = data.values
fig = plt.figure(figsize = (14,8), dpi = 200)
ax = fig.subplots()
if input('Set a default color?[y/n]') == 'y':
    my_color = [input('choose a color for high data:'),
                input('choose a color for medium data:'),
                input('choose a color for low data:'),]
    im = plt.imshow(data1,
                cmap = LinearSegmentedColormap.from_list('my_colormap', my_color) )
else:
    my_color = 'plasma'
    im = plt.imshow(data1, cmap = 'plasma')
ax.set_title(input('enter the title: '), fontsize = 10)
xlabel = input('enter the x label: ')
ax.set_xlabel(xlabel, fontsize=10)
ylabel = input('enter the y label: ')
ax.set_ylabel(ylabel, fontsize=10)
idx = data.index
columns = data.columns
ax.set_xticks(ticks = np.arange(len(columns)), labels = columns, fontsize = 10)
ax.set_yticks(ticks = np.arange(len(idx)), labels = idx, fontsize = 10)
color_bar = plt.colorbar(im, ax=ax)
title = input('enter the title for colar bar: ')
color_bar.ax.set_title(title, fontsize = 10)
plt.show()