def find_largest(numbers):
    if not numbers:
        return []
    else:
        numbers.sort()
        index_of_largest = len(numbers) - 1
        return numbers[index_of_largest]