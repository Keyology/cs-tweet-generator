#!python

# use this to run a single method test
# pytest hashtable_test.py::HashTableTest::test_contains
# pytest linkedlist.py::linkedlist_test.py::test_find

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        # O(n) dependent on how many keys you have"
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        # O(n) because youre returning many values that you have"""

        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        # O(n) because youre returning (n) many key value pairs"""
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        #  O(n) count the entire number if key-value pairs within the bucket depending on the length of bucket"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

        counter = 0

        for bucket in self.buckets:  # O(b)
            counter += bucket.length()  # o(l)
        return counter
        # overall 0(b * l)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # O(n) when it has to check over multiple buckets and check their values

        # TODO: Check if key-value entry exists in bucket
        # check out the entry that was returned - is is None
        index = self._bucket_index(key)
        found = False
        key_value = self.buckets[index].find(lambda item: item[0] == key)
        if key_value is not None:
            found = True
        return found

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(n) because it is just getting an item

        # TODO: Find bucket where given key belongs
        # O(1) because you are indexing an array
        buckets = self.buckets[self._bucket_index(key)]
        # TODO: Check if key-value entry exists in bucket
        # o(1) to check if value exsist
        entry = buckets.find(lambda item: item[0] == key)
        # TODO: If found, return value associated with given key
        if entry is not None:  # found o(1)
            return entry[1]  # get the value only at index 1
        # TODO: Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

        # Hint: raise KeyError('Key not found: {}'.format(key))

        # closure is is a function that can access the variable,parameters of the parent function
        #

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(n) it has to check bucket and  key value before it finds value and sets it
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        # gets the bucket index
        bucket = self.buckets[index]
        entry = bucket.find(lambda item: item[0] == key)
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        if (entry is not None):

            bucket.delete(entry)
        new_entry = (key, value)

        # append the bucket
        bucket.append(new_entry)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        bucket = self.buckets[self._bucket_index(key)]  # o(1) find
        key_value = bucket.find(lambda item: item[0] == key)  # O(l)

        if key_value == None:  # O(1)
            # overall O(3 + 2l) --> O(l)
            raise KeyError('Key not found: {}'.format(key))  # O()

        else:

            bucket.delete(key_value)  # O(l)


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
