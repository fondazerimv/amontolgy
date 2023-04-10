## Domande di competenza?

| No. | Domanda                                                     | Formato della risposta                                      | Risultato atteso   | SPARQL|
|-----|-------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Quali opere ha studiato SB?                                 | Lista di opere, artista attribuito e anno dell'attribuzione | San Rocco, Guido Reni, 2001; Deposizione, Domenichino, 2005. | ``` SELECT  ?object ?att_author ?year  WHERE { ?expertise am00:isCarriedOutBy am00:a_SB. ?expertise am00:isFocusedOn ?object. ?expertise am00:recognizesAsAuthor ?att_author. ?expertise am00:hasDate ?year. } ``` |
| 2.  | Quali sono stati valori attribuiti all’opera di Tintoretto? | Lista di prezzo e anno                                      | 1980, 15000€; 1990, 35000€; 1991, 30000€                     | ``` SELECT ?year ?val  WHERE { ?a a am00:ValueProposition. ?a am00:isFocusedOn am00:b_tintoretto_canvas. ?a am00:hasProposedPrice ?price. ?a am00:hasDate ?year. ?price am00:hasValue ?val.  } ORDER BY ?year  ``` |
| 3.  | Quali opere sono sotto notifica dello Stato?                | Lista di opere, anno della notifica e proprietario          | San Rocco, 2008, PT                                          | ``` SELECT ?obj ?year ?owner WHERE {    ?notifica am00:isValidFrom ?year.    ?notifica am00:hasValidityOn ?obj.    ?obj am00:hasCurrentOwner ?owner }   ```                                                        |

Dalle query in SPARQL sono stati omessi i seguenti prefissi:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX am00: <http://www.semanticweb.org/am00/events/attribute_assignment#>
```
