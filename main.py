import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    for task in tasks:
        status = "✔" if task["completed"] else "✗"
        print(f'{task["id"]}: [{status}] {task["title"]} | Категория: {task["category"]} | Срок: {task["due_date"]}')

def add_task(tasks):
    title = input("Введите название задачи: ")
    category = input("Введите категорию задачи: ")
    due_date = input("Введите срок выполнения (ГГГГ-ММ-ДД): ")
    task_id = max([task["id"] for task in tasks], default=0) + 1
    tasks.append({
        "id": task_id,
        "title": title,
        "category": category,
        "due_date": due_date,
        "completed": False
    })
    print("Задача добавлена.")

def delete_task(tasks):
    task_id = int(input("Введите ID задачи для удаления: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Задача удалена.")
            return
    print("Задача не найдена.")

def mark_completed(tasks):
    task_id = int(input("Введите ID задачи для отметки как выполненной: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("Задача отмечена как выполненная.")
            return
    print("Задача не найдена.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do Менеджер ---")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Отметить задачу как выполненную")
        print("5. Сохранить и выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Задачи сохранены. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
