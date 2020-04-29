#!/usr/bin/env python
# coding: utf-8

# # MSDS 430 Module 2 Python Assignment

# <div class="alert alert-block alert-warning"><b>In this assignment you will read through this notebook then complete the exercises. Once you are satisfied with your results, submit your notebook and html file to Canvas. Your files should include all output, i.e. run each cell and save your files before submitting.</b></div>

# <div class="alert alert-block alert-info"> This week we are starting to learn how to write short programs in Python beyond basic print statements. We're learning about different data types such as integers, floats, strings, and Boolean types. Each of these data types serves different purposes. In this assignment, we start working with these data types and get our feet wet with conditional statements. Conditionals are quite useful in programming and we will work with them in nearly every assignment from here on out. </div>

# ### Basic Calculations

# We've seen that Python can easily be used as a calculator. Notice we don't need a `print` command to return the result. We simply need to type in a mathematical expression then run the cell. Also, if all values in the expression are integers, Python will return an `int` value.

# In[1]:


19*5 - 31


# If at least one value in an expression is a float, Python will return a float value:

# In[2]:


19*5 - 31.0


# To verify this is a float, we use the `type()` command. When we do this, Python will not return the result of the expression - only the `type` of the end result:

# In[3]:


type(19*5 - 31.0)


# In this case we could assign a variable name to the expression, add a print statement to return the result of the calculation, and ask for the type.

# In[4]:


calc = 19*5 - 31.0
print(calc)
type(calc)


# We can also convert the result of the expression to another type. For example, we could convert the integer-valued expression above to a float. It will still return the result of the calculation, but notice the result is a float value:

# In[5]:


float(19*5 - 31)


# <div class="alert alert-block alert-success"><b>Problem 1 (2 pts.)</b>: In the <b><i>1st cell</i></b> below create a <b><i>single line of code</i></b> that uses Python to find the sum of -6.5 and 1.3 <b><i>and</i></b> converts the result to an integer. Do so without assigning a variable name and without using <font color=black><i>print(&nbsp;)</i></font>. Do the same in the <b><i>2nd cell</i></b> provided, except this time convert the sum to a string.</div>

# In[11]:


int(-6.5+1.3)


# In[12]:


str(-6.5+1.3)


# <div class="alert alert-block alert-success"><b>Problem 2 (2 pts.)</b>: Use Python as a calculator again. This time use <b><i>all five</i></b> mathematical operators (<font color=red>+</font>,<font color=red> –</font>,<font color=red> *</font>,<font color=red> /</font>,<font color=red> **</font>) in a <b><i>single expression</i></b> to produce the number 3.</div>

# In[24]:


int(1**2*6/3-3+4)


# ### The Input Function

# In this week's readings you also learned about a built-in function in Python called `input`. When this is used in a program it will prompt the user to enter something, say a number or a string. It's helpful when creating a prompt to provide clear instructions for the user, such as `Enter your birthdate in the form MM/DD/YYYY` or `Enter your postal code` instead of a blank entry box.

# In[1]:


name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name, "is", age, "years old.")


# In[ ]:





# Keep in mind that this function will return a string value unless told otherwise. If we try some type of mathematical calculation with `age`, it will treat it like a string:

# In[2]:


age*3


# An alternative is to convert `age` to an `int` when it is input:

# In[3]:


name = input("Enter your name: ")
age = int(input("Enter your age: ")) #We could also use float instead of int depending on preference.
print(name, "is", age, "years old.")


# Now when we attempt a mathematical calculation with age we get a more meaningful result.

# In[4]:


print(name, "will be 65 years old in", 65 - age, "years.")


# <div class="alert alert-block alert-success"><b>Problem 3 (5 pts.)</b>: Write a program that asks a user for two numbers, then prints two sentences displaying the sum and product of those numbers, respectively. More specifically, the program should display the prompt <font color=black><i>Enter any number:</i>&nbsp;</font> and then wait for the user's input. After the user enters his/her input followed by pressing the enter/return key, the program prompts the user to enter a second number in a similar fashion. <br>  <br>Here is a sample of what this should look like to the user when your program is run:</div>
# 
# `Enter any number: `5<br>
# `Enter a second number: `123 <br> 
# `The sum of 5 and 123 is 128.`<br>
# `The product of 5 and 123 is 615.`

# In[5]:


