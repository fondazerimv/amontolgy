## Domande di competenza

| No. | Domanda                           | Formato della risposta     | Risultato atteso                                                                                                                                     | SPARQL                                                                                                                                                                                                                                                                                                  |
|-----|-----------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Chi possiede l’archivio di GT     | Nome del possessore        | Fondazione SZ                                                                                                                                        | ``` SELECT ?agent WHERE { am00:ex1_archive_GT am00:hasCurrentOwner ?agent } ```                                                                                                                                                                                                                         |
| 2.  | Quali sono le fonti relative a KG | Fonte, nome del possessore | Archivio, Art Institute; <br> Ricevuta #KG1950, Art Institute; <br> Lettera a SZ, Art Institute; <br> <i>KG. My life</i>, FG; <br> <i>KG: An Art Collectionist</i>, n.a.; <br> KG on the web, n.a. | ```  SELECT DISTINCT ?source ?agent WHERE { ?source am00:isSourceFor \| am00:isPrimarySourceFor \| am00:isSecundarySourceFor am00:ex2_KG.    OPTIONAL { 	?source am00:hasCurrentOwner ?agent    }    OPTIONAL { 	?source ?isContainedIn ?curatedhold. 	?curatedhold am00:hasCurrentOwner ?agent    } } ``` |


Dalle query in SPARQL sono stati omessi i seguenti prefissi:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX am00: <http://www.semanticweb.org/am00/sources#>
```
