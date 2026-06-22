import matplotlib.pyplot as plt

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

def plot(values, title):

    my_list = values
    original_list = my_list.copy()

    merge_sort(my_list)

    x = range(len(my_list))

    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    axes[0].bar(x, original_list)
    axes[0].set_title(title)
    axes[0].set_ylabel("Value")
    axes[0].grid(axis="y", linestyle="--", alpha=0.5)

    axes[1].bar(x, my_list)
    axes[1].set_title(title)
    axes[1].set_xlabel("Index")
    axes[1].set_ylabel("Value")
    axes[1].set_xticks(x)
    axes[1].grid(axis="y", linestyle="--", alpha=0.5)

    fig.suptitle("Merge Sort Visualization")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    plot(my_list, "Merge Sort")
