 Exercises: Basic OOP Principles
================================

Problems for exercises and homework for the [“Python Fundamentals” course \@SoftUni](https://softuni.bg/opencourses/python-fundamentals-course).  

Please submit your solutions (source code) of all below described problems at: *https://judge.softuni.bg/Contests/Practice/Index/1556fbclid=IwAR0EIDrhz7MeS3Wu6ISGvcEuy8pRsVIpnakB3BXuBvcxFHpXYUuMn0rTbk\#0*


1.Person
------
You are asked to model an application for storing data about people. You should be able to have a person and a child.   
The child derives from the person. Your task is to model the application. The only constraints are:  
-   People should **not** be able to have a **negative age**
-   Children should **not** be able to have an age **more than 15**.
-   **Person** – represents the base class by which all of the others are implemented
-   **Child** - represents a class, which derives from **Person.**

### Note
Your class’s names **MUST** be the same as the names shown above!!!

### Step 1 – Define the fields
Define a **field** for each property the class should have (e.g. **Name**, **Age**)

### Step 2 - Define the Properties of a Person
Define the **Name** and **Age** properties of a Person.

### Step 3 - Define a Constructor
Define a constructor that accepts **name and age**.

### Step 4 - Perform Validations
After you have created a **field** for each property (e.g. **Name** and **Age**), the next step is to **perform validations** for each one.   
The **getter should return the corresponding field’s value** and the **setter should validate** the input data before setting it. 
Do this for each property.

### Constraints
-   If the age of a person is negative – exception’s message is: **"Age must be positive!"**
-   If the age of a child is bigger than 15 – exception’s message is: **"Child's age must be less than 15!"**
-   If the name of a child or a person is no longer than three symbols – exception’s message is: **"Name's length should not be less than 3 symbols!"**

### Step 5 - Override \__str__()
"Name: {self.name}, Age: {self.age}"    
And voila! If everything is correct, we can now create **Person objects** and display information about them.

### Step 6 – Create a Child
Create a **Child** class that inherits **Person** and has the same constructor definition. However, do not copy the code from the Person class - **reuse the Person class’s constructor**.    
There is **no need** to rewrite the Name and Age properties since **Child** inherits **Person** and by default has them.

### Step 7 – Validate the Child’s setter  


2.Book Shop
---------
You are working in a library. You are sick of writing descriptions for books by hand, so you wish to use the computer to speed up the process. 
The task is simple - your program should have two classes – one for the ordinary books – **Book**, and another for the special ones – **GoldenEditionBook**. 
So let’s get started! We need two classes:  
-   **Book** - represents a book that holds **title**, **author** and **price**. A book should offer **information** about itself in the format shown in the output below.
-   **GoldenEditionBook** - represents a special book that holds the same properties as any **Book**, but its **price** is always **30% higher**.

### Constraints
-   If the author’s second name is starting with a digit – the exception’s message is: **"Author not valid!"**
-   If the title’s length is less than 3 symbols – the exception’s message is: **"Title not valid!"**
-   If the price is zero or it is negative – the exception’s message is: **"Price not valid!"**
-   Price must be formatted to **two** symbols after the decimal separator

### Examples
| **Input**                                   | **Output**                                                           |
|---------------------------------------------|----------------------------------------------------------------------|
| Ivo 4ndonov                                 | Author not valid!                                                    |
| Under Cover                                 |                                                                      |
| 9999999999999999999                         |                                                                      |
| **Input**                                   | **Output**                                                           |
| Petur Ivanov                                | Type: Book                                                           |
| Life of Pesho                               | Title: Life of Pesho                                                 |
| 20                                          | Author: Petur Ivanov                                                 |
|                                             | Price: 20.00                                                         |
|                                             |                                                                      |
|                                             | Type: GoldenEditionBook                                              |
|                                             | Title: Life of Pesho                                                 |
|                                             | Author: Petur Ivanov                                                 |
|                                             | Price: 26.00                                                         |

### Step 1 - Create a Book Class
Create a new empty class and name it **Book**.

### Step 2 - Define the Properties of a Book
Define the **Title**, **Author** and **Price** properties of a Book.

### Step 3 - Define a Constructor
Define a constructor that accepts **author, title** and **price** arguments.

### Step 4 - Perform Validations
Create a **field** for each property (**Price**, **Title** and **Author**) and **perform validations** for each one.   
The **getter should return the corresponding field** and the **setter should validate** the input data before setting it.     
Do this for every property.

### Step 5 - Override \__str__()
All of the classes in Python inherit the **object** class and therefore have all its **public** members.   
Let's **override** (change) the **str()** method’s behavior again according to our **Book** class’s data.  
And voila! If everything is correct, we can now create **Book objects** and display information about them.  

### Step 6 – Create a GoldenEditionBook
Create a **GoldenEditionBook** class that inherits **Book** and has the same constructor definition.   
However, do not copy the code from the Book class - **reuse the Book class constructor**.  
There is **no need** to rewrite the Price, Title and Author properties since **GoldenEditionBook** inherits **Book** and by default has them.

### Step 7 - Override the Price Property
Golden edition books should return a **30%** higher **price** than the original price.   
In order for the getter to return a different value, we need to override the Price property.  


3.Mankind
-------
Your task is to model an application. It is very simple. The mandatory models of our application are 3: **Human**, **Worker** and **Student**.

The parent class – Human should have **first name** and **last name**. Every student has a **faculty number**. Every worker has a **week salary** and **work hours per day**.   
The class should be able to calculate the money he earns by an hour. You can see the constraints below.

### Input
On the first input line, you will be given info about a single student - a name and faculty number.  
On the second input line, you will be given info about a single worker - first name, last name, salary and working hours.

### Output
You should print the info about the student first, followed by a single blank line and after that the info about the worker in the given formats:

- Print the student info in the following format:  
**First Name: {student's first name}**  
**Last Name: {student's last name}**  
**Faculty number: {student's faculty number}**    

- Print the worker info in the following format:  
**First Name: {worker's first name}**  
**Last Name: {worker's second name}**  
**Week Salary: {worker's salary}**  
**Hours per day: {worker's working hours}**  
**Salary per hour: {worker's salary per hour}**  

Print exactly two digits after every double value's decimal separator (e.g. 10.00).   
Consider the workweek from Monday to Friday. A faculty number should be consisted only of digits and letters.

### Constraints
| **Parameter**    | **Constraint**                     | **Exception Message**                                     |
|------------------|------------------------------------|-----------------------------------------------------------|
| Human first name | Should start with a capital letter | "Expected upper case letter! Argument: firstName"         |
| Human first name | Should be more than 3 symbols      | "Expected length at least 4 symbols! Argument: firstName" |
| Human last name  | Should start with a capital letter | "Expected upper case letter! Argument: lastName"          |
| Human last name  | Should be more than 2 symbols      | "Expected length at least 3 symbols! Argument: lastName " |
| Faculty number   | Should be in range [5..10] symbols | "Invalid faculty number!"                                 |
| Week salary      | Should be more than 10             | "Expected value mismatch! Argument: weekSalary"           |
| Working hours    | Should be in the range [1..12]     | "Expected value mismatch! Argument: workHoursPerDay"      |

### Example
| **Input**                                 | **Output**                                                            |
|-------------------------------------------|-----------------------------------------------------------------------|
| Ivan Ivanov 08                            | Invalid faculty number!                                               | 
| Pesho Kirov 1590 10                       |                                                                       |
| **Input**                                 | **Output**                                                            |
| Stefo Mk321 0812111                       | First Name: Stefo                                                     |
| Ivcho Ivancov 1590 10                     | Last Name: Mk321                                                      |
|                                           | Faculty number: 0812111                                               |
|                                           |                                                                       |
|                                           | First Name: Ivcho                                                     |
|                                           | Last Name: Ivancov                                                    |
|                                           | Week Salary: 1590.00                                                  |
|                                           | Hours per day: 10.00                                                  |
|                                           | Salary per hour: 31.80                                                |  


4.Animals
-------
Create a hierarchy of **Animals**. Your program should have three different animals – **Dog**, **Frog** and **Cat**.    
Deeper in the hierarchy you should have two additional classes – **Kitten** and **Tomcat**. **Kittens are female and Tomcats are male!**  

All types of animals should be able to produce some kind of sound (**ProduceSound()**). For example, the dog should be able to bark.  

Your task is to model the hierarchy and test its functionality. Create an animal of each kind and make them all produce sound.  

You will be given some lines of input. Each two lines will represent an animal.   
On the first line will be the type of animal and on the second – the name, the age and the gender.   
When the command "**Beast!**" is given, stop the input and print all the animals in the format shown below.

### Output
-   Print the information for each animal on three lines. On the first line, print: "\<**AnimalType**\>"
-   On the second line print: "\<**Name**\> \<**Age**\> \<**Gender**\>"
-   On the third line print the sounds it produces: "\<**ProduceSound()**\>"

### Constraints
-   Each **Animal** should have a **name**, an **age** and a **gender**
-   **All** input values should **not be blank** (e.g. name, age and so on…)
-   If you receive an input for the **gender** of a **Tomcat** or a **Kitten**ignore it but **create** the animal
  -   If the input is invalid for one of the properties, throw an exception with message: "**Invalid input!**"
-   Each animal should have the functionality to **ProduceSound()**
-   Here is the type of sound each animal should produce:
    -   **Dog: "Woof!"**
    -   **Cat: "Meow meow"**
    -   **Frog: "Ribbit"**
    -   **Kittens: "Meow"**
    -   **Tomcat: "MEOW"**

### Examples
| **Input**                                     | **Output**                                         |
|-----------------------------------------------|----------------------------------------------------|
| Cat                                           | Cat                                                |
| Tom 12 Male                                   | Tom 12 Male                                        |
| Dog                                           | Meow Meow                                          |
| Sharo 132 Male                                | Dog                                                |
| Beast!                                        | Sharo 132 Male                                     |
|                                               | Woof!                                              |
| **Input**                                     | **Output**                                         |
| Frog                                          | Frog                                               |
| Kermit 12 Male                                | Kermit 12 Male                                     |
| Beast!                                        | Ribbit                                             |
| **Input**                                     | **Output**                                         |
| Frog                                          | Invalid input!                                     |
| Sashko -2 Male                                | Frog                                               |
| Frog                                          | Sashko 2 Male                                      |
| Sashko 2 Male                                 | Ribbit                                             | 
| Beast!                                        |                                                    |
