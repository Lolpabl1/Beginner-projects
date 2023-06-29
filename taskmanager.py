#task manager
from datetime import datetime
import time

#making the task template
class Task:
	def __init__ (self,name,description,category,priority,due_date):
		self.name=name
		self.description=description
		self.category=category
		self.priority=priority
		self.due_date=due_date
		
tasks=[]

#checking validity of due date
def validity_due_date():
	while True:
            new_due_date = input("When is the task due? (YYYY-MM-DD): ")
            try:
                due_date = datetime.strptime(new_due_date, "%Y-%m-%d")
                break  
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                print()
                continue
	return new_due_date

#checking validity of priority level
def validity_priority():
	possible_options = ["1", "2", "3", "4", "5"]
	while True:
	    new_priority = input("How important is the task, 1-5: ")
	    try:
	        if new_priority not in possible_options:
	        	raise ValueError
	        break
	    except ValueError:
	    	print("Invalid input, please choose from 1-5")
	    	print()
	return new_priority

#creating a task
def creating_task():	
	while True:
		new_task=input('\n'"Do you want to add a new task? yes or no: ")
		new_task=new_task.lower()
		if new_task=="no":
			task_listing()
			break
		elif new_task=="yes":
			new_name=input('\n'"What is the name of the task? ")
			new_description=input("Briefly describe the task. ")
			new_category=input("What category is this task in? ")
			new_priority=validity_priority()
			new_due_date=validity_due_date()
			task=Task(new_name,new_description,new_category,new_priority,new_due_date)
			tasks.append(task)
		else:
			print("Invalid input, please select yes or no")
					
def easier_task_listing(task):
	print('\n'"Task name: "+task.name)
	print("Task description: "+task.description)
	print("Task category: "+task.category)
	print("Task priority: "+task.priority)
	print("Task due date: "+task.due_date)
		
#listing tasks
def task_listing():
	for task in tasks:
		easier_task_listing(task)
		
#deleting tasks
def delete():
	while True:
		delete=input('\n'"Please write the name of the task you want to delete. (or write quit to exit) ")
		for task in tasks:
			if task.name==delete:
				tasks.remove(task)
				task_listing()
				break
			elif delete=="quit":
				break
			else:
				print("Invalid input, please write the name exactly as it is")
		break
			
#editing tasks
def edit(task):
	while True:
		edit_choice=input('\n'"What do you want to edit, name, description,category, priority or due date?(or write quit to exit) ")
		edit_choice=edit_choice.lower()
		if edit_choice=="name":
			editted_name=input("What do you want the new name of the task to be? ")
			task.name=editted_name
			break
		elif edit_choice=="description":
			editted_description=input("What do you want the new description of the task to be? ")
			task.description=editted_description
			break
		elif edit_choice=="category":
			editted_category=input("What do you want the new category to be? ")
			task.category=editted_category
			break
		elif edit_choice=="priority":
			editted_priority=input("What do you want the new priority of the task to be? ")
			task.priority=editted_priority
			break
		elif edit_choice=="due date":
			editted_due_date=input("What do you want the new due date of the task to be? ")
			task.due_date=editted_due_date
		elif edit_choice=="quit":
			break
		else:
			print("Invalid input, please select a valid option")
			continue
	task_listing()
			
#modifying tasks
def modify():
	while True:
		modify=input('\n'"Please write the name of the task you want to modify. (or write quit to exit) ")
		for task in tasks:
			if task.name==modify:
				edit(task)
				break
			elif modify=="quit":
				break
			else:
				print("Invalid input, please select a valid option")
		break
						
										
#deleting/modifying tasks
def delete_modify():
	while True:
			modify_delete=input('\n'"Do you want to delete or modify a task or write quit to exit: ")
			modify_delete=modify_delete.lower()
			if modify_delete=="delete":
				delete()
				break
			elif modify_delete=="modify":
				modify()
				break
			elif modify_delete=="quit":
				break
			else:
				print("Invalid input, please select a valid option.")
					
#accessing tasks
def access_choice():
	while True:
		access_choice=input('\n'"Do you want to access a task? yes or no: ")
		access_choice=access_choice.lower()
		if access_choice=="yes":
			delete_modify()
			break
		elif access_choice=="no":
			break
		else:
			print("Invalid input, please select yes or no")

#filtering by category
def filtering_by_category():
	while True:
				category_filter=input('\n'"Which category do you want the tasks to be? ")
				for task in tasks:
					if category_filter==task.category:
						easier_task_listing(task)
				break	
	
#filtering by priority
def filtering_by_priority():
	while True:
		priority_filter=input('\n'"Which priority level do you want the tasks to be? ")
		for task in tasks:
			if priority_filter==task.priority:
				easier_task_listing(task)
		break
		
#filtering by due date
def filtering_by_due_date():
	while True:
		date_filter=input('\n'"Which date do you want the tasks to be? ")
		for task in tasks:
			if date_filter==task.due_date:
				easier_task_listing(task)
		break

#task filtering
def filtering():
	while True:
		filter_option=input('\n'"Do you want to filter by category, priority or due date? (or press quit to exit) ")
		filter_option=filter_option.lower()
		if filter_option=="category":
			filtering_by_category()
		elif filter_option=="priority":
			filtering_by_priority()			
		elif filter_option=="due date":
			filtering_by_due_date()
		elif filter_option=="quit":
			break
		else:
			print("Invalid input, please select a valid option")
		break
		
#sorting by priority level
def sorting_priority():
	variable=5
	while True:
		for task in tasks:
			if task.priority==str(variable):
				easier_task_listing(task)
		variable-=1
			
#sorting by date
def sorting_due_date():
    sorted_tasks = sorted(tasks, key=lambda task: datetime.strptime(task.due_date, "%Y-%m-%d"))
    for task in sorted_tasks:
        easier_task_listing(task)
					
#task sorting
def sorting():
	while True:
		sorting_choice=input('\n'"Do you want to sort by priority or due date? (or press quit to exit) ")
		sorting_choice=sorting_choice.lower()
		if sorting_choice=="priority":
			sorting_priority()
			break
		elif sorting_choice=="due date":
			sorting_due_date()
			break
		elif sorting_choice=="quit":
			break
		else:
			print("Invalid option, please select a valid option")
			
#task statistics
def statistics():
	number_of_tasks=0
	for task in tasks:
		number_of_tasks+=1
	print('\n'"The number of tasks is "+ str(number_of_tasks))
			
def main():
	creating_task()
	access_choice()
	filtering()	
	sorting()
	statistics()
	
if __name__ == "__main__":
    main()
