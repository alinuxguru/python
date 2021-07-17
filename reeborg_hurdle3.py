#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

print(front_is_clear())
print(wall_in_front())
print(at_goal())

def turn_right():
    turn_left()
    turn_left()
    turn_left()
      
while at_goal() == False:
    if front_is_clear() == True and wall_in_front() == False:
        while wall_in_front() == False and at_goal() == False:
            move()
        if at_goal() == False:
            turn_left()
            move()
            turn_right()
            move()
            turn_right()
            move()
            turn_left()
        else:
            print("reached")
                             
    elif front_is_clear() == False and wall_in_front() == True:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
