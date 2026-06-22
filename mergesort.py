from matplotlib.pyplot import plt

def copy_value(target_list, target_index, source_list, source_index):
    """Copy"""
    target_list[target_index] = source_list[source_index]


def merge_sort(values):
    """
    Sort a list in-place using the merge sort algorithm.
    """
    if len(values) <= 1:
        return

    middle_index = len(values) // 2
    left_half = values[:middle_index]
    right_half = values[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_index = 0
    right_index = 0
    target_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            copy_value(values, target_index, left_half, left_index)
            left_index += 1
        else:
            copy_value(values, target_index, right_half, right_index)
            right_index += 1

        target_index += 1

    while left_index < len(left_half):
        copy_value(values, target_index, left_half, left_index)
        left_index += 1
        target_index += 1

    while right_index < len(right_half):
        copy_value(values, target_index, right_half, right_index)
        right_index += 1
        target_index += 1

def plot_values(values, title):
    """Plot the values of a list."""
    x_values = range(len(values))
    plt.plot(x_values, values)
    plt.title(title)
    plt.show()


def main():
    """Run a small example"""
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plot_values(my_list, "Before sorting")
    merge_sort(my_list)
    plot_values(my_list, "After sorting")


if __name__ == "__main__":
    main()