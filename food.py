import turtle
import random
colors=["blue","red","yellow","magenta","orange","black","green","gray","pink","purple","white","GOLD",]
turtle.hideturtle()
turtle.bgcolor("cyan")
SIZE_X= 800
SIZE_Y= 500
food=turtle.clone()
food.penup()
turtle.setup(SIZE_X+50, SIZE_Y+50)
triangle = turtle.clone()

triangle.penup()
triangle.goto(SIZE_X/2,-SIZE_Y/2)
triangle.pendown()
triangle.goto(SIZE_X/2,SIZE_Y/2)
triangle.goto(-SIZE_X/2,SIZE_Y/2)
triangle.goto(-SIZE_X/2,-SIZE_Y/2)
triangle.goto(SIZE_X/2,-SIZE_Y/2)

triangle.hideturtle()
turtle.penup()

UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
TIME_STEP = 100
START_LENGTH=5

SPACEBAR = 'space'

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


    
SQUARE_SIZE= 20
r = SQUARE_SIZE/2
food.shape("circle")
pos_list=[]
stamp_list=[]
food_stamps=[]
food_pos=[]
Food_size=[]
circle=turtle.clone()
circle.shape("circle")
c=0
turtle.hideturtle()
CIRCLE_SIZE = 50
score = 0
for i in range (START_LENGTH):
    food_pos_x=food.pos()[0]
    food_pos_y=food.pos()[1]
    x_pos=circle.pos()[0]
    y_pos=circle.pos()[1]
    my_pos=(x_pos,y_pos)
    circle.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    cstamp=circle.stamp
    stamp_list.append(cstamp)
def make_food():
    global x
    color=random.choice(colors)
    food.color(color)
    min_x=-int(SIZE_X/2.5/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2.5/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2.5/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2.5/SQUARE_SIZE)+1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food_size=random.randint(20,90)
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food.dot(food_size)
    aliens=food.stamp()
    food_stamps.append(aliens)
    Food_size.append(food_size)

for i in range(20):
    make_food()
    
direction=UP
UP_EDGE=SIZE_Y/2
DOWN_EDGE=-SIZE_Y/2
LEFT_EDGE = -SIZE_X/2
RIGHT_EDGE = SIZE_X/2

def up ():
    global direction
    if direction== DOWN:
        print("you pressed down")
def down():
    global direction
    if direction == UP:
        print ("you pressed up")
def left():
    global direction
    if direction== LEFT:
        print("you pressed left")
def right():
    global direction
    if direction == RIGHT:
        print("you pressed right")

def move_circle():
    global score
    my_pos = circle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = circle.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    i = 0
    for current_food in food_pos:
        x_food = current_food[0]
        y_food = current_food[1]

        distance = ((x_food - x_pos)**2 + (y_food - y_pos)**2)**0.5
        check = Food_size[i]/2 + CIRCLE_SIZE/2
        
        if distance <= check:
            food_ind = food_pos.index((x_food, y_food))
            food.clearstamp(food_stamps[food_ind])
            food_pos.pop(food_ind)
            food_stamps.pop(food_ind)
            circle.dot(CIRCLE_SIZE + 5)
            print('you have eaten the food')

            turtle.clear()
            score = score +1
            turtle.goto(-SIZE_X/2+5, SIZE_Y/2-12)
            turtle.write('score = ' + str(score))
        i = i + 1
    
 
    if new_y_pos >= UP_EDGE:
        print("you hit the upper edge... game over")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("you hit the right lower... game over")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("you hit the left edge... game over")
        quit()

    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge... game over")
        quit()


        
    if direction == RIGHT:
        circle.goto(x_pos + CIRCLE_SIZE, y_pos)
        print('you moved right!')
    
    elif direction == LEFT:
        circle.goto(x_pos - CIRCLE_SIZE, y_pos)
        print('you moved left!')
    elif direction == DOWN:
        circle.goto(x_pos, y_pos - CIRCLE_SIZE)
        print('you moved down!')
    elif direction == UP:
        circle.goto(x_pos, y_pos + CIRCLE_SIZE)
        print('you moved up!')

    my_pos = circle.pos()
    pos_list.append(my_pos)
    new_stamp = circle.stamp()
    stamp_list.append(new_stamp)
    old_stamp = stamp_list.pop(0)
    circle.clearstamp(old_stamp)
    pos_list.pop(0)

    turtle.ontimer(move_circle,TIME_STEP)
  
move_circle()
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW) 
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()


