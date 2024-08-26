# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:38:24 2024

@author: rhiai
"""

from findflux import findflux

from savemask import savemask

from plotit import plotit  

from getdata import getcubedata as getcube
from getdata import getmaskdata as getmask
from getdata import getregrid
from getdata import getgalaxy

from regrid import regrid

from astropy.io import fits

def mkmoment0(galaxy_name, method, version): #everything needs to be a string, version just a number (still a string)
    cube = getcube(galaxy_name)
    mask = getmask(galaxy_name, method, version) #set mask variable as the data retrieved from getmask
    maskfile = ('mask_%s_%s_v%s.fits' % (galaxy_name, method, version)) #regrid needs just the name of the file, not the data, so set it as separate maskfile variable
    cubefile = ('%s_12CO_rebase5_smooth1.3_hanning2.fits' % (galaxy_name)) #same as mask file but w/ cubefile for regrid, just use strings properly
    regrid(maskfile, cubefile) #run the regrid; don't set it equal to a variable bc idk what the variable would return (name, data, etc.)
    rgcube = getregrid(galaxy_name) #define the rgcube (regridded cube) as the data retrieved from getregrid
    galaxy = getgalaxy(galaxy_name) #define the galaxy as the stuff returned from getgalaxy, which is hdr and stuff
    foundflux = findflux(mask, rgcube, galaxy) #the big boy; run the findflux function and set it as a variable you can use afterward
    plotit(galaxy_name, method, foundflux) #plot the foundflux function and save it
    savemask(foundflux, galaxy, galaxy_name, method) #save the foundflux function as a fits file
    return                                                                                                                                                          