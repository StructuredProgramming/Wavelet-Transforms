#Discrete Wavelet Transform of ElectroCardiogram

import numpy as np
import pywt
from skimage.restoration import denoise_wavelet
import matplotlib.pyplot as plt
x = pywt.data.ecg().astype(float)/256
sigma = 0.05
x_noisy = x + sigma * np.random.randn(x.size) 
x_denoise = denoise_wavelet(x_noisy, method='BayesShrink', mode='soft', wavelet_levels=3, wavelet='sym8', rescale_sigma='True')
plt.figure(figsize=(20, 10), dpi=100)
plt.plot(x_noisy)
plt.plot(x_denoise)
plt.show()
