import turtle
import random

start = turtle.Turtle()
start.hideturtle()
start.penup()
start.goto(0,20)
start.write("승부차기를 시작합니다.", False, "center", ("",12,""))
start.goto(0,-20)
start.write("왼쪽으로 차려면 'l', 중앙으로 차려면 'c', 오른쪽으로 차려면 'r'을 눌러주세요", False, "center", ("",12,""))

tball = turtle.Turtle()
tkeep = turtle.Turtle()

screen = turtle.Screen()

iball = "image\\ball.gif"
ileft = "image\\left.gif"
icenter = "image\\center.gif"
iright = "image\\right.gif"

screen.addshape(iball)
screen.addshape(ileft)
screen.addshape(icenter)
screen.addshape(iright)

tball.hideturtle()
tball.shape(iball)
tball.penup()

tkeep.hideturtle()
tkeep.penup()

ox = []

cnt = 0

def score():
    start.goto(0, 200)
    start.clear()
    start.write("슈팅결과:" +str(ox), False, "center")

def ending():
    r = turtle.Turtle()
    r.hideturtle()
    result = turtle.textinput("승부차기 종료", "최종 결과를 확인하시겠습니까? - 예 = y, 아니오 = n")
    if(result == 'n'):
        screen.clear()
        r.write("승부차기 게임을 종료합니다.", False, "center", ("",15,""))
    else:
        screen.clear()
        if(ox.count('O')>ox.count('X')):
            r.write("승부차기에 성공하였습니다!", False, "center", ("",15,""))
        else:
            r.write("승부차기에 실패하였습니다.", False, "center", ("",15,""))

def keep_opt():
    options=['l','c','r']
    global keep_choice
    keep_choice = random.choice(options)
    if(keep_choice == 'l'):
        tkeep.hideturtle()
        tkeep.home()
        tkeep.shape(ileft)
        tkeep.stamp()               #왼쪽막는골키퍼

    elif(keep_choice == 'c'):
        tkeep.hideturtle()
        tkeep.home()
        tkeep.shape(icenter)
        tkeep.stamp()               #가운데막는골키퍼

    elif(keep_choice == 'r'):
        tkeep.hideturtle()
        tkeep.home()
        tkeep.shape(iright)
        tkeep.stamp()               #오른쪽막는골키퍼

def kick_l():
    global cnt
    cnt+=1
    tkeep.clear()
    keep_opt()
    start.clear()
    tball.hideturtle()
    tball.home()
    tball.showturtle()
    tball.goto(-100, 90)
    tball.stamp()
    if(keep_choice == 'l'):
        ox.append('X')
        score()
    else:
        ox.append('O')
        score()
    if(cnt==5):
        ending()

def kick_c():
    global cnt
    cnt+=1
    tkeep.clear()
    keep_opt()
    start.clear()
    tball.hideturtle()
    tball.home()
    tball.showturtle()
    tball.goto(5, 62)
    tball.stamp()
    if(keep_choice == 'c'):
        ox.append('X')
        score()
    else:
        ox.append('O')
        score()
    if(cnt==5):
        ending()

def kick_r():
    global cnt
    cnt+=1
    tkeep.clear()
    keep_opt()
    start.clear()
    tball.hideturtle()
    tball.home()
    tball.showturtle()
    tball.goto(100, 90)
    tball.stamp()
    if(keep_choice == 'r'):
        ox.append('X')
        score()
    else:
        ox.append('O')
        score()
    if(cnt==5):
        ending()

screen.onkey(kick_l, 'l')
screen.onkey(kick_c, 'c')
screen.onkey(kick_r, 'r')

screen.listen()
