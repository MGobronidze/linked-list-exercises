# Python3 program to remove duplicate
# nodes from a sorted linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def remove_duplicates(head):
    curr = head

    # Traverse the list
    while curr and curr.next:
      
        # Check if next value is the same as curr
        if curr.data == curr.next.data:
            next_next = curr.next.next
            curr.next = next_next
        else:
            curr = curr.next

    return head


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

    head = remove_duplicates(head)

    print("Linked list after duplicate removal:")
    print_list(head)
