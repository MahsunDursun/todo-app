#from functions import get_todos, write_todos
import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)
while True:
    action = input('Type add, show, edit, remove or exit: ')
    action = action.strip()

    if action.startswith('add'):
        todo = action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif action.startswith('show'):

#        file = open('todos.txt', 'r')
#        todos = file.readlines()
#        file.close()

        todos = functions.get_todos()

#            new_todos = []
#            for item in todos:
#                new_item = item.strip('\n')
#                new_todos.append(new_item)

#            new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
#            #print(int(index) + 1,'-' , item)
            row = f'{index+1}-{item}'
            print(row)
    elif action.startswith('edit'):
        try:
            number = int(action[5])
            number = number - 1

            todos = functions.get_todos()

            new_todo = action[7:]
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print('Your command is invalid')
            continue

    elif action.startswith('remove'):
        try:
            number = int(action[7:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_go = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo - {todo_to_go} - is deleted'
            print(message)
        except IndexError:
            print('Command invalid')
            print(f'Given index number should be less than {len(todos)}.')
            continue

    elif action.startswith('exit'):
        break

    else:
        print('Invalid command.')

print('Bye')
