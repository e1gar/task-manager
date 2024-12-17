class Task:
    to_do_list = []

    def __init__(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status

    @classmethod
    def add_task(cls):
        """Добавить задачу в список"""
        description = input("Введите описание задачи: ")
        deadline = input("Введите дедлайн: ")
        status = input("Введите статус: ")
        new_task = Task(description, deadline, status)
        cls.to_do_list.append(new_task)
        print("Задача добавлена!")

    @classmethod
    def show_tasks(cls):
        """Показать все задачи"""
        if not cls.to_do_list:
            print("Список задач пуст!")
        else:
            print("Список задач:")
            for idx, task in enumerate(cls.to_do_list, start=1):
                print(f"{idx}. Описание: {task.description}, Дедлайн: {task.deadline}, Статус: {task.status}")

    @classmethod
    def delete_task(cls):
        """Удалить задачу по индексу"""
        if not cls.to_do_list:
            print("Список задач пуст!")
        else:
            cls.show_tasks()
            try:
                task_index = int(input("Введите номер задачи, которую нужно удалить: ")) - 1
                if 0 <= task_index < len(cls.to_do_list):
                    deleted_task = cls.to_do_list.pop(task_index)
                    print(f"Задача '{deleted_task.description}' удалена.")
                else:
                    print("Неверный номер задачи.")
            except ValueError:
                print("Ошибка ввода! Введите число.")
            cls.show_tasks()


if __name__ == "__main__":
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Удалить задачу")
        print("4. Выйти")
        choice = input("Выберите действие (1/2/3/4): ")

        if choice == "1":
            Task.add_task()
        elif choice == "2":
            Task.show_tasks()
        elif choice == "3":
            Task.delete_task()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод! Попробуйте снова.")
