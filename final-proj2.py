import turtle
import random
#<<<<<<< HEAD
#=======
colors=["blue","red","yellow","magenta","orange","green","gray","pink","purple","white","GOLD",]
turtle.hideturtle()
turtle.bgcolor("cyan")
#>>>>>>> b99fa06fc78aa3b292502a317925802f29f8fdda

turtle.tracer(1,0)

SIZE_X = 800
SIZE_Y = 500
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


CIRCLE_SIZE = 20
START_LENGTH = 1


r = CIRCLE_SIZE/2

min_size_food = 20
max_size_food = 100

food = turtle.clone()
food.shape('circle')
food_size=[]
original_size = 20
x=random.randint(min_size_food , max_size_food)
food.dot(x)

UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
TIME_STEP = 100

SPACEBAR = 'space'

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

score_list = []
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
circle = turtle.clone()
circle.shape("circle")

score = 0

turtle.hideturtle()

for i in range(START_LENGTH):
    food_pos_x = food.pos()[0]
    food_pos_y = food.pos()[1]
    x_pos = circle.pos()[0]
    y_pos = circle.pos()[1]
    x_pos += CIRCLE_SIZE
    my_pos = (x_pos,y_pos)
    circle.goto(x_pos,y_pos)
    pos_list.append(x_pos)
    cstamp = circle.stamp()
    stamp_list.append(cstamp)

def make_food():
    min_x = -int(SIZE_X/2/CIRCLE_SIZE)+1
    max_x = int(SIZE_X/2/CIRCLE_SIZE)-1
    min_y = -int(SIZE_Y/2/CIRCLE_SIZE)+1
    max_y = int(SIZE_Y/2/CIRCLE_SIZE)-1

    food_x = random.randint(min_x,max_x) *CIRCLE_SIZE
    food_y = random.randint(min_y,max_y) *CIRCLE_SIZE
    food.goto(food_x,food_y)
    k = (food_x,food_y)
    food_pos.append(k)
    xfoodx = food.stamp()
    food_stamps.append(xfoodx)
    
Food_size=20
check = Food_size/2 + CIRCLE_SIZE/2
direction = UP
UP_EDGE = SIZE_Y/2
def up():
    global direction
    if direction != DOWN:
       direction = UP
    print('You pressed the up key!')
    

direction = DOWN
DOWN_EDGE = -SIZE_Y/2
def down():
    global direction
    if direction != UP:
        direction = DOWN
    print('You pressed the down key!')

direction = LEFT
LEFT_EDGE = -SIZE_X/2
def left():
    global direction
    if direction != RIGHT:
        direction = LEFT
    
    print('You pressed the left key!')

direction = RIGHT
RIGHT_EDGE = SIZE_X/2
def right():
    global direction
    if direction != LEFT:
        direction = RIGHT
    print('You pressed the right key!')

def move_circle():
    global score,check,Food_size,CIRCLE_SIZE
    my_pos = circle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = circle.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]



 
    global food_stamps, food_pos
    
    if ((food_pos_x - x_pos)**2 + (food_pos_y -  y_pos)**2) <= r**2:
        food_ind = food_pos.index((food_pos_x, food_pos_y))
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        circle.dot(CIRCLE_SIZE + 10)
        make_food()
        print('you have eaten the food')

        turtle.clear()
        score = score +1
        score_list.append(score)
        turtle.goto(-SIZE_X/2+5, SIZE_Y/2-12)
        turtle.write('score = ' + str(score))
        

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




make_food()
##food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
##food_stamps = []
##for a in food_pos:
##    food.goto(a)
##    food_stamp = food.stamp()
##    food_stamps.append(food_stamp)

def eat_food():
    if circle.pos() in food_pos:
        food_size=food_pos.index(circle.pos())
        food.clearstamp(food_stamps[food_size])
    if CIRCLE_SIZE>=check:
        print("you have eaten the food!")       

    else:
        quit()

eat_food()





















