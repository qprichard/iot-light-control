from sense_hat import SenseHat
import json

class SenseManager():
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()
        c = (0,0,0)
        self.matrice = [
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	]
    def clear(self):
        self.sense.clear()

    def set_color(self, color):
        c = color

        self.matrice = [
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	c,c,c,c,c,c,c,c,
        	]
        self.sense.set_pixels(self.matrice)

    def set_matrice(self, matrice):
        self.matrice = matrice
        self.sense.set_pixels(self.matrice)

    def get_matrice():
        return self.matrice

    def set_pixel(self, x,y, color):
        self.sense.set_pixel(x,y, color[0], color[1], color[2])

    def message(self, text, speed = 0.1, colour = (255,255,255), background = (0,0,0)):
        self.sense.show_message(text, speed, colour, background)
    
