class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # checking to see if the capacity that is given is equal to or greater than the Minimum 
        # Capacity that we set above.
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY

        # creating a table that has exact amount of indexes depending on the capacity.
        self.table = [HashTableEntry(None, None)] * self.capacity
        self.count = 0
        

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity

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
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)

        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        self.count += 1
        # using the DJB2 hashing algorithm to insert the value as a key for the index in the hash table.
        index = self.hash_index(key)
        current = self.table[index]

        # if theres nothing in the slot we are inserting it here
        if self.table[index] is None:
            self.table[index] = HashTableEntry(key,value)
        # going through the index's slots to find and open one 
        else:
            # while loop to traverse through the table
            while current.next is not None:
                # checking to see if the index key already exists with our key
                if current.key == key:
                    # overwrite value with new value 
                    current.value = value
                    # print(current.value)
                # if key is not the same, current is now updated to the next index in line
                current = current.next
            current.next = HashTableEntry(key, value)
        #print(self.count)
                
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.count -= 1

        index = self.hash_index(key)
        current = self.table[index]
        # checking to see if theres anything in the index location
        if self.table[index]:
            # while loop to traverse through indexes
            while current is not None:
                # checking to see if current key matches with given key
                if current.key == key:
                    # sets the current value as none (deleted)
                    current.value = None
                    #print(current.value)
                current = current.next
        else:
            return None

        # checking to see if the index we are looking at has a key or if its not none
        # if self.table[index] is not None:
        #     self.table[index] = None
        # else:
        #     print("Key not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # get the index of the key 
        index = self.hash_index(key)

        current = self.table[index]
        # searching through linked list to find key

        # checks current key and if it matches it will return the value
        if current.key == key:
            return current.value
        
        # while loop to traverse through linked list so that it will keep checking each index in the linked 
        # list and returns the value once the key is found or returns NONE if not found
        while current.next is not None:
            current = current.next

            if current.key == key:
                return current.value
        
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # duplicates current table to use later
        old_table = self.table.copy()
        #print(f"This is the OLD TABLE: {old_table}")

        # setting the capacity to given new capacity
        self.capacity = new_capacity

        # rehashing table to have new capacity included
        self.table = [HashTableEntry(None, None)] * self.capacity
        #print(f"This is the NEW TABLE: {self.table}")
        
        # using the PUT method to insert the data we already had from old_table
        for i in range(len(old_table)):
            current = old_table[i]

            while current is not None:
                if current.key is not None:
                    self.put(current.key, current.value)
                current = current.next




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
