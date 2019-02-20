import wave
import struct
import numpy as np
# frequency is the number of times a wave repeats a second
 
frequency = 1000
 
noisy_freq = 50
 
num_samples = 48000
 
# The sampling rate of the analog to digital convert
 
sampling_rate = 48000.0


#Create the sine wave and noise
 
sine_wave = [np.sin(2 * np.pi * frequency * x1 / sampling_rate) for x1 in range(num_samples)]
 
sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/  sampling_rate) for x1 in range(num_samples)]
 
#Convert them to numpy arrays
 
sine_wave = np.array(sine_wave)
 
sine_noise = np.array(sine_noise)

# Add them to create a noisy signal
 
combined_signal = sine_wave + sine_noise

data_fft = np.fft.fft(combined_signal)
 
freq = (np.abs(data_fft[:len(data_fft)]))

filtered_freq = []
 
index = 0

for f in freq:
    # Filter between lower and upper limits
    # Choosing 950, as closest to 1000. In real world, won't get exact numbers like these
    if index > 950 and index < 1050:
        # Has a real value. I'm choosing >1, as many values are like 0.000000001 etc
        if f > 1:
            filtered_freq.append(f)
 
        else:
            filtered_freq.append(0)
    else:
        filtered_freq.append(0)
    index += 1
recovered_signal = np.fft.ifft(filtered_freq)
# filtered_freq = [f if (950 < index < 1050 and f > 1) else 0 for index, f in enumerate(freq)]
