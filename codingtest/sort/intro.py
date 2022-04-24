array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array2 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

'''
선택 정렬
리스트의 원소를 순회하면서, 가장 작은 원소를 맨 앞으로 배치하는 정렬방법
O(N) = N^2  
'''
def selection_sort(arr):

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)): # 가장 작은 데이터를 찾기 위한 반복문
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

'''
삽입정렬
원소를 하나씩 확인하면 적절한 위치에 배치하느 정렬방법
버블정렬이라고도 부름 
O(N) = N ~ N^2  
'''
def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0 -1):
            if arr[j] < arr[j -1]: # 버블정렬 조건
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

'''
퀵 정렬
pivot을 기준으로 pivot보다 작은 리스트, 큰 리스트로 나누어 정렬하는 방법
O(N) = N(logN) ~ N^2
'''
def quick_sort1(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while (left <= right):
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    quick_sort1(arr, start, right-1)
    quick_sort1(arr, right+1, end)

    return arr

def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort2(left) + [pivot] + quick_sort2(right)

'''
계수 정렬
각 원소의 크기가 정수 형태인 경우 인덱스 리스트를 활용한 정렬
O(N) = (N + K) (N: 리스트 길이, K 리스트의 최대 값)
'''
def count_sort(arr):
    cnt = [0] * (max(arr) + 1)
    sorted_arr = []
    for i in range(len(arr)):
        cnt[arr[i]] += 1

    for i in range(len(cnt)):
        for j in range(cnt[i]):
            sorted_arr.append(i)

    return sorted_arr

select = selection_sort(array)
insert = insertion_sort(array)
quick1 = quick_sort1(array, 0, len(array)-1)
quick2= quick_sort2(array)
count= count_sort(array2)
print(select)
print(insert)
print(quick1)
print(quick2)
print(count)

