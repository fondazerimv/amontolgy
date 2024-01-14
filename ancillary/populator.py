import csv
from pprint import pprint

# Declare the tag
individual_tag = """
<!-- {iri} -->

    <owl:NamedIndividual rdf:about="{iri}">
        <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    </owl:NamedIndividual>
"""

# Extract your IRIs
with open('alignment-uri.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    iri_list = [row[0] for row in csv_reader]

pprint(iri_list)
print(">>>>>> ", len(iri_list))

# Create OWL/XML tag for the individuals
tag_list = []

for el in iri_list:
    tag_list.append(individual_tag.format(iri=el))

ir_tag_string = '\n'.join(tag_list)

# Export

# print(ir_tag_string)

with open('xml-tag.txt', 'w') as file:
    file.write(ir_tag_string)