#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create a file named zoo.py and define the function inside
with open('zoo.py', 'w') as file:
    file.write("""
def hours():
    print('Open 9-5 daily')
""")

# Now, let's import the module and call its function in the interactive interpreter
import zoo
zoo.hours()


# In[ ]:


import zoo as menagerie
menagerie.hours()
Open 9-5 daily


# In[ ]:


# Define the text lines
text_lines = [
    'author,book',
    'J R R Tolkien,The Hobbit',
    'Lynne Truss,"Eats, Shoots & Leaves"'
]

# Define the file name
file_name = 'books.csv'

# Write the text lines to the file
with open(file_name, 'w') as file:
    for line in text_lines:
        file.write(line + '\n')

print(f'File "{file_name}" has been created with the provided text lines.')

