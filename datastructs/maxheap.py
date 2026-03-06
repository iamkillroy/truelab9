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
        #we will keep looping until we find the node that is less 
        #than the newBinaryNode
        #we also have to check branches so that in this example
        #        50
        #      /    \
        #   30      40
        # and we try to add 35 that we add it to the right of 30
        #seems tough but recursion can help us out
        self.__recadd(self._adam, newBinaryNode) #start to add recursively starting at lowest Node
    def __reclean(self, compareNode: BinaryNode, newBinaryNode: BinaryNode):
        pass
    def __recadd(self, compareNode: BinaryNode, newBinaryNode: BinaryNode):
        
        if compareNode < newBinaryNode:
            #we found the spot here.
            #now there may be another node on another branch
            # so we have to check
            if compareNode.branch_count() != 2:
                if not compareNode.has_branch("right"):
                    compareNode.set_branch("right", newBinaryNode)
                if not compareNode.has_branch("left"):
                    compareNode.set_branch("left", newBinaryNode)
            else: #the compare node has two, this is where it gets tricky
                #__reclean every single branch
                #rec clean will basically make sure each binary tree segment is complete
                #when accounting for offsets n deep
                #like so

                #           50
                #         /   \
                #       30
                #     /   \
                #    25   27
                #   /    /  \
                #  3    19   22
                # if we wanna add element 29 and we default right
                # that means that 27 and the higher element in the branch needs to appear
                #so it becomes something like this
                #           50
                #         /   \
                #       30
                #     /   \
                #    25   29
                #   /    /  \
                #  3    27  22
                #      /
                #     19
                if compareNode.get_branch("left") > newBinaryNode:
                    self.__reclean(self, compareNode.get_branch("left"), newBinaryNode)
                if compareNode.get_branch("right") > newBinaryNode:
                    self.__reclean(self, compareNode.get_branch("right"), newBinaryNode)
             
        elif compareNode.branch_count() == 0:
            return False
        if compareNode.has_branch("left"):
            resultLeft = __recadd(self, compareNode.get_branch("left"), newBinaryNode)
        if compareNode.has_branch("right") and not resultLeft:
            resultRight = __recadd(self, compareNode.get_branch("right"), newBinaryNode)
        
    def dontuseoldlowestnoderecursiveadd(self, compareNode: BinaryNode, newBinaryNode: BinaryNode): 
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
            previousDad = self._adam 
            self._adam = newBinaryNode
            #okay now we want to set the left and right to keep the maxheap complete
            #this means we need to get the previousDad's largest branch and then
            #set his dad to the new dad
            newDadLeftBranchNode = None
            if previousDad.branch_count() == 2:
                if previousDad.get_branch("left").evalue() > previousDad.get_branch("right").evalue():
                    newDadLeftBranchNode = previousDad.get_branch("left")
                else:
                    newDadLeftBranchNode = previousDad.get_branch("right")
                self._dad.get_branch("left", newDadLeftBranchNode)
                self._dad.get_branch("right", previousDad)
            elif previousDad.branch_count == 1:
                #this is the same as the first branch compare
                #except we removed the comparison between the left and right
                #and also preserve the original right or left position
                if previousDad.has_branch("right"):
                    prevRightBranch = previousDad.get_branch("right")
                    self._dad.set_branch("right", prevRightBranch)
                else:
                    prevLeftBranch = previousDad.get_branch("left")
                    self._dad.set_branch("left", prevLeftBranch)
            return None
        elif compareNode.branch_count() > 0:
            #okay we move on to the next two reasons
            #this is the case where we have a comparenode that is bigger 
        #Reason 3: we found a compareNode that is greater, and it has (branches) that are
        #greater than the current one, so we do the same shift thing     
        if compareNode.get_branch("left") < newBinaryNode: 
            smallerLeftNode = compareNode.get_branch("left")
