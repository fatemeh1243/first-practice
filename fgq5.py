x = int(input("Enter the size of x: "))
y = (input("Please enter the color: "))
import turtle
wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("wuba luba dub dub")

turtleline = turtle.Turtle()
turtleline.shape("turtle")

turtleline.color(y)
size = 25
for turtle in range(4):
    size = size + x
    turtleline.forward(x)
    turtleline.left(90)
    turtleline.forward(x)
wn.mainloop()