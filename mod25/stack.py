class Stack:

    def __init__(self):
        self.__container = []

    def __str__(self):
        print('Элементы стека:')
        for i_item in self.__container:
            print('\t', i_item)
        return ''

    def load(self, object):
        self.__container.append(object)

    def unload(self):
        return self.__container.pop()

class TaskManager:

    def __init__(self):
        self.__container = {}

    def __str__(self):
        print('Результат:')
        for i_item in sorted(self.__container.keys()):
            print(i_item, end=' ')
            for j_item in self.__container[i_item]:
                print(j_item, end='')
            print()
        return ''

    def load(self, task, priority):
        if priority in self.__container.keys():
            self.__container[priority].append(task)
        else:
            self.__container[priority] = [task]



# my_stack = Stack()
# my_stack.load(45)
# my_stack.load('python')
# print(my_stack)
# print(my_stack.unload())
# print(my_stack.unload())
# print(my_stack)

manager = TaskManager()
manager.load('Есть', 1)
manager.load('пить', 2)
manager.load('дышать', 1)

print(manager)
