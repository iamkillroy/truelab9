################
# KU EECS 268  #
# KUMED - to do#
# the functions#
# of a hospital #
#################
# this file is really boring
#it's just a mask
from functools import total_ordering
from maxheap import MaxHeap
class Hospital:
    def __init__(self):
        """Make a maxheap
        self.mheap = MaxHeap()
        self.arrival = 0
    def addPatient(self, firstName: str, lastName: str, age: int, illness: str, severity: int):
        self.arrival += 1 
        newPatient = Patient(firstName, lastName, age, illness, severity, self.arrival)
        #make and add a new patient weee
        self.mheap.add(newPatient)
    def treatPatient(self):
        return self.mheap.pop() #treating removes them
    def nextPatient(self):
        return self.mheap.getHighest() #get the most priority patient
    def countPatients(self):
        return self.mheap.count() #get the count
#okay this is the more cool thing
#when i do totalodering i'm just able to do the comparison for every
#int operator with just defining the results of 2 (= and > or whatever other)
#and then that way i can actually have less slop because the decarator fills it in

@total_ordering
class Patient:
    def __init__(self, firstName, lastName, age, illness, severity, arrival):
        """Makes a patient"""
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.illness = illness
        self.severity = severity
        self.arrival = arrival
    def __lt__(self, other):
        #last cool thing about this lab
        #i return my severity plus my age times a supa small multiplier
        #that way we can resolve two severity level patients with the same 
        #severity but different ages
        #although this does mean a grandparent with a heart attack is more important
        #than a three year old with a heart attack but hey
        #you know what they say
        return (self.severity + self.age * 0.010) < (other.severity + other.age * 0.010)
        #boomer lives first
    def __eq__(self, other):
        return self.arrival == other.arrival #wowza!
