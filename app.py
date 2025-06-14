import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime, date

st.set_page_config(page_title="To-Do App", layout="centered")

st.title("📝 :blue[Simple To-Do List App]")

username = st.text_input("👤 Enter your username to access your tasks")

if not username:
    st.warning("Please enter your username to continue.")
    st.stop()

TASKS_FILE = f"tasks_{username}.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.tasks, f, indent=2)

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

new_task = st.text_input("➕ Add a new task")
due_date = st.date_input("📅 Due date (optional)")
task_type = st.selectbox(
    "📌 Select Task Type",
    ["🏫 Study", "💼 Work", "🏠 Personal", "🧹 Chores", "📚 Reading", "➕ Other"]
)

if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({
            "task": new_task.strip(),
            "completed": False,
            "type": task_type,
            "due": due_date.strftime("%Y-%m-%d")
        })
        save_tasks()
        st.rerun()

st.divider()
st.subheader("📌 Your Tasks:")

for i, task_obj in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([6, 2.5, 1.5])

    with col1:
        if st.session_state.edit_index == i:
            st.text_input("✏️ Task Name", value=task_obj["task"], key=f"edit_task_{i}")
        else:
            task_obj["completed"] = st.checkbox(
                f"{task_obj['task']} {task_obj.get('tag', '')}",
                value=task_obj["completed"],
                key=f"checkbox_{i}"
            )
            save_tasks()

    with col2:
        if st.session_state.edit_index == i:
            updated_task = st.text_input("📝 Edit Task", value=task_obj["task"], key=f"task_input_{i}")
            updated_type = st.selectbox("📌 Type", ["🏫 Study", "💼 Work", "🏠 Personal", "🧹 Chores", "📚 Reading", "➕ Other"], index=["🏫 Study", "💼 Work", "🏠 Personal", "🧹 Chores", "📚 Reading", "➕ Other"].index(task_obj.get("type", "➕ Other")), key=f"type_{i}")
            updated_due = st.date_input("📅 Due Date", value=datetime.strptime(task_obj.get("due", date.today().strftime("%Y-%m-%d")), "%Y-%m-%d").date(), key=f"due_{i}")

            if st.button("💾 Save", key=f"save_{i}"):
                st.session_state.tasks[i] = {
                    "task": updated_task.strip(),
                    "completed": task_obj["completed"],
                    "type": updated_type,
                    "due": updated_due.strftime("%Y-%m-%d"),
                }
                st.session_state.edit_index = None
                save_tasks()
                st.rerun()
        else:
            if st.button("✏️ Edit", key=f"edit_btn_{i}"):
                st.session_state.edit_index = i

    with col3:
        if st.button("🗑 Delete", key=f"delete_{i}"):
            del st.session_state.tasks[i]
            st.session_state.edit_index = None
            save_tasks()
            st.rerun()

with st.expander("📊 View All Task Information"):
    if st.session_state.tasks:
        summary_data = [
            {
                "Task": t["task"],
                "Type": t.get("type", ""),
                "Due Date": t.get("due", ""),
                "Status": "✅ Done" if t["completed"] else "🕘 Pending"
            }
            for t in st.session_state.tasks
        ]
        st.table(summary_data)
    else:
        st.info("No tasks found.")

