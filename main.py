to_do_list = []

class Task:
    def __init__(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status

    def add_task(self):
        description = input("Введите описание задачи: ")
        deadline = input("Введите дедлайн: ")
        status = input("Введите статус: ")
        new_task = Task(description, deadline, status)
        to_do_list.append(new_task)
        print("Задача добавлена!")

    @staticmethod
    def show_tasks():
        if not to_do_list:
            print("Список задач пуст!")
        else:
            print("Список задач:")
            for idx, task in enumerate(to_do_list, start=1):
                print(f"{idx}. Описание: {task.description}, Дедлайн: {task.deadline}, Статус: {task.status}")

    @staticmethod
    def delete_task():
        if not to_do_list:
            print("Список задач пуст!")
        else:
            Task.show_tasks()
            task_index = int(input("Введите номер задачи, которую нужно удалить: ")) - 1
            if 0 <= task_index < len(to_do_list):
                deleted_task = to_do_list.pop(task_index)
                print(f"Задача '{deleted_task.description}' удалена.")
            Task.show_tasks()

if __name__ == "__main__":
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Удалить задачу")
        print("4. Выйти")
        choice = input("Выберите действие (1/2/3/4): ")

        if choice == "1":
            task = Task("", "", "")  # Temporary Task object to use its methods
            task.add_task()
        elif choice == "2":
            Task.show_tasks()
        elif choice == "3":
            Task.delete_task()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод! Попробуйте снова.")
