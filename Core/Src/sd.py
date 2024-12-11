import numpy as np
import sounddevice as sd

# Завантаження даних із файлу
data = np.loadtxt(
    "/Users/veronikabagatyr-zaharcenko/STM32CubeIDE/workspace_1.16.1/our/Core/Src/results.txt"
)

# Обираємо першу колонку (виміри)
measurements = data[:, 0]  # Перший стовпець (виміри)

# Оригінальна частота дискретизації
original_sampling_rate = 991  # Гц (на основі ваших даних)

# Нова частота дискретизації для відтворення
new_sampling_rate = 8000  # Наприклад, 8000 Гц

# Перемасштабування даних до нової частоти
factor = new_sampling_rate / original_sampling_rate
new_length = int(len(measurements) * factor)
data_resampled = np.interp(
    np.linspace(0, len(measurements) - 1, new_length),
    np.arange(len(measurements)),
    measurements,
)

# Нормалізуємо дані (масштабуємо значення до [-1, 1])
data_normalized = data_resampled / np.max(np.abs(data_resampled))

# Відтворення звуку
sd.play(data_normalized, samplerate=new_sampling_rate)
sd.wait()
