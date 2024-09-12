# #Space Time Traveler
print ("Welcome to the space travel calculator")
distance = int(input("What is the distance to your destination in light years?"))
print (distance)
speed = float(input("What is the speed of your spaceship as a fraction of the speed of light?"))
print (speed)
time = distance/speed 
print("It will take you", time, "years to get to your destination")