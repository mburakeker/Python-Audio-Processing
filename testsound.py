import sys
import alsaaudio

import numpy as np
 
import wave
 
import struct



if __name__ == '__main__':

    	frequency = 1000
 
	num_samples = 3000
	 
	sampling_rate = 48000.0
	 
	amplitude = 32000
	periodsize = 1024

	sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]
	

	nframes=num_samples
	nchannels=1
	sampwidth=2
	device = 'default'

	device = alsaaudio.PCM(device=device)
	device.setchannels(nchannels)
	device.setrate(amplitude)
	device.setformat(alsaaudio.PCM_FORMAT_S16_LE)

	

	device.setperiodsize(periodsize)
	for s in sine_wave:
		device.write(s)


