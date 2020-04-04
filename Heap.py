# coding: utf-8

import numpy as np


class Heap(object):

    def __init__(self, k, array=[]):
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
            array = index * self.child + child_num
        array = array[array <= (len(self.tree) - 1)]
        return array

    def __sift_up(self, index, parent_index):
        while self.tree[index] < self.tree[parent_index]:
            self.tree[index], self.tree[parent_index] = self.tree[parent_index], self.tree[index]
            index = parent_index
            parent_index = self.get_parent_index(index)

    def __sift_down(self, index):
        children_index = self.get_child_by_parent(index, child_num='all')
        min_child_val = min(self.tree[children_index[0]:children_index[-1] + 1])
        min_child_index = self.tree.index(min_child_val)
        while self.tree[index] > self.tree[min_child_index]:
            self.tree[index], self.tree[min_child_index] = self.tree[min_child_index], self.tree[index]
            index = min_child_index
            children_index = self.get_child_by_parent(index, child_num='all')
            if children_index.size != 0:
                min_child_val = min(self.tree[children_index[0]:children_index[-1] + 1])
                min_child_index = self.tree.index(min_child)

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

    def print_tree(self):
        print(self.tree)
