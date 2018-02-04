# Hex

> Reproducing images using hex values found from a desired file

Hex is a Python program that takes an image of **.PNG** format, and a corresponding file, to recreate the image by replacing all pixels with colored hex values. The original author, [Steven Kang](https://github.com/sacert), wanted to put up some art for his place and thought it would be fun to blend it with a programmers prospective.

The output of the file is a PostScript (**.ps**) file.

# Input

`FILE` = Anything - the program just takes the hex values from it

`IMAGE` = Image file, preferably in **.PNG** format. 

_DISCLAIMER: The program has been tested with **PNG** files as `IMAGE`. **JPEG** files has not been tested. While **JPEG** files should theoretically work, the algorithm does take into account the alpha channel. If the user wishes to accept **JPEG** files as the input for `IMAGE`, corresponding lines of code regarding the alpha channel shall be commented out._

# Examples

<p align="center">
  <img src="https://github.com/sacert/Hex/blob/master/examples/link.png" alt="Screen shot 1" width="250"/>
  <img src="https://github.com/sacert/Hex/blob/master/examples/tardis.png" alt="Screen shot 2" width="250"/>
</p>

For **Toon Link**:

`FILE` = Legend of Zelda: Breath of the Wild theme song (mp3)

For **Tardis**

`FILE` = Doctor Who Theme song (mp3)


<p align="center">
  <img src="https://github.com/sacert/Hex/blob/master/examples/link_zoon.png" alt="Screen shot 1" width="400"/>
</p>
Here it is shown how each "pixel" of the image is simply a colored hex value.


# Getting Started

Within the [`config.py`](./config.py) are input parameters that the user has to specify.

* `FONT_NAME`: The name of the font for writing the ASCII hex text.
* `FONT_SIZE`: The size of the font for drawing on the canvas.
* `FILE_NAME`: The name of the input file where the hex values will be obtained from
* `IMAGE_NAME`: The name of the image file in **.png** format.
* `OUTPUT_FPATH`: The file path of the output in **.ps** format.
* `DATA_OFFSET`: Where to start reading data from (i.e. mp3 data starts at byte position 32)

# Running the Program

    (Hex) $ python art.py

# Licensing 

See [**LICENSE**](./LICENSE) for the complete MIT License.
