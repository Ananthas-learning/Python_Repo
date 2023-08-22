# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_colors.append(color_tuple)
# print(rgb_colors)
import turtle as tim

import random
tim.colormode(255)
color_list = [(239, 221, 113), (18, 111, 193), (223, 60, 95), (235, 150, 76), (116, 147, 208), (143, 88, 50), (212, 127, 164), (34, 194, 117), (139, 183, 18), (189, 18, 39), (108, 105, 194), (232, 55, 45), (244, 147, 183), (113, 191, 149), (191, 46, 66), (19, 187, 206), (45, 52, 105), (136, 221, 240), (146, 229, 169), (202, 210, 7), (22, 151, 116), (233, 174, 159), (31, 43, 76), (112, 42, 40), (181, 178, 220), (80, 34, 37)]


def paint():
    for _ in range(5):
        #tim.color(random.choice(color_list))
        tim.speed("fastest")
        tim.pendown()
        #tim.begin_fill()
        tim.dot(20,random.choice(color_list))
        #tim.end_fill()
        tim.penup()
        tim.fd(50)


for _ in range(5):
    tim.setx(0)
    tim.sety(50*_)
    paint()

tim.shape("turtle")
tim.exitonclick()





