# Raspberry-Pi-Object-detection-using-YOLOv8-and-Bluetooth-communication

This project uses the YOLOv8 object detection model on a Raspberry Pi to detect objects in real-time using a webcam. When a "stop sign" is detected, a Bluetooth signal is sent to a paired Bluetooth device (such as an HC-05 module connected to an Arduino board) for further actions such as collision prevention or road signal sensing.

## Features

- Real-time object detection using the YOLOv8 model.
- Detection of multiple objects from the COCO dataset.
- Bluetooth communication with other devices to perform actions based on object detection.
- Adjustable detection confidence threshold.
- Configurable frame size for optimization.

## Requirements

- Raspberry Pi 4
- Python 3.x
- Webcam or camera module connected to Raspberry Pi.
- HC-05 module connected to Arduino board for receiving Bluetooth signals (or another Bluetooth receiver).
- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8 model.
- PyBluez for Bluetooth communication.
- Other dependencies listed in the code.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Varsha02nats/Raspberry-Pi-Object-detection-using-YOLOv8-and-Bluetooth-communication.git
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Install the BlueZ library with the following command:
    ```bash
    sudo apt install bluetooth pi-bluetooth bluez blueman
    ```

4. Ensure that the Raspberry Pi is paired with the desired Bluetooth receiver (e.g., HC-05 module).

## Usage

1. Connect the camera module (webcam) to the Raspberry Pi.

2. Configure the Bluetooth connection:
    - Ensure the Raspberry Pi is paired with the Bluetooth receiver (e.g., HC-05 module connected to Arduino).
    - Modify the Bluetooth serial port (`/dev/rfcomm4`) in the script if necessary.
    - If HC-05 is used, then make sure to set it as 'slave' before pairing it to the raspberry pi.

3. Place the `coco.txt` file in the `utils` directory to use the trained object models.

4. Run the script on the Raspberry Pi:
    ```bash
    python3 object_detection.py
    ```

5. Once the script is running, the camera will start detecting objects in real-time. When a "stop sign" is detected, a Bluetooth signal will be sent to the paired Bluetooth device.

6. Use the Bluetooth receiver to handle the signal for further actions such as collision prevention.

7. Press 'Q' in the video display window to stop the program and exit.

NOTE: btsample.py can be used in raspberry pi to check if the bluetooth module receives a given input from raspberry pi.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for using the YOLOv8 Raspberry Pi Object Detection project! If you have any questions or feedback, feel free to open an issue on GitHub.
