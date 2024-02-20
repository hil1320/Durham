def get_valid_input():
    while True:
        try:
            input_str = input("Enter elements separated by space: ")
            elements = [int(element) for element in input_str.split()]
            if not all(isinstance(element, int) for element in elements):
                raise ValueError("Invalid input. Please enter only numeric values separated by space.")
            return elements
        except ValueError as ve:
            print(f"Error: {ve}")

def find_minimum(elements):
    if not elements:
        return None  # Return None for an empty list
    min_element = elements[0]
    for element in elements:
        if element < min_element:
            min_element = element
    return min_element

def main():
    try:
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        # Test Case 01: A very short list (of inputs) with the size of 1, 2, or 3 elements
        print("Test Case 01: A very short list")
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")

        # Test Case 02: An empty list i.e., of size 0
        print("\nTest Case 02: An empty list")
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")

        # Test Case 03: A list where the minimum element is the first or last element
        print("\nTest Case 03: Minimum element is the first or last element")
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")

        # Test Case 04: A list where the minimum element is negative
        print("\nTest Case 04: Minimum element is negative")
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")

        # Test Case 05: A list where all elements are negative
        print("\nTest Case 05: All elements are negative")
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")

        # Test Case 06: A list where some elements are real numbers
        print("\nTest Case 06: Some elements are real numbers")
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")

        # Test Case 07: A list where some elements are alphabetic characters and special characters
        print("\nTest Case 07: Some elements are alphabetic characters and special characters")
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")

        # Test Case 08: A list with duplicate elements
        print("\nTest Case 08: A list with duplicate elements")
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")

        # Test Case 09: A list where one element has a value greater than the maximum permissible limit of an int
        print("\nTest Case 09: One element has a value greater than the maximum permissible limit of an int")
        elements = get_valid_input()
        minimum = find_minimum(elements)
        if minimum is not None:
            print("The smallest element is:", minimum)
        else:
            print("List is empty.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

