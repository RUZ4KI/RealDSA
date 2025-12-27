class Heap:
    def __init__(self, arr=None):
        if arr is None:
            self.data = []
        else:
            self.data = arr
            self.heapify()

    def heapify(self):
        n = len(self.data)

        for i in range((n // 2) - 1, -1, -1):
            self._bubble_down(i)

    def _bubble_down(self, i):
        n = len(self.data)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == i:
                break

            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest


arr = [20, 5, 15, 22, 9, 13]
heap = Heap(arr)
print(heap.data)