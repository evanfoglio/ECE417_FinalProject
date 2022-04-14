# ECE417_FinalProject
ECE 417 Final Project. Use 2 mutually orthogonal checkerboards to calibrate a camera.


Webcam Passthough with VMWare:
  1) First open up VMWare
  2) Select the VM youd like to give access to the camera
  3) Right click and select settings
  4) Select "USB Controller"
  5) Change the USB compatibility to "USB 3.1" 
  6) Click OK and launch the VM
  7) Click the "Player" drop down menu in the top left
  8) In removeable devices, hover over your webcam and click connect
  9) Select OK (Both times if it asks 2 things)
  10) In a terminal, type "lsusb" to verify it is being detected



To Begin Sending Images to the ROS Topic:
  1) roscore
  2) rosrun cv_camera  cv_camera_node   _image_width:=640 _image_height:=480 _frame_id:=camera __name:=camera
