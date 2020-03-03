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

