#!/usr/bin/python3
"""This module defines a class Node that defines a node of a singly linked list
and a class SinglyLinkedList that defines a singly linked list"""


class Node:
    """This class represents a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """This method initializes a node with a given data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This property returns the current data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """This property setter sets the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This property returns the current next_node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This property setter sets the next_node of the node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly linked list"""

    def __init__(self):
        """This method initializes a singly linked list with a head"""
        self.__head = None

    def sorted_insert(self, value):
        """This method inserts a new Node into the correct sorted position in the list"""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __repr__(self):
        """This method returns the printable representation of the list"""
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]

