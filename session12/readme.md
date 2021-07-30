<h1 align="center">Iterators and iterable II </h1>

<h2 align="center"> Assignment Question </h2>


### Project: Description

* The starting point for this project is the Polygon class and the Polygons sequence type we created in the previous project.

The code for these classes along with the unit tests for the Polygon class are below if you want to use those as your starting point. But use whatever you came up with in the last project.
* We have two goals:

### Goal 1

* Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").

### Goal 2
* Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable, and an iterator.


## Test Cases

Test cases have been developed in the notebook to check the `Goal 1` and `Goal 2`. There are two sections in the notebook, first section tests `objective 1` over `properties`, `__repr__`,`__eq__` & `__gt__` function. The second section contains the test cases for `objective 2` over `properties`,`__repr__`, `__len__` & `__getitem__`.

## __repr__
In Python, __repr__ is a special method used to represent a class's objects as a string.

## __eq__
Python automatically calls the __eq__ method of a class when you use the == operator to compare the instances of the class

## __gt__
__gt__ (a, b) Perform “rich comparisons” between a and b. Specifically, lt(a, b) is equivalent to a < b , le(a, b) is equivalent to a <= b , eq(a, b) is equivalent to a == b , ne(a, b) is equivalent to a != b , gt(a, b) is equivalent to a > b and ge(a, b) is equivalent to a >= b
## __len__
Well, len(s) is a built-in Python method which returns the length of an object. Now __len__() is a special method that is internally called by len(s) method to return the length of an object. So, when we call len(s) method, s. __len__() is what actually happening behind the scenes to calculate the length.

## __getitem__
The method __getitem__(self, key) defines behavior for when an item is accessed, using the notation self[key]

## __iter__
The __iter__() function returns an iterator object that goes through the each element of the given object. 

## __next__
The next element can be accessed through __next__() function.