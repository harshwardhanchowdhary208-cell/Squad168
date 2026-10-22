# Question: Find the common elements between two sorted arrays.
# Add your solution here.
def find_common_elements(arr1, arr2):
    i, j = 0, 0
    common = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            # Avoid adding duplicate values if required
            if not common or common[-1] != arr1[i]:
                common.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return common


# Example Usage:
arr1 = [1, 2, 4, 5, 6, 8]
arr2 = [2, 3, 5, 7, 8, 9]

print(
    find_common_elements(arr1, arr2)
)  # Output: [2, 5, 8]