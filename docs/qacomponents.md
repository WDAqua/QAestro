---
layout: page
title: QA components
order: 2
---

# Semantic QA Component Descriptions
Following the Local-As-View approach, a QA component is defined using a conjunctive rule.
The head of the rule corresponds to the predicate that models the component, while the body of the rule is a conjunction of predicates in the QA ontology that represent the tasks performed by the component.
The following rules semantify the QA components discussed in [QA systems & tasks](/qasystems).

```
Agdistis(x,y,z) :- disambiguation(x,y,z,t), entity(x), question(y), disEntity(z)
Alchemy(y,z) :- disambiguation(x,y,z,t), question(y), disEntity(z)
StanfordNED(y,z) :- disambiguation(x,y,z,t), questiony), disEntity(z)
DBpediaspotlightNED(x,y,z) :- disambiguation(x,y,z,t), entity(x), question(y), disEntity(z)
OKAgdistis(t,z) :- disambiguation(x,y,z,t), template(t), disEntity(z)
AIDA(y,z) :- disambiguation(x,y,z,t), question(y), disEntity(z)
alexentity(y,z) :- disambiguation(x,y,z,t), question(y), disEntity(z)
quakisentity(y,z) :- disambiguation(x,y,z,t), question(y), disEntity(z)
fox(y,z) :- disambiguation(x,y,z,t), question(y), disEntity(z)
tagme(y,z) :-disambiguation(x,y,z,t), question(y), disEntity(z)
StanfordNER(y,x) :- recognition(y,x), question(y), entity(x)
DBpediaNER(y,x) :- recognition(y,x), question(y), entity(x)
casiaNER(y,x) :- recognition(y,x), question(y), entity(x)
selfwiringtokenizator(y,t1) :- tokenization(y,t1), question(y), token(t1)
AskTokenmerger(t1) :- tokenization(y,t1), token(t1)
selfpostagger(t1,p) :- postagging(y,t1,p), postag(p), token(t1) 
ApacheNLP(y,p,t1) :- tokenization(y,t1), postagging(y,t1,p), token(t1), postag(p), question(y)
ClearNLP(y,p,t1) :- tokenization(y,t1), postagging(y,t1,p), token(t1), postag(p), question(y)
TBSLpostagger(y,p,t1) :- tokenization(y,t1), postagging(y,t1,p), token(t1), question(y), postag(p)
TreeTagger(y,p,t1) :- tokenization(y,t1), postagging(y,t1,p), token(t1), question(y), postag(p)
SENNA(y,p,t1) :- tokenization(y,t1), postagging(y,t1,p), token(t1), question(y), postag(p)
Casiaparser(y,x,g) :- dependencyparsing(y,x,t1,p), question(y), entities(x), dependencygraph(g)
Chaosparser(y,g) :- dependencyparsing(y,x,t1,p), question(y), dependencygraph(g)
Isoftparser(y,g) :- dependencyparsing(y,x,t1,p), question(y), dependencygraph(g)
semparser(y,g) :- dependencyparsing(y,x,t1,p), question(y), dependencygraph(g)
qparser(y,g) :- dependencyparsing(y,x,t1,p), question(y), dependencygraph(g)
freyaparser(y,s) :- syntacticparsing(y,t1,p,s), question(y), syntacticgraph(s)
tbslparser(t1,p,s) :- syntacticparsing(y,t1,p,s), question(y), tokens(t1), postag(p), syntacticgraph(s)
ftriplegenerator(o,t3) :- triplegeneration(t,y,g,s,o,t3,t2), triplepatterns(t3), ontoConcepts(o)
powerlinguistic(y,t2) :- triplegeneration(t,y,g,s,o,t3,t2), linguistictripleform(t2), question(y)
aqualinguistic(y,t2) :- triplegeneration(t,y,g,s,o,t3,t2), linguistictripleform(t2), question(y)
Casiapattern(g,t3) :- triplegeneration(t,y,g,s,o,t3,t2), triplepatterns(t3), dependencygraph(g)
tbslpattern(s,t3) :- triplegeneration(t,y,g,s,o,t3,t2), triplepatterns(t3), syntacticgraph(s)
Ontologylookup(y,o) :- datamapping(y,x,p,g,p2,t2,t1,o,t3,m,t4,m1,n), question(y), ontoConcept(o)
consolidator(p2,o) :- datamapping(y,x,p,g,p2,t2,t1,o,t3,m,t4,m1,n), ontoConcept(o), potentialOntoConcepts(p2)
powermap(t2,m) :- datamapping(y,x,p,g,p2,t2,t1,o,t3,m,t4,m1,n), linguistictripleform(t2), mappingtable(m)
Aquamapper(t2,m) :- datamapping(y,x,p,g,p2,t2,t1,o,t3,m,t4,m1,n), linguistictripleform(t2), mappingtable(m)
HMMmodelling(p2,o) :- datamapping(y,x,p,g,p2,t2,t1,o,t3,m,t4,m1,n), potentialOntoConcepts(p2), ontoConcept(o)
freyaquerygenerator(t3,q) :- querygeneration(a,q1,t3,t4,g,g1,s,q), triplepattern(t3), sparql(q)
qakisquerygenerator(t3,q) :- querygeneration(a,q1,t3,t4,g,g1,s,q), triplepattern(t3), sparql(q) 
casiaqgenerator(t4,q1,q) :- querygeneration(a,q1,t3,t4,g,g1,s,q), ontologytriples(t4), questiontype(q1), sparql(q)
rtvqurygenerator(o,a,q) :- querygeneration(a,q1,t3,t4,g,g1,s,q), ontoConcepts(o), sparql(q), atype(a)
hawkquerygenerator(g,q) :- querygeneration(a,q1,t3,t4,g,g1,s,q), sparql(q), dependencygraph(g)
qanswerquerygenerator(g1,q) :- querygeneration(a,q1,t3,t4,g,g1,s,q), sparql(q), querygraph(g1)
xserquerygenerator(g,q) :- querygeneration(a,q1,t3,t4,g,g1,s,q), sparql(q), dependencygraph(g)
tbslquerygenerator(s,q) :- querygeneration(a,q1,t3,t4,g,g1,s,q), sparql(q), syntacticgraph(s)
poweranswer(m,ans) :- answergeneration(m,q,ans), mappingtable(m), finalanswer(ans)
aquaanswer(m,ans) :- answergeneration(m,q,ans), mappingtable(m), finalanswer(ans)
okbqaanswer(q,ans) :- answergeneration(m,q,ans), sparql(q), finalanswer(ans)
qakisatype(y,a) :- answertypeidentification(y,o,a), question(y), atype(a)
fanswertype(o,a) :- answertypeidentification(y,o,a), ontoConcept(o), atype(a)
```
