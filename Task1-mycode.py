def sort_list_of_dicts_manual(data, key):
    list_length = len(data)  

    # Outer loop: go through the entire list multiple times
    for pass_number in range(list_length):
        # Inner loop: compare each pair of adjacent items
        for current_index in range(0, list_length - pass_number - 1):
            current_item = data[current_index]
            next_item = data[current_index + 1]

            # If the current item is greater than the next, swap them
            if current_item[key] > next_item[key]:
                data[current_index], data[current_index + 1] = next_item, current_item

    return data

people = [
    {"name": "Fred", "age": 18},
    {"name": "Kaloki", "age": 22},
    {"name": "Charles", "age": 20},
    {"name": "Mutinda", "age": 19}
]

sorted_people = sort_list_of_dicts_manual(people, "age")
for person in sorted_people:
    print(person)