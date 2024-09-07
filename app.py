from flask import Flask, jsonify,request,Response
from flask_cors import CORS
from goal_pose_test import GoalPosePublisher
import rclpy

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for all routes

rclpy.init()
goal = GoalPosePublisher()

@app.route("/room_nav_no",methods=["POST"])
def room_naviation():

    data = request.json
    room_no = data.get("room_number")

    if room_no:

        print("Robot Moving to Room 305")
        # goal.post_goal(room_name=room_no)
        return jsonify({"status": "success", "message": "Moving To 305"})
    else:
        return jsonify({"status": "error", "message": "Room name not provided"}), 400



# @app.route('/room_305', methods=['POST'])
# def button1():

#     print("Robot Moving to Room 305")
#     goal.post_goal("room305")
    
#     # print("Button was pressed!")
#     return jsonify({"status": "success", "message": "Moving To 305"})


# @app.route('/room_311', methods=['POST'])
# def button2():
    
#     print("Robot Moving to Room 311")
#     goal.post_goal("room311")
#     # print("Button was pressed!")
#     return jsonify({"status": "success", "message": "Moving To 311"})

if __name__ == '__main__':
    try:
        app.run(debug=True, port=5555)
    finally:
        rclpy.shutdown()


# from flask import Flask, jsonify
# import threading
# import time

# app = Flask(__name__)

# count = 0

# def increment_counter():
#     global count
#     while True:
#         time.sleep(1)
#         count += 1



# @app.route('/get_count', methods=['GET'])
# def get_count():
#     global count
#     return jsonify({"count": count})

# if __name__ == '__main__':
#     # Start the background thread
#     thread = threading.Thread(target=increment_counter)
#     thread.daemon = True
#     thread.start()
    
#     app.run(debug=True, host='0.0.0.0', port=5555)


