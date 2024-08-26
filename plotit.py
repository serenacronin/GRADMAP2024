# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:56:40 2024

@author: rhiai
"""

import matplotlib.pyplot as plt
import matplotlib.axes as ax

def ogplotit(galaxy_name, method, foundflux): #galaxy name and methods need to be in strings when calling function
    fig = plt.imshow (foundflux, origin = 'lower', cmap = 'inferno') #define the figure as the image with foundflux data, 0 at left and bottom, inferno color
    plt.colorbar(fig, fraction = 0.045, pad = 0.04, label = "Intensity [K km/s]") #creat a cbar that is .045 the size of the image and label it with units
    plt.title("%s %s" % (galaxy_name, method)) #create title as a string, %s tells it what to put for each string
    plt.savefig("%s_applied_mask_%s.png" % (galaxy_name, method)) #save the figure generated with the galaxy name at front and method at back, applied_mask in between, as a png
    return

def plotit(galaxy_name, method, foundflux):
    data = foundflux.data
    fix, ax = plt.subplots(figsize = [7,7])
    fig = ax.imshow(data, origin = "lower", cmap = "inferno")
    bar = plt.colorbar (fig, fraction = 0.045, pad = 0.04)
    bar.set_label("Intensity K" r"$\frac{km}{s}$", fontsize = 17)
    bar.ax.tick_params(labelsize = 14)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.title("%s %s" % (galaxy_name, method))
    plt.tight_layout()
    plt.savefig("%s_applied_mask_%s_mom0_map.png" % (galaxy_name, method))
    return