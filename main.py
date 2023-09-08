# main.py
from math_operations import add, subtract, multiply
from string_operations import concatenate_strings, capitalize_string
from list_operations import find_max, find_min
from file_operations import read_file, write_file

# Example usage
if __name__ == "__main__":
    a = 10
    b = 5

    result_add = add(a, b)
    result_subtract = subtract(a, b)
    result_multiply = multiply(a, b)

    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")
    print(f"Multiplication: {result_multiply}")

    str1 = "Hello, "
    str2 = "World!"
    
    concatenated_str = concatenate_strings(str1, str2)
    capitalized_str = capitalize_string(concatenated_str)

    print(f"Concatenated String: {concatenated_str}")
    print(f"Capitalized String: {capitalized_str}")

    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    max_number = find_max(numbers)
    min_number = find_min(numbers)

    print(f"Max Number: {max_number}")
    print(f"Min Number: {min_number}")

    filename = "example.txt"
    content = "This is a sample text."

    write_file(filename, content)
    read_content = read_file(filename)

    print(f"Read from file: {read_content}")
