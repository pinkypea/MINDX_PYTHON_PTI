class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

class HomeworkList:
    def __init__(self):
        self.items = []
    
    def add_item(self, item): 
        self.items.append(item)

def all_finished(homework_list):
    check = [homework.name for homework in homework_list if not homework.completed]
    if check:
        for c in check:
            print(c)
    else: 
        print('All finished')

homework1 = Homework("Lập trình App Producer", 3, False)
homework2 = Homework("Làm văn", 2, True)
homework3 = Homework("Lập trình Gamemaker", 1, False)

homework_list = HomeworkList()

homework_list.add_item(homework1)
homework_list.add_item(homework2)
homework_list.add_item(homework3)

all_finished(homework_list.items)