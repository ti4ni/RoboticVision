# RoboticVision.
This is a robotic vision that I designed. Powered by PyTesseract and pyhon 3.10.7.

To use RoboticVision you need to install: pytesseract, opencv-python, PyAutoGUI, numpy, pyscreenshot (via pip3).
Some features can be changed (for example, data output delay, automatic program stop, and so on).
The Coordinates.py file is responsible for determining the coordinates of the mouse cursor (these values are needed for the RoboticVision file to resize the search area on the screen)
The RoboticVision.py file is responsible for the very implementation of the script for analysis, checking for similarity with the specified one, and displaying information from the screen.
