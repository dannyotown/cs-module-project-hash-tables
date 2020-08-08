class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'key:{self.key}, value:{self.value}, next: {self.next}'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hashtable = [None] * capacity
        self.added_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hashtable)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.added_items // self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        # find the start of the linked list using the index
        # search through the linked list
        # if the key already exists in the linked list
        # replace the value
        # else
        # add new hashtable entry to the node of linked list
        hashed_key = self.hash_index(key)
        index = self.hashtable[hashed_key]
        if self.hashtable[hashed_key] == None:
            self.hashtable[hashed_key] = HashTableEntry(key, value)
            self.added_items += 1
            return self.hashtable[hashed_key].value
        else:
            start_index = self.hashtable[hashed_key]
            while start_index.next is not None:
                if start_index.key == key:
                    start_index.value = value
                    return start_index.value
                start_index = start_index.next
            old_index = index
            new_entry = HashTableEntry(key, value)
            new_entry.next = old_index
            self.hashtable[hashed_key] = new_entry
            self.added_items += 1
            return self.hashtable[hashed_key].value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        # hash the key
        # search through the linked list for the matching key
        # delete that node
        # return value of the delete node or None
        hash_val = self.hash_index(key)
        if self.hashtable[hash_val] is None:
            return None
        else:
            node = self.hashtable[hash_val]
            prev = None
            while node is not None:
                if node.key == key:
                    if prev is None:
                        self.hashtable[hash_val] = None
                        self.added_items -= 1
                        return self.hashtable[hash_val]
                    prev.next = node.next
                    self.added_items -= 1
                    return node.value
                prev = node
                node = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # get the linked list at the computed index
        # search through the linked list for the key
        # compare keys until you find the right one
        # if it exists, return the value
        # else return None
        index = self.hashtable[self.hash_index(key)]
        if index == None:
            return None
        else:
            start_index = self.hashtable[self.hash_index(key)]
            while start_index != None:
                if start_index.key == key:
                    return start_index.value
                start_index = start_index.next
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # Make a new array thats DOUBLE the current size
        # go through each linked list in the array
        # go through each item and rehash it
        # insert the items into their new locations
        old_arr = self.hashtable
        self.hashtable = [None] * new_capacity
        for i in range(0, len(old_arr)):
            if old_arr[i] is not None:
                node = old_arr[i]
                while node is not None:
                    self.put(node.key, node.value)
                    node = node.next

    def shrink(self):
        # same as resize but reduce array by half
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    return_value = ht.get("key-0")
    print(return_value)
    # print(ht.get('line_1'))
    # print(ht.get('line_2'))
    # print(ht.get('line_3'))
    # print(ht.get('line_4'))
    # print(ht.get('line_5'))
    # print(ht.get('line_6'))
    # print(ht.get('line_7'))
    # print(ht.get('line_8'))
    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))
