def chatbot():
    # Welcome message
    print("Hello! Welcome to the Town East Mall Assistant.")
    print("I'm here to help you find your way around and learn what's happening at Town East Mall in Mesquite, Texas.")

    # Get user's name and age
    name = input("\nWhat's your name? ")
    age = input("How old are you? ")

    print(f"\nNice to meet you, {name}! You’re {age} years old.")
    print("How can I help you today?")

    # Main menu loop
    while True:
        print("\nMain Menu:")
        print("1. Learn about the mall")
        print("2. Get directions inside the mall")
        print("3. Check current promotions and store highlights")
        print("4. Food court and dining options")
        print("5. Events and announcements")
        print("6. Exit")

        choice = input("Please enter the number of your choice: ")

        if choice == "1":
            print("\nAbout Town East Mall:")
            print("Town East Mall is located at 2063 Town East Mall, Mesquite, TX 75150.")
            print("It is a two-level enclosed shopping center with over 1.2 million square feet of retail space.")
            print("Anchor stores include Macy’s, Dillard’s, JCPenney, and Dick’s Sporting Goods.")
            print("The mall is easily accessible from I-635, I-30, and US-80.")
            print("Mall hours: Monday–Thursday 11 AM–8 PM, Friday–Saturday 11 AM–9 PM, Sunday 12 PM–6 PM.")

        elif choice == "2":
            print("\nDirections and Mall Information:")
            print("Here are some common destinations inside the mall:")
            print("a. Clothing and fashion stores")
            print("b. Electronics and sporting goods")
            print("c. Restrooms and lounges")
            print("d. Parking and entrances")

            sub_choice = input("Enter your choice (a–d): ")

            if sub_choice.lower() == "a":
                print("Clothing stores are mostly located on the second floor near the center court escalators.")
            elif sub_choice.lower() == "b":
                print("Electronics and sporting goods, such as Dick’s Sporting Goods, are located on the first floor.")
            elif sub_choice.lower() == "c":
                print("Restrooms are on the first floor in the Dillard’s wing and on the second floor in the Macy’s wing.")
            elif sub_choice.lower() == "d":
                print("Parking lots surround the mall. Main entrances are off Town East Boulevard and nearby freeway exits.")
            else:
                print("Invalid option. Please try again.")

        elif choice == "3":
            print("\nCurrent Promotions and Store Highlights:")
            print("- Macy’s and Dillard’s frequently run seasonal clothing sales.")
            print("- JCPenney offers home and apparel discounts year-round.")
            print("- Check the mall’s main court for rotating pop-up shops and limited-time offers.")

        elif choice == "4":
            print("\nFood Court and Dining Options:")
            print("The Town East Mall food court has over 25 restaurants and seats more than 800 visitors.")
            print("Some popular spots include:")
            print("- Chick-fil-A")
            print("- Sbarro Pizza")
            print("- Charleys Philly Steaks")
            print("- BJ’s Restaurant & Brewhouse (sit-down dining option)")

        elif choice == "5":
            print("\nEvents and Announcements:")
            print("The mall occasionally hosts family events, holiday markets, and seasonal sales.")
            print("The former Sears space is being redeveloped for entertainment and mixed-use purposes.")
            print("Visit the Town East Mall website for updates on future events and new store openings.")

        elif choice == "6":
            print(f"\nGoodbye, {name}! Thanks for visiting the Town East Mall Assistant.")
            print("Have a great day and enjoy your time at the mall!")
            break

        else:
            print("Invalid choice. Please select a valid option from the menu.")


# Run the chatbot
chatbot()