number = int(input("Enter any number: "))
phone = int(input("Enter a second: "))
print("The sum of", number, "and", phone, "is", phone+number, ".")
print("The product of", number, "and", phone, "is", phone*number, ".")


# ### More Mathematical Operators

# Above we worked with five mathematical operators, `+`, `-`, `*`, `/`, and `**`. Other basic operators in Python are `%` and `//`. The first is a modulus operator that returns the remainder upon division of the left operand by the right operand. For example `299 % 2` will return the remainder when 299 is divided by 2, i.e. the result would be 1. Below are a few examples. Feel free to try some of your own.

# In[5]:


print(28 % 3)
print(400 % 211)
print(250 % 4.0)


# The second operator, `//` is a floor division operator. This is the quotient of two numbers without the decimals. This does not mean it will return an `int` type. That will depend on the expression. For example, `299//2` has a quotient of 149 with a remainder of 1. So, `299//2` will return `149`, which is an int. Whereas, `299.0//2` will return `149.0`, which is a float. 

# <div class="alert alert-block alert-success"><b>Problem 4 (3 pts.)</b>: Write a program that asks a user to enter any number then returns whether the number is a multiple of 5 or not then test it with any integer. Here's a sample of what this should look like to the user:</div>
# 
# `Enter any number: `319<br>
# `319 is not a multiple of 5.`

# In[4]:


number = int(input("Enter any number: "))
if(number % 5 != 0):
    print(number, "is not a multiple of 5.")
else: 
    print(number, "is a multiple of 5.")


# ### Conditional Statements

# In `Problem 4` you likely used a simple conditional statement to determine if the input number was a multiple of 5. In that type of conditional there are only two courses of action. We test the value with the `if statement` to see if it is true. If it is, we can have our program print something relevant (or do other things). If it is false, we can have our program print something different.

# In[6]:


x = 45

if x > 10:
    print(x, "is too large.")

else:
    print(x, "is small enough.")


# If we want to, say compare two or more numbers, we can use nested conditionals. Suppose we want to know if a number is at least three times as large as another number.

# In[7]:


number1 = 110
number2 = 330

if number2 > 3*number1:
    print(number2, "is at least three times", number1)

else:
    if number2 < 3*number1:
        print(number2, "is less than three times", number1)
    
    else:
        print(number2, "is exactly three times", number1)


# We can accomplish the same thing with what is sometimes called a chained conditional, which is sometimes preferred. This type of conditional uses the `elif` statement.

# In[8]:


number1 = 110
number2 = 330

if number2 > 3*number1:
    print(number2, "is at least three times", number1)

elif number2 < 3*number1:
    print(number2, "is less than three times", number1)
    
else:
    print(number2, "is exactly three times", number1)


# <div class="alert alert-block alert-success"><b>Problem 5 (6 pts.)</b>: Jake is looking for a job but has some conditions. He would love a job in Hawaii and would accept it if it pays at least 85,000 per year. He does not like New York but would take a job if it pays at least 100,000 per year. He would work anywhere else if it pays at least 60,000. Write a program that prompts the user to enter two input values, <font color=black><i><u>location</u></i></font> and <font color=black><i><u>pay</u></i></font>, and returns 
# 
# (1) "I'll take it!" if the user entered Hawaii and at least 85,000, New York and at least 100,000, or anywhere else with pay at least 60,000, for `location` and `pay`, respectively, or  <br> 
# (2) "No way." if the user enters Hawaii and less than 85,000 or New York and less than 100,000, for `location` and `pay`, respectively, or <br> 
# (3) "No thanks, I can find something better." if the `location` is anywhere else and the `pay` is less than 60,000.</div>

# In[42]:


location = str(input("Where would you like to work? "))
pay = int(input("How much would you like to make? "))

#TODO: Create a nested conditional statement to handle pay related to 'New York.'
if(location == "New York" and pay >= 100000): print("I'll take it!")
elif(location == "New York" and pay <= 100000): print("No way.")

#TODO: Create a nested 'elif' statement to handle pay related to "Hawaii."
elif(location == "Hawaii" and pay >= 85000): print("I'll take it!")
elif(location == "Hawaii" and pay <= 85000): print("No way.")

#TODO: Create another 'elif' statement to handle pay of at least 60,000 for all other locations.
elif(location != "New York" and location != "Hawaii" and pay >= 60000): print("I'll take it!")

#TODO: End the conditionals with the appropriate 'else' command for all other scenarios.
else:
    print("No thanks, I can find something better.")

