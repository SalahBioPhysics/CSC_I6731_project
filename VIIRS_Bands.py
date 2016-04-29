import random
import sys
import os
import scipy.io
import numpy as np
import h5py
from matplotlib import pyplot as plt
import urllib

mat_file_list = ['G_2015_229_0127_BU_N_VIR.mat',
                 'G_2015_229_0822_BU_N_VIR.mat',
                 'G_2015_229_1005_BU_N_VIR.mat',
                 'G_2015_229_1147_BU_N_VIR.mat',
                 'G_2015_229_1324_BU_N_VIR.mat',
                 'G_2015_229_1506_BU_N_VIR.mat',
                 'G_2015_229_1643_BU_N_VIR.mat',
                 'G_2015_229_1826_BU_N_VIR.mat',
                 'G_2015_229_2002_BU_N_VIR.mat',
                 'G_2015_229_2145_BU_N_VIR.mat',
                 'G_2015_229_2327_BU_N_VIR.mat',
                 ]


def load_mat_file(file_string):
    mat = scipy.io.loadmat(file_string)

    p_ib = mat['ibands']
    iband1 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            iband1[i,j] = (p_ib[0,i,j])

    plt.subplot(231)
    plt.imshow(iband1)
    plt.title('iband1')

    iband2 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            iband2[i,j] = (p_ib[1,i,j])

    plt.subplot(232)
    plt.imshow(iband2)
    plt.title('iband2')

    iband3 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            iband3[i,j] = (p_ib[2,i,j])

    plt.subplot(233)
    plt.imshow(iband3)
    plt.title('iband3')

    p_mb = mat['mbands']
    mband1 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            mband1[i,j] = (p_mb[0,i,j])

    plt.subplot(234)
    plt.imshow(mband1)
    plt.title('mband1')

    mband2 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            mband2[i,j] = (p_mb[1,i,j])

    plt.subplot(235)
    plt.imshow(mband2)
    plt.title('mband2')

    mband3 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            mband3[i,j] = (p_mb[2,i,j])

    plt.subplot(236)
    plt.imshow(mband3)
    plt.title('mband3')

    plt.show()


for num in range(0,10):
    file = "mat_files/" + mat_file_list[num]
    load_mat_file(file)



