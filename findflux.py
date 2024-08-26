# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:33:43 2024

@author: rhiai
"""

import sys
sys.path.append('/Users/rhiai/gradmap24/')

from regrid import regrid

from astropy import units as u 
from astropy.io import fits
from astropy.utils import data

import numpy as np
import matplotlib.pyplot as plt
from spectral_cube import SpectralCube as spectralcube

def findflux(mask, cube, galaxy):
    (nv, ny, nx) = cube.shape
    newcube = np.full((ny, nx), np.nan) #create an array called newcube with dimensions ny, nx, and populate with nan
    vel_axis = mask[:, 1, 1].spectral_axis.to_value() #define the spectral (x) axis as velocity axis
    galaxy[0].header #take the index of the header of the galaxy given
    hdr = galaxy[0].header #define hdr as the header of the galaxy
    hdr["CDELT3"] #take CDELT3 value from the header
    cuw = abs(hdr["CDELT3"])/1000 #solve for channel width using abs value of CDELT3 and divide by 1000
    for i in range(nx):
        for j in range(ny):
            mvalues = mask[:, j, i] #define mvalues as the y axis of the mask along all channels and given j and i values
            if np.any(mvalues > 0): #conditional statement for any value where mvalues > 0
                ind = np.where(mvalues > 0) #define ind as the array generated from all values where mvalues > 0
                goodchan = vel_axis[ind] #define goodchan as the vel_axis values along the values given and make that an array
                v1 = np.min(goodchan) #define v1 as the minimum value in goodchan array since first and last might not be least and greates
                v2 = np.max(goodchan) #define v2 as the maximum value in goodchan array
                vel_axis_cube = cube[:, j, i].spectral_axis.to_value() #define vel_axis_cube as spectral axis of cube, to_value to get rid of units
                goodcubvel = vel_axis_cube[(vel_axis_cube > v1) & (vel_axis_cube < v2)] #define goodcubvel as the array of values for vel_axis_cube indexed along > v1 and < v2
                cubeflux = cube[:, j, i][(vel_axis_cube > v1) & (vel_axis_cube < v2)].to_value() #define cubeflux as the y axis of cube along all channels, j, i, indexed v_a_c > v1 and < v2, no units
                sumflux = np.sum(cubeflux) #sum up the values of cubeflux and define as sumflux
                newcube[j, i] = sumflux * cuw #populate the newcube with the sumflux multiplied by the cuw; multiply bc you want integrated intensity, and need to use summation of area under curve
            else: #if mvalue = 0, finishing conditional statement
                newcube[j, i] = 0 #populate the array value for that j and i with 0
    return newcube #need return for end of function, return the newcube that is being created by the function 