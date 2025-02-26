# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))

#选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))

# 插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))

# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr))

# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))

# 堆排序
import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # 转换成最小堆
    return [heapq.heappop(arr) for _ in range(len(arr))]
arr = [64, 34, 25, 12, 22, 11, 90]
print(heap_sort(arr))

# 希尔排序
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(shell_sort(arr))

# 计数排序
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    count = [0] * (max_val - min_val + 1)
    for num in arr:
        count[num - min_val] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i + min_val] * c)

    return result
arr = [64, 34, 25, 12, 22, 11, 90]
print(counting_sort(arr))

# 基数排序
def radix_sort(arr):
    # 获取最大值的位数
    max_num = max(arr)
    exp = 1  # 从个位开始排序
    while max_num // exp > 0:
        arr = counting_sort_radix(arr, exp)
        exp *= 10
    return arr


def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 根据位数统计出现次数
    for num in arr:
        index = num // exp
        count[index % 10] += 1

    # 累加计数数组
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 排序
    for i in range(n - 1, -1, -1):
        num = arr[i]
        index = num // exp
        output[count[index % 10] - 1] = num
        count[index % 10] -= 1

    return output


# 示例
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))

# 桶排序
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # 创建桶
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    bucket_range = (max_val - min_val) / bucket_count + 1

    buckets = [[] for _ in range(bucket_count)]

    # 将元素分到桶中
    for num in arr:
        index = int((num - min_val) // bucket_range)
        buckets[index].append(num)

    # 对每个桶进行排序
    for i in range(bucket_count):
        buckets[i] = sorted(buckets[i])

    # 合并桶中的元素
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


# 示例
arr = [0.42, 0.32, 0.23, 0.57, 0.92, 0.34, 0.89]
print(bucket_sort(arr))

# TimSort
def tim_sort(arr):
    return sorted(arr)

# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
print(tim_sort(arr))

# 组合排序
def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3  # 步长收缩因子
    sorted_flag = False

    while not sorted_flag:
        gap = int(gap // shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False

    return arr


# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
print(comb_sort(arr))