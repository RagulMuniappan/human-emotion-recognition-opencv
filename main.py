from facial_emotion_recognition import EmotionRecognition
import cv2

er = EmotionRecognition(device = 'cpu')
cam = cv2.VideoCapture(0)

while True:
    sucess,frame = cam.read()
    frame = er.recognise_emotion(frame,return_type = 'BGR')
    # Resize to fixed size (width, height)
    frame = cv2.resize(frame, (580, 435))

    cv2.imshow("Emotion Recognition", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()