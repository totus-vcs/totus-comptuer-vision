from time import sleep
from objectDetection import Detector


detector = Detector()
while True:
    data =  detector.runCV()
    sleep(0.001) # TODO can this be reduced further for faster speed?
    print("items visible", data)
