"ESTE ES EL QUE EL TIPO DEL VIDEO HIZO"
print("Hello this is a car game. To start, try by typing 'help'")
user_input = ""
started = False
while True:
    user_input = input("> ").lower()
    if user_input == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit the game""")
    elif user_input == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif user_input == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif user_input == "quit":
        print("Thank you for playing!")
        break
    else:
        print("that's an input that I do not understand. Try typing 'help'")
        
"done 03/03/2020"

"DONE BY ME"
print("This is a car game, start by typing 'help': ")
command = ""
car_has_started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if car_has_started:
            print("Car has already started")
        else:
            car_has_started = True
            print("Car has started")
    elif command == "stop":
        if not car_has_started:
            print("Car has already stopped")
        else:
            car_has_started = False
            print("Car has stopped")
    elif command == "help":
        print("""
start - car starts
stop - car stops
quit - quits the game""")
    elif command == "quit":
        print("Thank you for playing")
        break
    else:
        print("Please type 'help' for instructions")

