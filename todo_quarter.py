from datetime import datetime
from operator import attrgetter
from todo_item import TodoItem


class TodoQuarter():

    def __init__(self):
        '''
        Method creates an instance of the class.

        Returns:
           None
        '''

        self.todo_items = []

    def sort_items(self):
        '''
        Method sorted descending list of object by deadline.

        Returns:
           None
        '''

        self.todo_items = sorted(self.todo_items, key=attrgetter('deadline'), reverse=False)

    def add_item(self, title, deadline):
        '''
        Method adds new Item object with attributes title and deadline to list.

        Args:
            title - string
            deadline - datetime object

        Returns:
           None
        '''

        self.todo_items.append(TodoItem(title, deadline))
        self.sort_items()

    def remove_item(self, index):
        '''
        Method removes Item object from list by index in list.

        Args:
            index - integer

        Returns:
            None
        '''

        if index not in range(len(self.todo_items)):
            raise IndexError("You can't remove this item, index out of range!")

        else:
            self.todo_items.pop(index)

    def archive_items(self):
        '''
        Method removes Item objects from list if is done.

        Returns:
            None
        '''

        for item in self.todo_items:
            if item.is_done is True:
                self.todo_items.remove(item)

    def get_item(self, index):
        '''
        Method gets Item object from list by index.

        Args:
            index = integer

        Returns:
            Item object from list in proper index
        '''

        if index not in range(len(self.todo_items)):
            raise IndexError("You can't get this item, index out of range!")

        else:
            return self.todo_items[index]

    def __str__(self):
        '''
        Method returns formatted string with Item object.

        Returns:
            string
        '''

        number = 1
        to_print = ''
        for item in self.todo_items:
            to_print += '{}. '.format(number) + str(item) + '\n'
            number += 1
        return to_print

    def __len__(self):
        '''
        Method returns length TodoQuarter object (list).

        Returns:
            length of list
        '''

        return len(self.todo_items)