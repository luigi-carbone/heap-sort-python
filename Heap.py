import numpy as np
import time


class Heap:
    def __init__(self, heap_size, min, max):
        self.heap_size = heap_size
        self.heap_vector=np.random.uniform(min, max, size=heap_size)


    @staticmethod
    def parent(i):
        return int((i - 1)/2)

    @staticmethod
    def left(i):
        return (2 * i) + 1


    @staticmethod
    def right(i):
        return (2 * i) + 2




    def max_heapify(self,i,hs):
        heap_size = hs
        l = self.left(i)
        r = self.right(i)
        largest = i
        if ((l < heap_size) and (self.heap_vector[l] > self.heap_vector[i])):
            largest = l
        if ((r < heap_size) and (self.heap_vector[r] > self.heap_vector[largest])):
            largest = r
        if (largest != i):
            x = self.heap_vector[i]
            self.heap_vector[i] = self.heap_vector[largest]
            self.heap_vector[largest] = x
            self.max_heapify(largest, hs)




    def build_max_heap(self):
        heap_size=self.heap_size
        for i in reversed(range(0, int((heap_size)/2))):
            self.max_heapify(i, heap_size)



    def heap_sort(self):
        heap_size = self.heap_size
        self.build_max_heap()
        for i in reversed(range(1, heap_size)):
            x = self.heap_vector[0]
            self.heap_vector[0] = self.heap_vector[i]
            self.heap_vector[i] = x
            heap_size -= 1
            self.max_heapify(0, heap_size)

    def print_heap_vector(self):
        print(self.heap_vector)



if __name__ == '__main__':

    h1 = Heap(100000, 0, 1000)

    h1.print_heap_vector()
    start = time.time()
    h1.heap_sort()
    end = time.time()
    h1.print_heap_vector()
    print(f'Running time for vector sorting: {end - start}')



