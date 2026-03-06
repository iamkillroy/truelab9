from kumed import Hospital

hospital = Hospital()
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
        print(f"There are {hospital.countPatients()} patients waiting")
    if line[0] == "T":
        hospital.treatPatient()
