import socket
import numpy as np
import time

UDP_IP = "192.168.50.50"
UDP_PORT = 2711

HEAD_BYTE = 0
HEAD_AMOUNT = 1

message = [HEAD_BYTE, 0, 0, 0, 100]

L = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

LHC = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

SHIP = np.array([[0, 1, 0],
                 [1, 1, 1]])

INVASOR = np.array([[1, 1],
                    [1, 1]])

BULLET = np.array([[1]])

class Sprite():
    def __init__(self):
        self.drawing = []
        # Position of left up pixel
        self.position = (0, 0)
        # RGB color, 8 bits each
        self.color = [0, 0, 0]
        self.visible = True

class LedPanelLHC():
    def __init__(self):
        self.spriteList = []
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def addSprite(self, sprite):
        self.spriteList.append(sprite)

    def draw(self):
        frame = [[[0, 0, 0] for a in range(10)] for b in range(10)]
        for sprite in self.spriteList:



'''
>>> import numpy as np
>>> frame = np.array([[[a, b, a+b] for a in range(10)] for b in range(10)])
>>> frame[0:2,0:2]=[[[111,111,111],[222,222,222]],[[333,333,333],[444,444,444]]]
'''


a = 0
fullFrame = LHC
while True:
    time.sleep(0.25)
    fullFrame = np.concatenate((fullFrame[:, 1:20], fullFrame[:, 0:1]), axis=1)

    frame = fullFrame[:, 0:10]
    frameArray = np.ravel(frame.T)
    COLOR = [0, 255, 0]
    image = []
    for pixel in frameArray:
        for color in COLOR:
            image.append(pixel * color)

    message += image
    message = bytearray(message)
    sock.sendto(message, (UDP_IP, UDP_PORT))

    message = [HEAD_BYTE, 0, 0, 0, 100]
