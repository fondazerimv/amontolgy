# This Python algorithm streamlines the population of the alignment ontology (via punning)

# It creates two distinct txt files containing the axioms in OWL/XML format

# The first one (TASK 1) is responsibile for the creation of individuals as instance of skos:Concept
# The tag of each individual is described as follows:
# <!-- <IRI> -->
#
#    <owl:NamedIndividual rdf:about="<IRI>">
#        <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
#    </owl:NamedIndividual>

# The second one (TASK 2) is responsibile for the assertion of the mapping properties between individuals
# The tag of each axiom is described as follows:
# <ObjectPropertyAssertion>
#     <ObjectProperty IRI="<Object Property IRI>"/>
#     <NamedIndividual IRI="<Subject Individual IRI>"/>
#     <NamedIndividual IRI="<Object Individual IRI>"/>
# </ObjectPropertyAssertion>

#########################

import csv
from pprint import pprint

# Declare the tags

individual_tag = """
<!-- {iri} -->

    <owl:NamedIndividual rdf:about="{iri}">
        <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    </owl:NamedIndividual>
""" #to instantiate each individual

alignment_axiom_tag = """
<ObjectPropertyAssertion>
        <ObjectProperty IRI="{p_iri}"/>
        <NamedIndividual IRI="{s_iri}"/>
        <NamedIndividual IRI="{o_iri}"/>
</ObjectPropertyAssertion>
""" #to create aligment axioms via SKOS

# ============= TASK 1 =================== For RDF / XML

def individual_populator(csv_path):

    # Extract IRIs from the source csv file
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        iri_list = [row[0] for row in csv_reader]

    tag_list = [] #initialize an empty list, which will contain the final OWL / XML tag

    # Iteratively replace the IRI in the base tag
    for el in iri_list:
        tag_list.append(individual_tag.format(iri=el))

    # Convert the tag list into a string and save it as txt file
    individual_iri_tag_string = '\n'.join(tag_list)

    with open('individual-xml-tag.txt', 'w') as file:
        file.write(individual_iri_tag_string)
    
    print("Instantiated {len} skos:Concept instances".format(len=len(tag_list)))

# print(individual_populator("alignment-individual-uri.csv"))

# ============= TASK 2 =================== For OWL / XML
    
def alignment_axiom_populator(csv_path):
    
    # Extract IRIs from the source csv file
    with open(csv_path, 'r') as file:
        csv_dict_reader = csv.DictReader(file, delimiter=';')
        iri_list = [row for row in csv_dict_reader]

    tag_list = [] #initialize an empty list, which will contain the final OWL / XML tag

    # Iteratively replace the IRI in the base tag
    for el in iri_list:
        tag_list.append(alignment_axiom_tag.format(p_iri=el["skos-match"], s_iri=el["zamo-uri"], o_iri=el["aligned-uri"]))
    
    # Convert the tag list into a string and save it as txt file
    alignment_axioms_tag_string = '\n'.join(tag_list)

    with open('alignment-axioms-xml-tag.txt', 'w') as file:
        file.write(alignment_axioms_tag_string)

    print(alignment_axioms_tag_string)
    print("{len} axioms have been asserted".format(len=len(tag_list)))

print(alignment_axiom_populator("alignment-axioms-uri.csv"))
