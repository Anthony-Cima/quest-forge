"""QuestForge - a tiny text-adventure engine.

Run it with:  python main.py
"""

import storage
from features import core, reports


def show_menu():
    print()
    print("=== QuestForge ===")
    print("1) Look")
    print("2) Move")
    print("3) List rooms")
    print("4) Room count")
    print("5) Exits here")
    print("6) Exit breakdown")
    print("7) First exit here")
    print("8) World summary")
    print("0) Quit")


def main():
    data = storage.load_data()
    current = core.start_room(data)
    while True:
        show_menu()
        try:
            choice = input("Pick an option: ").strip()
        except EOFError:
            print()
            break
        if choice == "0":
            print("See you next session!")
            break
        elif choice == "1":
            room = core.get_rooms(data)[current]
            print(core.describe(room))
            print("Exits: " + ", ".join(core.exits_for(room)))
        elif choice == "2":
            direction = input("Direction: ").strip()
            current = core.move(data, current, direction)
            print(core.describe(core.get_rooms(data)[current]))
        elif choice == "3":
            for key in core.get_rooms(data):
                print(key)
        elif choice == "4":
            print("This world has " + str(core.room_count(data)) + " rooms.")
        elif choice == "5":
            print(str(current) + " exits from here.")
        elif choice == "6":
            print(core.exits_by_room(data))
        elif choice == "7":
            room = core.get_rooms(data)[current]
            print(core.first_exit(room))
        elif choice == "8":
            print(reports.world_summary(data))
        else:
            print("Please pick a number from the menu.")


if __name__ == "__main__":
    main()
