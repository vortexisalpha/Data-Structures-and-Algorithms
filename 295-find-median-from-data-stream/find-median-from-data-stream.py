from bisect import insort
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        size = len(self.arr)
        print(size)
        mid = (size-1)//2
        if size % 2 == 0:
            return (self.arr[mid] + self.arr[mid+1])/2
        else:
            return self.arr[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()