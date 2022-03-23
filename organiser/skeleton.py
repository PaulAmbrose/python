#**LOADING**
#->load_dict: from text file and store ready and sorted.
#->display_menu: add, remove, display, save, exit.

#**ADDING**
#  ->collect_item_dets: name, completion date
#  ->save_to_dict
#  ->re_sort_dict (date order, nearest to furthest)
#  ->loading.display_menu

#**REMOVING**
#  ->collect_item_name
#  ->check_item_valid
#  ->remove_item
#  ->loading.display_menu

#**DISPLAYING**
# ->print_all_items
# ->loading.display_menu

class loading(object):

    def __init__(self, program1):
        self.proram1 = program1

    def load_dict(file_name):
        existing_data = open(file_name)
        working_list = []
        counter = 0
        for line in existing_data
            working_list[counter] = line
            counter = counter + 1

    def display_menu(self):
        print("Paul's Organiser")
        print("1>>add items")
        print("2>>remove items")
        print("3>>display items")
        print("4>>save items")
        print("5>>exit")

class adding(object):
    def collect_item_dets(self):
        item_to_add = input("Item Name >>")
        item_to_add_date = input("Item Completion Date >>")

    def save_to_dict(self):
        pass
    def re_sort_dict(self):
        pass

class removing(object):
    def collect_item_name(self):
        pass
    def check_item_valid(self):
        pass
    def remove_item(self):
        pass

class displaying
    def print_all_items(self):
        pass
