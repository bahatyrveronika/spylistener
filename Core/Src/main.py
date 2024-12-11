import serial
import time

# Specify port and UART settings
uart_port = "/dev/tty.usbserial-1230"  # Check the correct port
baud_rate = 115200
timeout = 0.25  # Timeout for waiting for data

# Duration for collecting data (4 seconds)
duration = 10

try:
    # Open the UART port
    with serial.Serial(uart_port, baud_rate, timeout=timeout) as ser:
        # Open a file to write the data
        with open(
            "/Users/veronikabagatyr-zaharcenko/STM32CubeIDE/workspace_1.16.1/our/Core/Src/shum.txt",
            "w",
        ) as file:
            print("Waiting for data...")
            end_time = time.time() + duration
            counter = 1
            while time.time() < end_time:
                data = ser.readline().decode().strip()

                if data:
                    val = data.split(" ")[-1]
                    print(val)
                    values = (val) + " " + str(counter)
                    file.write(values + "\n")
                    file.flush()
                    counter += 1

except KeyboardInterrupt:
    print("Stopped by user.")
except serial.SerialException as e:
    print(f"Error with serial port: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("UART connection closed.")
