import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
segmentor = SelfiSegmentation()

while True:
    success, img = cap.read()
    if not success:
        print("Could not read a frame from the webcam.")
        break

    # background colour is BGR, so this is magenta
    imgOut = segmentor.removeBG(img, (255, 0, 255))

    cv2.imshow("Image", img)
    cv2.imshow("Image Out", imgOut)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
