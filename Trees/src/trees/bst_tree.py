from typing import Optional, Callable, TypeVar, Generic

from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')


class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x: x) -> None:
        """
        You must have at least one member named root

        :param root: The root node of the tree if there is one.
        If you are provided a root node don't forget to count how many nodes are in it
        :param key: The function to be applied to a node's value for comparison purposes.
        It serves the same role as the key function in the min, max, and sorted builtin
        functions
        """
        self.root = None
        self.key = None

        ...

    @property
    def height(self) -> int:
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:

        """
        if self.root:
            return self.root.Height()
        elif self.root is None:
            return -1
        else:
            return 0


    def __len__(self) -> int:
        """
        :return: the number of nodes in the tree
        """
        if self.root:
            return self.root.__len__()
        else:
            return 0

    def add_value(self, value: T) -> None:
        """
        Add value to this BST
        :param value:
        :return:
        """
        ...
        if self.root:
            return self.root.add_value(value)
        else:
            self.root = BSTNode(value)
            return True

    def get_node(self, value: K) -> BSTNode[T]:
        """
        Get the node with the specified value
        :param value:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        if self.root:
            return self.root.get_node(value)
        elif self.root is None:
            raise  MissingValueError
        else:
            return False



    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        if self.root:
            return self.root.get_max_node()
        elif self.root is None:
            raise EmptyTreeError
        else:
            return 0

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        if self.root:
            return self.root.get_min_node()
        elif self.root is None:
            raise EmptyTreeError
        else:
            return 0

    def remove_value(self, value: T) -> None:
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """

        if self.root:
            self.root.remove_value(value)
        elif self.root is None:
            raise MissingValueError


    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       all((BST(c1) == BST(c2) for c1, c2 in zip(self.root, other.root)))
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)
