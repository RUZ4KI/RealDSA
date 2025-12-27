class Heap:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        i = len(self.data) - 1

        while i > 0:
            parent = (i - 1) // 2
            if self.data[parent] > self.data[i]:
                self.data[parent], self.data[i] = self.data[i], self.data[parent]
                i = parent
            else:
                break

    def delete_min(self):
        if len(self.data) == 0:
            return None
        
        min_val = self.data[0]

        last_val = self.data.pop()
        if len(self.data) > 0:
            self.data[0] = last_val

        i = 0
        length = len(self.data)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < length and self.data[left] < self.data[smallest]:
                smallest = left
            if right < length and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == i:
                break

            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest

        return min_val
