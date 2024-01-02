## Domande di competenza?

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | In which period was the RT’s organization <i>Tesori</i> active? | Name, period of activity and address of the activity | <i>Tesori</i>, 1870, 1910, Piazza Duomo, Florence          | ``` SELECT ?name ?startDate ?endDate ?address ?city WHERE { ?org am00:hasName ?name. ?org am00:hasSeat/am00:isActiveFrom ?startDate. ?org am00:hasSeat/am00:isActiveTo ?endDate . ?org am00:hasSeat/am00:isLocatedIn ?location. OPTIONAL { ?location am00:isContainedInPlace ?biggerLoc }   BIND (exists{?location am00:isContainedInPlace ?biggerLoc} AS ?existsAddress)   BIND (IF(?existsAddress, ?location, "") AS ?address)  BIND (IF(?existsAddress, ?biggerLoc, ?location) AS ?city) FILTER (?name="Galleria d'Arte Tesori"^^xsd:string) }```                                                                                                                                                                                                         |
| 2.  | Who is the buyer of SD’s auction house?  | Name of the buyer and year of the acquisition   | MB, 1915                                                  | ``` SELECT ?agent ?year WHERE { ?purchase am00:hasCompanySeller am00:ex2_SD. ?purchase am00:hasCompanyPurchaser ?agent. ?purchase am00:hasDate ?year } ```                                                                                                                                                                      |
| 3.  | Which events modified ZF’s organization? | Name of the agent responsible for the change,and name, establishment year and address of the new organization | LZ, 1920, <i>Les Arts de Paris</i>, Paris, Champs Élysées | ``` SELECT ?agent ?newName ?address ?city ?year WHERE { ?org am00:hasName ?name . ?org am00:hasName ?name . ?change am00:hasOriginalOrganization ?org. ?change am00:hasResultingOrganization ?new. ?change am00:hasParticipant ?agent. ?change am00:hasDate ?year. ?new am00:hasName ?newName . ?new am00:hasSeat/am00:isLocatedIn ?location . OPTIONAL { ?location am00:isContainedInPlace ?biggerLoc }   BIND (exists{?location am00:isContainedInPlace ?biggerLoc} AS ?existsAddress)   BIND (IF(?existsAddress, ?location, "") AS ?address)  BIND (IF(?existsAddress, ?biggerLoc, ?location) AS ?city) FILTER (?name="Arti fiorentine"^^xsd:string) }```|

****

In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/agent/3#>
```