import sys
from rich.console import Console
from rich.table import Table

console = Console()


def add_task(todos: list[list[str, bool]]) -> None:
    task_name = input('Task Name: ').strip().capitalize()
    todos.append(
        [task_name, False]
    )


def show_tasks(todos: list[list[str, bool]]) -> None:
    if todos:
        table = Table(title="Todos")

        table.add_column("Number")
        table.add_column("Name")
        table.add_column("Status")

        for index, todo in enumerate(todos, start=1):
            status = "Bajarilmagan"
            if todo[1]:
                status = "Bajarilgan"
            
            table.add_row(str(index), todo[0], status)

        console.print(table)
    else:
        print("Task mavjud emas")


def delete_task(todos: list[list[str, bool]]) -> None:
    if todos:
        show_tasks(todos)

        index = int(input("Qaysi taskni o'chiqmoqchisiz? ")) - 1

        if index < len(todos) and index >= 0:
            todos.pop(index)
            print("task o'chirildi")
        else:
            print("task nomeri xato kiritildi")
    else:
        print("Task mavjud emas")


def update_task(todos: list[list[str, bool]]) -> None:
    if todos:
        show_tasks(todos)

        index = int(input("Qaysi taskni o'zgartirmoqchisiz? ")) - 1

        if index < len(todos) and index >= 0:
            task_name = input('Task Name: ').strip().capitalize()
            todos[index][0] = task_name
            print("task o'zgartirildi")
        else:
            print("task nomeri xato kiritildi")
    else:
        print("Task mavjud emas")


def change_status(todos: list[list[str, bool]]) -> None:
    if todos:
        show_tasks(todos)

        index = int(input("Qaysi taskni holatini o'zgartirmoqchisiz? ")) - 1

        if index < len(todos) and index >= 0:
            todos[index][1] = not todos[index][1]
            print("task o'zgartirildi")
        else:
            print("task nomeri xato kiritildi")
    else:
        print("Task mavjud emas")


def main():
    todos: list[list[str, bool]] = [
        ["Yugirish", False],
        ["Kitob oqish", True]
    ]

    while True:
        print('----menu----')
        print('1. add task')
        print('2. show task')
        print('3. delete task')
        print('4. update task')
        print('5. change task status')
        print('0. exit')

        choice = input("> ")
        if choice == '1':
            add_task(todos)
        elif choice == '2':
            show_tasks(todos)
        elif choice == '3':
            delete_task(todos)
        elif choice == '4':
            update_task(todos)
        elif choice == '5':
            change_status(todos)
        elif choice == '0':
            sys.exit()
        else:
            print('bunday menu mavjud emas.')

main()
