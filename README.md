# Device Setup Instructions
1. Flash the appropriate raspberry pi os onto the device storage
2. Connect the device to wifi<br>
   a. Optionally connect the device to RaspberryPi Connect for remote shell use
3. Install the 'requests' and 'picamera2' libraries<br>
   In terminal:  
   a. sudo apt install requests
   b. sudo apt install picamera2
4. Install and connect to Tailscale
   In terminal:
   a. curl -fsSL https://tailscale.com/install.sh | sh
   b. sudo tailscale up
   c. follow the auth link and add the device to the same tailnet as the file receiving device
5. Download the project files from github
   In the home directory from terminal:
   a. git clone
6. Edit the values.json file to be correct
   a. "target_ip": "X.X.X.X:Port" must be changed to the ipv4 of the file receiving device on their shared tailnet
   b. "device_id": (int) is expecting any integer to define who it is among other file sending devices.
   device_id cannot be shared with any other file sending devices, an example use might be setting the integer to the number on the plot it is imaging
7. Schedule this application to run in crontab
   In terminal:
   a. crontab -e
   b. 0 * * * * /absolute/path/to/app.py
   This line runs hourly, it can be modified to fit your needs
