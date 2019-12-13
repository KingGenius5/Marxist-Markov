#!python

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
        TODO: Running time: O(???) Why and under what conditions?
        I originally thought that this was O(n^2) since it was a for loop
        nested in a for loop but as Ryan Hopkins pointed out (shout out to him) and Alan
        further elaborated, the values being run in the loops need to have the same length.
        N has to be the same size as the other N hence making it N^2. In this case, we have a
        runtime of O(b*L), the number of buckets by the load factor or just O(n).
        """
        # Collect all keys in each bucket

        #this seems like it is O(n^2) because it looks like it is a for loop nested in a for loop looking quadratic but they are different lengths
        #n usually is for methods that are of the same length so when they are nested they are quadratic
        #this is different, as it is buckets * load factor, b*l which is equal to O(n)
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        Run time of O(n) as you need to loop through all the buckets (b) and the
        items in the buckets (L)
        """
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)

        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        Run time of O(n) since it has to loop through all buckets and then add all
        items in the buckets.
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?
        Run time of O(n) for the number of times you access each item in each bucket
        and count it as well.
        """
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        items_count = 0
        for bucket in self.buckets:
            for item in bucket.items():
                items_count +=1

        return items_count


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?
        Run time of O(l) focusing on the load factor since it finds the index of the bucket
        and key in the linkedlist.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket = self.buckets[hash(key) % len(self.buckets)]
        for item_key, value in bucket.items():
                if item_key == key:
                    return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        Run time of O(l) focusing on the load factor since it finds the index of the bucket
        and key in the linkedlist.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[hash(key) % len(self.buckets)]

        for item_key, value in bucket.items():
            if item_key == key:
                return value

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?
        Run time of O(l) focusing on the load factor since it finds the index of the bucket
        and key in the linkedlist.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        bucket = self.buckets[hash(key) % len(self.buckets)]
        item = bucket.find(lambda item: item[0] == key)

        if item is not None:
            bucket.replace(item, (key, value))
        else:
            bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        Run time of O(l) because it finds the index of the bucket and finds the key in the linkedlist.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[hash(key) % len(self.buckets)]
        item = bucket.find(lambda item: item[0] == key)

        if item is not None:
            bucket.delete(item)
        else:
            raise KeyError(f'Key not found: {key}')


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
