import heapq
from collections import Counter
class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def get_codes(root, code, codes):
    if root.left is None and root.right is None:
        codes[root.ch] = code
        return
    get_codes(root.left, code + "0", codes)
    get_codes(root.right, code + "1", codes)
    
def decode(root, data):
    ans = ""
    cur = root
    for b in data:
        cur = cur.left if b == '0' else cur.right
        if cur.left is None and cur.right is None:
            ans += cur.ch
            cur = root
    return ans
text = input("Enter a string: ")
freq = Counter(text)

heap = []
for ch, f in freq.items():
    heapq.heappush(heap, Node(ch, f))

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    p = Node(None, a.freq + b.freq)
    p.left = a
    p.right = b
    heapq.heappush(heap, p)

root = heap[0]
codes = {}
get_codes(root, "", codes)

encoded = ""
for ch in text:
    encoded += codes[ch]

decoded = decode(root, encoded)

print("\nOriginal String is:", text)
print("Encoded String is:", encoded)
print("Decoded String is:", decoded)
