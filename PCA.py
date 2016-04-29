import random
import sys
import os
import scipy.io
import numpy as np
import h5py
from matplotlib import pyplot as plt
from matplotlib.mlab import PCA
import urllib

mat_file_list = ['G_2015_229_0010_BU_T_MOD.mat',
                 'G_2015_229_0015_BU_T_MOD.mat',
                 'G_2015_229_0030_BU_A_MOD.mat',
                 'G_2015_229_0035_BU_A_MOD.mat',
                 'G_2015_229_0145_BU_T_MOD.mat',
                 'G_2015_229_0150_BU_T_MOD.mat',
                 'G_2015_229_0325_BU_T_MOD.mat',
                 'G_2015_229_0500_BU_T_MOD.mat',
                 'G_2015_229_0505_BU_T_MOD.mat',
                 'G_2015_229_0640_BU_T_MOD.mat',
                 'G_2015_229_0820_BU_T_MOD.mat',
                 'G_2015_229_1035_BU_A_MOD.mat',
                 'G_2015_229_1210_BU_A_MOD.mat',
                 'G_2015_229_1215_BU_A_MOD.mat',
                 'G_2015_229_1350_BU_A_MOD.mat',
                 'G_2015_229_1705_BU_A_MOD.mat',
                 'G_2015_229_1845_BU_A_MOD.mat',
                 'G_2015_229_2000_BU_T_MOD.mat',
                 'G_2015_229_2020_BU_A_MOD.mat',
                 'G_2015_229_2140_BU_T_MOD.mat',
                 'G_2015_229_2200_BU_A_MOD.mat',
                 'G_2015_229_2315_BU_T_MOD.mat',
                 'G_2015_229_2320_BU_T_MOD.mat',
                 ]


def pca(bands):
    band_mtrx = np.array([np.array((bands[i])).flatten()
                  for i in range(2)], 'f')

    mean = band_mtrx.mean(axis=0)
    band_mtrx = band_mtrx - mean
    M = np.dot(band_mtrx,band_mtrx.T)
    e,ev = np.linalg.eigh(M)
    tmp = np.dot(band_mtrx.T,ev).T
    v = tmp[::-1]
    s = np.sqrt(e)[::-1]
    for i in range(v.shape[1]):
        v[:,i] /= s

    return mean


def load_mat_file(file_string):
    mat = scipy.io.loadmat(file_string)

    p_ref = mat['ref']

    band1 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            band1[i,j] = (p_ref[0,i,j])

    
    band3 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            band3[i,j] = (p_ref[2,i,j])


    band4 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            band4[i,j] = (p_ref[3,i,j])

    
    band_set1 = [band1,band4,]
    m1 = pca(band_set1)
    band_set2 = [m1,band3,]
    m2 = pca(band_set2)
    
    plt.imshow(m2.reshape(2000,2000))
    plt.title('PCA')
    plt.colorbar()

    plt.show()


for num in range(0,10):
    file = "mat_files/" + mat_file_list[num]
    load_mat_file(file)



