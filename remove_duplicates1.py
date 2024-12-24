# Python3 program to remove duplicate
# nodes from a sorted linked list using Hashset

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def remove_duplicates(head):

  # Set to track unique node values
    st = set()

    # Initialize pointers for traversing
    # the original list and building the 
    # new list without duplicates
    temp = head
    new_head = None
    tail = None

    # Traverse the original list
    while temp:

        # Check if the current node's data
        # is not in the set
        if temp.data not in st:

            # Create a new node for the unique data
            new_node = Node(temp.data)

            # If new_head is None, this is the 
            #first unique node
            if new_head is None:
                new_head = new_node
                tail = new_head
            else:
                # Append the new node to the end
                #of the new list
                tail.next = new_node
                tail = new_node

            # Mark this data as encountered
            st.add(temp.data)

        # Move to the next node in the original list
        temp = temp.next

    # Return the head of the new list with
    #duplicates removed
    return new_head


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