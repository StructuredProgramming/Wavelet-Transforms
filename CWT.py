#Import pywt to compute CWT
import pywt
import numpy as np
import matplotlib.pyplot as plt
#time-space
time = np.linspace(0, 1, 200)
#Define our signal
signal = np.cos(2 * np.pi * 7 * time) + np.real(np.exp(-7 * (time-0.4)**2)*np.exp(1j*2*np.pi*2*(time-0.4)))
#Define the scales
scales = np.arange(1, 31)
#Finds the CWT Coefficients and corresponding frequencies
coefficients, frequencies = pywt.cwt(signal, scales, 'gaus1')
#Scalogram plot
plt.figure(figsize=(15, 10))
plt.imshow(abs(coefficients), extent=[0, 200, 30, 1], interpolation='bilinear', cmap='bone',
           aspect='auto', vmax=abs(coef).max(), vmin=abs(coef).max())
plt.gca().invert_yaxis()
plt.yticks(np.arange(1, 31, 1))
plt.xticks(np.arange(0, 201, 10))
plt.show()
plt.figure(figsize=(15, 10))
plt.plot(time, signal)
plt.grid(color='gray', linestyle=':', linewidth=0.5)
plt.show()
