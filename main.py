class data:
    def __init__(self, value, index, count=0):
        self.value = value
        self.index = index
        self.count = count

def sortByFrequencyAndIndex(arr):
    if arr is None or len(arr) < 2:
        return
    
    hm = {}
    #for each array element, insert into the dictionary
    #its frequency and index of its first occurrence in the array

    for i in range(len(arr)):
        hm.setdefault(arr[i], data(arr[i], i)).count += 1

    values = [*hm.values()]

    '''
            sort the values based on a custom comparator
            1. if the two elements have different frequencies, then the one which has more frequency should come first.
            2. if the two elements have the same frequencies, then the one which has less index should come first.
    '''
    values.sort(key=lambda x: (-x.count, x.index))

    k = 0
    for item in values:
        for j in range(item.count):
            arr[k] = item.value
            k += 1

if __name__ == '__main__':
    arr=[]
    arr_s = int(input("enter array size: "))
    for i in range(arr_s):
        x = int(input("Enter element: "))
        arr.append(x)
    print("Original:", arr)
    sortByFrequencyAndIndex(arr)
    print("Sorted:",arr)

    print("Original:", arr)
    sortByFrequencyAndIndex(arr)
    print("Sorted:", arr)