import random
import sys
import os
import scipy.io
import numpy as np
import h5py
from matplotlib import pyplot as plt
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


def load_mat_file(file_string):
    mat = scipy.io.loadmat(file_string)

    p_ref = mat['ref']
    band1 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            band1[i,j] = (p_ref[0,i,j])

    plt.subplot(231)
    plt.imshow(band1)
    plt.title('band1')

    band2 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            band2[i,j] = (p_ref[1,i,j])

    plt.subplot(232)
    plt.imshow(band2)
    plt.title('band2')

    band3 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            band3[i,j] = (p_ref[2,i,j])

    plt.subplot(233)
    plt.imshow(band3)
    plt.title('band3')

    band4 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            band4[i,j] = (p_ref[3,i,j])

    plt.subplot(234)
    plt.imshow(band4)
    plt.title('band4')

    band5 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            band5[i,j] = (p_ref[4,i,j])

    plt.subplot(235)
    plt.imshow(band5)
    plt.title('band5')

    band6 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            band6[i,j] = (p_ref[5,i,j])

    plt.subplot(236)
    plt.imshow(band6)
    plt.title('band6')

    plt.show()


for num in range(0,10):
    file = "mat_files/" + mat_file_list[num]
    load_mat_file(file)



