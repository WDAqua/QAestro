---
layout: default
title: Home
---

# About QAestro
QAestro is an ontology-based framework to semantically describe QA components and QA developer requirements and to produce QA component orchestrations based on these semantic descriptions.

We introduce an ontology to model QA tasks and exploit the _Local-As-View_ (LAV) approach to express QA components.  In addition, QA developer requests are represented as conjunctive queries involving the concepts included in the ontology. 

The problem of QA component orchestrations into pipelines can be afterwards cast to the LAV <cite>[Query Rewriting Problem (QRP)][1]</cite> which is further translated into a logical theory.  Given the logical theory, state-of-the art <cite>[SAT solvers (QRP)][1]</cite> can find the solution models in the combinatorial space of all solutions which eventually correspond to QA component orchestrations.

QAestro has been built on top of the SAT solver <cite>[MCDSAT][3]</cite>.

_The QAestro project is part of the [WDAqua project](http://wdaqua.eu/) which has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement no 642795._

[1]: http://www.seas.upenn.edu/~zives/03s/cis650/view-survey.pdf
[2]: https://www.cs.cornell.edu/gomes/papers/satsolvers-kr-handbook.pdf
[3]: https://github.com/bonetblai/mcdsat