## Competency Questions

| No. | Question | Answer  | Example                                       | SPARQL |
|-----|---------------------------------------------------------------------------------------------------------|----------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | When did QC buy the painting <i>Sacra conversazione</i>?                                                | Year                                   | 1978                                                    | ``` SELECT ?d WHERE { ?transaction zamo:hasReceiver zamo:i-QC .  ?transaction zamo:transfersCustodyOf ?lot . ?lot zamo:consistsOf zamo:i-sacra-conversazione. ?transaction zamo:hasDate ?d }```   |
| 2.  | Who are the clients of ST?                | Name of the clients     | QC                                                      | ``` SELECT ?s WHERE {  ?transaction zamo:hasSurrender zamo:i-ST . ?transaction zamo:hasReceiver ?s . } ```  |
| 3.  | Who is the last owner of the artworks exhibited at <i>Neoclassicismo</i>?  | Artwork and last owner    | Terracotta by Canova, PP                                | ``` SELECT ?s ?work WHERE { ?transaction zamo:hasPurpose zamo:ii-exhibition-neoclassicism . ?transaction zamo:hasSurrender ?s .  ?transaction zamo:transfersCustodyOf ?lot.  ?lot zamo:consistsOf ?work} ```|
| 4.  | Who participated in the acquisition of Romano’s <i>Birth of Bacchus</i>? | Name and role of the different actors | Museo Civico di Belle Arti in Rome, buyer <br><br> TD, facilitator <br><br> RE, seller | ``` SELECT ?actor ?role WHERE { ?transaction a zamo:Purchase . ?transaction ?role ?actor . ?actor a zamo:Agent . ?transaction zamo:transfersPropertyOf ?lot.  ?lot zamo:consistsOf zamo:iv-birth-baccus-romano``` |                                                                                            |


In these SPARQL queries, the following prefixes should be stated:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX zamo: <http://www.w3.org/zamo/event/1#>
```
