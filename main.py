import sys


def add_task():
	"""Placeholder: add a new task."""
	pass


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