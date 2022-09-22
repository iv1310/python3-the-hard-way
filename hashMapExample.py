class HashTable:

    # Create an empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_table()

    def create_table(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def setVal(self, key, val):
        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # Check if the bucket has same key as the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted, update the key value. Otherwise append the new key-value pair to the bucket.
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key,val))

    # Return searched value with specific key
    def getVal(self, key):
        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

            # If the bucket has same key as the key being searched,
            # Return the value found
            # Otherwise indicate there was no record found
            if found_key:
                return record_val
            else:
                return "No record found."

    # Remove a value with specific key
    def delVal(self, key):
        # Get the index from the key using ash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = HashTable(50)

# Insert some values
hash_table.setVal('gfg@example.com', 'some value')
print(hash_table)
print()

hash_table.setVal('portal@example.com', 'some other value')
print(hash_table)
print()

# Search/access a record with key
print(hash_table.getVal('portal@example.com'))
print()

# Delete or remove a value
hash_table.delVal('portal@example.com')
print(hash_table)
