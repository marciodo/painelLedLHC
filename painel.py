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


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
