class BinaryNode:
    def __init__(self):
        """Makes a binary node"""
        self._entry = entry
        self._left = None
        self._right = None
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
        return int(has_branch("right") + int(has_branch("left")
    def value(self):
        """Returns the inner entry value"""
        return self._entry
    def evalue(self):
        """Returns the value in the entry of the binary node
        that is evaluated and compared as an integer, if supported"""
        if hasattr(self._entry, "evalue"):
            return self._entry.evalue
        return None 
    def has_branch(self, branchName: str) -> bool:
        """Returns if a branch exists"""
        match branchName:
            #ternary statements that evaluate True if
            #the type of data in the space is not None, 
            #which is the default of the class
            case "right":
                return True if self._right is not None else False 
            case "left":
                return True if self._left is not None else False 
            case _:
                raise Exception(f"Unknown branch name {branchName}")
