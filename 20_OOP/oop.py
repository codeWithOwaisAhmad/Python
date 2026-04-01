"""
Object-Oriented Programming (OOP) in Python
-----------------------------------------
Python is a multi-paradigm language, but its core is Object-Oriented.
Everything in Python is an Object (instances of classes).

Four Pillars of OOP:
1. Encapsulation (Bundling data and methods)
2. Abstraction (Hiding complex implementation)
3. Inheritance (Reusing code from parent classes)
4. Polymorphism (Many forms/behaviors from one interface)
"""

class Animal:
    """Base class demonstrating Inheritance and Polymorphism."""
    
    # Class attribute (Shared among ALL instances)
    kingdom = "Animalia"
    
    def __init__(self, name: str, age: int):
        # Instance attributes (Unique to each instance)
        self.name = name  # Public attribute
        self._age = age   # Protected attribute (Convention only!)
        self.__id = 123   # Private attribute (Name mangling: _Animal__id)
        
    def speak(self) -> str:
        """To be overridden by subclasses (Polymorphism)."""
        raise NotImplementedError("Subclass must implement abstract method")
        
    # Encapsulation (Getter)
    def get_age(self) -> int:
        return self._age

class Dog(Animal):
    """Subclass inheriting from Animal."""
    
    def __init__(self, name: str, age: int, breed: str):
        # Calling parent constructor
        super().__init__(name, age)
        self.breed = breed
        
    def speak(self) -> str:
        """Overriding the parent method."""
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

def demonstrate_oop() -> None:
    print("--- 1. OOP Principles ---")
    
    dog = Dog("Buddy", 5, "Golden Retriever")
    cat = Cat("Whiskers", 3)
    
    print(f"Dog: {dog.name}, Breed: {dog.breed}, Kingdom: {dog.kingdom}")
    
    # Polymorphism: Both objects have a 'speak' method, but behave differently
    animals = [dog, cat]
    print("\nPolymorphism:")
    for animal in animals:
        print(f"{animal.name} says {animal.speak()}")
        
    # Encapsulation & access modifiers
    print(f"\nProtected age via getter: {dog.get_age()}")
    
    # Trying to access a private variable __id normally will crash:
    # print(dog.__id) 
    print(f"Bypassing private var via Name Mangling: {dog._Animal__id}")

def magic_methods() -> None:
    """Methods surrounded by double underscores (Dunder methods)."""
    print("\n--- 2. Dunder (Magic) Methods ---")
    
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            
        def __str__(self):
            # Used by print() and str() - For end users
            return f"Point({self.x}, {self.y})"
            
        def __repr__(self):
            # Used for debugging / developers
            return f"Point(x={self.x}, y={self.y})"
            
        def __add__(self, other):
            # Allows adding two Point objects using the '+' operator (Operator Overloading)
            return Point(self.x + other.x, self.y + other.y)
            
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1) # Calls __str__
    
    p3 = p1 + p2 # Calls __add__
    print(f"P1 + P2 = {p3}")

def interview_prep_gotchas() -> None:
    print("\n--- 3. Interview Prep & Gotchas ---")
    print("Question 1: Does Python have true Private variables?")
    print("Answer: No. Python uses 'Name Mangling' (double underscore) to prevent accidental access, ")
    print("but they can still be accessed via _ClassName__variableName. We rely on convention.")
    
    print("\nQuestion 2: What is the difference between @staticmethod and @classmethod?")
    print("- @classmethod takes the class ('cls') as its first parameter instead of 'self'. ")
    print("  Used for factory patterns (e.g. creating objects in a specific way).")
    print("- @staticmethod takes NEITHER 'self' nor 'cls'. It is just a regular function ")
    print("  that happens to live inside a class namespace for organization.")

if __name__ == "__main__":
    print("🌟 Object-Oriented Programming 🌟")
    demonstrate_oop()
    magic_methods()
    interview_prep_gotchas()
