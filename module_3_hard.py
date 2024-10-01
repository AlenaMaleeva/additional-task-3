sum_digit = 0
def calculate_structure_sum (data_structure):
    global sum_digit
    if isinstance(data_structure, int):
        sum_digit += data_structure
    elif isinstance(data_structure, str):
        sum_digit += len(data_structure)
    elif isinstance(data_structure, (list, set, tuple)):
        for i in data_structure:
            calculate_structure_sum(i)
    elif isinstance(data_structure,dict):
        for key, value in data_structure.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)

    return sum_digit

data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
result = calculate_structure_sum(data_structure)
print(result)