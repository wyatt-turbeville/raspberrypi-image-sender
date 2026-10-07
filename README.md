# Device Setup Instructions
1. Flash the appropriate RaspberryPi OS onto the device storage<br>
2. Connect the device to wifi<br>
   a. Optionally connect the device to RaspberryPi Connect for remote shell use.<br>
3. Install the 'requests' and 'picamera2' libraries<br>
   In terminal:<br>
   a. sudo apt install python3-requests<br>
   b. sudo apt install picamera2<br>
4. Install and connect to Tailscale<br>
   In terminal:<br>
   a. curl -fsSL https://tailscale.com/install.sh | sh<br>
   b. sudo tailscale up<br>
   c. follow the auth link and add the device to the same Tailnet as the file receiving device.<br>
5. Download the project files from github<br>
   In the home directory from terminal:<br>
   a. git clone<br>
6. Edit the values.json file to be correct<br>
   a. "target_ip": "X.X.X.X:Port" must be changed to the ipv4 of the file receiving device on their shared Tailnet.<br>
   b. "device_id": (int) is expecting any integer to define who it is among other file sending devices.<br>
   device_id cannot be shared with any other file sending devices, an example use might be setting the integer to the number on the plot it is imaging.<br>
7. Schedule this application to run in crontab<br>
   In terminal:<br>
   a. crontab -e<br>
   b. 0 * * * * /absolute/path/to/app.py<br>
   This line runs hourly, it can be modified to fit your needs.<br>
