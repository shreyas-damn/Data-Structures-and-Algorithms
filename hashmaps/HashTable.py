class HashTable():
    def __init__(self):
        self.max=10
        self.arr=[[]for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=1
        return h%self.max
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=False
        for idx,element in self.arr[h]:
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
                break
        if not found:
            self.arr[h].append((key,value))
    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
    def __delitem__(self,key):
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]

hash=HashTable()
hash["brishti"]="brishh"
hash["inchara"]="inchy"
hash["udith"]="hoodie"
hash["pranit"]="smollpp"
hash["kaveri"]="kavya"
hash["shreyas"]="shrey"
hash["aditya"]="adi"

print(hash.__getitem__("pranit"))
print(hash.arr)
hash.__delitem__("shreyas")
print(hash.arr)