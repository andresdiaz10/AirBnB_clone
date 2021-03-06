# 0x00. AirBnB clone - The console
---

##  Background.

##### Write a command interpreter to manage your AirBnB objects.

This will help you to create your first web application: AirBnB clone.

- Create an initial class called BaseModel. This will take care of the initialization, serialization and deserialization of your next instances.

- Create the classes used for AirBnB, which will be inherited from BaseModel:

    - Amenity.
    - City.
    - Place.
    - Review.
    - State.
    - User.

- Create the project's abstracted storage engine:
    - File storage.

- Create the unit tests to validate all your classes and your file storage.

---

### Resources.

**Read or warch:**

- [cmd module](https://docs.python.org/3.4/library/cmd.html)

- [Packages concept page](https://intranet.hbtn.io/concepts/66)

- [uuid module](https://docs.python.org/3.4/library/uuid.html)

- [datetime](https://docs.python.org/3.4/library/datetime.html)

- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)

- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)

- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

### General.

- How to create a Python package.
- How to create a command interpreter in Python using the `cmd` module.
- What is Unit testing and how to implement it in a large project.
- How to serialize and deserialize a Class.
- How to write and read a JSON file.
- How to manage `datetime`.
- What is an `UUID`.
- What is `*args` and how to use it.
- What is `**kwargs` and how to use it.
- How to handle named arguments in a function.

### Execution.

Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: ```$ echo "python3 -m unittest discover tests" | bash```

[HBNB- Project overview.](https://youtu.be/E12Xc3H2xqo)

### Authors.

- [Andres Zapata.](https://github.com/andresdiaz10)
- [Laura Alejandra C.](https://github.com/LauraAlejandra2021)
- [Mayii Cadavid.](https://github.com/mayii527)