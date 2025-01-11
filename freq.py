test_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2,
}

value_to_check = 1

frequency = list(test_dict.values()).count(value_to_check)

print(f"The value {value_to_check} appears {frequency} time(s) in the  dictionary")