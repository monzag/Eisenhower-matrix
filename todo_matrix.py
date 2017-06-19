from datetime import datetime, timedelta
import os
import csv
from todo_quarter import TodoQuarter


class TodoMatrix():

    possible_status = ['IU', 'NU', 'IN', 'NN']

    def __init__(self):
        '''
        Method creates an instance of the class.

        Returns:
           None
        '''

        self.todo_quarters = {'IU': TodoQuarter(), 'IN': TodoQuarter(),
                              'NU': TodoQuarter(), 'NN': TodoQuarter()
                              }

    def get_quarter(self, status):
        '''
        Method gets Quarter object from Matrix by status.

        Args:
            status - string

        Returns:
            Quarter object (list with Item objects)
        '''

        if status not in self.possible_status:
            raise ValueError("%s is invalid status." % (status))

        else:

            for key, value in self.todo_quarters.items():
                if key == status:
                    return value

    def add_item(self, title, deadline, is_important=False):
        '''
        Method adds new item to proper quarter.
        Raises error when deadline has incorrect format.

        Args:
            title - string
            deadline - datetime object
            is_important - bool

        Returns:
           None
        '''

        if not isinstance(deadline, datetime):
            raise TypeError("wrong date format!")

        else:
            three_days = datetime.today() - timedelta(-3)
            if is_important and deadline <= three_days:
                self.todo_quarters['IU'].add_item(title, deadline)

            elif is_important:
                self.todo_quarters['IN'].add_item(title, deadline)

            elif is_important is False and deadline <= three_days:
                self.todo_quarters['NU'].add_item(title, deadline)

            elif is_important is False:
                self.todo_quarters['NN'].add_item(title, deadline)

    def add_items_from_file(self, file_name):
        '''
        Method reads data from file and create objects with proper attributes.
        Raises error when file not exists.

        Args:
            file_name - string

        Returns:
           None
        '''

        if not os.path.exists(file_name):
            raise FileNotFoundError("There is no such a file")

        else:
            with open(file_name, 'r') as file_1:
                from_file = file_1.readlines()
                splitted = [line.replace('\n', '').split('|') for line in from_file]

                index_title = 0
                index_deadline = 1
                index_boolean = 2
                for item in splitted:
                    split_data = item[1].split('-')
                    date = datetime(2017, int(split_data[1]), int(split_data[0]))

                    if len(item[index_boolean]) < 1:
                        self.add_item(item[index_title], date)
                    else:
                        self.add_item(item[index_title], date, True)

    def save_items_to_file(self, file_name):
        '''
        Method write data of objects to file.

        Args:
            file_name - string

        Returns:
           None
        '''

        list_to_save = []

        for key in self.todo_quarters:
            values = self.get_quarter(key)
            for i in range(values.__len__()):
                obj = values.get_item(i)
                item_to_save = []
                item_to_save.append(obj.title)
                date = str(obj.deadline.day) + '-' + str(obj.deadline.month)
                item_to_save.append(date)
                if key == 'IU' or key == 'IN':
                    item_to_save.append('important')
                else:
                    item_to_save.append('')

                string_to_save = '|'.join(item_to_save)
                list_to_save.append([string_to_save])

        with open(file_name, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(list_to_save)

    def archive_items(self):
        '''
        Method removes Item objects from proper quarters if is done.

        Returns:
            None
        '''
        for key in self.todo_quarters:
            values = self.get_quarter(key)
            values.archive_items()

    def __str__(self):
        '''
        Method returns formatted string with quarters.

        Returns:
            string
        '''

        result = ''
        for value in self.todo_quarters.values():
            result += str(value) + '\n'
        return result
