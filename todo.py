from flask import Flask, redirect
app = Flask(__name__)


# Our "database" is just a list
todos = []


@app.route('/')
def list_todos():
    for item in todos:
        return(item)

@app.route('/add/<task>')
def add_todo(task):
    # append the 'task' to the list
    for item in todos:
        if task == item:
            return("Error")
        todos.append(task)

    # Return back to the to-do list page
    return redirect('/')


@app.route('/delete/<int:task_id>')

def delete_todo(task_id):
    # delete the item at the specified position in the list

    # Return back to the to-do list page
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)