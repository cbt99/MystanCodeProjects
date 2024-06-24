"""
File: photoshop.py
Name: Jerry Liao
-------------------------------------
This program replaces the green screen
background of jerry.jpeg with wave.jpeg, 
providing students some intuitions on
photoshop techniques 
"""


from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.3

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def combine(bg, me):
    """
    : param1 bg: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


def main():
    """
    This function conducts green screen replacement
    which is able to photoshop a person onto any background
    """
    fg = SimpleImage('images/jerry.jpeg')
    bg = SimpleImage('images/wave.jpeg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
