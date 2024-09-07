
# **ARGOS - Autonomous Robot for Guidance, Operation, and Safety**

### **Overview**
ARGOS is an autonomous robot designed for indoor navigation, guidance, and operational tasks, utilizing cutting-edge technologies like ROS2 Galactic, Picovoice, and ChatGPT for intelligent interaction. The robot is powered by a Raspberry Pi 4, equipped with a YDLIDAR X2 for environment mapping, and controlled via a FlutterFlow-based mobile app with Flask as the backend for communication. NGrok is used for secure localhost forwarding, allowing remote access to ARGOS’ control functions.

---

### **Features**
- **ROS2 Galactic**: Provides the core robotics framework for navigation and task execution.
- **Flask API**: A lightweight web API that allows external systems to send navigation commands to ARGOS.
- **Picovoice**: Enables wake word detection and speech-to-intent functionality for voice control.
- **NGrok Integration**: Allows secure access to the robot’s control interface over the internet.
- **FlutterFlow App**: A mobile app interface that allows users to send commands and monitor the robot’s status remotely.
- **YDLIDAR X2**: Used for precise mapping and localization of the robot within its environment.
- **ChatGPT for Emotional Intelligence**: Enables ARGOS to engage in emotionally intelligent conversations, enhancing human-robot interaction.
- **Raspberry Pi 4**: Acts as the central processing unit, managing the robot’s hardware and software components.

---

### **Installation**

#### 1. **Setting Up Flask**
Flask serves as the web API for communication between the robot and external systems.

- **Install Flask and Flask-CORS**:
   ```bash
   pip install flask flask-cors
   ```

- **Basic Flask Structure**:
   Here’s a simple structure for setting up the Flask server:
   ```python
   from flask import Flask, jsonify, request
   from flask_cors import CORS

   app = Flask(__name__)
   CORS(app)

   @app.route('/move_robot', methods=['POST'])
   def move_robot():
       data = request.json
       room_name = data.get('room_name')
       return jsonify({"status": "success", "message": f"Moving to {room_name}"})

   if __name__ == '__main__':
       app.run(debug=True, port=5555)
   ```

#### 2. **Installing Picovoice (Wake Word & Speech-to-Intents)**
Picovoice provides the wake word detection and intent recognition features.

- **Install the Picovoice SDK**:
   First, follow the instructions on the official [Picovoice GitHub](https://github.com/Picovoice/porcupine) to install the Porcupine SDK.

- **Install Python SDK**:
   ```bash
   pip install pvporcupine
   ```

- **Using Picovoice in Python**:
   Set up a wake word detection system:
   ```python
   import pvporcupine
   import pyaudio

   porcupine = pvporcupine.create(keywords=["picovoice"])

   pa = pyaudio.PyAudio()

   stream = pa.open(
       format=pyaudio.paInt16,
       channels=1,
       rate=porcupine.sample_rate,
       input=True,
       frames_per_buffer=porcupine.frame_length)

   while True:
       pcm = stream.read(porcupine.frame_length)
       pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

       keyword_index = porcupine.process(pcm)
       if keyword_index >= 0:
           print("Wake word detected!")
   ```

#### 3. **Setting Up NGrok for Localhost Forwarding**
NGrok allows you to expose your Flask server to the internet securely.

- **Download and Install NGrok**:
   Visit [NGrok’s official website](https://ngrok.com/) to download and install it.
   
   Once installed, you can expose your Flask server by running:
   ```bash
   ngrok http 5555
   ```

   This will give you a public URL that you can use to access your Flask server from anywhere.

---

### **Usage**

1. **Run the ROS2 Node**:
   Start the goal pose publisher node by running the ROS2 script for sending navigation commands to ARGOS.

2. **Run the Flask Server**:
   Start the Flask server:
   ```bash
   python3 app.py
   ```
   With NGrok, the server will be accessible remotely via the public URL.

3. **Send Commands to ARGOS**:
   Use the FlutterFlow app or a POST request to send a room name:
   ```bash
   curl -X POST http://your-ngrok-url/move_robot -H "Content-Type: application/json" -d '{"room_name": "room305"}'
   ```

---

### **Future Enhancements**
- **Dynamic Voice Command Recognition**: Add more intents and commands for a wider range of voice-controlled functionalities.
- **Real-Time Mapping**: Enhance mapping capabilities using additional sensors and algorithms.
- **Mobile App**: Improve the mobile app’s user interface and add more control options.

---

### **Contributing**
Contributions are welcome! Please feel free to submit pull requests to help improve the ARGOS project.

---

### **License**
This project is licensed under the MIT License.
