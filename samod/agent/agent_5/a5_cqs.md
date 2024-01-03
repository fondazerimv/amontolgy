## Competency Questions

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | To which event did <i>Arti Belle</i> art gallery participate?                                              | Name, location and dates of the event  | Exhibition of <i>Arti Belle</i>, Roma, 2008, 2009 <br><br> BIF, AIT, Firenze, 2010 | ```SELECT ?name ?loc ?d ?d1 ?d2 ?organizer WHERE { ?org zamo:hasName ?org_name . ?org zamo:participatesIn OR zamo:organizes ?event . ?organizer zamo:organizes ?event . ?event zamo:hasName ?name . ?event zamo:takesPlaceIn ?loc . OPTIONAL {?event zamo:hasDate ?d} OPTIONAL {?event zamo:hasStartDate ?d1 . ?event zamo:hasEndDate ?d2} FILTER (str(?org_name) = "Arti belle")}```  |
| 2.  | Who participated in the editions of the event <i>Arti Romane</i> between 1981 and 1985? | Edition, location and organizer of the event and name of the participant | 1982, Roma, AIT, SA <br><br> 1984, Roma, AIT, SA| ```SELECT ?event_name ?d ?loc ?organizer ?participant WHERE { ?initiative zamo:hasName ?initiative_name . ?initiative zamo:recursAs ?event. ?event zamo:hasName ?event_name . ?participant zamo:participatesIn ?event . ?organizer zamo:promotes ?initiative . ?event zamo:takesPlaceIn ?loc . ?event zamo:hasDate ?d . FILTER (str(?initiative_name) = "Arti romane")} ```   |
| 3.  | Who are the members of the association AIT? | Name and duration of the membershipt |SA, 1970, 1985 <br><br> <i>Art</i>, 1977, 1988  | ```SELECT * WHERE {?membership zamo:hasReferenceAssociation zamo:ait-association. ?member zamo:joinsAsMember ?membership . ?membership zamo:hasStartDate ?d1 . ?membership zamo:hasEndDate ?d2}```|

Please, replace OR in the queries with `|`

In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/agent/5#>
```
