#!/usr/bin/env python
# coding: utf-8

# # MSDS 430 Module 3 Python Assignment

# <div class="alert alert-block alert-warning"><b>In this assignment you will read through the notebook and complete the exercises. Once you are satisfied with the results, submit your notebook and html file to Canvas. Your files should include all output, i.e. run each cell and save your file before submitting.</b></div>

# <div class="alert alert-block alert-info">The main topics this week are loops and functions. There are two types of loops that we are working with - the <font color=black>for loop</font> and the <font color=black>while loop</font>. You have a couple of questions in this assignment dealing with each that will give you a chance to compare the two. Think about which is more concise and when each might be used. Additionally we are working with functions, user-defined and built-in. It will be worth your time to explore Python's built in functions beyond what is asked of you in this assignment. User-defined functions will appear quite frequently throughout the course and can be difficult to grasp at first. Be sure to use the <font color=black>codelens</font> view in your interactive textbook for each of the sample programs provided to understand how Python processes functions. This will reinforce your understanding of the concept.  </div>

# ### Math Module

# Python has many built-in math functions within the math module. A list of these can be found at __[Math Module](https://docs.python.org/3/library/math.html)__. For example, `math.gcd(x, y)` returns the gcd of two numbers. To use any of the functions in this module, we first have to import the module for Python to recognize it.

# In[1]:


import math
math.gcd(24,1002)


# <div class="alert alert-block alert-success"><b>Problem 1 (2 pts.)</b>: Use the <font color=black><i><u>math.pi( )</u></i></font> function to calculate the volume of a sphere with radius 5, rounded to 3 decimals.</div>

# In[3]:


import math

pi = math.pi
radius = 5
volume = (4/3) * (pi) * (radius ** 3)

print(round(volume, 3))


# <div class="alert alert-block alert-success"><b>Problem 2 (2 pts.)</b>: Create a <font color=black><b>for loop</b></font> that uses the <font color=black><i><u>math.sqrt(&nbsp;)</u></i></font> function and calculates and prints the square root of each of the integers 1 through 10. Round to two decimal places. For example, the first iteration of the loop in the program should print:</div>
# 
# `The square root of 1 is 1.0`

# In[2]:


import math
for i in range(1, 11):
    base = i
    sqroot = round((math.sqrt(i)),2)
    print("The square root of", base, "is", sqroot, ".")


# <div class="alert alert-block alert-success"><b>Problem 3 (4 pts.)</b>: Redo the previous problem, except instead of creating a <font color=black>for loop</font>, create a <font color=black><b>while loop</b></font> that uses <font color=black><i><u>math.sqrt(&nbsp;)</u></i></font> and calculates and prints the square root of each of the the integers 1 through 10. Round to two decimal places. Your output should look the same as the previous problem.</div>

# In[7]:


import math

number = 1

while number <= 10:
    sqroot = round((math.sqrt(number)),2)
    print("The square root of", number, "is", sqroot, ".")
    number += 1


# ### User-defined Functions

# The remaining problems involve user defined functions. These have many benefits, one of which is reusability. They only need to be written once and can be reused several times. They are also a way to help us organize our code. For an additional resource on user-defined functions in Python, read through this tutorial: __[User-defined Functions](https://www.tutorialsteacher.com/python/python-user-defined-function)__

# <div class="alert alert-block alert-success"><b>Problem 4 (6 pts.)</b>: Suppose the operator <font color=red>!=</font> does not exist in Python. Define a function <font color=black><b>not_equal</b></font> that uses subtraction to compare any two numbers, then gives the same result as the <font color=red>!=</font> operator. You <b><i><u>cannot</u></i></b> use <font color=red>=</font>, <font color=red>==</font>, or <font color=red>!=</font> in your program. Test your program using <br>
# 
# (1) `x = -12` and `y = 3`<br>
# (2) `x = 3` and `y = -12`<br>
# (3) `x = y = -12` 
# <br><br>See sample output below:</div>
# 
# 
# `-12 and 3 are not equal.`<br>
# `3 and -12 are not equal.`<br>
# `3 and 3 are equal.`

# In[58]:


x = int(input("Please enter a number (x):"))
y = int(input("Please enter second number (y):"))

no_signs_sub = x - y

def not_equal(no_signs_sub):
    if no_signs_sub > 0:
        print(x, "and", y, "are not equal.")
    elif no_signs_sub < 0:
        print(x, "and", y, "are not equal.")
    else:
        print(x, "and", y, "are equal.")
        
not_equal(no_signs_sub)


# <div class="alert alert-block alert-success"><b>Problem 5 (8 pts.)</b>: Complete a program containing user defined functions that prints out an <font color=black><b>n x n</b></font> square. You can use a function to print the top line, a function to print each row, and a final function to print the whole grid. 
# 
# <b>Example Output</b>: <i>Your 1x1, 2x2, 3x3 and 10x10 squares should look like the following</i>:</div>
# 
# <img src="attachment:m3p5.png" style="max-width:100%">

# In[43]:


n = int(input("Please enter a number:"))

def print_top_line(n):
    line = ""
    for i in range(0,n):
        line+=" _"
    print(line)

def print_row(n):
    line = ""
    for i in range(0,n):
        line+="|_"
    for i in range(0,1):
        line+="|"
    print(line)
    
def print_square(n):
    print_top_line(n)
    for i in range(0,n):
        print_row(n)
    
print_square(n)


# In[ ]:




