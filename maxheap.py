#################
# KU EECS268 L9 #
# MAXHEAP       #
# Functional max#
# heap by yours #
# truly lucas   #
#################

#last lab of the year means that this code has gotta have
# 10x comments so i can live that 10x developer mindset

class MaxHeap:
    def __init__(self):
        """Initializes the maxheap"""
        self._heapList = []
        self._itemCount = 0
    def d(self):
        """Little display function nothing fancy"""
        if not self._heapList: #edge case
            print("(empty)")
            return
        #track levels and index
        level = 0
        index = 0
        n = len(self._heapList)

        while index < n:
            level_size = 2 ** level #i didn't know you could do ** for pow
            level_nodes = self._heapList[index:index + level_size] #set the level nodes
            #from the index to the end of the index on our current level size

            print(" ".join(str(x) for x in level_nodes))#join display them
            #tho since patient doesn't have a str magic method looks ugly
            index += level_size #increment all
            level += 1

    def add(self, entry):
        """Adds to the maxheap using array black magic"""
        entryIndex = len(self._heapList) #so every time we insert we set it at the bottom
        parentIndex = (entryIndex - 1) // 2 #get our daddy
        self._heapList.append(entry) #add to the heap
        #okay remember in main.py when i warned i didn't understand the best
        #implementation well this is it 
        #i actually use looping instead of recursion to upheap, which, unless i'm crazy
        #wrong doesn't actually make that much of a difference 
        #but still! unorthodox programming tricks with lucas frias below
        while entryIndex > 0 and self._heapList[entryIndex] > self._heapList[parentIndex]:
            #while loop goes while we're not the top dog AND our dad isn't greater
            #if either case happens then we fail the boolean statement and finish 
            #upheaping
            #quick tuple swap (weird)
            self._heapList[entryIndex], self._heapList[parentIndex] = self._heapList[parentIndex], self._heapList[entryIndex]
            #now we reshift the parent and entry indexes 
            entryIndex = parentIndex
            parentIndex = (entryIndex-1) // 2
        #now we increment our item count
        self._itemCount += 1
    def getHighest(self):
        return self._heapList[0]
    def count(self):
        return self._itemCount
    def pop(self):
        """Removes the top in a really confusing way"""
        #here's lucas trying to comment code i wrote three months ago
        #at 7 am in the morning. likttle comments here what a stupid guy
        self._heapList[0] = self._heapList[-1] #okay so get the lowest thing and put
        #that guy on top
        i = 0
        size = len(self._heapList) #why do we need this?
        while True:
            #okay get the left and right descending i guess
            left = 2*i + 1
            right = 2*i + 2 #opposite of -1 //2 and -2 //2 
            largest = i #dear past lucas, wtf? why did you make i=0 and not
            #just hardcode i? i is supposed to iterate and change in a while loop?
            # what was going on in your headspace in march bro? sincerely, me
            #left < size for bound checks, trying not to write to non-existant places
            #we keep going through the "largest" until we 
            #put the back down 
            if left < size and self._heapList[left] > self._heapList[largest]:
                #okay so the left is the biggest
                largest = left
            if right < size and self._heapList[right] > self._heapList[largest]:
                #erm actually the right is the biggest
                largest = right
            if largest == i: #break if we're the top guy
                break 
            self._heapList[i], self._heapList[largest] = self._heapList[largest], self._heapList[i] #swap i with the largest
            i = largest #ohhh you wanna change i for each loop and set it
            #and i guess it moves down for each layer of the tree 
            #which is kinda cool but hella confusing
            #name your variables something better than i
        self._itemCount -= 1
