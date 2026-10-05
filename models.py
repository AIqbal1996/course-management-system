from abc import ABC, abstractmethod


# =========================
# Parent Class: User
# =========================

class User(ABC):

    def __init__(self, name, email):
        self.name = name
        self._email = email   # Encapsulation

    # Encapsulation using property
    @property
    def email(self):
        return self._email

    # Abstract method
    @abstractmethod
    def get_role(self):
        pass

    # Instance method
    def show_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Role:", self.get_role())

    # Static method
    @staticmethod
    def platform_name():
        return "Online Learning Platform"

    # Class method
    @classmethod
    def create_guest(cls):
        return cls("Guest", "guest@example.com")


# =========================
# Student Class
# =========================

class Student(User):

    def get_role(self):
        return "Student"

    def enroll(self, course):
        print(self.name, "enrolled in", course.title)


# =========================
# Mentor Class
# =========================

class Mentor(User):

    def get_role(self):
        return "Mentor"

    def teach(self, course):
        print(self.name, "is teaching", course.title)


# =========================
# Course Class
# =========================

class Course:

    def __init__(self, course_id, title, mentor):
        self.course_id = course_id
        self.title = title
        self.mentor = mentor

    def show_course(self):
        print("Course ID:", self.course_id)
        print("Course:", self.title)
        print("Mentor:", self.mentor.name)


# =========================
# Enrollment Class
# =========================

class Enrollment:

    def __init__(self, student, course):
        self.student = student
        self.course = course

    def show_enrollment(self):
        print(
            self.student.name,
            "is enrolled in",
            self.course.title
        )