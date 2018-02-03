import binascii
import math
import turtle
from tkinter import *
from PIL import Image

from config import FONT_NAME, FONT_SIZE, FILE_NAME, IMAGE_NAME, DATA_OFFSET, OUTPUT_FPATH

# basic setup
img = Image.open(IMAGE_NAME)
image = img.load()

class HexArtDrawer(object):

    def __init__(self, image, input_hexfile, output_fname, font_name, font_size):
        # basic setup
        self._turtle = turtle
        self._turtle.setup(image.size[0], image.size[1]) # (width, height)
        self._image = image.load()
        self._wn = self._turtle.Screen()
        self._tess = self._turtle.Turtle()
        self._font = (font_name, font_size, "normal")  # (fontname, fontsize, fonttype)
        self._input_hexfile = input_hexfile
        self._output_fname = output_fname
        self._configured = False
        self.configure()

    def get_font_name(self):
        return self._font[0]

    def get_font_size(self):
        return self._font[1]

    def configure(self):
        assert(not self._configured)
        self.determine_char_width()
        self.determine_charspace_width()

        # double of (self._charspace_width - self._char_width) should
        # add some nice padding, but can be changed to whatever to best fit the image
        self._y_incr = self.get_font_size()

        # using double of charspace width would make it appear
        # as if text is being normally typed
        self._x_incr = self._charspace_width * 2

        # starting positions of x and y, (0,0) would be the center of the screen
        self._start_x = -self._wn.window_width() / 2
        self._start_y = (self._wn.window_height() / 2) - self._y_incr

        # minus 2 for padding left and right
        self._characters_per_line = (self._wn.window_width() / self._x_incr) - 1
        self._number_of_lines = (self._wn.window_height() / self._y_incr) - 1

        # mark flag
        self._configured = True

    def draw(self):
        self._draw()
        self._tess.getscreen().getcanvas().postscript(file=self._output_fname, colormode='color')
        print("Aha! Got the postscript output, didn't ya?")
        # wait for a user to click on the canvas
        self._wn.exitonclick()
        print("You have successfully exited the canvas via clicking.")

    def _draw(self):
        assert(self._configured)
        with open(self._input_hexfile, "rb") as fd:
            block = fd.read()

            # where to start reading the data from
            blockStart = 0 + DATA_OFFSET

            # how many values to read
            blockIncrement = int(math.floor(self._characters_per_line))

            # end of the values to be read
            blockEnd = blockStart + blockIncrement

            # current position of the image
            imgX = 0
            imgY = 0

            print("Starting to write hex values with color...")

            # interate from blockStart until the image is filled
            for i in range (blockStart,
                            (int(self._characters_per_line) * int(self._number_of_lines) + blockStart)):
                print("i={}".format(i))

                # when done writing down the line's values, move turtle to the next line
                if (i == blockEnd):
                    print("i={} : moving turtle to next line")
                    self._start_x = -self._wn.window_width() / 2
                    self._start_y -= self._y_incr
                    blockEnd += blockIncrement
                    imgY += self._y_incr
                    imgX = 0

                # write each value
                self._start_x += self._x_incr
                self._tess.penup()
                self._tess.goto(self._start_x, self._start_y)
                self._tess.pendown()

                img_r = 0
                img_g = 0
                img_b = 0
                img_a = 0

                # get the average color for the segment
                for x in range (imgX, imgX + self._x_incr):
                    for y in range (imgY, imgY + self._y_incr):
                        img_r += self._image[x,y][0]
                        img_g += self._image[x,y][1]
                        img_b += self._image[x,y][2]
                        img_a += self._image[x,y][3]
                img_r /= self._x_incr * self._y_incr
                img_g /= self._x_incr * self._y_incr
                img_b /= self._x_incr * self._y_incr
                img_a /= self._x_incr * self._y_incr

                imgX += self._x_incr

                # if the average color is transparent or white, don't display it
                if (img_a == 0 or (img_r == 255 and img_g == 255 and img_b == 255)):
                   continue
                else:
                   self._tess.color(img_r/255.0, img_g/255.0, img_b/255.0)

                print("i={} : writing the next hex value with the corresponding segment color...")

                # write the next hex value with the corresponding average segment color
                self._tess.write(
                    binascii.hexlify(bytes(str(block[i]), 'ascii')),
                    font=self._font
                )

                print("i={} : completed writing the next hex value with the corresponding segment color.".format(i))

            print("Completed writing all the hex values with color!")

    def determine_char_width(self):
        self._tess.hideturtle()
        self._tess.goto(0, 0)
        # "If _move_ is true, the pen is moved to the bottom-right corner of the text.
        self._tess.write("0", move=True, font=self._font)
        self._char_width = self._tess.xcor()
        self._tess.undo()

    def determine_charspace_width(self):
        self._tess.goto(0, 0)
        self._tess.write("00", move=True, font=self._font)
        self._charspace_width = self._tess.xcor()
        self._tess.undo()

def main():
    drawer = HexArtDrawer(
        image=Image.open(IMAGE_NAME),
        input_hexfile=FILE_NAME,
        output_fname=OUTPUT_FPATH,
        font_name=FONT_NAME,
        font_size=FONT_SIZE
    )
    drawer.draw()

if __name__ == '__main__':
    main()
