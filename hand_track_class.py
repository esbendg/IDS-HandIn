import cv2 # pip install opencv-python
import mediapipe as mp # pip install mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

class Hand_Track:
  
  def __init__(self):
      self.cap = cv2.VideoCapture(0)
      self.hands = mp_hands.Hands(
                  model_complexity=0,
                  min_detection_confidence=0.5,
                  min_tracking_confidence=0.5)
      self.hand_on_img = False

  def get_points(self):
      if self.cap.isOpened():
        success, self.image = self.cap.read() # getting the image, opening camera
        if not success:
          print("Ignoring empty camera frame.")

        self.image.flags.writeable = False
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(self.image) #processing image
        if self.results.multi_hand_landmarks:
          self.hand_on_img = True
          self.index_tip = self.results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
          self.thumb = self.results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.THUMB_TIP]
          return {"index": self.index_tip, "thumb": self.thumb}
        else: 
          self.hand_on_img = False
          return None

  def show_img(self):
      self.image.flags.writeable = True
      self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
      if self.hand_on_img:
        for hand_landmarks in self.results.multi_hand_landmarks:
          mp_drawing.draw_landmarks(
              self.image,
              hand_landmarks,
              mp_hands.HAND_CONNECTIONS,
              mp_drawing_styles.get_default_hand_landmarks_style(),
              mp_drawing_styles.get_default_hand_connections_style())
      # Flip the image horizontally for a selfie-view display.
      cv2.imshow('MediaPipe Hands', cv2.flip(self.image, 1)) #  showing the image

  def is_hand_visible(self):
    return self.hand_on_img

  def finish(self):
    self.cap.release()