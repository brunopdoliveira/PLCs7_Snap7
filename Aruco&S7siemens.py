##########################################################################################
#                          Aruco Detection  & PLC SIEMENS                                #
#                                Autor: Bruno Oliveira                                   #
##########################################################################################

# import libraries
import snap7
from snap7 import util
import cv2
import cv2.aruco as aruco

# define IP/rack/slot of PLC s7 siemens
IP = '192.168.0.1'
RACK = 0
SLOT = 1

# establish a client-type connection from python to PLC Siemens
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)
plc.get_connected()

# open camera 0 and print
video = cv2.VideoCapture(0)
print('Open Camera!')

# font for the text in the image
font = cv2.FONT_HERSHEY_PLAIN

# define aruco numbers
aruco10 = 55
aruco20 = 20
aruco30 = 30
aruco60 = 60

while (True):
    # capture frame-by-frame
    ret, frame = video.read()

    # our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
    parameters = aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    # edge colors of aruco markers
    borderColor = (0, 255, 0)

    image = aruco.drawDetectedMarkers(frame, corners, ids, borderColor)

    if ids is not None:
        for i in range(len(ids)):
            if ids[0] == aruco60:
                #print(ids[0])
                #print("Aruco 10 found!")
                # set first bit TRUE in DB 3, byte 0
                buffer = bytearray([0b00000011])
                wt = plc.db_write(5, 1, buffer)
                # read wrote bit from PLC
                db = plc.db_read(5, 1, 1)
                t = util.get_bool(db, 0, 0)
                print(t)

    else:
        buffer = bytearray([0b00000010])
        wt = plc.db_write(5, 1, buffer)



    cv2.imshow('frame', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()

