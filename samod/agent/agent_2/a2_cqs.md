## Competency Questions

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|---------------------------------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Which activities did ST found?                                                                   | Name and address of the activity, and establishment year       | <i>Arti d'Urbe</i>, 1949, Piazza delle Erbe, Rome, <br><br> P.za Navona, Rome, 1956    | ``` SELECT ?org ?date ?address ?place WHERE { zamo:i-ST zamo:participatesIn ?foundation . ?foundation zamo:hasFoundedOrganization ?org. OPTIONAL {?foundation zamo:hasDate ?date . ?org zamo:hasSeat ?seat. ?seat zamo:isLocatedIn ?address . ?address zamo:fallsWithin ?place}}```                                                                                                                                                                                                         |
| 2.  | Which are all the business activities referable to the P.family?                                  | Name and address of the activity, and establishment year            | <i>Artimercato</i>; <br><br> 1977, Via dei Fossi, Firenze                                                      | ``` SELECT DISTINCT ?s ?date ?seat ?address ?place WHERE { zamo:ii-venture-familyP zamo:isCarriedOutBy ?s. ?s rdf:type/rdfs:subClassOf* zamo:Organization. OPTIONAL { ?foundation a zamo:Foundation. ?foundation zamo:hasDate ?date.  ?foundation zamo:hasFoundedOrganization ?s. ?s zamo:hasSeat ?seat. ?seat zamo:isLocatedIn ?address . ?address zamo:fallsWithin ?place.}}```                                                                                                                                                                      |
| 3.  | Which are the activities opened in Rome between 1950 and 1985?  | Name and address of the activity, founder and establishment year   | P.za Navona, Roma, ST, 1956; <br><br> <i>Arti Libere</i> Roma, LZ e PS, 1980 | <i>Due to the length of the query, it was not possible to copy the text of the query in this cell; you can read it below|

<small><b>Third SPARQL Query</b>: ``` SELECT DISTINCT ?s ?seat ?found_year ?address ?city WHERE { ?org rdf:type/rdfs:subClassOf* zamo:ArtDealerOrganization. OPTIONAL {?founder zamo:participatesIn zamo:Foundation.  ?foundation zamo:hasDate ?date.  ?foundation zamo:hasFoundedOrganization ?org.}  ?s zamo:hasSeat ?seat.  ?seat zamo:isLocatedIn ?address . ?seat zamo:isActiveFrom ?found_year OPTIONAL {?address zamo:fallsWithin ?city} FILTER( (?address = zamo:rome || ?city = zamo:rome) && (str(?found_year) >= "1950" && str(?found_year) <= "1980") ) } ``` </small>

****

In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/agent/2#>
```