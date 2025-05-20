#import necessary libraries
import xml.dom.minidom
import time
 
# initialise the timer
start = time.time()

# load and parse the XML
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

# build a dictionary to initialse the "is_a" count for the 3 GO terms
max_is_a = {
    'biological_process': (None, 0),
    'molecular_function': (None, 0),
    'cellular_component': (None, 0)
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