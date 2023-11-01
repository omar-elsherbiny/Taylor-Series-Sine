import turtle
from math import factorial, sin, pi
from decimal import Decimal

L=300
def Taylor(x,limit):
    res=0
    for n in range(limit):
        odd_n=Decimal(2*n+1)
        sign=Decimal(1 if (n+1)%2==1 else -1)
        exp= Decimal(x)**odd_n
        fact=Decimal(factorial(float(odd_n)))
        res += Decimal(sign * exp / fact)
        #res += Decimal(1 if (n+1)%2==1 else -1) * Decimal(x**(2*n+1)) / Decimal(factorial(2*n+1))
        #print(2*n+1, (1 if (n+1)%2==1 else -1))
    return float(res)

turtle.title(f'Sin(x) estimator | Taylor series                                                    Limit: {L}')
turtle.Screen().cv._rootwindow.resizable(False, False)
turtle.Screen().setup(800, 500)
turtle.colormode(255)
turtle.tracer(0, 0)
p=turtle.Turtle()
p.hideturtle()
p.speed(0)
p.penup()
o=turtle.Turtle()
o.hideturtle()
o.speed(0)
o.penup()
o.color((255, 10, 50))

x=-400
p.goto(400,0)
p.pendown()
p.goto(-400,0)
o.goto(-400,100*Taylor(-400/(20*pi),L))
o.pendown()
while x<=400:
    x+=1
    p.goto(x,100*sin(x/(20*pi)))
    o.goto(x,100*Taylor(x/(20*pi),L))

turtle.update()
turtle.exitonclick()
