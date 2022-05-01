
"""
이진 탐색
"""

def binary_search_recursive(array, target, start, end):
    if start > end: # 시작점이 끝점을 넘어가는 경우: 리스트 내에 찾고자 하는 데이터가 없는 경우
        return None
    mid = (start + end) // 2

    if array[mid] == target: # 찾고자 하는 데이터가 중간값 일치하는 경우 => correct
        return mid

    elif array[mid] > target: # 찾고자 하는 데이터가 중간값보다 작은 경우 => down
        return binary_search_recursive(array, target, start, mid-1)

    else: # 찾고자 하는 데이터가 중간값보다 큰 경우 => up
        return binary_search_recursive(array, target, mid+1, end)

def binary_search_while(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 찾고자 하는 데이터가 중간값보다 작은 경우 => down
        if array[mid] > target:
            end = mid-1

        # 찾고자 하는 데이터가 중간값보다 큰 경우 => u
        elif array[mid] < target:
            start = mid + 1

        # 찾고자 하는 데이터가 중간값 일치하는 경우 => correct
        else:
            return mid

    # 시작점이 끝점을 넘어가는 경우: 리스트 내에 찾고자 하는 데이터가 없는 경우
    return None

N = 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
recursive = binary_search_recursive(array, N, 0, len(array)-1)
wh = binary_search_while(array, N, 0, len(array)-1)
print(wh)



