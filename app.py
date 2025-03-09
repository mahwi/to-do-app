import streamlit as st 

# app title
st.title("To Do List App")

# installation session state for tasks
if "tasks" not in st.session_state:
	st.session_state.tasks = []

# sidebar heading
st.sidebar.header("Manage Your Task")

# text input 
new_task = st.sidebar.text_input("Add A New Task:", placeholder= "Enter Your Task Here...")

if st.sidebar.button("Add Task"):
	if new_task.strip():
		st.session_state.tasks.append({"Task": new_task, "Completed":False})
		st.success("Task Added Successfuliy!")
	else:
		st.warning("Task Cannot Be Empty!")

 # Display tasks
st.sidebar.header("Your TO-DO List")
 
if not st.session_state.tasks:
	st.info("No Task added yet start by adding a task from the sidebar!")
else:
	for index, task in enumerate(st.session_state.tasks):
		col1 , col2 , col3 = st.columns([0.7,0.15,0.15])  
		
		#mark as completed
		completed = col1.checkbox(f"**{task['Task']}**",task["Completed"],key=f"check_{index}")
		if completed != task["Completed"]:
			st.session_state.tasks[index]["Completed"] = completed

		# Update task
		if col2.button("Edit",key=f"edit_{index}"):
			new_task = st.text_input("Edit task", task["Task"], key=f"Edit_{index}")
			if new_task and st.button("Save", key=f'Save_{index}'):
				st.session_state.tasks[index]["task"] = new_task
				st.experimental_rerun()

		 # Delete task
	if col3.button("Delete",key=f'delete {index}'):
			del st.session_state.tasks[index]
			st.rerun()

		# clear all tasks 
	if st.button("Clear all tasks"):
			st.session_state.tasks = []
			st.success("All tasks deleted successfully")  

		# Footer
st.markdown('---')
st.caption("Stay organized & productive with this simple TO-DO List App. ")                     
