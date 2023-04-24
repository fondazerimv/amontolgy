## Domande di competenza?

| No. | Domanda                                                                                                 | Formato della risposta                  | Risultato atteso                                        | SPARQL                                                                                                                                                                                                                                                                                                                           |
|-----|---------------------------------------------------------------------------------------------------------|-----------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Chi è il responsabile della casa d’aste <i>Antichità</i>?                                               | Nome dell'antiquario                    | SR                                                      | ``` SELECT ?agent  WHERE {  ?agent am00:hasRole ?manager . ?manager am00:isRoleIn am00:ex1_AuctionHouse_Antichità .} ```                                                                                                                                                                                                         |
| 2.  | In cosa è specializzato il responsabile della galleria <i>Beaux Arts</i>?                               | Ambito di competenza                    | Scultura barocca                                        | ``` SELECT ?field  WHERE {  ?agent am00:hasRole ?manager . ?manager am00:isRoleIn am00:ex2_ArtGallery_BeauxArts . ?agent am00:hasEducationIn ?field . } ```                                                                                                                                                                      |
| 3.  | Quali sono le organizzazioni che non sono gallerie d’arte?                                              | Nome dell'organizzazione e responsabile | Universo mostre, BV                                     | ```  SELECT DISTINCT ?agent  ?org WHERE {  ?agent am00:hasRole ?manager . ?manager am00:isRoleIn ?org. ?org a am00:Organization . }  ```                                                                                                                                                                                         |


Dalle query in SPARQL sono stati omessi i seguenti prefissi:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX am00: <http://www.semanticweb.org/am00/agents/overview#>
```
