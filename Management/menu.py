class Menu:
    shapes = list()
    @staticmethod
    def start_menu():
        pass
    @staticmethod
    def _print_main_menu():
        menu_actions = (
            "Choose an action:\n"
            "1. Add a shape\n"
            "2. Delete a shape\n"
            "3. Print all shapes in the list\n"
            "4. Sum the areas of two shapes\n"
            "5. Subtract the area of one shape from another\n"
            "6. Check if the areas of two shapes are equal\n"
            "Enter the number of your choice: "
        )
        return input(menu_actions)

    @staticmethod
    def _print_shapes_menu():
        menu = (
            "Choose a shape:\n"
            "1. Circle\n"
            "2. Right-angled triangle\n"
            "3. Regular hexagon\n"
            "4. Rectangle\n"
            "5. Square\n"
            "Enter the number of your choice: "
        )
        return input(menu)


    @staticmethod
    def _valid_num_input():
        num = input()
        while not num.isnumeric():
            num = input(f"The character {num} is invalid (not a number).\n "
                        f"Please enter it again.")
        return num

    @staticmethod
    def _print_all_shapes():
        if not Menu._is_empty():
            for inx, val in enumerate(Menu.shapes):
                print(f"The shape at index {inx} is {val}")
        else:
            print("There are no shapes in the list yet.")

    @staticmethod
    def _is_empty():
        return len(Menu.shapes) == 0