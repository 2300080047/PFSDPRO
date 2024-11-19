from flask import Flask,request,redirect,url_for
from flask import render_template
import datetime
from weatherapp import weather

import sqlite3
app = Flask(__name__)

import sqlite3

def init_db():
    with sqlite3.connect("pfsdskill.db") as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS todo_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            date_created TEXT NOT NULL
        )''')
        conn.commit()

@app.route('/todo')
def view_todo():
    with sqlite3.connect("pfsdskill.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM todo_items ORDER BY date_created DESC")
        tasks = c.fetchall()
    return render_template('view_todo.html', tasks=tasks)

# Route to add a new to-do item
@app.route('/todo/new', methods=['GET', 'POST'])
def add_todo_item():
    if request.method == 'POST':
        task = request.form['task']
        date_created = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        with sqlite3.connect("pfsdskill.db") as conn:
            c = conn.cursor()
            c.execute("INSERT INTO todo_items (task, date_created) VALUES (?, ?)",
                      (task, date_created))
            conn.commit()
        return redirect(url_for('view_todo'))
    return render_template('add_todo_item.html')

# Route to delete a to-do item
@app.route('/todo/delete/<int:id>')
def delete_todo_item(id):
    with sqlite3.connect("pfsdskill.db") as conn:
        c = conn.cursor()
        c.execute("DELETE FROM todo_items WHERE id = ?", (id,))
        conn.commit()
    return redirect(url_for('view_todo'))


@app.route('/home')
def hello():
    return 'Hello, World!'

@app.route('/page1')
def Welcome():
    return 'Welcome to S31 section'

@app.route('/')
def Login():
    return render_template('loginPage.html')

@app.route('/page3')
def function3():
    return render_template('random.html')

@app.route('/we', methods=['POST','GET'])
def func3():
    city = request.form['City'] if request.method == 'POST' else 'delhi'
    return weather(city)



if __name__ == "__main__":
    init_db()
    app.run()
