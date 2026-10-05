from models import Student, Mentor, Course, Enrollment, User


# Create Student
student = Student(
    "Arif",
    "arif@gmail.com"
)

# Create Mentor
mentor = Mentor(
    "Rahulam",
    "rahul@gmail.com"
)

# Create Course
course = Course(
    101,
    "Welcome to Python",
    mentor
)

# Create Enrollment
enrollment = Enrollment(
    student,
    course
)


print("===== STUDENT =====")

student.show_info()

print()


print("===== MENTOR =====")

mentor.show_info()

print()


print("===== COURSE =====")

course.show_course()

print()


print("===== ENROLLMENT =====")

enrollment.show_enrollment()

print()


print("===== ACTIONS =====")

student.enroll(course)

mentor.teach(course)

print()


print("===== STATIC METHOD =====")

print(User.platform_name())

print()


print("===== CLASS METHOD =====")

guest = Student.create_guest()

guest.show_info()