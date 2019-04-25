#!python

# pytest linkedlist_test.py::LinkedListTest::test_length_after_append
#  pytest linkedlist_test.py::LinkedListTest::test_find


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        # O(1) it's constant
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""

        # o(n) for all n nodes in the list because we have to interate all n nodes and count 1
        # Loop through all nodes and count one for each

        # start with the head of the node
        # end the loop at the tail
        # create a variable named count
        # increment the count variable every time it loop through a node
        # return the count variable when the loop is finished

        # counter variable that increment by 1 every time the loop goes through it
        count = 0

        # keep track of the head node
        keep_track = self.head

        while (keep_track):
            count += 1
            # keep_track is passed to the next node
            keep_track = keep_track.next
        # return count
        return count
    # start at self.head
    # increment by 1
    # point to the next node
    # keep looping until there are no more nodes being passed.

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        "O(1) only change the tail node"
        #  Create new node to hold given item

        # create a new node
        new_node = Node(item)

        current_value = self.tail  # store current value
        #  Append node after tail, if it exists
        self.tail = new_node

        # landa function is anynomous function

        # check if current value is not empty
        if current_value is not None:
            # the next value is the value passed to new node
            current_value.next = new_node
        if self.head is None:
            # add the first item to the head
            self.head = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        "O(1) because we are only change the first node neaver loop through all nodes"
        # Create new node to hold given item
        new_node = Node(item)

        # Prepend node before head, if it exists
        # check if the head is not empty
        if self.head is not None:
            # if it's not empty set the next item passed as the head
            new_node.next = self.head
            self.head = new_node

        # if the head of the linked list is empty set the new node to head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # beast case o(1) if first item
        # worst case O(n) if item is near tail of list or dose not exist
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        # how can I acces the linkned list?
        # once I can access the linkend list how can I access the data inside the node?
        # how can I check if quality matches the data inside the node?
        # once i find out if quality matches the data how can I return it?

        # # check if head node is value
        # if quality(self.head.data):
        #     return self.head.data
        # # check if tail value is value
        # if quality(self.tail.data):
        #     return self.tail.data

        # create new node instance to access the linkend list
        current_node = self.head

        # start the while loop at the head of the linkend list
        while(current_node is not None):
            # if data found return data
            if quality(current_node.data):
                return current_node.data
                # once data is found stop the loop
            # if data is not found move on to the next node
            current_node = current_node.next
        # if data does not exist then return none
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?

        TODO: Worst case running time: O(???) Why and under what conditions?"""

        # best case O(1) if the item that needs to be deleted is the head
        # Worst case O(n) if the item does not exist or at the tail
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        # item has been removed
        remove = False
        # track the previous node
        previous_node = None
        # keep track of current node
        current_node = self.head

        # loop through all the nodes
        while (not remove and current_node is not None):
            # check if item is in linkend list
            if (current_node.data == item):
                # check if previous node is empty
                if(previous_node is not None):
                    # previous node will be set to current node
                    previous_node.next = current_node.next

                else:
                    # update head node
                    self.head = current_node.next
                if(current_node.next is None):
                    # update the tail
                    self.tail = previous_node
                #item is removed
                remove = True

            previous_node = current_node
            current_node = current_node.next
        if not remove:
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
