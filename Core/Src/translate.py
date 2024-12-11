import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Читання даних
with open(
    "/Users/veronikabagatyr-zaharcenko/STM32CubeIDE/workspace_1.16.1/our/Core/Src/gimn.txt",
    "r",
) as file:
    lines = file.readlines()

# Розбір даних напруги
voltages = [float(line.split()[0][-1:]) for line in lines]


sample_rate = 991  # частота дискретизації, Гц
time = np.linspace(0, len(voltages) / sample_rate, len(voltages))

# Модель синусоїди
def sinusoid(t, A, f, phi, C):
    return A * np.sin(2 * np.pi * f * t + phi) + C

# Початкові здогадки для параметрів
A_guess = (max(voltages) - min(voltages)) / 2  # амплітуда
f_guess = 991  # частота, Гц
phi_guess = 0  # початкова фаза
C_guess = np.mean(voltages)  # зсув

# Апроксимація (пошук параметрів синусоїди)
params, _ = curve_fit(sinusoid, time, voltages, p0=[A_guess, f_guess, phi_guess, C_guess])
A, f, phi, C = params

# Генерація синусоїди з отриманими параметрами
fitted_sinusoid = sinusoid(time, A, f, phi, C)

# Візуалізація
plt.figure(figsize=(10, 6))
plt.plot(time, voltages, label="Оригінальні дані", alpha=0.6)
plt.plot(time, fitted_sinusoid, label=f"Синусоїда (A={A:.2f}, f={f:.2f} Гц, φ={phi:.2f})", color="red")
plt.title("Перетворення сигналу в синусоїду")
plt.xlabel("Час (с)")
plt.ylabel("Напруга (В)")
plt.legend()
plt.grid()
plt.show()

# Частота дискретизації (ваша частота вимірів)
sample_rate = 991  # 2000 вибірок на секунду

# Нормалізація даних (-1 до 1)
min_v = min(voltages)
max_v = max(voltages)
normalized = [(2 * (v - min_v) / (max_v - min_v)) - 1 for v in voltages]

# Перетворення до float32 (формат для soundfile)
audio_data = np.array(normalized, dtype=np.float32)

# Запис у WAV файл
output_file = "/Users/veronikabagatyr-zaharcenko/STM32CubeIDE/workspace_1.16.1/our/Core/Src/output_soundfile.wav"
sf.write(output_file, audio_data, sample_rate)

print(f"Звуковий файл збережено як {output_file}")
