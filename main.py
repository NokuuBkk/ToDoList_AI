import sys
import uuid
from datetime import datetime

tasks = []


def add_task():
	"""Prompt user to add a new task and append to tasks list."""
	title = input("Title: ").strip()
	description = input("Description: ").strip()
	due_date_str = input("Due date (YYYY-MM-DD) [optional]: ").strip()

	due_date = None
	if due_date_str:
		try:
			due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date().isoformat()
		except ValueError:
			print("Invalid date format. Saving without due date.")

	task = {
		"id": str(uuid.uuid4()),
		"title": title,
		"description": description,
		"due_date": due_date,
		"completed": False,
	}

	tasks.append(task)
	print(f"Task added. id={task['id']}")


def view_tasks():
	"""Placeholder: view all tasks."""
	pass


def edit_task():
	"""Placeholder: edit an existing task."""
	pass


def delete_task():
	"""Placeholder: delete a task."""
	pass


def main_menu():
	while True:
		print()
		print("=== ToDoList CLI ===")
		print("1. เพิ่มงานใหม่")
		print("2. ดูงานทั้งหมด")
		print("3. แก้ไขงาน")
		print("4. ลบงาน")
		print("5. ออกจากโปรแกรม")
		choice = input("เลือกเมนู (1-5): ").strip()

		if choice == "1":
			add_task()
		elif choice == "2":
			view_tasks()
		elif choice == "3":
			edit_task()
		elif choice == "4":
			delete_task()
		elif choice == "5":
			print("ออกจากโปรแกรม. ลาก่อน!")
			sys.exit(0)
		else:
			print("ตัวเลือกไม่ถูกต้อง กรุณาเลือก 1-5")


if __name__ == "__main__":
	main_menu()