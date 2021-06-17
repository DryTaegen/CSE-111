import math
from datetime import datetime
current_time = datetime.now(tz=None)
def equasion(width, aspect, diameter):
    volume = (math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter))/10000000
    return volume
while True:
    try:
        width = int(input("Enter the width of the tire in mm.: "))
        aspect = int(input("Enter the aspect ratio of the tire: "))
        diameter = int(input("Enter the diameter of the wheel in inches: "))        
    except ValueError:
        print("I'm sorry, that wasn't a recognized value. Make sure to enter only numerical values.")
    volume = equasion(width, aspect, diameter)
    print(f"The approximate volume is {volume:.1f} milliliters.")
    with open("volumes.txt", "at") as volumes_file:
        print(f"{current_time}: width of tire: {width} mm, aspect ratio of tire: {aspect}, diameter of the wheel: {diameter} inches, Volume: {volume} ml.", file=volumes_file)
    try_again = input("Do you want to calculate another volume? [yes/no]: ")
        
    if try_again.lower() == "yes":
        continue
    elif try_again.lower() == "no":
        break


    