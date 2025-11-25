a) Method Overriding vs Method Overloading in Python(With Example)
 1. Method Overriding
Definition:
Method overriding occurs when a child (sub) class defines a method with the same name and parameters as a method in its parent class, thereby replacing the parent’s version.
Purpose:
Used to implement runtime polymorphism and allow subclasses to change or extend the behavior of inherited methods.
Key Points:
Happens across inheritance.
Same method name, same parameters.
The child's method replaces the parent's method.
Decision happens at runtime.
 2. Method Overloading
Definition:
Method overloading means having multiple methods with the same name but different parameter lists.
 Python does not support traditional compile-time method overloading.
If you define two methods with the same name, the last one overrides the previous ones.
<img width="1911" height="1017" alt="Screenshot 2025-11-25 221548" src="https://github.com/user-attachments/assets/943170da-839c-4e09-94bb-1e5e5d1fe401" />
<img width="1919" height="1012" alt="Screenshot 2025-11-25 221240" src="https://github.com/user-attachments/assets/85a0bc4e-f80c-4fc7-827f-e4955b4b90ee" />
b) Role and Types of Constructors in Python (With Example)
 Role of Constructors in Python
1.Initialize Object Attributes
Constructors set the initial values of data members when an object is created.
2.Allocate Necessary Resources
They can open files, allocate memory, initialize connections, etc.
3.Ensure Objects Start in a Valid State
Constructors guarantee that required attributes exist and are initialized.
4.Improve Code Readability and Maintenance
Grouping initialization logic inside __init__ avoids duplication.
Types of Constructors in Python:
1. Default Constructor
A constructor that does not accept any parameters except self.
<img width="1917" height="1019" alt="Screenshot 2025-11-25 222638" src="https://github.com/user-attachments/assets/cbabb638-2cbf-4275-9538-72e68fcaf15b" />
2. Parameterized Constructor
A constructor that accepts parameters to initialize object attributes with custom values.
<img width="1919" height="1019" alt="Screenshot 2025-11-25 222958" src="https://github.com/user-attachments/assets/709df898-a28d-4cab-bdd2-6ff756044a92" />



