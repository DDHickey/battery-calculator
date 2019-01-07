import pyscreenshot as ImageGrab
from PIL import Image
from pytesseract import image_to_string
import time
import cv2
import os

# fullscreen
#im=ImageGrab.grab()
#im.show()

try:
    while True:
        # part of the screen  -- in this case battery %
        im=ImageGrab.grab(bbox=(1053,0,1080,20))

        # Shows temp image.
        im.show()

        # Rescale the image, if needed.
        os.system('convert -quiet -resize 400% im.png im.png')

        # Convert photo to text and place in file.
        os.system('tesseract im.png res')

        # Save picture
        im.save('im.png')

        file = open('res.txt')
        batteryPercentStr = file.read().strip()
        batteryPercent = int(batteryPercentStr)
        file.close()

        if(batteryPercent == 100):
            print("Battery Percent is full: " + str(batteryPercent) + "%")
        elif (batteryPercent > 10):
            print("Battery is not full: " + str(batteryPercent) + "%")
        elif (batteryPercent == 0):
            print("Calculating computer percent...")
        else:
            print("Battery is critically low: " + str(batteryPercent) + "%")


        time.sleep(15);
        print("Going in for another photo!")
        #print(image_to_string(Image.open('im.png'),lang='eng'))

except KeyboardInterrupt:
    files = open("res.txt", "w");
    files.write("0");
    files.close();
    print("Stopped");
