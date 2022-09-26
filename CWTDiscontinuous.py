import pywt
import numpy as np
import matplotlib.pyplot as plt
samplesPerSecond = 44100.0  
signalLengthOfTime = 10e-3
numSeconds = np.int(samplesPerSecond*signalLengthOfTime)
tpoints = np.linspace(0, 10e-3, numSeconds) 
x = np.cos(2*np.pi*500*tpoints)
scales = np.arange(1, 21, 1)
x[87:89] = 0
x[307:309] = 0  
coefficients, freqs = pywt.cwt(x, scales, 'gaus4')  
#Plot scalogram
plt.figure(figsize=(15, 10))
plt.imshow(abs(coefficients), extent=[0, 10e-3, 20, 1], interpolation='bilinear', cmap='copper',
           aspect='auto', vmax=abs(coefficients).max(), vmin=abs(coefficients).max())
plt.gca().invert_yaxis()
plt.yticks(np.arange(1, 21, 1))
plt.xticks(np.arange(0, numSeconds/samplesPerSecond, numSeconds/(20*samplesPerSecond)))
plt.show()
plt.figure(figsize=(15, 10))
plt.plot(tpoints, x)
plt.grid(color='gray', linestyle=':', linewidth=0.5)
plt.show()
