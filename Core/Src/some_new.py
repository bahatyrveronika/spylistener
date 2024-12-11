import matplotlib.pyplot as plt
import librosa
import numpy as np


def read_frequencies_from_file(filename):
    """
    Зчитує частоти з текстового файлу.
    Кожен рядок у файлі повинен містити одну частоту.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    data_list = []
    for line in lines:
        value1, value2 = map(float, line.split(" "))
        data_list.append((value1, value2))
    return data_list


frequency_file = "/Users/veronikabagatyr-zaharcenko/STM32CubeIDE/workspace_1.16.1/our/Core/Src/results.txt"  # Ім'я файлу з частотами
frequencies = read_frequencies_from_file(frequency_file)
# Розбір даних напруги
voltages = np.array([float(tup[0]) for tup in frequencies[0::2]])
timestamps = np.array([float(tup[1]) for tup in frequencies[0::2]])

sampling_rate = 991


# Time axis in seconds based on timestamps and sampling rate
time = (timestamps - timestamps[0]) / sampling_rate  # Normalize to start at 0

S = librosa.feature.melspectrogram(y=voltages, sr=991, n_mels=1024, fmax=2000)
S_dB = librosa.power_to_db(S, ref=np.max)

plt.figure().set_figwidth(6)
librosa.display.specshow(S_dB, x_axis="time", y_axis="mel", sr=991, fmax=2000)
plt.colorbar()

plt.show()
