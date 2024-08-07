from to_prettyoutput import convert
import glob
from os.path import getsize

# Compares processed data with reference file to see if it has correctly been processed.
def verif_output(data, reference):

    with open(reference,'r') as f:
        ref = f.read()
    ref = "\n".join([ll.rstrip() for ll in ref.splitlines() if ll.strip()])

    if ref == data:
        return True
    else:
        # For debugging purposes.
        # print("REFERENCE: \n" + ref)
        # print("OUTPUT FILE: \n" + data)
        return False
    
def get_file(file):

    with open(file,'r') as f:
        data = f.read()
    return data
    
    
def verif_error_expat(file):

    with open(file,'r') as f:
        data = f.read()

    if "not well-formed" in data:
        return True
    if "unclosed token" in data:
        return True
    else:
        return False
    
def verif_error_xerces(file):
    with open(file,'r') as f:
        data = f.read()

    if "Unexpected Exception" in data:
        return True
    if "Fatal Error" in data:
        return True
    if "SAX Parse Exception" in data:
        return True
    else:
        return False
    
def verif_error_noko(file):
    with open(file,'r') as f:
        data = f.read()

    if "FATAL" in data:
        return True
    else:
        return False
    
def verif_error_simple(file):
    with open(file,'r') as f:
        data = f.read()

    if "Error." in data:
        return True
    if data == '':
        return True
    else:
        return False

