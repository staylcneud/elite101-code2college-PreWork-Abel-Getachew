def chatbot():
    # Welcome the user
    print(" Hello! Welcome to the Mall!")

    # Get user's name and age
    name = input(" What's your name? ")
    age = input(" How old are you? ")

    print(f"\nNice to meet you, {name}! You're {age} years old.")
    print("How can I help you today?")

    # Start menu loop
    while True:
        print("\n Menu Options:")
        print("1. Learn about the mall")
        print("2. Get directions")
        print("3. Check promotions")
        print("4. Exit")

        choice = input("Please enter the number of your choice: ")

        if choice == "1":
            print("Here's some info about the mall...")
        elif choice == "2":
            print("Let me help you with directions...")
        elif choice == "3":
            print("Let's check out some promotions...")
        elif choice == "4":
            print(f"👋 Goodbye, {name}! Thanks for talking. Have a great day!")
            break
        else:
            print(" Invalid choice. Please select a valid option from the menu.")

chatbot()
