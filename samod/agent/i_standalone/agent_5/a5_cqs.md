## Competency Questions

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | To which event did <i>Arti Belle</i> art gallery participate?                                              | Name, seat and dates of the event  | <i>Arti Belle</i>, Roma, 2008, 2009 <br><br> BIF, AIT, Firenze, 2010 | ``` SELECT * WHERE {  am00:ex1_artiBelle am00:organizes \ am00:participatesIn ?event . ?event ^am00:organizes ?organizer . OPTIONAL { ?event am00:hasDate ?date . } OPTIONAL { ?event am00:hasStartDate ?startDate . ?event am00:hasEndDate ?endDate . } }```  |
| 2.  | Who participated in the editions of the event <i>Arti Romane</i> between 1981 and 1985? | Edition, seat and organizer of the event and name of the participant | 1982, Roma, AIT, SA <br><br> 1984, Roma, AIT, SA| ``` SELECT * WHERE {  ?agent am00:participatesIn ?event . am00:ex2_ArtiRomane am00:recursAs ?event . ?event am00:hasDate ?date . FILTER(str(?date) <= "1985" \\ str(?date) >= "1982") }```   |
| 3.  | Who are the members of the association AIT? | Name and duration of the membershipt |SA, 1970, 1985 <br><br> <i>Art</i>, 1977, 1988  | ```  SELECT ?agent ?startDate ?endDate WHERE {  ?membership am00:hasReferenceAssociation am00:AIT . ?agent am00:joinsAsMember ?membership . ?membership am00:hasStartDate ?startDate . ?membership am00:hasEndDate ?endDate . }```|


In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/agent/5#>
```
