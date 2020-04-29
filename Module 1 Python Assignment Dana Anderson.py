#!/usr/bin/env python
# coding: utf-8

# # MSDS 430 Module 1 Python Assignment

# #### <div class="alert alert-block alert-warning"> Read through this notebook and follow the instructions provided. In this assignment you will complete the exercises that follow and submit your notebook (ipynb file) and html file to Canvas. Your files should include all output, i.e. run each cell and save before submitting for a grade.  In this course we will use only Python 3.0+</div>

# <div class="alert alert-block alert-info"><i>Each week we will be asking you to submit your completed notebook along with an html file. Some assignments will require additional types of files, so watch for that later on. Once you've run every cell in the notebook and you're satisfied with the results, submit the notebook and the html file to Canvas. To download the html file to your computer, go to <u>File --> Download as --> HTML.</u></i></div>

# ![save-as-html-screenshot%20%28Custom%29.png](attachment:save-as-html-screenshot%20%28Custom%29.png)

# #### Comments in Code Cells

# There are two primary types of cells that we will work with. The first type is a `code` cell. When you insert a cell in a Jupyter notebook, the default is to create a code cell. To add comments to a code cell, the `hash` symbol, `#` is typically used:

# In[2]:


#This is one way to add comments to your code.
#For each line of comments, a 'hash' symbol must be used while working in a code cell.


# Another method of adding (**multiline**) comments within a `code` cell is to use triple quotations like the cell below:

# In[3]:


'''When triple quotations are used, the comments will be enclosed by one set of quotations.
There is no need to start new quotations on each line. Just make sure all of your comments are wrapped
with quotations.'''


# With a `Markdown` cell we can type as we normally would. Double click on this cell to see that it is a markdown cell. This is indicated in the drop-down menu in the tool bar. Run the cell to return it to the formatted version.

# ### Data Types 

# The cell below has assigned values to different types of variables: `string`, `integer`, `float`, `Boolean`, and `null`. Run the cell so these can be used later in `Problem 2`.

# In[4]:


# Python defined variables are global and hence can be recalled later on in any other cell
name = 'Albert' # this is a string, assigned to name
height = 6      # this is an integer value, assigned to x1
pounds = 181.389321    # this is a numeric value, assigned to x2
tvalue = True   # this is a Boolean value, assigned to x3
flag=None     # this is a null in Python and has nothing defined for x4.


# We could check the type of each variable by using the command `type(variable_name)`. Now that you have run the previous cell, you can run the following cell to see what is displayed. Feel free to change `tvalue` to any of the other variables to see what is displayed.

# In[5]:


type(True)


# <div class="alert alert-block alert-success"><b>Problem 1 (1 pt.)</b>: Run the cell immediately below this one and notice the error message it generates. Correct the print statement in the cell below it and run that cell to check your correction. Explain why the initial print statement wasn't working by adding comments to your code in the new cell. </div>

# In[6]:


print 'This is my first Python print execution.'


# In[7]:


print ('This is my first Python print execution.')
#Print is a command/function/method and commands/functions/methods require parentheses in order to know what they are working on (their target).


# ### Formatting Print Statements

# Print statements can be formatted nicely using various methods. One possibility is the `String` format method. An example of this method would be: </br>
# 
# ```python
# print("My name is {} and I am {} feet tall.".format(name, height))
# ```
# 
# The output will look like this: </br>
# 
# `My name is Albert and I am 6 feet tall.` </br>
# 
# As you may have guessed, the brackets `{}` represent format fields and are replaced with objects passed through them in the `str.format` method. In this case we have already defined the variables `name` and `height` above, but we can still use this method without having predefined variables. </br>
# 
# If we place numbers in the brackets, this indicates the position of where the object should be passed. Remember the 1st position will be represented by `0`, the 2nd by `1`, etc. For example,

# In[8]:


print("{0} and {1} are my best friends.".format('Camille', 'Grace'))


# However, if we switch the placement of `0` and `1` we have:

# In[9]:


print("{1} and {0} are my best friends.".format('Camille', 'Grace'))


# Another method of formatting print statements is to use `f-strings`. This is done by typing an `f` or `F` in front of the string and using `{}` to pass our objects through. One of the benefits of the f-string method is that it affords us more formatting options.

# In[10]:


print(f'{name} weighs {pounds:.2f} pounds.')


# Notice this even rounded appropriately. In other words, it rounded to two decimals and round up with the last decimal. Another option is to use the right side of the `:` to indicate the minimum number of characters to use. This can be useful to line up columns. Notice how the second column lines up. Feel free to play around with the character lengths to see the effect.

# In[11]:


print(f'{name:10} --> {height:5d} feet tall')
print(f'{name:10} --> {int(pounds):5d} pounds')


