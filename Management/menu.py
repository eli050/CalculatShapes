from Shapes.circle import Circle
from Shapes.rectangle import Rectangle
from Shapes.regular_hexagon import RegularHexagon
from Shapes.shape import Shape
from Shapes.square import Square
from Shapes.triangle import RightAngledTriangle


class Menu:
    shapes = list()
    @staticmethod
    def main_menu():
        to_exit = True
        while to_exit:
            choose = Menu._print_main_menu()
            match choose:
                case "1":
                    Menu._print_all_shapes()
                case "2":
                    check_choose = False
                    while not check_choose:
                        shape = Menu._print_shapes_menu()
                        match shape:
                            case "1":
                                print("Enter the radius of the circle.")
                                radius = float(Menu._valid_num_input())
                                Menu._add_shape(Circle(radius))
                                print("The shape was added successfully.")
                                check_choose = True
                            case "2":
                                print("Enter the length of the base of the triangle.")
                                base = float(Menu._valid_num_input())
                                print("Enter the length of the height of the triangle.")
                                height = float(Menu._valid_num_input())
                                Menu._add_shape(RightAngledTriangle(base,height))
                                print("The shape was added successfully.")
                                check_choose = True
                            case "3":
                                print("Enter the length of the side of the hexagon.")
                                side = float(Menu._valid_num_input())
                                Menu._add_shape(RegularHexagon(side))
                                print("The shape was added successfully.")
                                check_choose = True
                            case "4":
                                print("Enter the length of the rectangle.")
                                length = float(Menu._valid_num_input())
                                print("Enter the width of the rectangle.")
                                width = float(Menu._valid_num_input())
                                Menu._add_shape(Rectangle(length,width))
                                print("The shape was added successfully.")
                                check_choose = True
                            case "5":
                                print("Enter the length of the side of the square.")
                                side = float(Menu._valid_num_input())
                                Menu._add_shape(Square(side))
                                print("The shape was added successfully.")
                                check_choose = True
                            case _:
                                print(f"We don't have the {shape} option in the menu yet, please select again.")
                case "3":
                    print("From which index would you like to delete the shape? ")
                    inx = int(Menu._valid_num_input())
                    if Menu._delete_by_inx(inx):
                        print("The shape was successfully deleted.")
                    else:
                        print("Index larger than list range, deletion failed")
                case "4":
                    print("Insert index of the first shape")
                    inx1 = int(Menu._valid_num_input())
                    shape1 = Menu._get_shape_by_inx(inx1)
                    if shape1 is not None:
                        print("Insert index of the second shape")
                        inx2 = int(Menu._valid_num_input())
                        shape2 = Menu._get_shape_by_inx(inx2)
                        if shape2 is not None:
                            print(shape1 + shape2)
                        else:
                            print("There are not enough members to make a connection.")
                    else:
                        print("There are not enough members to make a connection.")


                case "5":
                    print("Insert index of the first shape")
                    inx1 = int(Menu._valid_num_input())
                    shape1 = Menu._get_shape_by_inx(inx1)
                    if shape1 is not None:
                        print("Insert index of the second shape")
                        inx2 = int(Menu._valid_num_input())
                        shape2 = Menu._get_shape_by_inx(inx2)
                        if shape2 is not None:
                            print(shape1 - shape2)
                        else:
                            print("There are not enough members to make a subtraction.")
                    else:
                        print("There are not enough members to make a subtraction.")

                case "6":
                    print("Insert index of the first shape")
                    inx1 = int(Menu._valid_num_input())
                    shape1 = Menu._get_shape_by_inx(inx1)
                    if shape1 is not None:
                        print("Insert index of the second shape")
                        inx2 = int(Menu._valid_num_input())
                        shape2 = Menu._get_shape_by_inx(inx2)
                        if shape2 is not None:
                            print(shape1 == shape2)
                        else:
                            print("There are not enough members to make a comparison.")
                    else:
                        print("There are not enough members to make a comparison.")

                case "7":
                    print("Insert index of the shape")
                    inx = int(Menu._valid_num_input())
                    shape = Menu._get_shape_by_inx(inx)
                    if shape is not None:
                        print(shape.get_area())
                case "8":
                    print("Insert index of the shape")
                    inx = int(Menu._valid_num_input())
                    shape = Menu._get_shape_by_inx(inx)
                    if shape is not None:
                        print(shape.get_perimeter())
                case "9":
                    to_exit = False
                case _:
                    print(f"We don't have the {choose} option in the menu yet, please select again.")

    @staticmethod
    def _print_main_menu():
        menu_actions = (
            "Choose an action:\n"
            
            "1. Print all shapes in the list\n"
            "2. Add a shape\n"
            "3. Delete a shape (by index)\n"
            "4. Sum the areas of two shapes\n"
            "5. Subtract the area of one shape from another\n"
            "6. Check if the areas of two shapes are equal\n"
            "7. Get area of the shape\n"
            "8. Get the perimeter of the shape\n"
            "9. Exit.\n"
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
        while not ''.join(num.split('.')).isdigit():
            num = input(f"The character {num} is invalid (not a number).\n"
                        f"Please enter it again.\n")
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
    @staticmethod
    def _add_shape(shape:Shape):
        Menu.shapes.append(shape)
        print()
    @staticmethod
    def _delete_by_inx(inx:int):
        if inx < len(Menu.shapes):
            Menu.shapes.pop(inx)
            return True
        else:
            return False
    @staticmethod
    def _get_shape_by_inx(inx:int):
        if Menu._is_empty():
            print("There are no shapes in the list yet.")
            return None
        else:
            while inx >= len(Menu.shapes):
                print("Large index of the range of shapes in the list, please enter again")
                inx = Menu._valid_num_input()
            return Menu.shapes[inx]

