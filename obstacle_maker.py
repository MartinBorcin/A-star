import tkinter

WIDTH = 10
HEIGHT = 10

A = (9, 2)
B = (1, 9)
obstacles = []

f=open('obst.txt', 'w')
f.write('')
f.close()

win = tkinter.Tk()
saveButton = tkinter.Button(win, text='SAVE')
saveButton.pack(side=tkinter.RIGHT)
canvas = tkinter.Canvas(win, width=1000, height = 1000, bg='white')
canvas.pack()

for x in range(0, WIDTH*100, 100): canvas.create_line(x, 0, x, 1200, width=5)
for y in range(0, HEIGHT*100, 100): canvas.create_line(0, y, 1200, y, width=5)
canvas.create_rectangle(A[1]*100, A[0]*100, A[1]*100+100, A[0]*100+100, fill='blue')
canvas.create_text(A[1]*100+50, A[0]*100+50, text='A', font = 'Arial 40')
canvas.create_rectangle(B[1]*100, B[0]*100, B[1]*100+100, B[0]*100+100, fill='blue') 
canvas.create_text(B[1]*100+50, B[0]*100+50, text='B', font = 'Arial 40')
canvas.update()

graphic = list()
def add_obs(event):
    global obstacles, graphic
    x=event.x//100
    y=event.y//100
    if (y, x) not in obstacles:
        obstacles.append((y, x))
        graphic.append(canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, fill='black'))
        print(obstacles)


def del_obs(event):
    global obstacles, graphic
    x=event.x//100
    y=event.y//100
    if (y, x) in obstacles:
        canvas.delete(graphic[obstacles.index((y, x))])
        graphic.pop(obstacles.index((y, x)))
        obstacles.remove((y, x))
        print(obstacles)

    
def save(event):
    global obstacles
    f = open('obst.txt', 'a')
    for o in obstacles:
        for x, y in o: f.write(str(x)+', '+str(y)+'\n')
    print('successfully saved')

    
canvas.bind('<Button-1>', add_obs)
canvas.bind('<Button-3>', del_obs)
canvas.bind(saveButton, save)
