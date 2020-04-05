# coding: utf-8
import numpy as np


class Heap(object):

    def __init__(self, k, array=None):
        self.tree = []
        self.child = k
        self.array = array
        if array:
            for i in array:
                self.add(i)

    def get_parent_index(self, index):
        if index == 0:
            return 0
        else:
            return (index - 1) // self.child

    def get_child_by_parent(self, index, child_num):
        if child_num is 'all':
            array = index * self.child + np.array(range(1, self.child + 1))
        else:
            array = np.array(index * self.child + child_num)
        array = array[array <= (len(self.tree) - 1)]
        return array.tolist()

    def __sift_up(self, index, parent_index):
        while self.tree[index] < self.tree[parent_index]:
            self.tree[index], self.tree[parent_index] = self.tree[parent_index], self.tree[index]
            index = parent_index
            parent_index = self.get_parent_index(index)

    def __index_of_min(self, index):
        min_child_index = -10
        children_index = self.get_child_by_parent(index, child_num='all')
        if children_index:
            min_child_val = min(self.tree[children_index[0]:children_index[-1] + 1])
            min_child_index = self.tree.index(min_child_val, children_index[0])
        return min_child_index

    def __sift_down(self, index):
        if index >= len(self.tree):
            raise SystemExit('Вы ввели не существующий индекс')
        min_child_index = self.__index_of_min(index)
        if min_child_index != -10:
            while self.tree[index] > self.tree[min_child_index]:
                self.tree[index], self.tree[min_child_index] = self.tree[min_child_index], self.tree[index]
                index = min_child_index
                min_child_index = self.__index_of_min(index)
                if min_child_index != -10:
                    break

    def add(self, value):
        if not self.tree:
            self.tree.append(value)
        else:
            self.tree.append(value)
            index = len(self.tree) - 1
            parent_index = self.get_parent_index(index)
            if self.tree[index] < self.tree[parent_index]:
                self.__sift_up(index, parent_index)

    def get_min(self):
        return self.tree[0]

    def extract_min(self):
        minimum = self.tree[0]
        self.tree[0] = self.tree[-1]
        self.tree.pop(-1)
        self.__sift_down(0)
        return minimum

    def __decrease_key(self, index):
        if index >= len(self.tree):
            raise SystemExit('Вы ввели не существующий индекс')
        self.tree[index] = float('-inf')
        parent_index = self.get_parent_index(index)
        self.__sift_up(index, parent_index)

    def delete_by_index(self, index):
        self.__decrease_key(index=index)
        self.extract_min()

    def print_tree(self):
        print(self.tree)
