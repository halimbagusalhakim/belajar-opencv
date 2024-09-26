import numpy as np
import cv2

def get_limits(color):
    # Insert the BGR values you want to convert to HSV
    c = np.uint8([[color]])  # Wrap in double brackets to ensure the correct shape for cvtColor
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue_value = hsvC[0][0][0]

    # Adjust hue ±10, saturation and value are fixed
    lowerred =  - 0, 0, 200  # Adjust hue ±10, saturation and value are fixed
    upperred =  + 180, 55, 255

    # Convert to np.uint8 arrays
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)


    return lowerLimit, upperLimit
