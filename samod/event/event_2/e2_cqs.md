## Competency Questions

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|-------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Which artworks did SB study?  | Artwork, attributed artists and year of attribution | <i>San Rocco</i>, Guido Reni, 2001 <br><br> <i>Deposizione</i>, Domenichino, 2005. | ``` SELECT  ?object ?att_author ?year  WHERE { ?expertise am00:isCarriedOutBy am00:a_SB. ?expertise am00:isFocusedOn ?object. ?expertise am00:recognizesAsAuthor ?att_author. ?expertise am00:hasDate ?year. } ``` |
| 2.  | Which are the different value attributions of the canvas by Tintoretto? | Year and proposed value  | 1980, 15000€ <br><br> 1990, 35000€ <br><br> 1991, 30000€                     | ``` SELECT ?year ?val  WHERE { ?a a am00:ValueProposition. ?a am00:isFocusedOn am00:b_tintoretto_canvas. ?a am00:hasProposedPrice ?price. ?a am00:hasDate ?year. ?price am00:hasValue ?val.  } ORDER BY ?year  ``` |
| 3.  | Are there artworks under notification? | Artwork, owner, year of notification  | <i>San Rocco</i>, 2008, PT | ``` SELECT ?obj ?year ?owner WHERE {    ?notifica am00:isValidFrom ?year.    ?notifica am00:hasValidityOn ?obj.    ?obj am00:hasCurrentOwner ?owner }   ```  |

In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/event/2#>
```