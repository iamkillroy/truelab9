from datastructs.bnode import BinaryNode 
import logging
logger = logging.getLogger(__name__)
open("log.txt", "w").write("")
logging.basicConfig(filename="log.txt", encoding="utf-8", level=logging.DEBUG)

class MaxHeap:
    def __init__(self):
        self._adam = None
    
    def add(self, entry):
        """Creates a new binary node from the given user value"""
        logger.debug(f"Adding {entry}")
        newBinaryNode = BinaryNode(entry)
        if self._adam is None: #gotta start with the basics
            self._adam = newBinaryNode
            return None
        #first let's traverse to the lowest value on the tree.
        lowestNode = self._adam
        while lowestNode.has_branch("right"):
            logger.debug(f"Traversing down, currently at {lowestNode}")
            lowestNode = lowestNode.get_branch("right")
            #we go down to the tippity bottom of the tree
            #all the way to the rightmost node
        #we now have the lowest node in the entire tree
        #we will keep looping until we find the node that is greater
        #than the newBinaryNode
        #we also have to check branches so that in this example
        #        50
        #      /    \
        #   30      40
        # and we try to add 35 that we add it to the right of 30
        #seems tough but recursion can help us out
        self.__recadd( lowestNode, newBinaryNode) #start to add recursively starting at lowest Node
    def __recadd(self, compareNode: BinaryNode, newBinaryNode: BinaryNode): 
        reachedTop = False
        #aka while the new node is greater than 
        #the node we are traversing up
        while compareNode < newBinaryNode:
            if compareNode is self._adam:
                #we can't go higher than the top
                reachedTop = True
                break
            else:
                compareNode = compareNode.get_dad()
        #okay now we've broke out of the loop
        #this can be for three reasons
        #Reason 1: we found an element that's the greatest and we passed it
        #this means compare node has reached the top. if that's so, we reassign the adam
        if reachedTop:
            #now we reassign adam to this element because it is evidently
            #the largest in the heap
            previousDad = self._dad
            self._dad = newBinaryNode
            #okay now we want to set the left and right to keep the maxheap complete
            #this means we need to get the previousDad's largest branch and then
            #set his dad to the new dad
            newDadLeftBranchNode = None
            if previousDad.get_branch("left").evalue() > previousDad.get_branch("right").evalue():
                newDadLeftBranchNode = previousDad.get_branch("left")
            else:
                newDadLeftBranchNode = previousDad.get_branch("right")
            self._dad.setBranch("left", newDadLeftBranchNode)
            self._dad.setBranch("right", previousDad)
        #Reason 2: we found a compareNode that is greater, and it has (branches) that are
        #greater than the current
                 
