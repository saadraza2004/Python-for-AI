# def get_ice():
#     print("your ice cream !")
# get_ice()

# val1= input("enter first number:")
# val2 = input("enter second number:")
# add = int(val1) + float(val2)
# print("the sum is : ", add)

# course = "python programming"
# print(course.upper())
# print(course.replace("python", "nothing"))
# print("python" in course)

# x = 10
#  x = x + 2  #instead we can use
# x += 2

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         average = sum(self.marks) / len(self.marks)
#         return average

#     def grade(self):
#         average = self.average()
#         if average >= 80:
#             return "A"
#         elif average >= 70:
#             return "C"
#         else:
#             return "F"
      
# New = Student("John", [85, 90, 78])
# New_average = New.average()
# New_grade = New.grade()
# # New_name = New.name()
# print(New_average, "and has grade", New_gra

def top_items(n, *sales):
    # top_items = [2, ("pen", 50), ("book", 300), ("bag", 120)]
    sorted_sales = sorted(sales, key=lambda x: x[1], reverse=True)

print(top_items(2, ("pen", 50), ("book", 300), ("bag", 120)))
print(top_items(5, ("pen", 50), ("book", 300)))
print(top_items(3))