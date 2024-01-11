## Competency Questions

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|-------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Which artworks did SB study?  | Artwork, attributed artists and year of attribution | <i>San Rocco</i>, Guido Reni, 2001 <br><br> <i>Deposizione</i>, Domenichino, 2005. | ``` SELECT ?artwork ?date WHERE { ?s rdf:type/rdfs:subClassOf* zamo:AttributeAssignment . ?s zamo:hasAttributeType zamo:authorship . ?s zamo:isPerformedBy zamo:i-SB . ?s zamo:assignsAttributeTo ?artwork . ?s zamo:assignsAgentAsAttribute ?author . OPTIONAL {?s zamo:hasDate ?date}} ``` |
| 2.  | Which are the different value attributions of the canvas by Tintoretto? | Year and proposed value  | 1980, 15000€ <br><br> 1990, 35000€ <br><br> 1991, 30000€                     | ``` SELECT ?year ?v ?val WHERE { ?s a zamo:ValueProposition . ?s zamo:hasDate ?year . ?s zamo:assignsAttributeTo zamo:iii-canvas-tintoretto.  ?s zamo:hasProposedPrice ?price . ?price zamo:hasValue ?v . ?price zamo:hasCurrency ?val }  ``` |
| 3.  | Are there artworks under notification? | Artwork, year of notification  | <i>San Rocco</i>, 2008 | ```SELECT ?artwork ?year WHERE { ?s a zamo:LegalNotice . ?s zamo:hasValidityOn ?artwork . ?s zamo:isValidFrom ?year  } ```  |

In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/event/2#>
```