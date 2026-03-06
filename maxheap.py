class MaxHeap:
    def __init__(self):
        self._heapList = []
    def d(self):
        if not self._heapList:
            print("(empty)")
            return

        level = 0
        index = 0
        n = len(self._heapList)

        while index < n:
            level_size = 2 ** level
            level_nodes = self._heapList[index:index + level_size]

            print(" ".join(str(x) for x in level_nodes))

            index += level_size
            level += 1
    def add(self, entry):
        entryIndex = len(self._heapList)
        parentIndex = (entryIndex - 1) // 2
        self._heapList.append(entry)
        while entryIndex > 0 and self._heapList[entryIndex] > self._heapList[parentIndex]:
            #quick tuple sway
            self._heapList[entryIndex], self._heapList[parentIndex] = self._heapList[parentIndex], self._heapList[entryIndex]
            entryIndex = parentIndex
            parentIndex = (entryIndex-1) // 2
    def getHighest(self):
        return self._heapList[0]
    def count(self):
        return len(self._heapList)
    def pop(self):
        """Removes the top"""
        self._heapList[0] = self._heapList[-1]
        i = 0
        size = len(self._heapList)
        while True:
            left = 2*i + 1
            right = 2*i + 2
            largest = i
            #left < size for bound checks, trying not to write to non-existant places
            #we keep going through the "largest" until we 
            #put the back down 
            if left < size and self._heapList[left] > self._heapList[largest]:
                largest = left
            if right < size and self._heapList[right] > self._heapList[largest]:
                largest = right
            if largest == i:
                break 
            self._heapList[i], self._heapList[largest] = self._heapList[largest], self._heapList[i]
            i = largest
