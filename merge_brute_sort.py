# Python program to merge two sorted linked list by storing
# them into array
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def merge_sorted_list(a, b):
    # List to temporarily store the values
    vec = []
    # Pushing the values of a linked list
    while a:
        vec.append(a.data)
        a = a.next
    # Pushing the values of b linked list
    while b:
        vec.append(b.data)
        b = b.next
    # Sorting the list
    vec.sort()
    # Creating a new list with sorted values
    temp = Node(-1)
    head = temp
    for value in vec:
        temp.next = Node(value)
        temp = temp.next
    head = head.next
    # Returning the resultant linked list
    return head

# Driver code

# Create a hard-coded linked list:
# 2 -> 4 -> 8 -> 9
a = Node(2)
a.next = Node(4)
a.next.next = Node(8)
a.next.next.next = Node(9)

# Create another hard-coded linked list:
# 1 -> 3 -> 8 -> 10
b = Node(1)
b.next = Node(3)
b.next.next = Node(8)
b.next.next.next = Node(10)

merged_list = merge_sorted_list(a, b)

temp = merged_list
print("Merged Sorted Link List is:")
while temp:
    print(temp.data, end=" ")
    temp = temp.next
