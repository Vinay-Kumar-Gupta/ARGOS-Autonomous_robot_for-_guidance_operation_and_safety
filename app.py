# =================================================== API CONTROL SCRIPT ===========================================

# ============================= IMPORTS ================================= 

from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from publisher_module import GoalPosePublisher
import rclpy

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}) # Allow all origins for all routes

rclpy.init()
goal = GoalPosePublisher()

# ============================================ ROOM NAVIGATION ============================================


@app.route("/room_nav_no", methods=["POST"])
def room_naviation():

    data = request.json
    room_no = data.get("room_number")

    # ========================= ROOM CONDTION =========================

    if room_no[0:4] == "room":

        print(f"MOVING TO {room_no}")

        goal.publish_goal_pose(room_name=room_no)

        return jsonify({"status": "SUCCESS", "message": f"MOVING TO {room_no}"})

    # ========================= TOUR MODE CONDITION =============================

    elif room_no == "tour_mode":

        print("TOUR MODE ON")
        return jsonify({"status": "SUCCESS", "message": f"{room_no} ON"})
    
    # ========================= TOUR MODE CONDITION =============================

    elif room_no == "fire":

        print(" ALERT FIRE !!!")
        return jsonify({"status": "SUCCESS", "message": f"{room_no} MODE ON"})
 
    # ======================== TEST CALL ===============================

    elif room_no == "test_call":

        print("TEST CALL PASSED ✅ ")
        return jsonify({"status": "SUCCESS", "message": f"{room_no} PASSED ✅"})

    else:
        return jsonify({"status": "ERROR", "message": "PLS CHECK END POINT"}), 400


# ============================================ MANUAL NAVIGATION ============================================

@app.route("/manual_nav_cmd", methods=["POST"])
def manual_navigation():

    data = request.json
    nav_cmd = data.get("manual_command")

    # ======================== MANUAL CONDITION ===============================

    if nav_cmd == "forward":

        print("MOVING FORWARD")
        return jsonify({"status": "SUCCESS", "message": "MOVING FORWARD"})

    elif nav_cmd == "backward":

        print("MOVING BACKWARD")
        return jsonify({"status": "SUCCESS", "message": "MOVING BACKWARD"})

    elif nav_cmd == "rt_right":

        print("MOVING RIGHT")
        return jsonify({"status": "SUCCESS", "message": "MOVING RIGHT"})

    elif nav_cmd == "rt_left":

        print("MOVING LEFT")
        return jsonify({"status": "SUCCESS", "message": "MOVING LEFT"})

    elif nav_cmd == "stop":

        print("MOVING STOP")
        return jsonify({"status": "SUCCESS", "message": "MOVING STOP"})
    
    # ======================== TEST CALL ===============================

    elif nav_cmd == "test_call":

        print("TEST CALL PASSED ✅ ")
        return jsonify({"status": "SUCCESS", "message": f"{nav_cmd} PASSED ✅"})

    else:
        return jsonify({"status": "ERROR", "message": "PLS CHECK END POINT"}), 400


if __name__ == '__main__':
    try:
        app.run(debug=True, port=5555)
    finally:
        rclpy.shutdown()


# ====================================== TEST =====================================

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

# ============================================== GET METHOD TEST ====================================

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
