
import turtle
import random

turtle.tracer(1,0)

colors=["blue","red","yellow","magenta","orange","green","gray","pink","purple","white","GOLD",]
turtle.hideturtle()
turtle.bgcolor("cyan")
SIZE_X= 1200
SIZE_Y= 600

turtle.setup(SIZE_X+50, SIZE_Y+50)

border = turtle.clone()
border.penup()
border.goto(SIZE_X/2,-SIZE_Y/2)
border.pendown()
border.goto(SIZE_X/2,SIZE_Y/2)
border.goto(-SIZE_X/2,SIZE_Y/2)
border.goto(-SIZE_X/2,-SIZE_Y/2)
border.goto(SIZE_X/2,-SIZE_Y/2)
border.hideturtle()

turtle.hideturtle()
turtle.resizemode('user')
turtle.penup()

UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
TIME_STEP = 100
START_LENGTH=1

SPACEBAR = 'space'

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3





food=turtle.clone()
food.penup()
food.shape("circle")
pos_list=[]
score_list = []
stamp_list=[]
food_stamps=[]
food_pos=[]
Food_size=[]
original_size = 20
r = original_size/2

circle=turtle.clone()
circle.shape("circle")
CIRCLE_SIZE = 1
circle.shapesize(CIRCLE_SIZE, CIRCLE_SIZE , 1)
my_pos=circle.pos()
pos_list.append(my_pos)
cstamp=circle.stamp()
stamp_list.append(cstamp)

delay_food = 1000

score = 0
   
def make_food():
    color=random.choice(colors)
    food.color(color)
    min_x=-int(SIZE_X/2/original_size)+1
    max_x=int(SIZE_X/2/original_size)-1
    min_y=-int(SIZE_Y/2/original_size)+1
    max_y=int(SIZE_Y/2/original_size)-1
    food_x=random.randint(min_x,max_x)*original_size
    food_y=random.randint(min_y,max_y)*original_size
    food_size=random.randint(1,6)*0.25*CIRCLE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food.shapesize(food_size,food_size,1)
    aliens=food.stamp()
    food_stamps.append(aliens)
    Food_size.append(food_size*original_size)
for i in range(10):
    make_food()


direction = UP
UP_EDGE = SIZE_Y/2
DOWN_EDGE = -SIZE_Y/2
LEFT_EDGE = -SIZE_X/2
RIGHT_EDGE = SIZE_X/2

def up():
    global direction
    direction = UP
    print('You pressed the up key!')
    
def down():
    global direction
    direction = DOWN
    print('You pressed the down key!')

def left():
    global direction
    direction = LEFT
    print('You pressed the left key!')

def right():
    global direction
    direction = RIGHT
    print('You pressed the right key!')





def eat_food():
    global CIRCLE_SIZE, score
    
    new_pos = circle.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    eaten_food = []
    
    for i in range(len(food_pos)):
        current_food = food_pos[i]
        x_food = current_food[0]
        y_food = current_food[1]

        distance = ((x_food - new_x_pos)**2 + (y_food - new_y_pos)**2)**0.5
        check = Food_size[i]/2 + CIRCLE_SIZE*original_size/2
        if distance <= check and Food_size[i] >= CIRCLE_SIZE*original_size:
            quit()
        if distance <= check and Food_size[i] <= CIRCLE_SIZE*original_size:
            eaten_food.append(i)
            make_food()

        
    for food_ind in eaten_food:
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        Food_size.pop(food_ind)
        CIRCLE_SIZE += 0.1
        circle.shapesize(CIRCLE_SIZE,CIRCLE_SIZE,1)
        print('you have eaten the food')

        turtle.clear()
        score = score +1
        turtle.goto(-SIZE_X/2+5, SIZE_Y/2-12)
        turtle.write('score = ' + str(score))

        
def move_circle():
    global score
    new_pos = circle.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    eaten_food = []
   
    
 
    if UP_EDGE - new_y_pos <= CIRCLE_SIZE*original_size/2:
        print("you hit the upper edge... game over")
        quit()
    if new_y_pos - DOWN_EDGE <= CIRCLE_SIZE*original_size/2:
        print("you hit the right lower... game over")
        quit()
    if new_x_pos - LEFT_EDGE <= CIRCLE_SIZE*original_size/2:
        print("you hit the left edge... game over")
        quit()

    if RIGHT_EDGE - new_x_pos <= CIRCLE_SIZE*original_size/2:
        print("you hit the right edge... game over")
        quit()


# CIRCLE_SIZE is the scaling factor and not the actual number of pixels
    step = CIRCLE_SIZE*original_size*0.5
    if direction == RIGHT:
        circle.goto(new_x_pos + step, new_y_pos)
        print('you moved right!')
    
    elif direction == LEFT:
        circle.goto(new_x_pos - step, new_y_pos)
        print('you moved left!')
    elif direction == DOWN:
        circle.goto(new_x_pos, new_y_pos - step)
        print('you moved down!')


    elif direction == UP:
        circle.goto(new_x_pos, new_y_pos + step)
        print('you moved up!')
        
    pos_list.append(my_pos)
    lubna = stamp_list.pop(0)
    circle.clearstamp(lubna)
    cstamp = circle.stamp()
    stamp_list.append(cstamp)

    eat_food()

    turtle.ontimer(move_circle,TIME_STEP)
  
move_circle()
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW) 
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()



