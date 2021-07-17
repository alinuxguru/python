##find a String from a file
stringToMatch = 'input id'
with open('source_output.txt', 'r') as file:
    for line in file:
        if stringToMatch in line:
            #print(line)
            firstdelimit = line.find("id=")
            lastdelimit  = line.find("type")
            extract = line[firstdelimit+4:lastdelimit-2]
            print(extract)
