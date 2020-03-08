from typing import Generic, Iterable, TypeVar, Optional


T = TypeVar('T')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: gert the right child
    """
    def __init__(self,
                 value: T, left: Optional["BSTNode[T]"] = None,
                 right: Optional["BSTNode[T]"] = None,
                 children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        """
        :param value: The value to store in the node
        :param children: optional children
        :param parent: an optional parent node
        """
        self.value = value
        self.left = left
        self.right = right
        self.children = children
        self.parent = parent
        self.leftChild = None
        self.rightChild = None
    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """

        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    def add_value(value: T, root: BSTNode[T]) -> BSTNode[T]:
        if root is None:  # empty node
            raise NotFoundError()
        elif value == root.value:  # match
            return root
        elif value < root.value:  # search left
            return add_value(value, root.left)
        else:  # search right
            return add_value(value, root.right)


    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(),self.rightChild.getHeight())

        elif self.leftChild:
            return 1 + self.leftChild.getHeight()

        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1

    def get_node(value: T, root: BSTNode[T]) -> BSTNode[T]:
        if root is None:  # empty node
            raise NotFoundError()
        elif value == root.value:  # match
            return root
        elif value < root.value:  # search left
            return get_node(value, root.left)
        else:  # search right
            return get_node(value, root.right)

    def __len__(self):
        if self.leftChild and self.rightChild:
            return 1 + self.leftChild.__len__() + self.rightChild.__len__()
        elif self.leftChild:
            return  1 + self.leftChild.__len__()
        elif self.rightChild:
            return 1 + self.rightChild.__len__()
        else:
            return 1

    def get_max_node(root: BSTNode[T]) -> BSTNode[T]:

        if root.right is None:
            raise NotImplementedError

        elif root.right is None:
            return root

        else:
            return get_max_node(root.right)

    def get_min_node(root: BSTNode[T]) -> BSTNode[T]:

        if root.right is None:
            raise NotImplementedError

        elif root.left is None:
            return root

        else:
            return get_min_node(root.left)

    def remove_value(value: T, root: Node[T]):
        node_to_remove = remove_value(value, root)
        if node_to_remove.has_no_children():
            node_to_remove.parent.remove_child(node_to_remove)
        elif node_to_remove.num_children == 1:
            node_to_remove.parent.replace_child(node_to_remove,
                                                node_to_remove.left if node_to_remove.left is not None else node_to_remove.right)
        else:
            successor = remove_value(node_to_remove.left)
            remove_value(successor.value, successor.parent)
            node_to_remove.parent.replace_child(node_to_remove, successor)