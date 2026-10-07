import os, datetime, time, requests, json
from picamera2 import Picamera2

current_dateTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
picam2 = Picamera2()

with open("values.json", "r") as file:
    data = json.load(file)

file_name = f"device{data['device_id']}_plot_{current_dateTime}.jpg"

target_dir = "~/Pictures/"
full_dir = os.path.expanduser(target_dir)
file_path = os.path.join(full_dir, file_name)

config = picam2.create_still_configuration(main={"size": (3280, 2464)})
picam2.configure(config)

picam2.start()
time.sleep(2)
picam2.capture_file(file_path)
time.sleep(2)
picam2.stop()

url = f"http://{data['target_ip']}/save_image/"

body_data = {
    "cameraID": data['device_id']
}

with open(file_path, "rb") as image_file:
    files = {"image": image_file}
    response = requests.post(url, data=body_data, files=files)

if (response.json().get("status") == "success"):
    os.remove(file_path)
