import turtle as t
import datetime as dt
import time
#import simpleaudio as sa

clock=t.Screen()
clock.bgcolor('black')
clock.setup(800,800)
clock.tracer(0)
#画笔
pen=t.Turtle()
pen.ht()
#pen.up()
pen.speed(0)
pen.pensize(3)
#bgmusic=sa.WaveObject.from_wave_file('bgmusic.wav')

def draw_clock(h,m,s):
    
    pen.clear()
    pen.up()
    pen.goto(0,-350)
    pen.color('green')
    pen.down()
    pen.seth(0)
    pen.circle(350)
    #刻度
    
    pen.up()
    pen.goto(0,0)
    pen.seth(90)
    for _ in range(12):
        pen.fd(330)
        pen.down()
        pen.fd(20)
        pen.up()
        pen.goto(0,0)
        pen.rt(30)
        
    #分针、秒针
    pen.up()
    pen.goto(0,0)
    pen.color('blue')
    pen.down()
    pen.seth(90)
    pen.rt(s/5*30)
    pen.fd(280)
    
    pen.up()
    pen.goto(0,0)
    pen.color('yellow')
    pen.down()
    pen.seth(90)
    pen.rt(m/5*30+s/5*30/360*6)
    pen.fd(240)
    
    #时针
    pen.up()
    pen.goto(0,0)
    pen.color('red')
    pen.down()
    pen.seth(90)
    pen.rt(h%12*30+m/5*30/360*30)
    pen.fd(200)
    
    pen.up()
    pen.goto(-250,360)
    font=("宋体",20,'bold')
    Hello = "新年快乐！今天是{}年{}月{}日".format(now.year,now.month,now.day)
    pen.write(Hello,'center',font=font)
    



now=dt.datetime.now()
draw_clock(now.hour,now.minute,now.second)

while True:
    clock.update()
    time.sleep(1)
    now=dt.datetime.now()
    draw_clock(now.hour,now.minute,now.second)
    
   


clock.mainloop()