from turtle import *

width(5)
begin_fill()

#body

color("green")

forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

end_fill()

#Roof



forward(200)
left(90)

forward(200)

color("red")
begin_fill()


left(45)
forward(150)

left(94)
forward(145)

left(130)
forward(200)
end_fill()


#door

penup()
goto(60, 0)
pendown()

begin_fill()
color("black")

left(90)
forward(100)

right(90)
forward(75)

right(90)
forward(100)

end_fill()

#winows

penup()
goto(20, 160)
pendown()
color("white")
begin_fill()

forward(40) 

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill()


#window2
penup()
goto(180, 160)
pendown()
color("white")
begin_fill()

forward(40) 

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill()




