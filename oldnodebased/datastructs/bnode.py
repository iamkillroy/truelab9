from functools import total_ordering

@total_ordering
class BinaryNode:
    def __init__(self, entry):
        """Makes a binary node"""
        self._entry = entry
        self._left = None
        self._right = None
        self._dad = None
    def set_dad(self, newNode):
        """Sets the Binary Node's father"""
        self._dad = newNode
    def get_dad(self):
        """Gets the dad of the element"""
        return self._dad
    def has_dad(self):
        """Returns bool if BinaryNode has dad"""
        return self._dad is not None 
    def get_branch(self, branchName: str):
        """Gets the value of the branch at branchName"""
        match branchName:
            #using match casing return each branch 
            case "right":
                return self._right
            case "left":
                return self._left
            case _:
                raise Exception(f"Unknown branch name {branchName}")
    def set_branch(self, branchName: str, newNode):
        """Sets the value of the branch"""
        match branchName:
            #using match statements set the new node
            #equal to either the left or right branch
            case "right":
                self._right = newNode
            case "left":
               self._left = newNode 
            case _:
                raise Exception(f"Unknown branch name {branchName}")
    def branch_count(self):
        """Gets branch count (how many branches are connected""" 
        #here we can type case right and left's having branches
        #as two integers and return the result of those two
        return int(self.has_branch("right")) + int(self.has_branch("left"))
    def value(self):
        """Returns the inner entry value"""
        return self._entry
    def evalue(self):
        """Returns the value in the entry of the binary node
        that is evaluated and compared as an integer, if supported"""
        if hasattr(self._entry, "evalue"):
            return self._entry.evalue
        return self._entry 
    def has_branch(self, branchName: str) -> bool:
        """Returns if a branch exists"""
        match branchName:
            #ternary statements that evaluate True if
            #the type of data in the space is not None, 
            #which is the default of the class
            case "right":
                return self._right is not None 
            case "left":
                return self._left is not None 
            case _:
                raise Exception(f"Unknown branch name {branchName}")
    #total_ordering decorator should add all compare
    #functionalities with just __eq__ and __lt__
    def __eq__(self, other):
        if type(other) == int:
            return self._entry == other
        else:
            return self._entry == other._entry
    def __lt__(self, other):
        if type(other) == int:
            return self._entry < other
        else:
            return self._entry < other

