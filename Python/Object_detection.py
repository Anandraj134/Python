import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap = cv.VideoCapture("D:\Anand\Videos\Learn Colors With Balls _ Colours For Kids And Children _ Learning & Education For Toddlers & Babies ( 480 X 854 ).mp4");

cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv.createTrackbar("HH", "Tracking", 255, 255, nothing)
cv.createTrackbar("HS", "Tracking", 255, 255, nothing)
cv.createTrackbar("HV", "Tracking", 255, 255, nothing)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lh = cv.getTrackbarPos("LH", "Tracking")
    ls = cv.getTrackbarPos("LS", "Tracking")
    lv = cv.getTrackbarPos("LV", "Tracking")

    hh = cv.getTrackbarPos("HH", "Tracking")
    hs = cv.getTrackbarPos("HS", "Tracking")
    hv = cv.getTrackbarPos("HV", "Tracking")

    lb = np.array([lh, ls, lv])
    ub = np.array([hh, hs, hv])

    mask = cv.inRange(hsv, lb, ub)
    res = cv.bitwise_and(frame, frame, mask = mask)

    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
    cv.imshow("Res", res)

    key = cv.waitKey(30)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()