import turtle
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.pensize(2)
t2.pensize(1)
t1.pencolor('crimson')
t2.pencolor('black')



def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def GoldenSpiral(t1, t2, n):
    if n == 1:
        pass
    else:
        t1.circle(Fibonacci(n)*8, 90)
        for i in range(6):
            t2.forward(Fibonacci(n)*8)
            t2.left(90)
        t2.right(90)
        GoldenSpiral(t1, t2, n-1)

t1.penup()
t2.penup()
t1.goto(-100,-200)
t2.goto(-100,-200)
t1.pendown()
t2.pendown()
print(Fibonacci(10))
GoldenSpiral(t1, t2, 10)
t1.hideturtle()
t2.hideturtle()
turtle.done()
