class HashTable():
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max
    def __getitem__(self,key):
        h=self.get_hash(key)
        return(self.arr[h])
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
                break
        if not found:
            self.arr[h].append((key,value))

hash=HashTable()
hash["brishti"]="brishh"
hash["inchara"]="inchy"
hash["udith"]="hoodie"
hash["pranit"]="smollpp"
hash["kaveri"]="kavya"
hash["shreyas"]="shrey"
print(hash.arr)