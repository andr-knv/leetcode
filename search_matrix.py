def search_matrix(matrix: list[list[int]], target: int) -> bool:
    for row in matrix:
        if target >= row[0] and target <= row[-1]:
            left, right = 0, len(row)-1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
    return False

print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))