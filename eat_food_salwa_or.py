def eat_food():
    if circle.pos() in food_pos:
        food_size=food_pos.index(circle.pos())
        food.clearstamp(food_stamps[food_size])
    if circle_size>=check:
        print("you have eaten the food!")       

    else:
        quit()

eat_food()
