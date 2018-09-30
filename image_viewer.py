# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 14:33:45 2018

@author: Sourav
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from cv2 import imshow,waitKey,imread,destroyAllWindows
Tk().withdraw()
filename=askopenfilename()
img=imread(filename);
#       Press esc to exit.........
while True:
    imshow("Frame",img)
    if waitKey(1)==27:
        break
destroyAllWindows()