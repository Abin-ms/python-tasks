# 41
def student(name, city):
    print(name, city)

student(name="Abin", city="Kochi")


# 42
def employee(name, department):
    print(name, department)

employee(name="Rahul", department="IT")


# 43
def course(name, duration):
    print(name, duration)

course(name="Python", duration="3 months")


# 44
def person(name, city, age):
    print(name, city, age)

person(name="Abin", city="Kochi", age=22)


# 45
def college(name, course, city):
    print(name, course, city)

college(name="MIT", course="B.Tech CSE", city="Kayamkulam")


# 46
def teacher(name, subject):
    print(name, subject)

teacher(name="Anu", subject="Python")


# 47
def company(name, location):
    print(name, location)

company(name="Google", location="Bangalore")


# 48
def book(title, author):
    print(title, author)

book(title="Wings of Fire", author="A.P.J. Abdul Kalam")


# 49
def movie(name, language):
    print(name, language)

movie(name="Drishyam", language="Malayalam")


# 50
def laptop(brand, model):
    print(brand, model)

laptop(brand="Dell", model="Inspiron")


# 51
def address(city, state):
    print(city, state)

address(city="Kochi", state="Kerala")


# 52
def job(role, company):
    print(role, company)

job(role="Developer", company="Google")


# 53
def food(name, type):
    print(name, type)

food(name="Pizza", type="Fast Food")


# 54
def profile(name, city, course):
    print(name, city, course)

profile(name="Abin", city="Kochi", course="B.Tech CSE")


# 55
def student(name, course, city):
    print(name, course, city)

student(city="Kochi", name="Abin", course="B.Tech CSE")


# 56
def employee(name, department, city):
    print(name, department, city)

employee(city="Kochi", department="IT", name="Rahul")


# 57
def teacher(name, subject, city):
    print(name, subject, city)

teacher(name="Anu", city="Kochi", subject="Mathematics")


# 58
def company(name, location, department):
    print(name, location, department)

company(department="IT", name="Google", location="Bangalore")


# 59
def details(name, age, city, course):
    print(name, age, city, course)

details(name="Abin", age=22, city="Kochi", course="B.Tech CSE")


# 60
def student_details(name, course, college, city):
    print(name, course, college, city)

student_details(city="Kochi", college="MIT", name="Abin", course="B.Tech CSE")


# 61
def students(*names):
    print(*names)

students("Abin", "Rahul", "Arun")


# 62
def cities(*cities):
    print(*cities)

cities("Kochi", "Kollam", "Trivandrum")


# 63
def courses(*courses):
    print(*courses)

courses("Python", "Java", "C++")


# 64
def subjects(*subjects):
    print(*subjects)

subjects("Maths", "Physics", "Computer Science")


# 65
def friends(*names):
    print(*names)

friends("Abin", "Rahul", "Arun")


# 66
def colors(*colors):
    print(*colors)

colors("Red", "Blue", "Green")


# 67
def foods(*foods):
    print(*foods)

foods("Pizza", "Burger", "Pasta")


# 68
def languages(*languages):
    print(*languages)

languages("Python", "Java", "C")


# 69
def companies(*companies):
    print(*companies)

companies("Google", "Microsoft", "Amazon")


# 70
def books(*books):
    print(*books)

books("Wings of Fire", "Harry Potter", "The Alchemist")


# 71
def movies(*movies):
    print(*movies)

movies("Drishyam", "Interstellar", "Inception")


# 72
def teachers(*teachers):
    print(*teachers)

teachers("Anu", "Ravi", "Suresh")


# 73
def employees(*employees):
    print(*employees)

employees("Abin", "Rahul", "Arun")


# 74
def sports(*sports):
    print(*sports)

sports("Football", "Cricket", "Tennis")


# 75
def fruits(*fruits):
    print(*fruits)

fruits("Apple", "Mango", "Banana")


# 76
def devices(*devices):
    print(*devices)

devices("Laptop", "Mobile", "Tablet")


# 77
def places(*places):
    print(*places)

places("Kochi", "Delhi", "Mumbai")


# 78
def animals(*animals):
    print(*animals)

animals("Dog", "Cat", "Elephant")


# 79
def skills(*skills):
    print(*skills)

skills("Python", "Java", "SQL")


# 80
def details(*details):
    print(*details)

details("Abin", 22, "Kochi", "Python")


# 81
def student(**details):
    print(details)

student(name="Abin", age=22, city="Kochi")


# 82
def employee(**details):
    print(details)

employee(name="Rahul", department="IT", salary=30000)


# 83
def person(**details):
    print(details)

person(name="Abin", age=22, city="Kochi")


# 84
def college(**details):
    print(details)

college(name="MIT", course="CSE", city="Kayamkulam")


# 85
def teacher(**details):
    print(details)

teacher(name="Anu", subject="Python", experience=5)


# 86
def company(**details):
    print(details)

company(name="Google", location="Bangalore", department="IT")


# 87
def profile(**details):
    print(details)

profile(name="Abin", city="Kochi", course="CSE")


# 88
def address(**details):
    print(details)

address(city="Kochi", state="Kerala", pincode=682001)


# 89
def course(**details):
    print(details)

course(name="Python", duration="3 months", fee=5000)


# 90
def book(**details):
    print(details)

book(title="Wings of Fire", author="A.P.J. Abdul Kalam", price=300)


# 91
def movie(**details):
    print(details)

movie(name="Drishyam", language="Malayalam", year=2013)


# 92
def laptop(**details):
    print(details)

laptop(brand="Dell", model="Inspiron", price=50000)


# 93
def job(**details):
    print(details)

job(role="Developer", company="Google", salary=50000)


# 94
def food(**details):
    print(details)

food(name="Pizza", type="Fast Food", price=250)


# 95
def hospital(**details):
    print(details)

hospital(name="City Hospital", location="Kochi", beds=100)


# 96
def school(**details):
    print(details)

school(name="ABC School", city="Kochi", students=500)


# 97
def project(**details):
    print(details)

project(name="CIMS", language="Python", framework="Flask")


# 98
def product(**details):
    print(details)

product(name="Laptop", brand="Dell", price=50000)


# 99
def customer(**details):
    print(details)

customer(name="Abin", city="Kochi", phone=9876543210)