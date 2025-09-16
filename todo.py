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


def delete_task(todos: list[list[str, bool]]) -> None:
    pass


def update_task(todos: list[list[str, bool]]) -> None:
    pass


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
        elif choice == '0':
            sys.exit()
        else:
            print('bunday menu mavjud emas.')

main()
