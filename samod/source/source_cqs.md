## Competency Questions

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|-----------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Who is the owner of GT’s archive?    | Name of the owner       | Foundation SZ SZ   | ``` SELECT ?s WHERE { zamo:i-archive-GT zamo:hasCurrentOwner ?s} ```       |
| 2.  | Which are the sources which can be used to reconstruct the life and the activity of KG? | Source and name of the owner | KG’s archive, Art Institute <br><br> Receipt  #KG1950,  Art  Institute <br><br>  Letter  to  SZ,  Art Institute <br><br> <i>KG. My life</i>, FG <br><br> <i>KG: An Art Collectionist</i> <br><br> <i>KG on the web</i> | ``` SELECT ?source ?owner WHERE { ?source zamo:isSourceFor OR zamo:isPrimarySourceFor OR zamo:isSecondarySourceFor ?reconstruction. ?reconstruction zamo:reconstructs zamo:ii-KG. OPTIONAL { ?source zamo:hasCurrentOwner ?owner}    OPTIONAL { ?source zamo:isContainedIn ?curatedhold. ?curatedhold zamo:hasCurrentOwner ?owner }} ``` |

Please, replace OR in the queries with `|`

In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/sources#>
```
