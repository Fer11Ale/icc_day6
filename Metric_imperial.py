# let's next write a program that converts
# feet inches to meters
print("I will ask for 2 numbers: your feet first, and then, inches second. So, if you are 5 foot 4, please answer 5 first, and then 4 second. ")

# 1 foot = 0.3048 meters
feet = (input("How many feet tall are you? "))
# 1 inch = 0.0254 meters
inches = int(input(" ...and how many inches? "))

# note: the conversion rates are "HARD-CODED"
meters = str(feet * 0.3048 + inches * 0.0254)
# it appears that str() can also be added to line 13 directly 
print ("You are: " + meters + " meters tall." ) 
