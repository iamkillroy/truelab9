################
#      @>      #
#   /KU        #
#    "         #
# EECS 268 L9  #
# By Lucas F   #
# Rock Chalk!  #
################

#lowkirk a disclaimer
#so basically this is code from
#when i worked ahead to finish every lab
#and learned everything by myself
# 10/10 would recommend again but
# the TLDR is that there's some decision choices
#that are probably not what Senor Gibbons would 
#recommend
from kumed import Hospital

hospital = Hospital() #make a hospital instance
fileText = open(input("Please input a file>"), "r").read()
for line in fileText.split("\n"):
    if len(line) == 0:
        continue #skip empty lines
    if line[0] == "A": #Arrive
        _, firstName, lastName, ageStr, illness, severityStr = line.split(" ")
        age, severity = int(ageStr), int(severityStr)
        hospital.addPatient(firstName, lastName, age, illness, severity)
    if line[0] == "N":
        nextPatient = hospital.nextPatient()
        print(f"Name: {nextPatient.firstName} {nextPatient.lastName} \n Age: {nextPatient.age} \n Suffers from: {nextPatient.illness} \n Severity: {nextPatient.severity} \n Arrival Order: {nextPatient.arrival}")
    if line[0] == "C":
        onlyOnePatient = False if hospital.countPatients() > 1 else True 
        print(f"There {"is" if onlyOnePatient else "are"} {hospital.countPatients()} patient{"s" if not onlyOnePatient else ""} waiting")
    if line[0] == "T":
        hospital.treatPatient()
