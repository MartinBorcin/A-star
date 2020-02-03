import time, tkinter

WIDTH = 10
HEIGHT = 10

A = (9, 2)
B = (1, 9)
obstacles = [(9, 3), (8, 3), (8, 2),]#[(8, 0), (8, 1), (8, 3), (8, 4), (8, 5), (8, 7), (8, 6), (8, 2), (8, 9), (7, 9), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 0), (4, 9), (4, 6), (4, 7), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (5, 9), (3, 9), (2, 9), (2, 8), (1, 8), (1, 7), (1, 6), (1, 5), (3, 6), (1, 4), (2, 4), (1, 3), (1, 2), (3, 2), (3, 0), (2, 0), (1, 0), (0, 0)]

win = tkinter.Tk()
canvas = tkinter.Canvas(win, width=1000, height = 1000)
canvas.pack()

for x in range(0, WIDTH*100, 100): canvas.create_line(x, 0, x, 1200, width=5)
for y in range(0, HEIGHT*100, 100): canvas.create_line(0, y, 1200, y, width=5)
canvas.create_rectangle(A[1]*100, A[0]*100, A[1]*100+100, A[0]*100+100, fill='blue')
canvas.create_text(A[1]*100+50, A[0]*100+50, text='A', font = 'Arial 40')
canvas.create_rectangle(B[1]*100, B[0]*100, B[1]*100+100, B[0]*100+100, fill='blue') 
canvas.create_text(B[1]*100+50, B[0]*100+50, text='B', font = 'Arial 40')
canvas.update()

matrix = [['.' for x in range(WIDTH)] for y in range(HEIGHT)]
matrix[A[0]][A[1]] = 'A'
matrix[B[0]][B[1]] = 'B'
for o in obstacles:
    matrix[o[0]][o[1]] = 'X'
    canvas.create_rectangle(o[1]*100,o[0]*100, o[1]*100+100,o[0]*100+100, fill='black')
    canvas.update()

def show_matrix(matrix):
    for l in matrix: print(l)
    

def h(S, B):
    return int((abs(S[0]-B[0])**2+abs(S[1]-B[1])**2)**0.5)*10
    
    
def reconstruct_path(cameFrom, current):
    totalPath = [current]
    while current in cameFrom.keys():
        current=cameFrom[current]
        totalPath = [current]+totalPath
    return totalPath


def find_path(A, B):
    global matrix
    openSet=[A]
    cameFrom = {}
    g = {A:0}
    f = {A:h(A, B)}
    while openSet!=[]:        
        openSet.sort(key=lambda x: f.get(x, float('inf')))
        current = openSet[0]
        print('current', current)
        canvas.create_oval(current[1]*100+45, current[0]*100+45, current[1]*100+55, current[0]*100+55, fill='black')
        if current==B:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        canvas.create_rectangle(current[1]*100+10, current[0]*100+10, current[1]*100+90, current[0]*100+90, fill='red')
        
        for tile in [(current[0]-1,current[1]),(current[0], current[1]-1),(current[0]+1, current[1]),(current[0], current[1]+1)]:
            print('looking at:', tile)
            if tile[0]>0 and tile[1]>0:
                try:
                    if matrix[tile[0]][tile[1]]!='X':
                        pre_g = g[current]+10
                        if pre_g < g.get((tile[0], tile[1]), float('inf')):
                            cameFrom[(tile[0], tile[1])] = current
                            g[(tile[0], tile[1])] = pre_g
                            f[(tile[0], tile[1])] = g[(tile[0], tile[1])]+h((tile[0], tile[1]), B)
                            matrix[tile[0]][tile[1]]=str(f[(tile[0], tile[1])])
                            show_matrix(matrix)
                            canvas.create_rectangle(tile[1]*100+10, tile[0]*100+10, tile[1]*100+90, tile[0]*100+90, fill='green')
                            canvas.update()
                            #time.sleep(.1)
                            if (tile[0], tile[1]) not in openSet:
                                openSet.append((tile[0], tile[1]))
                except IndexError: print('out')

        #diagonal movement
        for tile in [(current[0]+1, current[1]+1), (current[0]-1, current[1]+1), (current[0]-1, current[1]-1), (current[0]+1, current[1]-1)]:
            print('looking at:', tile)
            if tile[0]>0 and tile[1]>0:
                try:
                    if matrix[tile[0]][tile[1]]!='X':
                        pre_g = g[current]+14
                        if pre_g < g.get((tile[0], tile[1]), float('inf')):
                            cameFrom[(tile[0], tile[1])] = current
                            g[(tile[0], tile[1])] = pre_g
                            f[(tile[0], tile[1])] = g[(tile[0], tile[1])]+h((tile[0], tile[1]), B)
                            matrix[tile[0]][tile[1]]=str(f[(tile[0], tile[1])])
                            show_matrix(matrix)
                            canvas.create_rectangle(tile[1]*100+10, tile[0]*100+10, tile[1]*100+90, tile[0]*100+90, fill='green')
                            canvas.update()
                            #time.sleep(.01)
                            if (tile[0], tile[1]) not in openSet:
                                openSet.append((tile[0], tile[1]))
                except IndexError: print('out')                                                                                                                      
                
    return 'There is no path'

path=find_path(A, B)
print('path:', path)
matrix = [['.' for x in range(10)] for y in range(10)]
matrix[A[0]][A[1]] = 'A'
matrix[B[0]][B[1]] = 'B'
for o in obstacles: matrix[o[0]][o[1]] = 'X'
for tile in path[1:-1]:
    matrix[tile[0]][tile[1]]='o'
    canvas.create_rectangle(tile[1]*100+25,tile[0]*100+25, tile[1]*100+75,tile[0]*100+75, fill='yellow')
    canvas.update()
show_matrix(matrix)

