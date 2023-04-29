## Caveat

Per completare correttamente il <i>merge</i> dei diversi modelli, è stato necessario modificare gli individui relativi al primo scenario. Le domande di competenza sono quindi le seguenti:

1) 

```
SELECT ?agent  WHERE {   ?agent am00:providesServiceIn ?managerialPos .  am00:ex1_AuctionHouse_Antichità am00:requestsServiceIn ?managerialPos . am00:managingDirector am00:isSatisfiedBy ?managerialPos. }
```

2)

```
SELECT ?field  WHERE {  
?agent am00:providesServiceIn ?managerialPos . 
am00:ex2_ArtGallery_BeauxArts am00:requestsServiceIn ?managerialPos .
am00:managingDirector am00:isSatisfiedBy ?managerialPos.
?agent am00:hasEducationIn ?field
}
```

3)
```
SELECT DISTINCT ?agent  ?org WHERE {  
?agent am00:providesServiceIn ?managerialPos . 
?org am00:requestsServiceIn ?managerialPos .
am00:managingDirector am00:isSatisfiedBy ?managerialPos.
?org a am00:Organization . 
```

Si avvisa inoltre che alcuni compiler di query SPARQL non supportano alcune combinazione descritte dalla [Property Path Syntax](https://www.w3.org/TR/sparql11-query/) (ad esempio i <i>SequencePath</i>) o l'utilizzo di BIND, utilizzato in questi knowledge graph nella descrizione delle sedi per scindere l'indirizzo dalla città (es. in Python con ```rdflib```). Per risolvere questi problemi è sufficiente sciogliere i percorsi abbreviati o richiedere solamente  ```?location```. Di seguito, si allegano alcuni esempi relativi alla seconda casistica:

```
#2 ITER - CQ 1
SELECT DISTINCT ?org ?name ?date ?location WHERE {  am00:ex1_ST  am00:participatesIn ?foundation . ?foundation am00:hasFoundedOrganization ?org . OPTIONAL { ?org am00:hasName ?name . } ?foundation am00:hasDate ?date . ?org am00:hasSeat/am00:isLocatedIn ?location .}

#2 ITER - CQ 2
SELECT DISTINCT ?org ?name ?date ?location WHERE {  am00:ex2_VentureFamP am00:isCarriedOutBy ?org. ?org rdf:type/rdfs:subClassOf* am00:ArtDealerCompany . OPTIONAL { ?org am00:hasName ?name . } OPTIONAL { ?foundation am00:hasFoundedOrganization ?org . ?foundation am00:hasDate ?date }  ?org am00:hasSeat/am00:isLocatedIn ?location . }

# 2 ITER - CQ 3
SELECT DISTINCT ?org ?name ?location ?founder WHERE { ?founder am00:participatesIn ?foundation . ?foundation am00:hasFoundedOrganization ?org . ?org am00:hasSeat/am00:isLocatedIn ?location .  OPTIONAL { ?org am00:hasName ?name . } OPTIONAL { ?org am00:hasSeat/am00:isActiveFrom ?startDate }  OPTIONAL { ?org am00:hasSeat/am00:isActiveTo ?endDate } OPTIONAL { ?location am00:isContainedInPlace ?city }  FILTER((?city = am00:Roma || ?location = am00:Roma) && (str(?startDate) <= "1980" || str(?endDate) >= "1950")) }

#3 ITER - CQ1
SELECT ?name ?startDate ?endDate ?location WHERE { ?org am00:hasName ?name. ?org am00:hasSeat/am00:isActiveFrom ?startDate. ?org am00:hasSeat/am00:isActiveTo ?endDate . ?org am00:hasSeat/am00:isLocatedIn ?location. FILTER (?name="Galleria d'Arte Tesori"^^xsd:string)

#3 ITER - CQ2
SELECT ?agent ?location ?year WHERE { ?org am00:hasName ?name . ?org am00:hasName ?name . ?change am00:hasOriginalOrganization ?org. ?change am00:hasResultingOrganization ?new. ?change am00:hasParticipant ?agent. ?change am00:hasDate ?year. ?new am00:hasName ?newName . ?new am00:hasSeat/am00:isLocatedIn ?location . FILTER (?name="Arti fiorentine"^^xsd:string) }
```