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


def histogram_matching(img1,img2):
    shape = img1.shape
    src = img1.ravel()
    dest = img2.ravel()

    src_values, bin_idx, src_counts = np.unique(src, return_inverse=True, return_counts=True)
    dest_values, dest_counts = np.unique(dest, return_counts=True)

    src_qntl = np.cumsum(src_counts).astype(np.float64)
    src_qntl /= src_qntl[-1]
    dest_qntl = np.cumsum(dest_counts).astype(np.float64)
    dest_qntl /= dest_qntl[-1]

    interp_dest_values = np.interp(src_qntl, dest_qntl, dest_values)

    return interp_dest_values[bin_idx].reshape(shape)


def load_mat_file(file_string):
    mat = scipy.io.loadmat(file_string)

    p_ib = mat['ibands']
    iband1 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            iband1[i,j] = (p_ib[0,i,j])


    iband2 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            iband2[i,j] = (p_ib[1,i,j])


    iband3 = np.zeros((2000,2000))
    for i in np.arange(2000):
        for j in np.arange(2000):
            iband3[i,j] = (p_ib[2,i,j])
    
    
    # Perform histogram matching on the three ibands.
    hm1 = histogram_matching(iband1,iband2)
    hm2 = histogram_matching(hm1,iband3)

    # Calculate and plot the i band histograms.
    hist1,bins1 = np.histogram(iband1.flatten(),256,normed=True)
    hist2,bins2 = np.histogram(iband2.flatten(),256,normed=True)
    hist3,bins3 = np.histogram(iband3.flatten(),256,normed=True)
    hist4,bins4 = np.histogram(hm2.flatten(),256,normed=True)
    plt.subplot(231)
    plt.plot(hist1, '-b')
    plt.plot(hist2, '-r')
    plt.plot(hist3, '-y')
    plt.plot(hist4, '--k')
    plt.legend(('iband1','iband2','iband3','hist match'), loc = 'upper right')
    plt.title('I Band Histograms')

    # Calculate and plot the i band cdf. 
    cdf1 = hist1.cumsum()
    cdf_norm1 = cdf1 * hist1.max()/ cdf1.max()
    cdf2 = hist2.cumsum()
    cdf_norm2 = cdf2 * hist2.max()/ cdf2.max()
    cdf3 = hist3.cumsum()
    cdf_norm3 = cdf3 * hist3.max()/ cdf3.max()
    cdf4 = hist4.cumsum()
    cdf_norm4 = cdf4 * hist4.max()/ cdf4.max()
    plt.subplot(232)
    plt.plot(cdf_norm1, '-b')
    plt.plot(cdf_norm2, '-r')    
    plt.plot(cdf_norm3, '-y')
    plt.plot(cdf_norm4, '--k')
    plt.legend(('iband1','iband2','iband3','hist match'), loc = 'lower right')
    plt.title('I Band cdf')

    # Display the i band histogram matching result.
    plt.subplot(233)
    plt.imshow(hm2)
    plt.title('I Band Histogram Matching')
    plt.colorbar()

    plt.show()


for num in range(0,10):
    file = "mat_files/" + mat_file_list[num]
    load_mat_file(file)



