## Organization of the materials for SAMOD Methodology implementation

This subfolder contains the material produced during the iterations foreseen by [SAMOD Methodology](https://essepuntato.it/samod/), subdivided into the three different modules in which the ontology is articulated (agents, events and sources). 

![Samod methodology](https://essepuntato.it/samod/img/10000201000008180000044441F74BCB.png "a title").

In each of the three folders you can find Motivating Scenario, a set of examples use case, a list of Informal Competency Questions (in English), their translation into SPARQL, a Graffoo diagram of the model in .png format (along with its .graphml file), a TBox and a ABox (created and tested with Protegé). Following this methodology, the standalone modelets have been iteratively merged and refactored. Please note that in this last step also the URI of the ontology has been changed, which should be taken into account when trying to reproduce the SPARQL competency questions.

> `https://w3id.org/zeri/ontology/zamo/`

The different modules are specified as `zamo/agents#`, `zamo/events#`, and `zamo/sources#`.
