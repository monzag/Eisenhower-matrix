from datetime import datetime
from todo_matrix import TodoMatrix
from todo_quarter import TodoQuarter


def show_welcome():
    '''
    Welcome board.

    Returns:
        string
    '''

    return '''

    #########################################################
    #                                                       #
    #   'Plany są niczym, planowanie jest wszystkim'        #
    #                                                       #
    #                               - Dwight D. Eisenhower  #
    #                                                       #
    #########################################################

    '''


def add_new_item(matrix):
    '''
    Take inputs from user and add new item to matrix.

    Args:
        matrix - object of class TodoMatrix

    Returns:
        matrix with new item
    '''

    list_labels = ['new item: ', 'deadline month', 'deadline day', 'priority: is_ important? (y/n): ']
    user_choice = get_input('Add new item', list_labels)
    date_1 = datetime(2017, int(user_choice[1]), int(user_choice[2]))

    if user_choice[3].lower() == 'y':
        important = True
    elif user_choice[3].lower() == 'n':
        important = False
    else:
        print('Incorrect answer! y/n')
        return None

    return matrix.add_item(user_choice[0], date_1, important)


def choose_status():
    '''
    Print options and choose quaters by input.

    Returns:
        status - string
    '''

    list_labels = ['''
                    1) important and urgent
                    2) important and not urgent
                    3) not important and urgent
                    4) not important and not urgent''']

    status = get_input('Choose status', list_labels)
    status = ''.join(status)

    if status == '1':
        return 'IU'
    elif status == '2':
        return 'IN'
    elif status == '3':
        return 'NU'
    elif status == '4':
        return 'NN'
    else:
        print('Bad choice')


def mark_done(quarter):
    '''
    Choose object TodoItem by number and change attribute 'is_done' to True.

    Args:
        quarter - object of class TodoQuarter

    Returns:
        True for is_done
    '''

    number = get_input('', ['Number of item: '])
    index = int(number[0]) - 1

    item = quarter.get_item(index)
    return item.mark()


def unmark_done(quarter):
    '''
    Choose object TodoItem by number and change attribute 'is_done' to False.

    Args:
        quarter - object of class TodoQuarter

    Returns:
        None
    '''

    number = get_input('', ['Number of item: '])
    index = int(number[0]) - 1

    item = quarter.get_item(index)
    item.unmark()


def remove_item(quarter):
    '''
    Choose object TodoItem by number and remove them.

    Args:
        quarter - object of class TodoQuarter

    Returns:
        None
    '''

    number = get_input('', ['Number of item: '])
    index = int(number[0]) - 1

    quarter.remove_item(index)


def get_input(title, list_labels):
    '''
    Get inputs from user.

    Args:
        title - string
        list_labels - list

    Returns:
        list of user's answer
    '''

    inputs = []
    print('{}'.format(title))
    for i in list_labels:
        answer = (input('{} '.format(i)))
        inputs.append(answer)
    print('')

    return inputs


def save_todo(matrix, file_name='Eisenhower.csv'):
    '''
    Save data to file.

    Args:
        matrix - object of class TodoMatrix
        file_name - string, default

    Returns:
        None
    '''

    matrix.save_items_to_file(file_name)


def menu():
    '''
    Display menu and user choice option to turn. 

    Return:
        None
    '''

    info = 'Welcome in Eisenhower matrix. What can I help you?'
    print(info)

    show_menu = '''
    1) choose a status and show TODO items
    2) add new item with deadline and priority
    3) mark TODO item by cross if it's done
    4) undo marking a TODO item
    5) remove a chosen TODO item

    0) archive, save and exit
    '''
    matrix = TodoMatrix()
    start = True
    while start is True:
        print(show_menu)

        user_option = input('Your choice: ')

        if user_option == '1':
            status = choose_status()
            print(matrix.get_quarter(status))

        elif user_option == '2':
            add_new_item(matrix)

        elif user_option == '3':
            status = choose_status()
            quarter = matrix.get_quarter(status)
            mark_done(quarter)

        elif user_option == '4':
            status = choose_status()
            quarter = matrix.get_quarter(status)
            unmark_done(quarter)

        elif user_option == '5':
            status = choose_status()
            quarter = matrix.get_quarter(status)
            remove_item(quarter)

        elif user_option == '0':
            matrix.archive_items()
            save_todo(matrix)
            print('Good bye')
            start = False
            return start

        else:
            print('Error choice!')


def main():
    '''
    Display welcome board and turn on menu.

    Returns:
        None
    '''

    print(show_welcome())
    menu()


if __name__ == '__main__':
    main()