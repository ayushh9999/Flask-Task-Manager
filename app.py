# ===================================================================
# IMPORTS - Bringing in necessary libraries and modules
# ===================================================================

# Flask imports - Core web framework components
from flask import Flask, render_template, request, redirect, url_for, jsonify
# Flask: Main application class
# render_template: Renders HTML templates with data (like res.render in Express)
# request: Contains data from incoming HTTP requests (like req in Express)
# redirect: Redirects user to another route (like res.redirect in Express)
# url_for: Generates URLs for routes by function name
# jsonify: Converts Python data to JSON format (not used in this app but imported)

# SQLAlchemy - Database ORM (Object-Relational Mapping)
from flask_sqlalchemy import SQLAlchemy
# This lets us interact with database using Python objects instead of SQL queries

# DateTime - For working with dates and timestamps
from datetime import datetime

# ===================================================================
# APPLICATION SETUP - Initialize Flask app and configure database
# ===================================================================

# Create Flask application instance (like const app = express() in Express)
app = Flask(__name__)

# Configure database connection
# 'sqlite:///todo.db' means use SQLite database file named 'todo.db'
# SQLite is a lightweight database that stores data in a single file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# Disable modification tracking to save memory (best practice)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with our Flask app
# This creates the 'db' object we'll use for all database operations
db = SQLAlchemy(app)

# ===================================================================
# DATABASE MODEL - Define structure of Todo table
# ===================================================================

# Todo Model - This class represents the 'todo' table in our database
# Similar to defining a Mongoose schema in Express/MongoDB
class Todo(db.Model):
    # Primary key - unique ID for each todo (auto-increments)
    id = db.Column(db.Integer, primary_key=True)
    
    # Title column - stores the todo text (max 200 characters, required)
    title = db.Column(db.String(200), nullable=False)
    
    # Completed column - stores True/False status (defaults to False)
    completed = db.Column(db.Boolean, default=False)
    
    # Timestamp column - stores when todo was created (auto-sets current time)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # String representation of Todo object (useful for debugging)
    # When you print a Todo, it shows: <Todo 1: Buy groceries>
    def __repr__(self):
        return f'<Todo {self.id}: {self.title}>'

# ===================================================================
# DATABASE INITIALIZATION - Create tables if they don't exist
# ===================================================================

# Create all database tables based on models defined above
# This runs once when the app starts
with app.app_context():
    db.create_all()  # Creates 'todo' table if it doesn't exist

# ===================================================================
# ROUTES - Define URL endpoints and their functions
# ===================================================================

# HOME PAGE ROUTE - Display all todos
# This is like: app.get('/', (req, res) => {...}) in Express
@app.route('/')
def index():
    # Query database for all todos, ordered by newest first
    # .query.order_by() - sorts results
    # .desc() - descending order (newest first)
    # .all() - get all matching records
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    
    # Render the index.html template and pass 'todos' data to it
    # Template can access 'todos' variable in Jinja2 syntax
    return render_template('index.html', todos=todos)


# ADD TODO ROUTE - Create new todo
# methods=['POST'] - only accepts POST requests (like app.post() in Express)
@app.route('/add', methods=['POST'])
def add_todo():
    # Get 'title' field from submitted form data
    # request.form is like req.body in Express
    title = request.form.get('title')
    
    # Only create todo if title is not empty
    if title:
        # Create new Todo object with the title
        new_todo = Todo(title=title)
        
        # Add to database session (staging area)
        db.session.add(new_todo)
        
        # Save changes to database (like await todo.save() in Mongoose)
        db.session.commit()
    
    # Redirect back to home page to show updated list
    # url_for('index') generates URL for the index() function
    return redirect(url_for('index'))


# TOGGLE TODO ROUTE - Mark todo as complete/incomplete
# <int:id> - captures number from URL as 'id' parameter
# Example: /toggle/5 will set id=5
@app.route('/toggle/<int:id>')
def toggle_todo(id):
    # Find todo by ID, or return 404 error if not found
    # Like: Todo.findByPk(id) in Sequelize
    todo = Todo.query.get_or_404(id)
    
    # Flip the completed status (True becomes False, False becomes True)
    # 'not' is Python's boolean negation operator (like ! in JavaScript)
    todo.completed = not todo.completed
    
    # Save changes to database
    db.session.commit()
    
    # Redirect back to home page
    return redirect(url_for('index'))


# DELETE TODO ROUTE - Remove todo from database
@app.route('/delete/<int:id>')
def delete_todo(id):
    # Find todo by ID, or return 404 error if not found
    todo = Todo.query.get_or_404(id)
    
    # Delete the todo from database
    # Like: await todo.destroy() in Sequelize
    db.session.delete(todo)
    
    # Save changes to database
    db.session.commit()
    
    # Redirect back to home page
    return redirect(url_for('index'))


# EDIT TODO ROUTE - Update todo title
@app.route('/edit/<int:id>', methods=['POST'])
def edit_todo(id):
    # Find todo by ID, or return 404 error if not found
    todo = Todo.query.get_or_404(id)
    
    # Get new title from submitted form
    title = request.form.get('title')
    
    # Only update if new title is not empty
    if title:
        # Update the title property
        todo.title = title
        
        # Save changes to database
        db.session.commit()
    
    # Redirect back to home page
    return redirect(url_for('index'))

# ===================================================================
# RUN SERVER - Start the Flask development server
# ===================================================================

# This runs only if script is executed directly (not imported)
# Like: app.listen(5000) in Express
if __name__ == '__main__':
    # Start Flask development server
    # debug=True - enables auto-reload and detailed error messages
    # Runs on http://127.0.0.1:5000 by default
    app.run(debug=True)
