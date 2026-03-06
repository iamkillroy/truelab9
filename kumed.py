from functools import total_ordering
from maxheap import MaxHeap
class Hospital:
    def __init__(self):
        self.mheap = MaxHeap()
        self.arrival = 0
    def addPatient(self, firstName: str, lastName: str, age: int, illness: str, severity: int):
        self.arrival += 1 
        newPatient = Patient(firstName, lastName, age, illness, severity, self.arrival)
        self.mheap.add(newPatient)
    def treatPatient(self):
        self.mheap.d()
        return self.mheap.pop()
    def nextPatient(self):
        return self.mheap.getHighest()
    def countPatients(self):
        return self.mheap.count()
@total_ordering
class Patient:
    def __init__(self, firstName, lastName, age, illness, severity, arrival):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.illness = illness
        self.severity = severity
        self.arrival = arrival
    def __lt__(self, other):
        return (self.severity + self.age * 0.10) < (other.severity + other.age * 0.10)
    def __eq__(self, other):
        return self.arrival == other.arrival
