"""
This file is so every group member understands well how to use the handtracker.
We decided to keep it because it explains well the hand_track_class file.
"""

import time
#First the class file has to be imported
import hand_track_class

#To use the hand tracker, you need to create a hand tracker object
tracker_object = hand_track_class.Hand_track() #This will take a while since it loads the model and makes ready the video feed

#Then you need to start the tracking
tracker_object.start() #It uses threading so doesn't stop the code
#Once started it will update the variables of the object

#Variables to use
for i in range(5):
    print(tracker_object.hand_on_img) #Tells you iff a hand is visible on the screen or not. If not tindex_tip and thumb_tip are null objects!!
    time.sleep(1.5) #Waiting for the object to load properly
    if tracker_object.hand_on_img: #TO SEE THESE PRINTED MAKE SURE YOUR HAND IS VISIBLE
        print(tracker_object.index_tip) #You can reach the indextip this way. It has attributes x, y, z. They are relative to the input screen, ranging from 0 to 1.
        print(tracker_object.index_tip.x) #Getting the x coordinate of the tip of the index finger
        print(tracker_object.thumb_tip) #Same as index_tip but for the thumb
        print(tracker_object.is_pinch) #If the index and thumb tips are close enough to each other this is True otherwise False
        print(tracker_object.click_sensitivity) #You can change this value to make the click easier or harder to achive

#If you want to see what is going on you can start the projection of the image
tracker_object.img_on()
time.sleep(10)
tracker_object.img_off() #An you can turn it off once not needed

# The variables are still updated
if tracker_object.hand_on_img: #So use the variables when hand is visible
    print(tracker_object.index_tip)

time.sleep(3)

#To use with a specific program and screen, set the screen size for the object
tracker_object.set_window_size(500, 300)
#Then it is possible to return the relative x and y position for the index tip (use it as the mouse)
index_x, index_y = tracker_object.get_relative_index_pos() #It will return the exact pixel where the index finger is
#And you can ask the object if the index tip is inside of an object (returns True/False)
box_x0, box_y0, box_x1, box_y1 = 0, 0, 50, 50
tracker_object.is_inside_box(box_x0, box_y0, box_x1, box_y1)

#finally you can stop the tracking object
tracker_object.stop()

#But the code can go on
for j in range(3):
    print("finished")
    time.sleep(3)