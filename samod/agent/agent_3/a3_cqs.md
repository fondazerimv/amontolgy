## Domande di competenza?

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | In which period was the RT’s organization <i>Tesori</i> active? | Name, period of activity and address of the activity | <i>Tesori</i>, 1870, 1910, Piazza Duomo, Florence          | ```SELECT ?name ?start ?end ?address ?city WHERE { zamo:i-tesori zamo:hasName ?name . zamo:i-tesori zamo:hasSeat ?seat . ?seat zamo:isActiveFrom ?start . ?seat zamo:isActiveTo ?end . ?seat zamo:isLocatedIn ?address . ?address zamo:fallsWithin ?city}``` |
| 2.  | Who is the buyer of SD’s auction house?  | Name of the buyer and year of the acquisition   | MB, 1915                                                  | ```SELECT ?s ?date WHERE { ?purchase zamo:hasCompanySeller zamo:ii-SD. ?purchase zamo:hasCompanyPurchaser ?s . ?purchase zamo:hasDate ?date} ```  |
| 3.  | Which events modified the organization "Arti fiorentine"? | Name of the agent responsible for the change,and name, establishment year and address of the new organization | LZ, 1920, <i>Les Arts de Paris</i>, Paris, Champs Élysées | ```SELECT ?s ?date ?new_name ?address ?city  WHERE { ?or_org zamo:hasName ?name. ?change zamo:hasOriginalOrganization ?or_org . ?change zamo:hasDate ?date . ?change zamo:hasParticipant ?s . ?change zamo:hasResultingOrganization ?new_org . ?new_org zamo:hasName ?new_name . ?new_org zamo:hasSeat ?seat . ?seat zamo:isLocatedIn ?address . ?address zamo:fallsWithin ?city . FILTER (str(?name) = "Arti fiorentine")}```|

****

In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/agent/3#>
```