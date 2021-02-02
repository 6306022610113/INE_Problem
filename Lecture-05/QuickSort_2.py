def quickSort(data_list):
    quickSortHlp(data_list, 0, len(data_list) -1)

def quickSrtHlp(data_list, first, last):
    if first < last:

        splitpoint = parttition(data_list, first, last)

        quickSortHlp(data_list, first, splitpoint - 1)
        quickSortHlp(data_list, splitpoint + 1, last)

def parttition(data_list, first, last):
    pivotvalue = data_list[first]

    leftmark = first + 1
    rightmark = last
    done = False
    while not done:

        while left <= rightmark and data_list[leftmark]