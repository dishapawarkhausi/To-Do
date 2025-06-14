# To-Do App

A simple and interactive To-Do List web application built with Streamlit. This app allows you to add, edit, delete, and track tasks with details such as task type and due date. It also saves tasks locally in a JSON file to persist data between sessions.

---

## Features

- Add new tasks with task name, type, and due date.
- Edit existing tasks including all details.
- Mark tasks as completed or pending.
- Delete tasks.
- View all tasks in a summary table.
- Tasks saved locally in `tasks.json` file.
- Filter and reminder support can be added easily.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dishapawar/todo-app.git
cd todo-app
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your default browser. You can add, edit, and manage your tasks easily.

---

## File Structure

- `app.py` - Main Streamlit app source code.
- `tasks.json` - JSON file storing tasks data (created automatically).
- `README.md` - Project documentation.

---

## How It Works

- Tasks are stored as dictionaries containing:
  - `task`: Task description
  - `completed`: Boolean status
  - `type`: Task category/type (Work, Study, etc.)
  - `due`: Due date as string (`YYYY-MM-DD`)

- Tasks are saved and loaded from `tasks.json` file for persistence.
- Streamlit session state is used to manage UI states like editing.

---

## Contributions

Contributions are welcome! Feel free to open issues or pull requests to enhance this app.

---

## License

This project is licensed under the MIT License.

---

## Author

Created by [Disha Pawar]

## 🔗 Live App

You can try the app live here: [Open To-Do App](https://your-app-link.streamlit.app)  

---