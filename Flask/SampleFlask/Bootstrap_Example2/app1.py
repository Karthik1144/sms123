from flask import *
import sqlite3

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

#create the object of Flask
app  = Flask(__name__)


#creating our routes
@app.route('/')
def Index():
    name = 'KL University - Car Rental System'
    return render_template('index.html', data = name)
@app.route('/login')
def login1():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']
    if uname == "klu" and passwrd == "123":
        return "<h1><center><font color = 'blue'><br><br><br><b><i>Welcome %s </i></b></font></center><h1>" % uname
    else:
        return "<h1><center><font color = 'red'><br><br><br><b>Wrong Username and password</b></font></h1></center>"

@app.route('/contact')
def Contact():
    return render_template('contact.html')



# List to store tasks (for simplicity, we'll store tasks in memory)
tasks = []

# Home route to display the tasks
@app.route('/todolist')
def todolist():
    return render_template('todolist.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('todolist'))

# Route to delete a task
@app.route('/delete/<int:task_index>')
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('todolist'))


posts = [
    {'id': 1, 'title': 'First Blog Post', 'content': 'This is the content of the first post.',
     'date_posted': datetime.now()},
    {'id': 2, 'title': 'Second Blog Post', 'content': 'This is the content of the second post.',
     'date_posted': datetime.now()}
]


# Home route - display the list of posts and allow creating new posts
@app.route('/blogpage', methods=['GET', 'POST'])
def blogpage():
    if request.method == 'POST':
        # Get data from form submission
        title = request.form['title']
        content = request.form['content']

        # Create a new post dictionary
        new_post = {
            'id': len(posts) + 1,  # Generate a new ID based on the length of the posts list
            'title': title,
            'content': content,
            'date_posted': datetime.now()
        }

        # Add the new post to the posts list
        posts.append(new_post)

        # Redirect to the home page after submitting the form
        return redirect(url_for('blogpage'))

    # Render home page with list of posts
    return render_template('blogpage.html', posts=posts)


# View a single post
@app.route('/post/<int:id>')
def postblog(id):
    post = next((post for post in posts if post['id'] == id), None)
    if post is None:
        return "Post not found", 404
    return render_template('postblog.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)