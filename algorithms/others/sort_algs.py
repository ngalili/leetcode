
def bubble_sort(nums):
    """ iterates over a list, comparing elements in pairs and swapping them
    until the larger elements bubble up to the end of the list and the 
    smaller elements stay at the bottom
    """

    n = len(nums)
    # # traditional way
    # # time complexity: always runs O(n^2) even if array is sorted
    # for i in range(n - 1):
    #     for j in range(n - i - 1):
    #         if nums[i] > nums[j + 1]:
    #             nums[i], nums[j + 1] = nums[j + 1], nums[i]
    
    # optimized algorithm
    # # time complexity:
    # Worst and average case: O(n*n) = O(n^2) when array is reverse sorted
    # Best case: O(1) when array is already sorted
    is_swapped = True
    while is_swapped is True:
        is_swapped = False
        for i in range(n- 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_swapped = True

def selection_sort(nums):
    """ selects the smallest element from an unsorted list 
    in each iteration and places that element at the beginning of
    the unsorted list
    """
    
    n = len(nums)
    # Time complexity: O(n^2)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

def insertion_sort(nums):
    """ places an unsorted element at its suitable place 
    in each iteration
    """

    n = len(nums)
    # Time complexity: O(n^2)
    for i in range(1, n):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

def heap_sort(nums):
    """ Popular sorting algorithm: converts the unsorted segment 
    of the list to a Heap data structure, so than we can efficiently
    determine the largest element
    Max-Heap tree uses Swap, Remove Heapify
    """
    # Time complexity: O(nlog(n))
    def heapify(nums, heap_size, root_index):
        # Assume the index of the largest element is the root index
        largest = root_index
        left_child = (2*root_index) + 1
        right_child = (2*root_index) + 2

        # If the left child of the root is a valid index, and the element is greater
        # than the current largest element, then update the largest element
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        # Do the same for the right child of the root
        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child
        
        # If the largest element is no longer the root element, swap them
        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            # Heapify the new root element to ensure it's the largest
            heapify(nums, heap_size, largest)
    
    n = len(nums)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    
    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def merge_sort(nums):
    """ divides the input array into 2 halves, calls itself 
    for the 2 halves and then merges the 2 sorted halves
    """
    # Time complexity: O(nlog(n))
    def merge(left_lst, right_lst):
        sorted_lst = []
        left_lst_index = right_lst_index = 0

        left_lst_len, right_lst_len = len(left_lst), len(right_lst)
        
        for _ in range(left_lst_len + right_lst_len):
            if left_lst_index < left_lst_len and right_lst_index < right_lst_len:
                # check which value from the start of each list is smaller
                if left_lst[left_lst_index] <= right_lst[right_lst_index]:
                    sorted_lst.append(left_lst[left_lst_index])
                    left_lst_index += 1
                else:
                    sorted_lst.append(right_lst[right_lst_index])
                    right_lst_index += 1
            # reaches the end of left list
            elif left_lst_index == left_lst_len:
                sorted_lst.append(right_lst[right_lst_index])
                right_lst_index += 1 
            # reaches the end of right list
            elif right_lst_index == right_lst_len:
                sorted_lst.append(left_lst[left_lst_index])
                left_lst_index += 1
        
        return sorted_lst
    
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2

    left_lst = merge_sort(nums[:mid])
    right_lst = merge_sort(nums[mid:])

    return merge(left_lst, right_lst)

def quick_sort(nums):
    """ pick one value of the list that will be in its sorted place is called a pivot.
    All elements smaller than the pivot are moved to its left. 
    All larger elements are moved to its right.
    """
    # Time complexity: O(nlog(n)): Very fast 
    def partition(nums, low, high):
        pivot = nums[(low + high) // 2]
        i, j = low - 1, high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1
            j -= 1
            while nums[j] > pivot:
                j -= 1
            
            if i >= j:
                return j
            
            nums[i], nums[j] = nums[j], nums[i]
    
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    
    _quick_sort(nums, 0, len(nums) - 1)

# Python's Built-in Sort Functions using Timsort
def timSort(arr):
    MIN_MERGE = 32
    def calcMinRun(n):
        r = 0
        while n >= MIN_MERGE:
            r |= n & 1
            n >>= 1 # /2 
        return n + r
    # sorts arr from left index to right index which is of size atmost RUN
    def insertionSort(arr, left, right):
        for i in range(left + 1, right + 1):
            j = i
            while j > left and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
    
    # merges the sorted runs
    def merge (arr, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in range(0, len1):
            left.append(arr[l + i])
        for i in range(0, len2):
            right.append(arr[m + 1 + i])

        i, j, k = 0, 0, l
        # after comparing, merge those 2 arrays 
        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # copy remaining elements of left 
        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1
        
        # copy remaining elements of right
        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1

    n = len(arr)
    minRun = calcMinRun(n)
    
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n -1)
        insertionSort(arr, start, end)
    
    size = minRun
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2*size - 1), (n - 1))
            merge(arr, left, mid, right)
    size = 2*size







