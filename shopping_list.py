"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.
"""
shopping_list = []

def menu():
    print " 0 - Main Menu \n 1 - Show current list \n 2- Add an item to shopping list \n 3 - Exit"
    chosen_menu = raw_input("Please choose one option from the menu")

def add_shopping_list(item):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "Here's your updated list", sorted_shopping_list()
    else:
        print "This item %s already exists!" % (item)


def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list


def remove_item(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed. Here's your updated list" % (item), sorted_shopping_list()
    else:
        print "%s was not on the list." % (item)


def replace_item(old_item, new_item):
    old_item = old_item.lower()
    new_item = new_item.lower()

    if old_item in shopping_list:
        item_index = shopping_list.index(old_item)
        print "%s has replaced %s in the list." % (new_item, old_item)
    else:
        print "%s is not in the list." % (old_item)

def main():
    while (True):
        menu()
        if chosen_menu == "0":
            menu()
        elif chosen_menu == "1":
            sorted_shopping_list()
        elif chosen_menu == "2":
            add_shopping_list()
        elif chosen_menu == "3":
            break

if __name__ == __'main'__:
    main()

# TEST FUNCTIONS
# 1 - add 4 times to your shopping list
add_shopping_list("apple")
add_shopping_list("steak")
add_shopping_list("beef")
add_shopping_list("mustard")

# 2 - Add an item that is already in the list. what happens?
add_shopping_list("apple")

# 3 - Remove an item on your list
remove_item("apple")

# 4 - Remove an item that is not in the list. what happens?
remove_item("chicken")

# 5 - you've changed your mind on one of your items. you want to substitute it with something else.
replace_item("mustard", "ketchup")
