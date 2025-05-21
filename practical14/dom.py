#import necessary libraries
import xml.dom.minidom
import time
import xml.sax
 
# initialise the timer
start = time.time()

# load and parse the XML
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

# build a dictionary to initialse the "is_a" count for the 3 GO terms
max_is_a = {
    'biological_process': ("", 0),
    'molecular_function': ("", 0),
    'cellular_component': ("", 0)
}

# Process each term
for term in terms: #firstChild.data represent the "hhh" in <namespace> hhh </namespace>
    namespace = term.getElementsByTagName("namespace")[0].firstChild.data #namespace represent one of the 3 types of GO terms
    go_id = term.getElementsByTagName("id")[0].firstChild.data
    is_a = term.getElementsByTagName("is_a")
    count = len(is_a)
    
    if count > max_is_a[namespace][1]: #the same as (None, 0)[1], so can find the second element of the tuple
        max_is_a[namespace] = (go_id, count)

# Print results
for ns, (go_id, count) in max_is_a.items():
    print(f"{ns}: {go_id} with {count} is_a elements")

end = time.time()
print("DOM parsing time:", end - start, "seconds")

# Create a class object to handle the SAX events one tag at a time
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.namespace = ""
        self.id = ""
        self.is_a_count = 0 

        # Dictionary to store max is_a count for each ontology
        self.max_is_a = {
            'biological_process': ("", 0),
            'molecular_function': ("", 0),
            'cellular_component': ("", 0)
        }

    # Triggered when a new XML element starts
    def startElement(self, tag, attributes):
        self.current_element = tag  # e.g., <namespace>, <id>, <is_a>, etc.

        # If starting a new <term>, reset values
        if tag == "term":
            self.namespace = "" 
            self.id = "" 
            self.is_a_count = 0  

    # Triggered when an element ends
    def endElement(self, tag):
        # When a <term> ends, check if it has the most is_a links in its namespace
        if tag == "term":
            if self.namespace in self.max_is_a: # can be deleted in GO.xml
                if self.is_a_count > self.max_is_a[self.namespace][1]: #e.g. 'biological_process':(GO:000001,3)
                    # If current term has more is_a entries, update max for that namespace
                    self.max_is_a[self.namespace] = (self.id, self.is_a_count)
        self.current_element = "" #clear the current element

    # Triggered when text content is read inside elements
    def characters(self, content): #use += instead of replace because there might be mutiple conetnts in the characters
        #ontology
        if self.current_element == "namespace":
            self.namespace += content.strip()  
        #id
        elif self.current_element == "id" and content.strip().startswith("GO:"):
            self.id = content.strip()
        #<is_a>
        elif self.current_element == "is_a":
            self.is_a_count += 1 

#start timing
start = time.time()

#create a SAX parser
parser = xml.sax.make_parser()

#create a handler and attach it to the parser
handler = GOHandler()
parser.setContentHandler(handler)

# Parse the file
parser.parse("go_obo.xml")

# Print the results: the term with the most <is_a> links in each ontology
for namespace, (go_id, count) in handler.max_is_a.items():
    print(f"{namespace}: {go_id} with {count} is_a elements")

end = time.time()  # End timing
print("SAX parsing time:", end - start, "seconds")

# SAX is faster than DOM for large files because it reads the file sequentially
# without loading the entire XML tree into memory. It uses less memory and is more efficient
# for big XML datasets.