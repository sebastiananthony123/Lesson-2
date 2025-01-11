data = {1:"Python" ,
        2: "Java" ,
        3:"Java script" ,
        5: "C++"}

print(data[2])

print(data.get(2))
print(data.get(4))

print(data.get(4, "Not Found"))

print("-------------")

print(dict)

keys = ["Alex" , "John" , "Louis" , "DJ"]
values = ["Java", "Python" , "Anaconda" , "SQL"]

dict = dict(zip(keys, values))

print(dict)
print(dict["Alex"])

dict["Monika"] = "C Sharp"

print(dict)
print(dict["Monika"])

print("-------------")

del dict["DJ"]

print(dict)

cars =  {
  "brand": "BMW",
  "model": "M4 Convertible",
  "year": 2021
}

print(cars)

cars.popitem
print(cars)

print("----------------")

students_scores = {
    "Alice": 84,
    "Carl": 68,
    "DJ": 93,
    "Bob": 90,
    "Alex": 77
}

def find_highest_score(students_scores):
    highest_score_student = max(students_scores, key=students_scores.get)
    highest_score = students_scores[highest_score_student]
    return highest_score_student, highest_score

student, score = find_highest_score(students_scores)
print(f"The student with the highest score is... {student}! with a score of {score}.")

print("-----------")

inventory = {'apples': 10, 'oranges': 5, 'bananas': 8}

inventory['oranges'] += 3
inventory['grapes'] = 12

print(inventory)

print("------------------")

contact_info = {'John': 'john@example,com', 'Emma': 'emma@example.com'}

if 'John' in contact_info:
    print(f"John's contact is available: {contact_info['John']}")
else:
    print("John's contact not found")