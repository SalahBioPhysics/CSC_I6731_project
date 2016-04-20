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
    print mat.keys()

    p_temp = mat['temp'] # Ice Surface Temperature
    plt.subplot(231)
    plt.imshow(p_temp)
    plt.title('temp')


    p_sic = mat['mw_sic']  # Microwave Sea Ice Concentration (Height,Width)
    plt.subplot(232)
    plt.imshow(p_sic)
    plt.title('mw_sic')


    p_sic = mat['mw_ngr']
    plt.subplot(233)
    plt.imshow(p_sic)
    plt.title('mw_ngr')

    p_sic = mat['mw_npr']
    plt.subplot(234)
    plt.imshow(p_sic)
    plt.title('mw_npr')

    p_sic = mat['lm']
    plt.subplot(235)
    plt.imshow(p_sic)
    plt.title('lm')


    plt.show()

    #f = h5py.File(file_string, 'r')
    #data = f.get('mw_sic')
    #data = np.array(data)  # For converting to numpy array

for num in range(0,10):
    file = "mat_files/" + mat_file_list[num]
    load_mat_file(file)



