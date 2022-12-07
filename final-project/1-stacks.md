# Stacks

Stacks are neatly-organized piles of objects. For example, imagine a stack of books now. Each book is piled upon the other. And the last book to be added to the stack needs to be the first to be removed, otherwise the entire pile will fall!

![Stack of Books](images/stack-books.jpg)


## Python Lists

This analogy was brought to programming languages like Python. The data structure called **lists** are stacks of data that will keep the information organized while following the best practice called as "LIFO" *(Last in, First Out)*.

Python lists are created with square brackets like in:

`new_list = []`

They keep the data organized by using indexes. The first item added to the list will have index 0; the second, 1; the third, 2; and it will go like this until the last element in the list.


```python
# Creating a list of names
list_of_names = ['Bob', 'Mike', 'Rachel']

# Printing Bob's index ----> 0 expected
print(list_of_names.index('Bob'))

# Printing Rachel's index ----> 2 expected
print(list_of_names.index('Rachel'))
```


Items will be naturally added to the end of the list (just like adding books to the top of the stack) using the `append` method.


 ```python
# Adding a new name to the end of the list 
list_of_names.append('Vallery')

# Printing the new item's index ---> 3 expected
print(list_of_names.index('Vallery'))

# Printing the new list
print(list_of_names)
```
The last item is easily removed with `pop`:

```python
list_of_names.pop()
# will return 'Vallery'
```

## Performance and Big-O notation
In programming languages, performance measures how effectivelly code performs a task, taking into account how much memory is used, or how fast the code will run. It is normally expressed by using **Big-O notation**. In Big-O notation, the letter **n** represents the size of the data set. Thus, if we say that the performance for an algorithm is **O(n)**, it means that, in the worst case-scenario, it will run **n times** to perform the task, like:


```python
for name in list_of_names:
    print(name)
```

Something like adding an element to the end of the list, or removing it, is much faster and simpler, as it it only runs once. In this case, we say its performance is **O(1)**.

## Stack Example in Python:
One simple application of stacks could be used to keep track of the students who have enrolled in a course with limited number of seats. 


```python
# Setting the maximum number of seats available
max_seats = 50

# Creating a list to store the subscriber's e-mail
subscribers = []

# Adding new subscribers if there are spots availabe
if len(subscribers) < max_spots:
    subscribers.append(input('Please, enter your e-mail to subscribe to our course: '))
    print("Congratulations! We are looking foward to seeing you in our course! ")

# Telling future students they can't enroll this time
else:
    print("We're sorry! There isn't any spot available right now. Please wait for the next course to open.")
```
## Strecth Problem for You to Solve
Now, let's stretch a little bit.

*  It would be nice to create a waiting list to keep track of potential students as well as their position in a queue.
* If one of the students in our subscribers list drops our course, we should add the first student from the waiting list directly to the end of the subscribers list, while removing his email from the waiting list.


Try finding a solution for these problems first on your own. When you finish or after you hjave tried your best, you can check a sample solution on the link below

[Stacks Sample Python File](python-files/stacks.py)



