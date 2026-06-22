from collections import Counter


def find_single_element(numbers):
    """
    Finds the only element that occurs exactly once.
    """

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    if len(numbers) == 0:
        raise ValueError("List must not be empty.")

    if len(numbers) % 2 == 0:
        raise ValueError("List length must be odd.")

    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements must be integers.")

    counts = Counter(numbers)

    single_elements = [number for number, count in counts.items() if count == 1]

    if len(single_elements) != 1:
        raise ValueError("There must be exactly one element that occurs once.")

    for number, count in counts.items():
        if number != single_elements[0] and count != 2:
            raise ValueError("All other elements must occur exactly twice.")

    return single_elements[0]