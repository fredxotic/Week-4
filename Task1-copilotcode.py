def sort_list_of_dicts_ai(data, key):
    return sorted(data, key=lambda x: x[key])

people = [
    {"name": "Fred", "age": 18},
    {"name": "Kaloki", "age": 22},
    {"name": "Charles", "age": 20},
    {"name": "Mutinda", "age": 19}
]

sorted_people = sort_list_of_dicts_ai(people, "age")
for person in sorted_people:
    print(person)