# These are just a few basic examples of how to format output nicely. For more details about powerful print options to play with, read through this article on __[f-strings](https://realpython.com/python-f-strings/)__

# <div class="alert alert-block alert-success"><b>Problem 2 (3 pts.)</b>: In the cell below, create a formatted print statement using an f-string that passes through the objects `name`, `height`, and `weight` defined above and returns the following sentence: </div></br>
# 
# `ALBERT was 6 feet tall in high school, but weighed less than 181 pounds.`

# In[12]:


print(f'{name} was {height} feet tall in high school, but weighed less than {(int(pounds))} pounds.')


# <div class="alert alert-block alert-warning"><i><b>For the remaining problems you will want to convert the provided code cells provided to some other type of cell before inputting your answers. To do this, place your cursor in the cell and select the cell type from the drop-down menu in the tool bar.</b></i></div>

# <div class="alert alert-block alert-success"><b>Problem 3 (1 pt.)</b>: First, convert the cell below to <i><u>Raw NBConvert</u></i>. If you want to insert a cell below and move to that cell, what is the keyboard command? What is the keyboard command for executing the cell? Type your answers in the converted cell below. <br/><br/>
# 
# 
# <i>Note that all keyboard commands are decipherable by clicking on the `keyboard icon` in the tool bar.</i></div>
'Inserting a cell below' keyboard command = INSERT CELL BELOW = (command mode) B
'Move to cell below' keyboard command = SELECT NEXT CELL = (command mode) Down
'Executing the cell' keyboard command = RUN SELECTED CELLS = (command mode) Ctrl-Enter
# <div class="alert alert-block alert-success"><b>Problem 4 (1 pt.)</b>: First, convert the cell below to <i><u>Markdown</u></i>. List the top five keyboard commands you think are useful to speed up your iPython notebook execution. (To create a list in Markdown start each line with hyphen or an asterisk, followed by a space.) Type your answers in the converted cell below. For more information on working with Markdown cells, refer to this article:</div>

# __[Markdown Cells](http://nestacms.com/docs/creating-content/markdown-cheat-sheet)__

# - Copy selected cells = (command mode) C
# - Cut selected cells = (command mode) X
# - Paste cells below = (command mode) V
# - Enter command mode = (edit) ESC
# - Run cell and select next = (command mode) Shift-Enter

# <div class="alert alert-block alert-success"><b>Problem 5 (1 pt.)</b>: First, convert the cell provided to <u><i>Raw NBConvert</i></u>. Within an iPython notebook, how will you get help on any Python command? Type your answers in the converted cell below.</div>
There is a 'Help' pull down menu that lists a 'notebook help' option. This leads to tutorials and examples. Also, the 'Help' pull down menu also has a 'keyboard shortcuts' option which brings up a list that is a little easier to digest than the one provided from the 'keyboard' icon/button. These two things will help me get help on any Python command. Should that not help, I will email Dr. Dugan or the TA for assistance or research the internet/the textbook for answers.
# <div class="alert alert-block alert-success"><b>Problem 6 (1 pt.)</b>: First, convert the cell provided to <u><i>Markdown</i></u>. What are the top 5 magic commands that you feel are useful to interact with your operating system or Python execution? Type your answers in the converted cell below.</div>

# - %cd - This line magic changes the current directory.
# - %edit - This magic command calls upon the default text editor of current operating system (Notepad for Windows) for editing a Python script.
# - %env - This magic command will list all environment variables. 
# - %lsmagic - Displays all magic functions currently available.
# - %run - This command runs a Python script from within IPython shell.

# <div class="alert alert-block alert-warning">The following problem requires you to insert a screenshot into this notebook. There are several ways to do this. One default method is to use <u><i>Edit --> Insert Image</i></u> in a markdown cell then run the cell. Other methods are provided in this short video:</div>

# __[Inserting Images](https://www.youtube.com/watch?v=xlD8FIM5biA)__

# <div class="alert alert-block alert-success"><b>Problem 7 (2 pts.)</b>: First, convert the cell provided to a <u><i>Markdown</i></u> cell. From the <b><i>interactive interpreter</i></b> on your computer (also called <b><i>terminal</i></b> or <b><i>command prompt</i></b>) use Python to print 'Hello, world!'. Insert a screenshot of the executed print command in the converted cell below.</div>

# ![Hello%20World%20Image.jpg](attachment:Hello%20World%20Image.jpg)

# <div class="alert alert-block alert-danger">Be sure to <i><u>run all cells in your notebook</u></i> then submit the following for a grade:
#     
# 
# 1. Your completed <b>notebook</b>
# 2. Your <b>html file</b>
# 
# </div>

# In[ ]:




