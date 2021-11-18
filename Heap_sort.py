#!/usr/bin/python3
"""
  Define heap data structure
"""
# define heap data tree
# heap_data = {}

# Define heap function
def heap_fixer(u_list):
    w_list = u_list
    number_of_parents = int((len(w_list)-1)/2 if len(w_list) % 2 else len(w_list)/2)
    if number_of_parents <= 0: return w_list    # No children are remain
    pi = 0;  c1i = 1;  c2i = 2

    for pi in range(0, number_of_parents):
        p = w_list[pi]
        c1 = w_list[c1i]
        c2 = w_list[c2i] if c2i < len(w_list)  else None    # Assume there is no 99 in the list
        # Check which value deserve to be a parent and place it
        if c2 == None:
             if c1 < p:
                p = c1
                c1 = w_list[pi]
        else:
            if c1 < c2:
                if c1 < p:
                    p = c1
                    c1 = w_list[pi]
            else:
                if c2 < p:
                    p = c2
                    c2 = w_list[pi]
            
        # Put new parent and child in the working array
        w_list[pi] = p
        w_list[c1i] = c1
        if c2 == None:
            pass
        else:
            w_list[c2i] = c2

        # Increment the index pointers for parent and children
        c1i += 2;  c2i += 2

    print("Heap after correction: ", w_list)
    return w_list


def main():
    unsorted_list = [2, 5, 1, 3, 4, 7, 10, 20, 18, 19, 15, 11, 23, 13, 9, 21, 22, 29]
    print("Unsorted list: ", unsorted_list)
    heap_tree = heap_fixer(unsorted_list)
    sorted_list = []

    while(len(heap_tree) > 1):
        # Pick the top value and append into resultant list
        sorted_list.append( heap_tree[0] )

        # Take the lowest generation's children and place on top
        heap_tree[0] = heap_tree.pop()
        print(heap_tree)

        # Call the heap_fixer to correct the broken heap
        heap_tree = heap_fixer(heap_tree)
    
    # Take the last two elements and append on last in the resultant list
    sorted_list.append(heap_tree[0])
    # sorted_list.append(heap_tree[1])

    print("sorted list: ", sorted_list)


main()

