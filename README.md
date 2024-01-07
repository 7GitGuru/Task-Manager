This project is a basic Task Manager web application built using Flask, a Python web framework. Its primary functionalities include managing tasks, marking them as completed, deleting tasks, and exporting reports into an Excel file.

Here's an overview of its components and features:

### Backend
- **Flask App Setup**: Initializes the Flask app and connects it to a SQLite database using SQLAlchemy for data storage.
- **Task Model**: Defines a Task class as a database model with attributes like title, description, and completion status.
- **Routes**:
  - `/`: Renders the main page where users can add, view, and manage tasks.
  - `/complete/<int:task_id>`: Marks a task as completed based on its ID.
  - `/delete/<int:task_id>`: Deletes a task based on its ID.
  - `/download_excel`: Generates an Excel file containing completed and incomplete tasks for download.
  - `/sort_tasks/<criteria>`: Sorts all tasks based on the selected criterion.

### Frontend
- **HTML Structure**: Defines the structure of the web page using HTML5.
- **CSS Styling**: Provides styling for a clean and user-friendly interface.
- **Task Management**:
  - Allows users to add new tasks with titles and optional descriptions.
  - Lists all tasks with options to mark them as completed or delete them.
  - Completed tasks are displayed with a strike-through effect to differentiate them.
- **Download Button**: Provides a button to download completed tasks in an Excel file.

### Features:
1. **Task Creation**: Users can add new tasks by inputting titles and optional descriptions via a form.
2. **Task Completion**: Tasks can be marked as completed, visually differentiating them from pending tasks.
3. **Task Deletion**: Allows users to remove tasks from the list, decluttering the view.
4. **Sorting Tasks**: Provides sorting options to organize tasks based on their completion status: showing all tasks, completed tasks, or pending tasks.

### User Interactions:
- **Adding Tasks**: Users can input task names and descriptions via a form on the web interface.
- **Marking Completion**: By clicking on the "complete" button next to a task, users can mark it as completed, which changes the visual appearance of the task.
- **Deleting Tasks**: The "delete" button enables users to remove tasks from the list.
- **Sorting Functionality**: Users can use the dropdown menu to sort tasks based on completion status, altering the display to show different subsets of tasks.
- **Save all tasks**: Helps you save all tasks in Excel when you click "Download the report in Excel".

### Visual Cues and Interface Design:
- **Task Color Differentiation**: Completed tasks are visually distinguished from pending tasks by a change in color, with completed tasks  having a strikethrough to indicate their status.
- **Clear Icons**: The use of icons (e.g., checkmark for completion, trash can for deletion) provides intuitive cues for users to understand and interact with the tasks easily.
- **Responsive Interface**: The interface is designed to be user-friendly, responsive, and visually appealing, allowing for an efficient management experience.
---
![image](https://github.com/7GitGuru/Task-Manager/assets/154711952/a803d971-29cd-4999-8eac-e5eee49f384c)
![image](https://github.com/7GitGuru/Task-Manager/assets/154711952/054746c7-28af-40db-8817-b383dcf12cba)
![image](https://github.com/7GitGuru/Task-Manager/assets/154711952/36f35e9a-ad76-4a66-a3ac-c6c07da83bec)
