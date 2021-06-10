from grabscreen import grab_screen
import cv2
import numpy as np
import time
import keys as k

keys = k.Keys()


def pathing(minimap):
    lower = np.array([75,150,150])
    upper = np.array([150,255,255])

    hsv = cv2.cvtColor(minimap, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    matches = np.argwhere(mask==255)
    mean_y = np.mean(matches[:,1])
    target = minimap.shape[1]/2

    error = target - mean_y

    print(error)
    keys.directMouse(-1*int(error*3), 0)

    cv2.imshow("Masked", mask)
    cv2.waitKey(10)

for i in range(5):
    print(i)
    time.sleep(1)

keys.directKey("w")
# run for n frames
for i in range(2000):
    screen = grab_screen(region=(0, 0, 1440, 900))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    minimap = screen[50:200, 1230:1382]
    miniminimap = screen[105:125, 1285:1332]

    pathing(miniminimap)
    # screen = cv2.resize(screen, (960, 540))
    # cv2.imshow("cv2screen", screen)
    # cv2.waitKey(10)
keys.directKey("w", keys.key_release)
cv2.destroyAllWindows()