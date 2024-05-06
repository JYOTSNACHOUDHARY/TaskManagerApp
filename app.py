from flask import Flask, render_template, request, redirect, url_for

from task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def index():
    tasks = task_manager.get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        description = request.form['description']
        priority = request.form['priority']
        due_date = request.form['due_date']
        status = request.form['status']
        task_manager.add_task(description, due_date= due_date, completed = status, priority=priority)
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = task_manager.get_task_by_id(task_id)
    if task is None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        description = request.form['description']
        priority = request.form['priority']
        due_date = request.form['due_date']
        status = request.form['status']
        task_manager.edit_task(task_id, description, due_date= due_date, completed = status, priority=priority)
        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
