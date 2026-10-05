# Course Management System

A simple Course Management System built using Python OOP concepts.

## OOP Concepts

This project demonstrates:

- Inheritance
- Encapsulation
- Polymorphism
- Abstraction
- Instance methods
- Static methods
- Class methods

## Classes

### User
Parent abstract class.

### Student
Child class of User.

### Mentor
Child class of User.

### Course
Stores course information.

### Enrollment
Connects students with courses.

## Architecture

```text
             User
            /    \
           /      \
      Student    Mentor
           \      /
            \    /
            Course
              |
          Enrollment