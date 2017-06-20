from datetime import datetime


class TodoItem():

    def __init__(self, title, deadline):
        '''
        Method creates an instance of the class.
        Raise error if title is not a string and when deadline has incorrect format.

        Returns:
           None
        '''

        if not isinstance(title, str):
            raise TypeError

        elif not isinstance(deadline, datetime):
            raise TypeError("wrong date format!")

        self.title = title
        self.deadline = deadline
        self.is_done = False

    def mark(self):
        '''
        Method changes parametr is_done to True.

        Returns:
            None
        '''

        self.is_done = True

    def unmark(self):
        '''
        Method changes parametr is_done to False.

        Returns:
            None
        '''

        self.is_done = False

    def __str__(self):
        '''
        Method returns property string, depending on parameter is_done. 

        Returns:
            string
        '''

        if self.is_done is True:
            return '[x] ' + str(self.deadline.day) + '-' + str(self.deadline.month) + ' ' + self.title
        else:
            return '[ ] ' + str(self.deadline.day) + '-' + str(self.deadline.month) + ' ' + self.title