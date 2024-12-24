# Recursive Python program to reverse a linked list

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Given the head of a list, reverse the list and return the
# head of reversed list
def reverse_list(head):
    if head is None or head.next is None:
        return head

    # reverse the rest of linked list and put the 
    # first element at the end
    rest = reverse_list(head.next)

    # Make the current head as last node of remaining linked list
    head.next.next = head

    # Update next of current head to NULL
    head.next = None

    # Return the reversed linked list
    return rest

def print_list(node):
    while node is not None:
        print(f" {node.data}", end='')
        node = node.next
    print()


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked List:", end='')
    print_list(head)

    head = reverse_list(head)

    print("\nReversed Linked List:", end='')
    print_list(head)
