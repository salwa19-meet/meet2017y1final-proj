import turtle
import random
colors=["blue","red","yellow","magenta","orange","black","green","gray","pink","purple","white","GOLD",]
turtle.hideturtle()
turtle.bgcolor("cyan")
SIZE_X= 800
SIZE_Y= 500
food=turtle.clone()
food.penup()

    
SQUARE_SIZE= 20
food.shape("circle")
pos_list=[]
food_stamps=[]
food_pos=[]
x=0
delay_food = 1000
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
    food_size=random.randint(20,100)
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food.dot(food_size)
    aliens=food.stamp()
    food_stamps.append(aliens) 
    turtle.ontimer(make_food,delay_food)    
        
    
make_food()
