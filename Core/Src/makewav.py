# import wave
# import numpy as np


# def read_frequencies_from_file(filename):
#     """
#     Зчитує частоти з текстового файлу.
#     Кожен рядок у файлі повинен містити одну частоту.
#     """
#     with open(filename, "r") as file:
#         frequencies = [float(line.strip()) for line in file if line.strip()]
#     return frequencies

# frequency_file = "/Users/veronikabagatyr-zaharcenko/STM32CubeIDE/workspace_1.16.1/our/Core/Src/results.txt"  # Ім'я файлу з частотами
# frequencies = read_frequencies_from_file(frequency_file)

# # Параметри синусоїдальної хвилі
# duration_sec = 0.002  # Тривалість кожного тону (в секундах)
# rate = 2000  # Частота дискретизації (зразки на секунду)


# # Генерація звукового сигналу для кожної частоти
# combined_wave = np.array([], dtype=np.int16)
# for frequency in frequencies:
#     # Генерація часу для звукової хвилі
#     t = np.linspace(0, duration_sec, int(rate * duration_sec), endpoint=False)
#     # Генерація синусоїдальної хвилі
#     amplitude = np.sin(2 * np.pi * frequency * t)
#     # Нормалізація значень для 16-бітного аудіо
#     amplitude = np.int16(amplitude * 32767)
#     # Додавання до загального сигналу
#     combined_wave = np.append(combined_wave, amplitude)

# # Створення WAV файлу
# output_file = "output_sine_wave.wav"
# with wave.open(output_file, "wb") as wav_file:
#     wav_file.setnchannels(1)  # Моно звук (1 канал)
#     wav_file.setsampwidth(2)  # 16-бітне аудіо (2 байти на зразок)
#     wav_file.setframerate(rate)  # Частота дискретизації
#     wav_file.writeframes(combined_wave.tobytes())  # Записуємо дані у WAV файл

# print(f"WAV файл створено: {output_file}")
# # import wave
# # import numpy as np

# # # Параметри синусоїдальної хвилі
# # frequency = 440.0  # Частота (наприклад, 440 Гц для ноти Ля)
# # duration_sec = 10  # Тривалість звуку (в секундах)
# # rate = 44100  # Частота дискретизації (зразки на секунду)

# # # Генерація часу для звукової хвилі
# # t = np.linspace(0, duration_sec, int(rate * duration_sec), endpoint=False)

# # # Генерація синусоїдальної хвилі
# # amplitude = np.sin(2 * np.pi * frequency * t)

# # # Нормалізація значень для 16-бітного аудіо
# # amplitude = np.int16(amplitude * 32767)

# # # Створення WAV файлу
# # with wave.open("output_sine_wave.wav", "wb") as wav_file:
# #     wav_file.setnchannels(1)  # Моно звук (1 канал)
# #     wav_file.setsampwidth(2)  # 16-бітне аудіо (2 байти на зразок)
# #     wav_file.setframerate(rate)  # Частота дискретизації
# #     wav_file.writeframes(amplitude.tobytes())  # Записуємо дані у WAV файл

# # print("WAV файл створено.")


def read_frequencies_from_file(filename):
    """
    Зчитує частоти з текстового файлу.
    Кожен рядок у файлі повинен містити одну частоту.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    data_list = []
    for line in lines:
        value1, value2 = map(float, line.split(" "))
        data_list.append((value1, value2))
    return data_list

frequency_file = "/Users/veronikabagatyr-zaharcenko/STM32CubeIDE/workspace_1.16.1/our/Core/Src/results.txt"  # Ім'я файлу з частотами
frequencies = read_frequencies_from_file(frequency_file)

import numpy as np
import scipy.io.wavfile


# Function to convert microseconds to milliseconds
def us_to_ms(us):
    return us / 1000.0

data_array = read_frequencies_from_file(frequency_file)

# Separate the value and time_us
values = [item[0]*100 for item in data_array]
time_ms = [item[1] for item in data_array]

# Convert time_us to time_ms

# Append to the respective lists
y_data = values  # Assuming `y_data` is already declared as list
x_time = time_ms  # Assuming `x_time` is already declared as list

samplerate = 1000 * len(y_data) / time_ms[-1]  # last time_ms value used for duration

wav_wave = np.int16(y_data)

# scaling around the mean
mean = int(sum(wav_wave) / len(wav_wave))
print("Mean:", mean, len(wav_wave))
wav_wave = wav_wave - mean

# scaling the wave:
scaler = int((30000 // 2) / max([abs(min(wav_wave)), max(wav_wave)]))
wav_wave *= scaler

print("scaler:", scaler)

# converting to wav
scipy.io.wavfile.write("received.wav", int(samplerate), wav_wave)