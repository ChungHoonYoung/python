# """
# ========================
# Visualizing named colors
# ========================

# Simple plot example with the named colors and its visual representation.
# """
# from __future__ import division

# import matplotlib.pyplot as plt
# from matplotlib import colors as mcolors


# colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# # Sort colors by hue, saturation, value and name.
# by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
#                 for name, color in colors.items())
# sorted_names = [name for hsv, name in by_hsv]

# n = len(sorted_names)
# ncols = 4
# nrows = n // ncols + 1

# fig, ax = plt.subplots(figsize=(8, 5))

# # Get height and width
# X, Y = fig.get_dpi() * fig.get_size_inches()
# h = Y / (nrows + 1)
# w = X / ncols

# for i, name in enumerate(sorted_names):
#     col = i % ncols
#     row = i // ncols
#     y = Y - (row * h) - h

#     xi_line = w * (col + 0.05)
#     xf_line = w * (col + 0.25)
#     xi_text = w * (col + 0.3)

#     ax.text(xi_text, y, name, fontsize=(h * 0.8),
#             horizontalalignment='left',
#             verticalalignment='center')

#     ax.hlines(y + h * 0.1, xi_line, xf_line,
#               color=colors[name], linewidth=(h * 0.6))

# ax.set_xlim(0, X)
# ax.set_ylim(0, Y)
# ax.set_axis_off()

# fig.subplots_adjust(left=0, right=1,
#                     top=1, bottom=0,
#                     hspace=0, wspace=0)
# plt.show()


# # 색상코드표 출력
# import matplotlib.colors
# import numpy as np 

# for key, hex_value in matplotlib.colors.CSS4_COLORS.items():
#     print("%20s : #%6s" % (key, hex_value))

"""
========================
Visualizing named colors
========================

Simple plot example with the named colors and its visual representation.
"""
from __future__ import division

import matplotlib.pyplot as plt
import numpy as np 
from matplotlib import colors as mcolors



colors = dict(**mcolors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())

sorted_names = [name for hsv, name in by_hsv]

n = len(sorted_names)
ncols = 4
nrows = n // ncols + 1

fig, ax = plt.subplots(figsize=(12, 23), dpi=200)

# Get height and width
X, Y = fig.get_dpi() * fig.get_size_inches()
h = 40 #Y / (nrows + 1)
w = X / ncols

for i, name in enumerate(sorted_names):
    col = i % ncols
    row = i // ncols
    y = Y - 3*(row * h) - h*3

    xi_line = w * (col + 0.05)
    xf_line = w * (col + 0.25)
    xi_text = w * (col + 0.3)

    # [R,G,B] + color_name 
    rgb_value = [n*255 for n in mcolors.to_rgb(name)]
    hex_value = mcolors.to_hex(name)
    color_name = "RGB  : " + str(rgb_value) + "\nHEX  : " + str(hex_value) + "\nNAME: " + name 
    color_name = color_name.replace(".0","")
    ax.text(xi_text, y, color_name, fontsize=(10),
            horizontalalignment='left',
            verticalalignment='center')

    ax.hlines(y, xi_line, xf_line,
              color=colors[name], linewidth=(30))


ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()
ax.set_title("[Matplotlib Named Colors]", fontsize=25)
ax.text(x=X*0.96, y=Y*0.99, s="[HEXA-CODING] https://hexa-coding.tistory.com", ha='right', va='center', color='gray', fontsize=9)
fig.subplots_adjust(left=0, right=1,
                    top=1, bottom=0,
                    hspace=0, wspace=0)
plt.show()
fig.savefig("./named_colors_mpl.png", bbox_inches = 'tight')