import numpy as np

import matplotlib.pyplot as plt

# Parameters
duration = 1.0  # seconds
frequency = 440.0  # Hz
sampling_rate = 44100  # samples per second

# Generate time axis
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate sound wave
wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# Plot the wave
plt.plot(t, wave)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Generated Sound Wave')
plt.show()