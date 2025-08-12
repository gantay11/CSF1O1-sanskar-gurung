name = "John Doe"
age = 25
hight = 1.75
is_student = True

person_info = {
    "name": name,
    "age": age,
    "hight": hight,
    "is_student": is_student
}
print(person_info)
person_info["favorite_color"] = "blue"
print(person_info)
try:
    print(person_info)["weight"]
except keyError as e:
    print(f"error: {e}")