# This function launches all tests using every parser developped using Expat.
def check_expat():

    # Tests Expat parser on valid payloads.

    print("\nTests for valid payloads with Expat parser:\n")

    references = glob.glob("references/valid/*")
    parser_output_sax = glob.glob("output/expat/sax/valid/*")
    parser_output_xxe = glob.glob("output/expat/xxe/valid/*")

    results_sax = []
    results_xxe = []
    for index in range(len(parser_output_sax)):
        output = convert(parser_output_sax[index])
        results_sax.append(verif_output(output, references[index]))

        output = convert(parser_output_xxe[index])
        results_xxe.append(verif_output(output, references[index]))

    valid_ctr_sax = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_sax += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_sax = round(( valid_ctr_sax / len(references) ) * 100, 2)
    print("Tests results for SAX-like parser: " + str(ratio_sax) + "%")

    ratio_xxe = round(( valid_ctr_xxe / len(references) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    # Tests Expat parser on not well-formed payloads.

    print("\nTests for not well-formed payloads with Expat parser.\n")

    # references = glob.glob("references/not-wf/*")
    parser_output_sax = glob.glob("output/expat/sax/not-wf/*")
    parser_output_xxe = glob.glob("output/expat/xxe/not-wf/*")

    results_sax = []
    results_xxe = []
    for index in range(len(parser_output_sax)):
        results_sax.append(verif_error_expat(parser_output_sax[index]))
        results_xxe.append(verif_error_expat(parser_output_xxe[index]))

    valid_ctr_sax = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_sax += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_sax = round(( valid_ctr_sax / len(parser_output_sax) ) * 100, 2)
    print("Tests results for SAX-like parser: " + str(ratio_sax) + "%")

    ratio_xxe = round(( valid_ctr_xxe / len(parser_output_sax) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    # Tests Expat parser on other type of payloads.

    print("\nTests for not other type of payloads with Expat parser.\n")

    references = glob.glob("references/other/*")
    parser_output_sax = glob.glob("output/expat/sax/other/*")
    parser_output_xxe = glob.glob("output/expat/xxe/other/*")

    

    results_sax = []
    results_xxe = []
    for index in range(len(parser_output_sax)):

        # Billion laugh attack particular management.
        if parser_output_sax[index] == "output/expat/sax/other\\001.txt":
            if getsize("output/expat/sax/other\\001.txt") > 10000:
                results_sax.append(True)
            else:
                results_sax.append(False)
        if parser_output_xxe[index] == "output/expat/xxe/other\\001.txt":
            if getsize("output/expat/xxe/other\\001.txt") > 10000:
                results_xxe.append(True)
            else:
                results_xxe.append(False)

        else:
            output = convert(parser_output_sax[index])
            results_sax.append(verif_output(output, references[index]))

            output = convert(parser_output_xxe[index])
            results_xxe.append(verif_output(output, references[index]))

    valid_ctr_sax = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_sax += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_sax = 100 - round(( valid_ctr_sax / len(references) ) * 100, 2)
    print("Tests results for SAX-like parser: " + str(ratio_sax) + "%")

    ratio_xxe = 100 - round(( valid_ctr_xxe / len(references) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")



# This function launches all tests using every parser developped using Xerces-C++.
def check_xerces():

    # Tests Xerces parser on valid payloads.

    print("\nTests for valid payloads with Xerces-C++ parser:\n")

    references = glob.glob("references/valid/*")
    parser_output_sax = glob.glob("output/xerces/sax/valid/*")
    parser_output_dom = glob.glob("output/xerces/dom/valid/*")
    parser_output_xxe = glob.glob("output/xerces/xxe/valid/*")
    

    results_sax = []
    results_dom = []
    results_xxe = []

    for index in range(len(parser_output_sax)):
        output_sax = convert(parser_output_sax[index])
        results_sax.append(verif_output(output_sax, references[index]))

        # The [:-1] removes the \n from the Xerces DOM output. 
        output_dom = get_file(parser_output_dom[index])[:-1]
        results_dom.append(verif_output(output_dom, references[index]))

        output_xxe = get_file(parser_output_xxe[index])[:-1]
        results_xxe.append(verif_output(output_xxe, references[index]))

    valid_ctr_sax = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_sax += 1

    valid_ctr_dom = 0
    for answer in results_dom:
        if answer == True:
            valid_ctr_dom += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_sax = round(( valid_ctr_sax / len(results_sax) ) * 100, 2)
    print("Tests results for SAX-like parser: " + str(ratio_sax) + "%")

    ratio_dom = round(( valid_ctr_dom / len(results_sax) ) * 100, 2)
    print("Tests results for DOM-like parser: " + str(ratio_dom) + "%")

    ratio_xxe = round(( valid_ctr_xxe / len(results_xxe) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    # Tests Xerces parser on not well-formed payloads.

    print("\nTests for not well-formed payloads with Xerces parser.\n")

    # references = glob.glob("references/not-wf/*")
    parser_output_sax = glob.glob("output/xerces/sax/not-wf/*")
    parser_output_dom = glob.glob("output/xerces/dom/not-wf/*")
    parser_output_xxe = glob.glob("output/xerces/xxe/not-wf/*")

    results_sax = []
    results_dom = []
    results_xxe = []
    for index in range(len(parser_output_sax)):
        results_sax.append(verif_error_xerces(parser_output_sax[index]))
        results_dom.append(verif_error_xerces(parser_output_dom[index]))
        results_xxe.append(verif_error_xerces(parser_output_xxe[index]))

    valid_ctr_sax = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_sax += 1

    valid_ctr_dom = 0
    for answer in results_dom:
        if answer == True:
            valid_ctr_dom += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_sax = round(( valid_ctr_sax / len(parser_output_sax) ) * 100, 2)
    print("Tests results for SAX-like parser: " + str(ratio_sax) + "%")

    ratio_dom = round(( valid_ctr_dom / len(results_sax) ) * 100, 2)
    print("Tests results for DOM-like parser: " + str(ratio_dom) + "%")

    ratio_xxe = round(( valid_ctr_xxe / len(parser_output_sax) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    # Tests Xerces parser on other type of payloads.

    print("\nTests for other type of payloads with Xerces parser.\n")

    references = glob.glob("references/other/*")
    parser_output_sax = glob.glob("output/xerces/sax/other/*")
    parser_output_dom = glob.glob("output/xerces/dom/other/*")
    parser_output_xxe = glob.glob("output/xerces/xxe/other/*")

    

    results_sax = []
    results_dom = []
    results_xxe = []
    for index in range(len(parser_output_sax)):

        # Billion laugh attack particular management.
        if parser_output_sax[index] == "output/xerces/sax/other\\001.txt":
            if getsize("output/expat/sax/other\\001.txt") > 10000:
                results_sax.append(True)
            else:
                results_sax.append(False)
        if parser_output_dom[index] == "output/xerces/xxe/other\\001.txt":
            if getsize("output/expat/dom/other\\001.txt") > 10000:
                results_dom.append(True)
            else:
                results_dom.append(False)
        if parser_output_xxe[index] == "output/xerces/xxe/other\\001.txt":
            if getsize("output/expat/xxe/other\\001.txt") > 10000:
                results_xxe.append(True)
            else:
                results_xxe.append(False)

        else:
            output = convert(parser_output_sax[index])
            results_sax.append(verif_output(output, references[index]))

            output = convert(parser_output_dom[index])
            results_dom.append(verif_output(output, references[index]))

            output = convert(parser_output_xxe[index])
            results_xxe.append(verif_output(output, references[index]))

    valid_ctr_sax = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_sax += 1

    valid_ctr_dom = 0
    for answer in results_dom:
        if answer == True:
            valid_ctr_dom += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_sax = 100 - round(( valid_ctr_sax / len(references) ) * 100, 2)
    print("Tests results for SAX-like parser: " + str(ratio_sax) + "%")

    ratio_dom = 100 - round(( valid_ctr_xxe / len(references) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    ratio_xxe = 100 - round(( valid_ctr_xxe / len(references) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")


# This function launches all tests using every parser developped using SimpleXML.
def check_simplexml():

    # Tests SimpleXML parser on valid payloads.

    print("\nTests for valid payloads with SimpleXML parser:\n")

    references = glob.glob("references/valid/*")
    parser_output_dom = glob.glob("output/simplexml/dom/valid/*")
    parser_output_xxe = glob.glob("output/simplexml/xxe/valid/*")

    results_dom = []
    results_xxe = []

    for index in range(len(parser_output_dom)):
        # The [:-1] removes the \n from the output.   
        output_dom = get_file(parser_output_dom[index])[:-1]
        results_dom.append(verif_output(output_dom, references[index]))

        output_xxe = get_file(parser_output_xxe[index])[:-1]
        results_xxe.append(verif_output(output_xxe, references[index]))

    valid_ctr_dom = 0
    for answer in results_dom:
        if answer == True:
            valid_ctr_dom += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_dom = round(( valid_ctr_dom / len(results_dom) ) * 100, 2)
    print("Tests results for DOM-like parser: " + str(ratio_dom) + "%")

    ratio_xxe = round(( valid_ctr_xxe / len(results_xxe) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    # Tests Nokogiri parser on not well-formed payloads.

    print("\nTests for not well-formed payloads with SimpleXML parser.\n")

    # references = glob.glob("references/not-wf/*")
    parser_output_dom = glob.glob("output/simplexml/dom/not-wf/*")
    parser_output_xxe = glob.glob("output/simplexml/xxe/not-wf/*")

    results_dom = []
    results_xxe = []
    for index in range(len(parser_output_dom)):
        results_dom.append(verif_error_simple(parser_output_dom[index]))
        results_xxe.append(verif_error_simple(parser_output_xxe[index]))

    valid_ctr_dom = 0
    for answer in results_dom:
        if answer == True:
            valid_ctr_dom += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_dom = round(( valid_ctr_dom / len(results_dom) ) * 100, 2)
    print("Tests results for DOM-like parser: " + str(ratio_dom) + "%")

    ratio_xxe = round(( valid_ctr_xxe / len(parser_output_dom) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    # Tests SimpleXML parser on other type of payloads.

    print("\nTests for other type of payloads with SimpleXML parser.\n")

    references = glob.glob("references/other/*")
    parser_output_dom = glob.glob("output/simplexml/dom/other/*")
    parser_output_xxe = glob.glob("output/simplexml/xxe/other/*")

    

    results_dom = []
    results_xxe = []
    for index in range(len(parser_output_dom)):

        # Billion laugh attack particular management.
        if parser_output_dom[index] == "output/simplexml/xxe/other\\001.txt":
            if getsize("output/expat/dom/other\\001.txt") > 10000:
                results_dom.append(True)
            else:
                results_dom.append(False)
        if parser_output_xxe[index] == "output/simplexml/xxe/other\\001.txt":
            if getsize("output/expat/xxe/other\\001.txt") > 10000:
                results_xxe.append(True)
            else:
                results_xxe.append(False)

        else:
            output = convert(parser_output_dom[index])
            results_dom.append(verif_output(output, references[index]))

            output = convert(parser_output_xxe[index])
            results_xxe.append(verif_output(output, references[index]))

    valid_ctr_dom = 0
    for answer in results_dom:
        if answer == True:
            valid_ctr_dom += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1

    ratio_dom = 100 - round(( valid_ctr_xxe / len(references) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    ratio_xxe = 100 - round(( valid_ctr_xxe / len(references) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

# This function launches all tests using every parser developped using Nokogiri.
def check_nokogiri():

    # Tests Nokogiri parser on valid payloads.

    print("\nTests for valid payloads with Nokogiri parser:\n")


    references = glob.glob("references/valid/*")
    parser_output_sax = glob.glob("output/rexml/sax/valid/*")
    parser_output_dom = glob.glob("output/rexml/dom/valid/*")
    parser_output_xxe = glob.glob("output/rexml/xxe/valid/*")
    

    results_sax = []
    results_dom = []
    results_xxe = []

    for index in range(len(parser_output_sax)):
        # The [:-1] removes the \n from the output. 
        output_sax = get_file(parser_output_sax[index])[:-1]
        results_sax.append(verif_output(output_sax, references[index]))
        
        output_dom = get_file(parser_output_dom[index])[:-1]
        results_dom.append(verif_output(output_dom, references[index]))

        output_xxe = get_file(parser_output_xxe[index])[:-1]
        results_xxe.append(verif_output(output_xxe, references[index]))

    valid_ctr_sax = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_sax += 1

    valid_ctr_dom = 0
    for answer in results_dom:
        if answer == True:
            valid_ctr_dom += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_sax = round(( valid_ctr_sax / len(results_sax) ) * 100, 2)
    print("Tests results for SAX-like parser: " + str(ratio_sax) + "%")

    ratio_dom = round(( valid_ctr_dom / len(results_sax) ) * 100, 2)
    print("Tests results for DOM-like parser: " + str(ratio_dom) + "%")

    ratio_xxe = round(( valid_ctr_xxe / len(results_xxe) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    # Tests Nokogiri parser on not well-formed payloads.

    print("\nTests for not well-formed payloads with Nokogiri parser.\n")

    # references = glob.glob("references/not-wf/*")
    parser_output_sax = glob.glob("output/rexml/sax/not-wf/*")
    parser_output_dom = glob.glob("output/rexml/dom/not-wf/*")
    parser_output_xxe = glob.glob("output/rexml/xxe/not-wf/*")

    results_sax = []
    results_dom = []
    results_xxe = []
    for index in range(len(parser_output_sax)):
        results_sax.append(verif_error_noko(parser_output_sax[index]))
        results_dom.append(verif_error_noko(parser_output_dom[index]))
        results_xxe.append(verif_error_noko(parser_output_xxe[index]))

    valid_ctr_sax = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_sax += 1

    valid_ctr_dom = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_dom += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_sax = round(( valid_ctr_sax / len(parser_output_sax) ) * 100, 2)
    print("Tests results for SAX-like parser: " + str(ratio_sax) + "%")

    ratio_dom = round(( valid_ctr_dom / len(results_sax) ) * 100, 2)
    print("Tests results for DOM-like parser: " + str(ratio_dom) + "%")

    ratio_xxe = round(( valid_ctr_xxe / len(parser_output_sax) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    # Tests Nokogiri parser on other type of payloads.

    print("\nTests for other type of payloads with Nokogiri parser.\n")

    references = glob.glob("references/other/*")
    parser_output_sax = glob.glob("output/rexml/sax/other/*")
    parser_output_dom = glob.glob("output/rexml/dom/other/*")
    parser_output_xxe = glob.glob("output/rexml/xxe/other/*")

    

    results_sax = []
    results_dom = []
    results_xxe = []
    for index in range(len(parser_output_sax)):

        # Billion laugh attack particular management.
        if parser_output_sax[index] == "output/rexml/sax/other\\001.txt":
            if getsize("output/expat/sax/other\\001.txt") > 10000:
                results_sax.append(True)
            else:
                results_sax.append(False)
        if parser_output_dom[index] == "output/rexml/xxe/other\\001.txt":
            if getsize("output/expat/dom/other\\001.txt") > 10000:
                results_dom.append(True)
            else:
                results_dom.append(False)
        if parser_output_xxe[index] == "output/rexml/xxe/other\\001.txt":
            if getsize("output/expat/xxe/other\\001.txt") > 10000:
                results_xxe.append(True)
            else:
                results_xxe.append(False)

        else:
            output = convert(parser_output_sax[index])
            results_sax.append(verif_output(output, references[index]))

            output = convert(parser_output_dom[index])
            results_dom.append(verif_output(output, references[index]))

            output = convert(parser_output_xxe[index])
            results_xxe.append(verif_output(output, references[index]))

    valid_ctr_sax = 0
    for answer in results_sax:
        if answer == True:
            valid_ctr_sax += 1

    valid_ctr_dom = 0
    for answer in results_dom:
        if answer == True:
            valid_ctr_dom += 1

    valid_ctr_xxe = 0
    for answer in results_xxe:
        if answer == True:
            valid_ctr_xxe += 1
    
    ratio_sax = 100 - round(( valid_ctr_sax / len(references) ) * 100, 2)
    print("Tests results for SAX-like parser: " + str(ratio_sax) + "%")

    ratio_dom = 100 - round(( valid_ctr_xxe / len(references) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")

    ratio_xxe = 100 - round(( valid_ctr_xxe / len(references) ) * 100, 2)
    print("Tests results for XXE parser: " + str(ratio_xxe) + "%")


if __name__ == '__main__':

    check_expat()
    check_xerces()
    check_nokogiri()
    check_simplexml()