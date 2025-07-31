- description : python language에 대해서 몰랐던 코딩 스킬 (OOP)
- tag : python , OOP
- date : 2025-07-25

TOC
- [1. property](#1-property)
  - [1.1. @property](#11-property)
  - [1.2. @\<property\_name\>.deleter](#12-property_namedeleter)
  - [1.3. decorator function](#13-decorator-function)
- [2. Method Chaining](#2-method-chaining)
- [3. aggregation과 compsition의 차이](#3-aggregation과-compsition의-차이)
- [4. is vs ==](#4-is-vs-)
- [5. alias , mutable , cloning](#5-alias--mutable--cloning)
  - [5.1. Common Bug: Be Careful with Mutable Data Types as Default Arguments](#51-common-bug-be-careful-with-mutable-data-types-as-default-arguments)
  - [5.2. Important Tip: Immutable doesn't mean that its elements are immutable](#52-important-tip-immutable-doesnt-mean-that-its-elements-are-immutable)
  - [5.3. cloning for loop to avoid changing loop variable's size](#53-cloning-for-loop-to-avoid-changing-loop-variables-size)
- [6. inheritance](#6-inheritance)
  - [6.1. issubclass()](#61-issubclass)
  - [6.2. Multiple Inheritance](#62-multiple-inheritance)
  - [6.3. inheritance method](#63-inheritance-method)
- [7. magic methods](#7-magic-methods)





-------

# 1. property
- property라는 것을 사용하면 자동으로 get,set함수를 호출해준다. 
  - ```python
    class Dog:
      def __init__(self,age):
        ...
      def get_age(self):
        ...
      def set_age(self,age):
        ...
          
      age = property(get_age,set_age)

    a = Dog(3)
    a.age += 3
    ```
## 1.1. @property
- 
  - ```python
    class Dog:
      def __init__(self,age):
        self._age = age
      @property
      def age(self):
        return self._age
      @age.setter
      def age(self,age):
        self._age = age

    a = Dog(3)
    a.age += 3
    ```

## 1.2. @<property_name>.deleter
- This is the deleter, the method that deletes the property of a particular instance.
  - ```python
    class Bus:
    
        def __init__(self, color):
            self._color = color
    
        @property
        def color(self):
            return self._color
    
        @color.setter
        def color(self, new_color):
            self._color = new_color
    
        @color.deleter
        def color(self):
            del self._color
    ```

## 1.3. decorator function
- This is the general syntax of a decorator function:
  - ```python
    def decorator_function(arg_function):
        def wrapper_function():
            # Code to extend the functionality 
            arg_function()
            # Code to extend the functionality
        return wrapper_function
    ```

# 2. Method Chaining
```python
def add_topping(self, topping):
    self.toppings.append(topping.lower())
    return self
```

# 3. aggregation과 compsition의 차이
- Aggregation
  - Aggregation is a "has a" relationship.
  - ```python
    class Player:
        def __init__(self, die):
          self.die = die
    ```
- compisition
  - In composition, a composed object cannot exist without the object that contains it.
  - ```python
    class Player:
    
      def __init__(self):
        # Create the instance of Die 
        # inside the instance of Player.
        # This Die instance cannot exist without 
        # the Player instance that contains it. 
        self.die = Die(5)
    ```

# 4. is vs ==
- a is b : same object
  - id(a) , id(b)
- a == b : same value
- Let's Check that Objects are Passed by Reference
  - Let's confirm that objects are passed by reference in Python.
  - To do this, we will use the id() function to get the id of an object outside and inside a function.

# 5. alias , mutable , cloning
- Aliasing. Two variables reference the same object in memory.
- cloning
  - ```python
    a = [6,2,6,2]
    b = a[:]   # copied with different id (clone)
    ```
- mutable
  - list , set , dictionary
- immutable
  - boolean , integer , float , string , tuple

## 5.1. Common Bug: Be Careful with Mutable Data Types as Default Arguments
- Default arguments are not created every time you call the method. Instead, they are created once when the program starts to run.
  - ```python
    class WaitingList:
      
        # The default argument is an empty list.
        def __init__(self, customers=[]):
            self.customers = customers
        
        def add_customer(self, customer):
            self.customers.append(customer)
    
    # Create the instances.		
    waiting_list1 = WaitingList()
    waiting_list2 = WaitingList()
    
    # Add a customer to the first waiting list.
    waiting_list1.add_customer("Jake")
    
    # Both of them were modified!
    print(waiting_list1.customers)
    print(waiting_list2.customers)
    ```
  - output
    - ```python
      # Both of them were modified!
      ['Jake']
      ['Jake']
      ```
- solution
  - ```python
    class WaitingList:
      
        def __init__(self, customers=None):
            if customers is None:
                self.customers = []
            else:
                self.customers = customers
        
        def add_customer(self, customer):
            self.customers.append(customer)
    ```

## 5.2. Important Tip: Immutable doesn't mean that its elements are immutable
- ```my_list = ([1, 2, 3], "abc", 56)```

## 5.3. cloning for loop to avoid changing loop variable's size
- copy of dictiionary
  - ```python
    for k,v in dictionary.copy().items():
      if v % 2 == 0:
        del dictionary[k]
    ```

# 6. inheritance
## 6.1. issubclass()
- With this function, you can check if a class is a subclass of another class.
- super init
  - ```python
    class P:
      def __init__(self):

    class A(P):
      def __init__(self):
        P.__init__(self)
    ```
  - ```python
    class Sprite:
    
        def __init__(self, x, y, speed, direction):
            self.x = x
            self.y = y
            self.speed = speed
            self.direction = direction
    
    
    class Enemy(Sprite):
    
        def __init__(self, x, y, speed, direction, num_lives):
            Sprite.__init__(self, x, y, speed, direction)  # super().__init__(x, y, speed, direction)
            self.num_lives = num_lives
    ```

## 6.2. Multiple Inheritance
- ```python
  class Rectangle:
  
      def __init__(self, length, width, color):
          self.length = length
          self.width = width
          self.color = color
  
  
  class GUIElement:
  
      def click(self):
          print("The object was clicked...")
  
  
  class Button(Rectangle, GUIElement):
  
      def __init__(self, length, width, color, text):
          Rectangle.__init__(self, length, width, color)
          self.text = text
  ```

## 6.3. inheritance method
- Define common functionality in super class and sub classes will have access to these methods
- overloading :involves modifying the behavior of a method within a hierarchy. When a method is overridden, its new implementation takes precedence over previous implementations located higher in the hierarchy.
- Method Overloading occurs when two methods of the same class have the same name but different parameters.
- polymorphism
  - ```python
    class File:
        def __init__(self, name, extension):
            self.name = name
            self.extension = extension
    
        def open(self):
            print("Opening a generic file...")
    
    
    class PDFFile(File):
    
        def __init__(self, name):
            File.__init__(self, name, ".pdf")
    
        def open(self):
            print("Opening a PDF File...")
    
    
    class TextFile(File):
    
        def __init__(self, name):
            File.__init__(self, name, ".txt")
    
        def open(self):
            print("Opening a Text File...")


    # Then we have this function:

    def open_files(files):
        for file in files:
            file.open()
    ```

# 7. magic methods
- __str__()  <- print() , format() , str()
- __repr__() :  With the eval() function, we can use the string returned by repr() to recreate the object.
- (5).__add__(6)   : 5 + 6 
- __len__() <- len()
- object.__getitem__(self,key) : self[key] , object[index]
- __bool__() : bool()
- __len__() and __bool__()
  - When __bool__() is not defined, __len__() is called, if it is defined, and the object is considered true if its result is nonzero."
  - "If a class defines neither __len__() nor __bool__(), all its instances are considered true."
- __iter__() and __next__()
  - The special method __iter__() returns an iterator object from the iterable and the special method __next__() returns the next element in the iterator.
  - In these examples, we worked with lists but we can also implement these special methods in our classes to customize how we can iterate over custom objects with for loops.

