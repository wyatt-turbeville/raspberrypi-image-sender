import os, datetime, time, socket, requests, re
import Picamera2

current_dateTime = datetime.datetime.now()
picam2 = Picamera2()

# take picture and save to specified path
host_name = socket.gethostbyname
file_name = f"{host_name}_plot_{current_dateTime}.jpg"

target_dir = "~/Pictures/"
full_dir = os.path.expanduser(target_dir)
file_path = os.path.join(full_dir, file_name)

config = picam2.create_still_configuration(main={"size": (3280, 2464)})
picam2.configure(config)

picam2.start()
time.sleep(1)
picam2.capture_file(file_path)
time.sleep(1)
picam2.stop()

url = "http://http://100.76.229.28:8000/save_image/"
cleaned_text = re.sub(r"\D", "", host_name) 
clean_number = int(cleaned_text)

body_data = {
    "cameraID": clean_number
}

with open(file_path, "rb") as image_file:
    files = {"image": image_file}

response = requests.post(url, data=body_data, files=files)

if (response.json().get("status") == "success"):
    os.remove(file_path)