def get_unique_list(input_list):
    return list(set(input_list))


sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = get_unique_list(sample_list)
print(unique_list)
