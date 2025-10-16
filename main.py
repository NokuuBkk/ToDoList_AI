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
	if not tasks:
		print("ยังไม่มีงานในรายการ")
		return

	print()
	print("รายการงานทั้งหมด:")
	for idx, t in enumerate(tasks, start=1):
		status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
		due = t.get("due_date") or "-"
		print(f"{idx}. {t.get('title')} | due: {due} | {status}")


def edit_task():
	"""Entry point for editing a task. Uses update_task() implementation."""
	update_task()


def update_task():
	"""Allow user to update a task selected by index.

	User can update title, description, and completed status. Index is validated.
	"""
	if not tasks:
		print("ยังไม่มีงานในรายการ")
		return

	# show brief list with indices
	for idx, t in enumerate(tasks, start=1):
		print(f"{idx}. {t.get('title')}")

	idx_str = input("เลือกหมายเลขงานที่ต้องการแก้ไข: ").strip()
	if not idx_str.isdigit():
		print("หมายเลขไม่ถูกต้อง")
		return

	idx = int(idx_str) - 1
	if idx < 0 or idx >= len(tasks):
		print("หมายเลขงานไม่ถูกต้อง")
		return

	task = tasks[idx]

	print("ปล่อยว่างเพื่อไม่แก้ไขฟิลด์นั้น")
	new_title = input(f"Title [{task.get('title')}]: ").strip()
	if new_title:
		task['title'] = new_title

	new_desc = input(f"Description [{task.get('description')}]: ").strip()
	if new_desc:
		task['description'] = new_desc

	new_completed = input(f"Completed? (y/N) [current: {task.get('completed')}]: ").strip().lower()
	if new_completed in ('y', 'yes'):
		task['completed'] = True
	elif new_completed in ('n', 'no'):
		task['completed'] = False

	print("งานถูกปรับปรุงเรียบร้อย")


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