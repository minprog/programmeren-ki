# Queue

Let's see what it means to define a useful *interface* for a class by implementing a **queue** data structure. The goal of a queue is to be able to store items that you might retrieve later, in the order in which they were stored. As such, a queue supports two core operations:

- **enqueue**, which adds an item to the back of queue, waiting to be collected again
- **dequeue**, which removes an item from the front of the queue

![A visual description of the queue structure. It is a row of elements. One end is labeled 'back' and the other end 'front'. On the periphery near the back is another element, with an arrow pointing from that element to the back, labeled 'enqueue'. From the front an arrow points to a different element outside the queue. That arrow is labeled 'dequeue'.](wikipedia_queue.png){:style="max-width:300px"}  
<small>Image by [Vegpuff/Wikipedia](https://commons.wikimedia.org/wiki/File:Data_Queue.svg).</small>

The idea of a queue is used in many applications, but an important one is scheduling. Computers can administer many tasks that have to be performed, and when one task is done, another may be started. The list of open tasks is kept in a queue, ensuring that the oldest task is always scheduled next.

Note our use of "front" and "back" in the description above. The most important thing about queues is that elements are added to one end, while removing elements is done at the other end. This ensures that elements which are first into the queue, will also be removed first (this is often called first-in-first-out, or FIFO).


{% next "Let's get started" %}


## Defining a class interface

From the description above you might understand that a queue is, in its essence, a list of items, but that it enables a very specific way of dealing with that data --- using the **enqueue** and **dequeue** operations. These two operations form the *interface* of the queue data structure, which defines how it is supposed to be used by a programmer. Now if we fully implement this class in Python, we might use the class like this:

    q = Queue()          # create new queue
    q.enqueue(3)         # add number 3 to back of queue
    q.enqueue(1)         # add number 1 to back of queue
    print(q.dequeue())   # prints first number "in", so 3

This means that the class definition must look like this:

    class Queue:

        # add element to back of queue
        def enqueue(self, element):
            # TODO

        # remove and return element from front of queue
        def dequeue(self):
            # TODO

**Before you go on**, copy the class definition from above into the editor on the right. You can also copy the testing code below it. Study it well.

We have now defined the *class interface* in Python. The class interface, consisting of two methods, prescribes how you could **use** the class by calling its methods. However, our interface does not have an implementation yet, so the testing code doesn't work.

{% next %}


## Choosing an internal representation

As we mentioned, a queue is similar to a list, yet with a different set of supported operations. Our queue objects will need to have some data storage for keeping items. We will use a standard Python list to build our class around. Specifically, each queue object will *contain* its own private list object.

To create an object that is internal to our queue objects, we should store and retrieve it using the `self` keyword:

    self._data = []

This line creates a new list and stores it in the object under the name `_data`. We chose to start the name with an underscore (`_`) to indicate that the variable is private to the object, and that one should not to write code to manipulate that variable from anywhere else but the code of the class itself.

> The underscore is a Python *convention*, a common way of doing. Python itself will not enforce the data to be private.

Because each object needs such a list from the very beginning, the line above should be placed in the *object initializer*, which will then look like this:

    def __init__(self):
        self._data = []

**Before you go on**, add this method to the top of the `Queue` class definition.

From now on, each time a new object is created using `Queue()`, it will also create an internal list, which is accessible from the class code using `self._data`.

{% next %}


## Enqueueing

Now that we have storage, it's time to implement the `enqueue()` operation. Recall that items should be stored at one end, but removed at the other end of the queue. How could we do this using the standard Python list that we chose to use?

Python lists support a variety of operations for adding and removing items. [Have a look at the documentation](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types). You probably know `append()` to add an item to the "end" of a list. That seems a good starting point.

**Implement** `enqueue()` to append the given element to the internal `_data` list.

{% next %}


## Dequeueing

Now that you have implemented this method, how should you implement `dequeue()`? As it happens, it is essential that you think hard about the two methods and how they work in tandem.

As we have defined enqueue to use `append()`, which adds items to the **end** of a list, we should be looking to remove items from the **start**. Think about this. Which element should you remove? What standard method could you use?

And there's a catch! What use is it to remove elements from a queue if we can't do anything with those? The method should not only remove the element but also `return` it.

Take another look at the Python [documentation](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) for lists and see if you can find a method that you can use to remove elements from the start of a list.

**Implement** `dequeue()`.

{% next %}


## Features

While `enqueue()` and `dequeue()` are quite essential for implementing the queue data structure, there are some additional features that may come in handy.

We now ask you to implement three of those operations as methods of the `Queue` class:

- **size**, which returns the number of elements "waiting" in the queue
- **peek**, which returns the frontmost element but does not remove it from the queue (yet)
- **empty**, which clears the queue, removing all elements

**Implement** these operations and add some testing code at the bottom of `queue.py` to see if it all works well.

{% next %}


## Helping to debug

When you're going to use the `Queue` class somewhere in your own project, you might encounter an error when trying to `dequeue()` when the queue is actually empty. Depending on how you chose to implement that method, you will get some kind of exception. This exception is not very queue-specific.

One method to alert yourself to potential problems is to add **assertions** to your code. In this case you can add the following assertion to the very top of your `dequeue()` method.

    assert self.size() > 0

Once you have done this, and some other part of the code tries to dequeue an element while the queue is empty, you will get an `AssertionError` on the line you just added. This helps you immediately understand that there's a problem in `dequeue()` and that the problem is that the queue size is `0`.

**Add the assertion** above to the `dequeue()` method and add a test to check if an error can be triggered.

Note that such an error will **not** help the *user* of a program in which your `Queue` class is implemented. To a user, an `AssertionError` means nothing but confusion! So, assertions are first and foremost a tool to help find the root cause of problems in your own code.

{% next %}


## Conclusion

Having implemented the `Queue` class, you should notice what it *doesn't* support. You can't, for example, take a look at the second element of a queue, unless you remove the first one. And you definitely can't dequeue an element from the back of the queue. All in all, a queue is a lot less flexible than a standard Python structure such as a list or a dictionary. So why use a queue at all? Two principles of object oriented programming are at play here:

1. Our class provides a simple to use *interface* for a very specific task. This makes the code that *uses* the queue much simpler to read. In this case, an experienced programmer recognizes the enqueue and dequeue operations and immediately understands what's going on.

2. Our class *hides its implementation*. Because we use Python, it's obvious that we can use a list as the storage mechanism for the queue. But the fact that we do isn't visible to the programmer who uses the class. They only need to be concerned with the queue operations. And if you want to change the inner workings of the queue "under the hood", that's no problem: the interface stays the same.

There are a few standard structures like queues that you might be aware of as a programmer. One that you might have encountered before is the **stack**. Having done the exercises above, you might look up the stack data type on Wikipedia and try to implement its operations in a Python class. It is quite similar to a queue, yet very different in its behavior and its applications!

This was Queue.
