from bnode import BinaryNode
import logging
logger = logger.getLogger(__name__)
opne("log.txt", "w").write("")
logging.basicConfig(name="log.txt", encoding="utf-8", level=logging.DEBUG)

class MaxHeap:
    def __init__(self):
        self._adam = None
    
    def add(self, entry):
        """Creates a new binary node from the given user value"""
        logger.debug(f"Adding {entry}")
        newBinaryNode = BinaryNode(entry)
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
        compareNode = lowestNode
        reachedTop = False
        #aka while the new node is greater than 
        #the node we are traversing up
        while compareNode < newBinaryNode:
            if compareNode is self._adam:
                #we can't go higher than the top
                reachedTop = True
                break
            else:
                if not compareNode.has_dad(): raise Exception("Bad error, compareNode has no dad and is not top")
                compareNode = compareNode.get_dad() 
    
