## Competency Questions

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | With whom did the art dealer GT collaborate between 1979 and 1985? | Name and role and duration of the collaboration                                              | AB, Art historian consultant, 1980, 1982 <br><br> AA, Photographer, AA, 1960, 1985 | ```SELECT ?s ?role ?d1 ?d2 WHERE { zamo:i-ii-GT zamo:requestsServiceIn ?colab . ?s zamo:providesServiceIn ?colab . ?colab zamo:hasRole ?role . OPTIONAL {?colab zamo:hasStartDate ?d1 . ?colab zamo:hasEndDate ?d2 }}  ``` |
| 2.  | Which  photographers are active between 1960 and 2000? | Name of the photographer, duration of the collaboration and name of the collaborator                                                        | AA, 1960, 1985, GT <br><br> DD, 1950, 1975, FR| ```SELECT ?s ?d1 ?d2 ?artdealer WHERE { ?artdealer zamo:requestsServiceIn ?colab . ?s zamo:providesServiceIn ?colab . ?colab zamo:hasRole zamo:photographer . ?colab zamo:hasStartDate ?d1 . ?colab zamo:hasEndDate ?d2 FILTER(str(?d1) <= "2000" && str(?d2) >= "1960")} ``` |
| 3.  | Who are the art historian consultants who worked with FR to prepare his catalog?        | Name and field of expertise |GO, Baroque sculpture <br><br> LA, Mannerist painting <br><br> AB, History of the miniature | ```SELECT ?s ?domain WHERE { zamo:iii-FR zamo:requestsServiceIn ?colab . ?s zamo:providesServiceIn ?colab . ?colab zamo:hasRole zamo:art-historian-consultant . ?s zamo:isExpertIn ?domain} ```|
| 4.  | Who are the directors of <i>Antichità fiorentine</i>? In which period were they active? | Name and period of activity| AQ, 1910, 1920 <br><br> FZ, 1920, 1948 <br><br> MZ, 1948, 1970 | ```SELECT ?s ?d1 ?d2 WHERE { ?org zamo:hasName ?name . ?org zamo:requestsServiceIn ?colab . ?s zamo:providesServiceIn ?colab . ?colab zamo:hasStartDate ?d1 . ?colab zamo:hasEndDate ?d2 . FILTER (str(?name) = "Antichità fiorentine") } ORDER BY ?d1 ```|

****

In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/agent/4#>
```
