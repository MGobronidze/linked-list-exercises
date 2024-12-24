# Python3 program to remove duplicate
# nodes from a sorted linked list

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def remove_duplicates(head):

    # Base case: if the list is empty, return
    if head is None:
        return

    # Check if the next node exists
    if head.next is not None:
      
        # If current node has duplicate data with the next node
        if head.data == head.next.data:
            head.next = head.next.next
            remove_duplicates(head)
        else:

             # Continue with next node
            remove_duplicates(head.next)


def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":

    # Create a sorted linked list:
    # 11->11->11->13->13->20
    head = Node(11)
    head.next = Node(11)
    head.next.next = Node(11)
    head.next.next.next = Node(13)
    head.next.next.next.next = Node(13)
    head.next.next.next.next.next = Node(20)

    print("Linked list before duplicate removal:")
    print_list(head)

    remove_duplicates(head)

    print("Linked list after duplicate removal:")
    print_list(head)
