def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

def plot(values, title):

    my_list = values
    original_list = my_list.copy()

    mergeSort(my_list)

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
