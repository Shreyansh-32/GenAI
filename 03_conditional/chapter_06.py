seat_type = input("Enter the seat type (sleeper/AC/general/luxury) : ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper --> No air condition but beds available")
    case "ac":
        print("AC --> Air conditioned and comfy")
    case "general":
        print("General --> Cheapest, no beds")
    case "luxury":
        print("Luxury --> premium seats with meals")
    case _:
        print("Invalid seat type")