A = [4, 3, 2 ,7, 8, 1, 5, 6]

def merge_sort(A):
    if len(A) <=1:
        return A
    middle = int(len(A) / 2)
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merger(left, right)
def merger(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result
print(A)
print(merge_sort(A))