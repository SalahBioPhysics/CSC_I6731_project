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
                 'G_2015_229_0127_BU_N_VIR.mat',
                 'G_2015_229_0145_BU_T_MOD.mat',
                 'G_2015_229_0150_BU_T_MOD.mat',
                 'G_2015_229_0325_BU_T_MOD.mat',
                 'G_2015_229_0500_BU_T_MOD.mat',
                 'G_2015_229_0505_BU_T_MOD.mat',
                 'G_2015_229_0640_BU_T_MOD.mat',
                 'G_2015_229_0820_BU_T_MOD.mat',
                 'G_2015_229_0822_BU_N_VIR.mat',
                 'G_2015_229_1005_BU_N_VIR.mat',
                 'G_2015_229_1035_BU_A_MOD.mat',
                 'G_2015_229_1147_BU_N_VIR.mat',
                 'G_2015_229_1210_BU_A_MOD.mat',
                 'G_2015_229_1215_BU_A_MOD.mat',
                 'G_2015_229_1324_BU_N_VIR.mat',
                 'G_2015_229_1350_BU_A_MOD.mat',
                 'G_2015_229_1506_BU_N_VIR.mat',
                 'G_2015_229_1643_BU_N_VIR.mat',
                 'G_2015_229_1705_BU_A_MOD.mat',
                 'G_2015_229_1826_BU_N_VIR.mat',
                 'G_2015_229_1845_BU_A_MOD.mat',
                 'G_2015_229_2000_BU_T_MOD.mat',
                 'G_2015_229_2002_BU_N_VIR.mat',
                 'G_2015_229_2020_BU_A_MOD.mat',
                 'G_2015_229_2140_BU_T_MOD.mat',
                 'G_2015_229_2145_BU_N_VIR.mat',
                 'G_2015_229_2200_BU_A_MOD.mat',
                 'G_2015_229_2315_BU_T_MOD.mat',
                 'G_2015_229_2320_BU_T_MOD.mat',
                 'G_2015_229_2327_BU_N_VIR.mat',
                 ]


def load_mat_file(file_string):
    mat = scipy.io.loadmat(file_string)

    p_fc = mat['fc']
    fc1 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            fc1[i,j] = (p_fc[0,i,j])

    fc2 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            fc2[i,j] = (p_fc[1,i,j])


    fc3 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            fc3[i,j] = (p_fc[2,i,j])


    plt.subplot(231)
    plt.imshow(fc1)
    plt.title('fc1')

    plt.subplot(232)
    plt.imshow(fc2)
    plt.title('fc2')

    plt.subplot(233)
    plt.imshow(fc3)
    plt.title('fc3')

    plt.show()


for num in range(0,10):
    file = "mat_files/" + mat_file_list[num]
    load_mat_file(file)



