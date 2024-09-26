import cv2
from PIL import Image
from util import get_limits

red = [0, 0, 255]

cap =cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit1, lowerLimit2, upperLimit1, upperLimit2 = get_limits(color=red)

    mask1 = cv2.inRange(hsvImage, lowerLimit1, upperLimit1)
    mask2 = cv2.inRange(hsvImage, lowerLimit2, upperLimit2)

    combined_mask = cv2.bitwise_or(mask1, mask2)


    cv2.imshow("frame", frame)

    mask_ = Image.fromarray(combined_mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        cv2.putText(frame, 'Red', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        
    
    cv2.imshow ('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

