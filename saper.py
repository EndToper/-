import tkinter as tk
import random as r

types = 1
def hello(event):
    global types
    x = event.widget.his_x
    y = event.widget.his_y
    massive = [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]
    count_bombs = 0
    for i in range(len(massive)):
        for btn in btns:
            if btn.his_x == massive[i][0] and btn.his_y == massive[i][1] and btn.bomb == True:
                count_bombs = count_bombs + 1
    event.widget["state"] = "disabled"
    if types == 90:
        print("победа")
    if event.widget.bomb == False:
        event.widget["text"] = count_bombs
        if event.widget.type == 0:
            event.widget.type = types
            print(event.widget.type)
            types = types + 1
    if event.widget.bomb == True:
        event.widget["text"] = "boom"
        print("поражение")
        lose()
        
def lose():
    global types
    for i in range(len(btns)):
        x = btns[i].his_x
        y = btns[i].his_y
        massive = [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]
        count_bombs = 0
        for j in range(len(massive)):
            for btn in btns:
                if btn.his_x == massive[j][0] and btn.his_y == massive[j][1] and btn.bomb == True:
                    count_bombs = count_bombs + 1
        btns[i]["state"] = "disabled"
        if btns[i].bomb == False:
            btns[i]["text"] = count_bombs
            if btns[i].type == 0:
                btns[i].type = types
                types = types + 1
        if btns[i].bomb == True:
            btns[i]["text"] = "boom"
            
   
    





window= tk.Tk()
window.geometry("500x500")
pixelVirtual = tk.PhotoImage(width=1, height=1)

window.bind("<Button-1>", hello)
y1,x1 = 0,0

btns = []
for i in range(1,101,1):
    btn = tk.Button(window, text=" ", height = 50, width = 50,  compound="c", image=pixelVirtual)
    btn.num = i
    btn.bomb = False
    btn.his_x = None
    btn.his_y = None
    btn.type = 0
    btns.append(btn)

for btn in btns:
    btn.his_x = int(x1 / 50)
    btn.his_y = int(y1 / 50)
    btn.place(x = x1, y = y1)
    if btn.num % 10 == 0:
        y1 = int(btn.num*5)
        x1 = 0
    else:
        x1 = (btn.num % 10) * 50
        
for i in range(10):
    rint = r.randint(1,100)
    for btn in btns:
        if btn.num == rint:
            btn.bomb = True
            btn.type = -1


window.mainloop()