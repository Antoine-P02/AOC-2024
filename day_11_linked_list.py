class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.end = getEnd()
    
    def add(self, new):
        self.value = new
        newNode = solve(new)
        self.next = newNode

    
    def getEnd(self):
        current = self
        while current.next is not None:
            current = current.next
        return current.value
            
            
    def solve(value):
        if (stoneValue == 0):
            return [1]

        elif (len(str(stoneValue)) % 2 == 0):

            stoneString = str(stoneValue)

            mid = len(stoneString) // 2
            stoneValue = stoneString[:mid]
            newStone = stoneString[mid:]
            return [int(stoneValue), int(newStone)]

        else:
            return [value * 2024]