#
# import colorgram
#
# colors_objects = colorgram.extract('hirstpaint.jpg', 30)
# print(type(colors_objects))
# colors = []
# colors_objects[0].rgb
# for i in colors_objects:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_tuple = (r,g,b)
#     colors.append(new_tuple)
# print(colors)
import turtle

import turtle as turtle_module
import random
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed('fastest')
tim.hideturtle()
colors_list = [(226, 229, 235), (244, 237, 222), (243, 234, 240), (232, 242, 237), (192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165), (25, 91, 65), (172, 205, 180)]
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for _ in range(10):
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colors_list))
        tim.penup()
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()






screen.exitonclick()