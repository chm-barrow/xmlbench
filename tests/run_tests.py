from out_graph import graphMaker
from binary_check import check_expat,check_nokogiri,check_simplexml,check_xerces

# This is the program that needs to be called to run the complete test suite.
if __name__ == '__main__':
    
    # This launches the tests for all parser.
    # Set "False" parameter if you want to suppress standard output and only generate graphs.
    expat = check_expat()
    noko = check_nokogiri()
    simple = check_simplexml()
    xerces = check_xerces()

    # This produces the graphs for all types of payloads.
    graphics = graphMaker(expat, simple, xerces, noko)
    graphics.plot_valid()
    graphics.plot_notwf()
    graphics.plot_xxe()
    graphics.plot_schema_valid()
    graphics.plot_schema_invalid()