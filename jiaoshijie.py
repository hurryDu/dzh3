'''
-luyi-
-教师节贺卡
'''
import turtle as t
t.setup(480,600)
t.bgcolor("#2e92cd")
t.title("祝老师们教师节快乐！")
t.speed(5)

#爱心
def love(du,x,y,c):
    t.penup()
    t.goto(x,y)
    t.setheading(135+du)
    t.color(c)
    t.pendown()
    t.begin_fill()
    t.forward(25)
    t.left(10)
    t.circle(-12,220)
    t.setheading(70+du)
    t.circle(-12,220)
    t.left(10)
    t.forward(25)
    t.end_fill()

#边框
t.pensize(2)
t.pencolor("red")
P = ((-220,280),(-215,275))
A = (436,556,436,556,426,546,426,546)
for i in range(2):
    t.penup()
    t.goto(P[i])
    t.pendown()
    for j in range(4):
        t.forward(A[4*i+j])
        t.right(90)

#花盆
t.penup()
t.goto(-150,-100)
t.color("#72699e")
t.pendown()
t.begin_fill()
t.forward(200)
t.right(110)
t.forward(120)
t.right(70)
t.forward(118)
t.right(70)
t.forward(120)
t.end_fill()

#花杆
t.speed(2)
t.penup()
t.home()
t.goto(-60,-100)
t.color("#68aa60")
t.pendown()
t.begin_fill()
A = (10,200)
for i in range(4):
    t.forward(A[i%2])
    t.left(90)
t.end_fill()

#左叶子
t.penup()
t.goto(-60,-50)
t.setheading(140)
t.color("#559242")
t.pendown()
t.begin_fill()
t.circle(40, 60) 
t.circle(-70, 90)
t.setheading(-20)
t.circle(40, 40) 
t.circle(-60, 60)
t.end_fill()

#右叶子
t.penup()
t.goto(-50,-50)
t.setheading(40)
t.color("#559242")
t.pendown()
t.begin_fill()
t.circle(-40, 60) 
t.circle(70, 90)
t.setheading(200)
t.circle(-40, 40) 
t.circle(60, 60)
t.end_fill()

#花朵
t.speed(10)
t.penup()
t.goto(-55,100)
C = ["#e0f157","#fb9ebd"]
for i in range(12):
    t.setheading(i*30)
    t.color(C[i%2])
    t.pendown()
    t.begin_fill()
    t.circle(70, 90)
    t.setheading(i*30+180)
    t.circle(70, 90)
    t.end_fill()

#教师节快乐文字
t.speed(1)
t.color("#b1352b")
txt="教师节快乐"
x=((100,170),(110,110),(120,50),(130,-10),(140,-70))
for i in range(5):
    t.penup()
    t.goto(x[i])
    t.pendown()
    t.write(txt[i],align="center",font=("华文行楷",52,"bold"))

t.speed(5)
love(45,50,220,"#e4f188")
love(-30,160,160,"#f8a7c7")
love(30,-140,-130,"#f8a7c7")
love(20,140,-160,"#e4f188")
love(26,-30,-260,"#f8a7c7")

t.color("#b1352b")
t.penup()
t.goto(160,-260)
t.pendown()
t.write("9.10",align="center",font=("华文行楷",26,"bold"))

t.hideturtle()
t.done()




