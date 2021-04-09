# Speed Calculator, AJ Dues, April 09, 2021, 2:19PM v0.1

keep_going = "Yes"

while keep_going == "Yes" or keep_going == "yes":

    distance = float(input("Please enter the distance and press enter.\n"))
    time = float(input("Please enter the time and press enter.\n"))

    speed = distance / time

    print(f"Using the distance of {distance} and time of {time} seconds, the speed is {speed} m/s.\n" )

    keep_going = input("Would you like to do another calculation? Type yes or no and push enter.\n")

print("Thank you for using this calculator.\n")


