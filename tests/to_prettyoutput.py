import glob

# This file allows to process the data from not-XML outputs.

# Converts output to an XML string sequence.
def convert(file):

    with open(file,'r') as f:
        buffer = f.readlines()

    xml = ""
    shift = 0
    for line in buffer:
        
        if "Start element" in line:
            xml = xml + set_shift(shift) + "<" + line.split("element: ")[1][:-1] + ">"
            shift = shift + 1
        if "End element" in line:
            xml = xml + "</" + line.split("element: ")[1][:-1] + ">\n"
            shift = shift - 1
        if "Character data" in line:
            data = line.split("data: ")[1][:-1]
            if data.isspace():
                xml = xml + "\n"
            else:
                xml = xml + data

    # Clears white lines.
    xml = "\n".join([ll.rstrip() for ll in xml.splitlines() if ll.strip()])
    
    return xml

# Adjusts shifts in nested XML entities.
def set_shift(nb):
    shift = ""
    for i in range(nb):
        shift = shift + " "
    return shift
