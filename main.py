from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from io import BytesIO

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
    completed_tasks = [task for task in all_tasks if task.completed]
    incomplete_tasks = [task for task in all_tasks if not task.completed]

    excel_file = BytesIO()
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        df_completed = pd.DataFrame(
            [{'Title': task.title, 'Description': task.description} for task in completed_tasks])
        df_completed.to_excel(writer, index=False, sheet_name='Done')

        df_incomplete = pd.DataFrame(
            [{'Title': task.title, 'Description': task.description} for task in incomplete_tasks])
        df_incomplete.to_excel(writer, index=False, sheet_name='Not done')

    excel_file.seek(0)
    return send_file(
        excel_file,
        as_attachment=True,
        download_name='tasks.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)