from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from io import BytesIO
from flask import jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)

# db.create_all() COMMENTED IN THIS VERSION

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)
pass

@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get(task_id)
    task.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/download_excel')
def download_excel():
    all_tasks = Task.query.all()

    excel_file = BytesIO()
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        workbook = writer.book
        bold_format = workbook.add_format({'bold': True})

        worksheet = workbook.add_worksheet('All Tasks')

        # Установка ширины колонок в таблице Excel
        worksheet.set_column('A:C', 20)

        # Заголовки таблицы
        headers = ['Status', 'Title', 'Description']

        # Запись заголовков таблицы
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, bold_format)

        # Запись данных в таблицу Excel
        for idx, task in enumerate(all_tasks, start=1):
            status = 'Completed' if task.completed else 'Not Completed'
            task_data = [status, task.title, task.description]
            worksheet.write_row(idx, 0, task_data)

    excel_file.seek(0)
    return send_file(
        excel_file,
        as_attachment=True,
        download_name='tasks.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

@app.route('/sort_tasks/<criteria>')
def sort_tasks(criteria):
    if criteria == 'alphabetically':
        sorted_tasks = Task.query.order_by(Task.title).all()
    elif criteria == 'completed':
        sorted_tasks = Task.query.filter_by(completed=True).all()
    elif criteria == 'notCompleted':
        sorted_tasks = Task.query.filter_by(completed=False).all()
    else:
        sorted_tasks = Task.query.all()

    tasks = [{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed
    } for task in sorted_tasks]

    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
