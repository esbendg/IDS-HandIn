import hand_track_class
import time

obj = hand_track_class.Hand_Track()

while(True):
    points = obj.get_points()
    if obj.is_hand_visible():
        print(points["index"].y)
    else: print("No hand")
    # time.sleep(0.1)

obj.finish()



# time.sleep