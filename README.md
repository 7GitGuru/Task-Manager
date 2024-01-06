This project is a basic Task Manager web application built using Flask, a Python web framework. Its primary functionalities include managing tasks, marking them as completed, deleting tasks, and exporting reports into an Excel file.

Here's an overview of its components and features:

### Backend (main.py)
- **Flask App Setup**: Initializes the Flask app and connects it to a SQLite database using SQLAlchemy for data storage.
- **Task Model**: Defines a Task class as a database model with attributes like title, description, and completion status.
- **Routes**:
  - `/`: Renders the main page where users can add, view, and manage tasks.
  - `/complete/<int:task_id>`: Marks a task as completed based on its ID.
  - `/delete/<int:task_id>`: Deletes a task based on its ID.
  - `/download_excel`: Generates an Excel file containing completed and incomplete tasks for download.

### Frontend (index.html)
- **HTML Structure**: Defines the structure of the web page using HTML5.
- **CSS Styling**: Provides styling for a clean and user-friendly interface.
- **Task Management**:
  - Allows users to add new tasks with titles and optional descriptions.
  - Lists all tasks with options to mark them as completed or delete them.
  - Completed tasks are displayed with a strike-through effect to differentiate them.
- **Download Button**: Provides a button to download completed tasks in an Excel file.

### Workflow
1. Users can add tasks by entering a title and description (optional) in the form provided.
2. Listed tasks display options to mark them as completed or delete them.
3. Completed tasks are visually distinguished with a strike-through effect.
4. The "Download the report in Excel" button triggers the download of completed tasks in an Excel file, separating completed and incomplete tasks into different sheets.

![image](https://github.com/7GitGuru/Task-Manager/assets/154711952/744ea906-bc20-4095-af21-62b83aed8278)



### TO DO LIST
- number the list of tasks.
- add sorting by date added, alphabet, etc.
- redesign
- Improve the appearance of saving to an Excel file.
