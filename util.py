import numpy as np
import cv2

def get_limits(color):
    # Insert the BGR values you want to convert to HSV
    c = np.uint8([[color]])  # Wrap in double brackets to ensure the correct shape for cvtColor
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Extract hue value from the converted HSV color
    hue_value = hsvC[0][0][0]

    # Define lower and upper limits for HSV range
    # Adjust hue ±10, saturation and value are fixed
    lowerLimit1 = (hue_value - 10, 100, 100)
    upperLimit1 = (hue_value + 10, 255, 255)

    # Wrap-around hue adjustment for red (since red is at both 0 and 180 in HSV)
    lowerLimit2 = (hue_value + 170, 100, 100)
    upperLimit2 = (hue_value + 180, 255, 255)

    # Convert to np.uint8 arrays
    lowerLimit1 = np.array(lowerLimit1, dtype=np.uint8)
    upperLimit1 = np.array(upperLimit1, dtype=np.uint8)
    lowerLimit2 = np.array(lowerLimit2, dtype=np.uint8)
    upperLimit2 = np.array(upperLimit2, dtype=np.uint8)

    return lowerLimit1, lowerLimit2, upperLimit1, upperLimit2
