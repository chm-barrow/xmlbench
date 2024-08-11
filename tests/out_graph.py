import numpy as np
import matplotlib.pyplot as plt 

class graphMaker():

    def __init__(self, expat, simplexml, xerces, nokogiri):
        self.expat = expat
        self.simplexml = simplexml
        self.xerces = xerces
        self.nokogiri = nokogiri

    def plot_valid(self):
        # creating the dataset
        data = {'Expat (SAX)':self.expat[0], 'Expat(XXE)':self.expat[1],
                'SimpleXML (DOM)':self.simplexml[0], 'SimpleXML':self.simplexml[1],
                'Xerces (SAX)':self.xerces[0], 'Xerces (DOM)':self.xerces[1], 'Xerces (XXE)':self.xerces[2],
                'Nokogiri (SAX)':self.nokogiri[0], 'Nokogiri (DOM)':self.nokogiri[1], 'Nokogiri (XXE)':self.nokogiri[2]}
        parsers = list(data.keys())
        values = list(data.values())
        
        fig = plt.figure(figsize = (15, 5))

        # creating the bar plot
        plt.bar(parsers, values, color ='maroon', 
                width = 0.4)

        plt.xlabel("Parser implementation")
        plt.ylabel("Success Ratio")
        plt.title("Valid payload's test report")
        plt.savefig('graphs/valid.png', dpi=300, bbox_inches='tight')
        # plt.show()

    def plot_notwf(self):
        # creating the dataset
        data = {'Expat (SAX)':self.expat[2], 'Expat(XXE)':self.expat[3],
                'SimpleXML (DOM)':self.simplexml[2], 'SimpleXML':self.simplexml[3],
                'Xerces (SAX)':self.xerces[3], 'Xerces (DOM)':self.xerces[4], 'Xerces (XXE)':self.xerces[5],
                'Nokogiri (SAX)':self.nokogiri[3], 'Nokogiri (DOM)':self.nokogiri[4], 'Nokogiri (XXE)':self.nokogiri[5]}
        parsers = list(data.keys())
        values = list(data.values())
        
        fig = plt.figure(figsize = (15, 5))

        # creating the bar plot
        plt.bar(parsers, values, color ='maroon', 
                width = 0.4)

        plt.xlabel("Parser implementation")
        plt.ylabel("Success Ratio")
        plt.title("Not well-formed payload's test report")
        plt.savefig('graphs/not-wf.png', dpi=300, bbox_inches='tight')
        # plt.show()

    def plot_xxe(self):
        # creating the dataset
        data = {'Expat (SAX)':self.expat[4], 'Expat(XXE)':self.expat[5], 'SimpleXML (DOM)':self.simplexml[4], 'SimpleXML':self.simplexml[5],
                'Xerces (SAX)':self.xerces[6], 'Xerces (DOM)':self.xerces[7], 'Xerces (XXE)':self.xerces[8],
                'Nokogiri (SAX)':self.nokogiri[6], 'Nokogiri (DOM)':self.nokogiri[7], 'Nokogiri (XXE)':self.nokogiri[8]}
        parsers = list(data.keys())
        values = list(data.values())
        
        fig = plt.figure(figsize = (15, 5))

        # creating the bar plot
        plt.bar(parsers, values, color ='maroon', 
                width = 0.4)

        plt.xlabel("Parser implementation")
        plt.ylabel("Success Ratio")
        plt.title("Injection payloads test report")
        plt.savefig('graphs/XXE.png', dpi=300, bbox_inches='tight')
        # plt.show()

    def plot_schema_valid(self):
        # creating the dataset
        data = {'SimpleXML':self.simplexml[6],
                'Xerces (SAX)':self.xerces[9], 'Xerces (DOM)':self.xerces[10],
                'Nokogiri':self.nokogiri[9]}
        parsers = list(data.keys())
        values = list(data.values())
        
        fig = plt.figure(figsize = (15, 5))

        # creating the bar plot
        plt.bar(parsers, values, color ='maroon', 
                width = 0.4)

        plt.xlabel("Parser implementation")
        plt.ylabel("Success Ratio")
        plt.title("Valid schema validation payloads test report")
        plt.savefig('graphs/valid-schema.png', dpi=300, bbox_inches='tight')
        # plt.show()

    def plot_schema_invalid(self):
        # creating the dataset
        data = {'SimpleXML':self.simplexml[7],
                'Xerces (SAX)':self.xerces[11], 'Xerces (DOM)':self.xerces[12],
                'Nokogiri':self.nokogiri[10]}
        parsers = list(data.keys())
        values = list(data.values())
        
        fig = plt.figure(figsize = (15, 5))

        # creating the bar plot
        plt.bar(parsers, values, color ='maroon', 
                width = 0.4)

        plt.xlabel("Parser implementation")
        plt.ylabel("Success Ratio")
        plt.title("Invalid schema validation payloads test report")
        plt.savefig('graphs/invalid-schema.png', dpi=300, bbox_inches='tight')
        # plt.show()