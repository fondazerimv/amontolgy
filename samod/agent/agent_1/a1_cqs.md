## Competency Questions

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|---------------------------------------------------------------------------------------------------------|-----------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Who is the managing director of the auction house <i>Antichità</i>?                                               | Name of the director                    | SR                                                      | ```SELECT ?person WHERE {zamo:i-antichità-auction-house  zamo:requestsServiceIn ?collaboration. ?person zamo:providesServiceIn ?collaboration.}```                                                                                                                                                                                                         |
| 2.  | In which field is the managing director of <i>Beaux Arts</i> specialized?                               | Subject                    | Baroque Sculpture                                       | ```SELECT ?subject WHERE { zamo:ii-beauxarts-art-gallery  zamo:requestsServiceIn ?collaboration. ?director zamo:providesServiceIn ?collaboration. ?director zamo:hasEducationIn ?subject. } ```                                                                                                                                                                      |
| 3.  | Are there organizations which are not art dealers?                                              | Name of the director and of the organization | BV, Universo mostre                                   | ```SELECT ?organization ?director WHERE { ?organization  zamo:requestsServiceIn ?collaboration. ?director zamo:providesServiceIn ?collaboration. ?organization a zamo:Organization. } ```                                                                                                                                                                                         |


In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/agent/1#>
```
