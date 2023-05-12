## Domande di competenza?

| No. | Domanda                                                                                                 | Formato della risposta                                           | Risultato atteso                                          | SPARQL                                                                                                                                                                                                                                                                                                                           |
|-----|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | A quali eventi ha partecipato la galleria “Arti Belle”?                                                   | Nome, organizzatore, sede dell’evento, periodo                          | [Arti Belle, Roma, 2008, 2009], [BIF, AIT, Firenze, 2010] | ``` SELECT * WHERE {  am00:ex1_artiBelle am00:organizes \ am00:participatesIn ?event . ?event ^am00:organizes ?organizer . OPTIONAL { ?event am00:hasDate ?date . } OPTIONAL { ?event am00:hasStartDate ?startDate . ?event am00:hasEndDate ?endDate . } }```                                                                                                                                                                                                         |
| 2.  | Quali sono le società che hanno partecipato alle edizioni comprese tra 1981 e 1985 dell’evento “Arti romane”?  | Edizione dell’evento, sede, organizzatore dell’evento, partecipante | [1982, Roma, AIT, SA], [1984, Roma, AIT, SA]| ``` SELECT * WHERE {  ?agent am00:participatesIn ?event . am00:ex2_ArtiRomane am00:recursAs ?event . ?event am00:hasDate ?date . FILTER(str(?date) <= "1985" \\ str(?date) >= "1982") }```                                                                                                                                                                      |
| 3.  | Trova tutti i membri dell’organizzazione AIT  | Nome, Periodo di associazione |[SA, 1970, 1985], [“Art”, 1977, 1988]  | ```  SELECT ?agent ?startDate ?endDate WHERE {  ?membership am00:hasReferenceAssociation am00:AIT . ?agent am00:joinsAsMember ?membership . ?membership am00:hasStartDate ?startDate . ?membership am00:hasEndDate ?endDate . }```|

> A causa della formattazione md è stato necessario sostituire nelle prime due query il carattere | con \. Va quindi corretto come segue:
1) ```WHERE {  am00:ex1_artiBelle am00:organizes | am00:participatesIn ?event .```
2) ```FILTER(str(?date) <= "1985" || str(?date) >= "1982")```
****

Dalle query in SPARQL sono stati omessi i seguenti prefissi:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX am00: <http://www.semanticweb.org/am00/agents/events_associations#>
```
