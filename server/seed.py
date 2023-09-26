from random import randint, choice as rc,sample
from faker import Faker
from app import app
from models import db, TableToDo
import random
fake = Faker()

todo_lists = [
    "Work Tasks",
    "Home Chores",
    "Fitness Goals",
    "Grocery Shopping",
    "Personal Projects"
]
todo_descriptions = [
    "Complete the quarterly report for the sales team.",
    "Clean the kitchen and do the dishes.",
    "Go for a 30-minute jog in the park.",
    "Buy milk, eggs, and bread from the grocery store.",
    "Start working on the new website design project."
]



# delete any existing data
with app.app_context():
    db.session.query(TableToDo).delete()
    
    
    db.session.commit()
      
    # Create and add fake restaurants
    table_to_do = [
        TableToDo( 
            username = fake.name(),
            title =rc(todo_lists),
    
            description = rc(todo_descriptions) 
        )
        for i in range(10)
    ]
    db.session.add_all(table_to_do)  # Use db.session.add_all() to add the list
    db.session.commit()

   