#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2


class Myface:
    def __init__(self):
        self.gread = 'MNHQ&OC?7>!:-;.'
        self.ascii_char = list("$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:, ")
        self.jibie = 255 / len(self.gread)

    def renderStr(self, imgData):
        str = ''
        image = imgData

        for letter in image:  # 第一个实例
            for garr in letter:
                r, g, b = garr
                grr = r * 0.299 + g * 0.587 + b * 0.114
                if grr >= 150:
                    str += '.'
                else:
                    str += self.gread[min(int(round(grr / self.jibie)), len(self.gread) - 1)]
            str += '\n'
        print(str)

    def beforeRender(self):
        print("\n" * 10000)

    def show(self, video=0):
        cap = cv2.VideoCapture(video)
        self.beforeRender()

        while cap.isOpened():
            _, frame = cap.read()
            if frame is None:
                break
            resize = cv2.resize(frame, (int(800 / 10), int(500 / 10)), interpolation=cv2.INTER_CUBIC)
            self.renderStr(resize)

        cap.release()
        cv2.destroyAllWindows()
