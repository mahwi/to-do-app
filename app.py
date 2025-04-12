import streamlit as st

st.title("📝To-Do App (Add, Edit, Update, Delete)")

# Session state initialization
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

# Add new task
st.subheader("➕ Add New Task")
new_task = st.text_input("Enter task")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success("Task added!")
    else:
        st.warning("Please enter something.")

# List of tasks
st.subheader("📋 Your Tasks")

if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([6, 1, 1])
        
        if st.session_state.edit_index == i:
            edited_task = col1.text_input("Edit Task", value=task, key=f"edit_{i}")
            if col2.button("💾", key=f"save_{i}"):
                if edited_task.strip():
                    st.session_state.tasks[i] = edited_task
                    st.session_state.edit_index = None
                    st.success("Task updated!")
                    st.rerun()
            if col3.button("❌", key=f"cancel_{i}"):
                st.session_state.edit_index = None
        else:
            col1.write(f"{i+1}. {task}")
            if col2.button("✏️", key=f"edit_{i}"):
                st.session_state.edit_index = i
                st.rerun()
            if col3.button("🗑️", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.success("Task deleted!")
                st.rerun()
else:
    st.write("No tasks yet.")
