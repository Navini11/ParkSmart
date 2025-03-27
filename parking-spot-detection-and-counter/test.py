# filepath: c:\Users\DELL\Documents\Internship\ParkSmart\parking-spot-detection-and-counter\test.py
import cv2

video_path = r'C:\Users\DELL\Documents\Internship\ParkSmart\parking-spot-detection-and-counter\data\parking_crop_loop.mp4'

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

ret = True
while ret:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()