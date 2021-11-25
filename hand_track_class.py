import cv2 # pip install opencv-python
import mediapipe as mp # pip install mediapipe
import threading
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

class Hand_track:

    #Initialize object
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.index_tip = None
        self.thumb_tip = None
        self.is_click = False
        self.click_sensitivity = 0.03    #Sensitivity of the check_if_click function. Higher value -> more sensitive -> easier to click
        self.hand_on_img = False
        self.img_state = 0                # 0 is off, 1 is on, 2 is closing window
        self.stop_thread = False

    def start(self):
        def loop():
            with mp_hands.Hands(
                model_complexity=0,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as hands:
                while self.cap.isOpened():
                    success, image = self.cap.read()
                    if not success:
                        print("Ignoring empty camera frame.")
                        # If loading a video, use 'break' instead of 'continue'.
                        continue

                    # To improve performance, optionally mark the image as not writeable to
                    # pass by reference.
                    image.flags.writeable = False
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    results = hands.process(image)
                    if results.multi_hand_landmarks:
                        self.hand_on_img = True
                        self.index_tip = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                        self.thumb_tip = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.THUMB_TIP]
                        self.check_if_click()
                    else: self.hand_on_img = False
                    
                    if self.img_state == 1:
                        # Draw the hand annotations on the image.
                        image.flags.writeable = True
                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                        if results.multi_hand_landmarks:
                            for hand_landmarks in results.multi_hand_landmarks:
                                mp_drawing.draw_landmarks(
                                    image,
                                    hand_landmarks,
                                    mp_hands.HAND_CONNECTIONS,
                                    mp_drawing_styles.get_default_hand_landmarks_style(),
                                    mp_drawing_styles.get_default_hand_connections_style())
                        # Flip the image horizontally for a selfie-view display.
                        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
                        if cv2.waitKey(5) & 0xFF == 27:
                            break
                    elif self.img_state == 2:                                     #Close the window then set showImg to 0 (off)
                            try:
                                cv2.destroyWindow('MediaPipe Hands')
                            except: pass
                            self.img_state == 0
                    if self.stop_thread:
                        break
        self.thread = threading.Thread(target = loop)
        self.thread.start()

    def stop(self):
        # self.img_off()
        self.stop_thread = True
        self.thread.join()
        self.cap.release()
    
    def img_on(self):
            self.img_state = 1
    def img_off(self):
            self.img_state = 2

    def check_if_click(self):
        if abs(self.index_tip.x - self.thumb_tip.x) < self.click_sensitivity and abs(self.index_tip.y - self.thumb_tip.y) < self.click_sensitivity and abs(self.index_tip.z - self.thumb_tip.z) < self.click_sensitivity:
            self.is_click = True
        else:
            self.is_click = False

    
        

    #Function to reasign variables: indexTip, thumbTip and isClick //START function

    #Function to determine when to change isClick [private]