---
layout: page
title: QAestro results
order: 3
---



## QA Developer Requirements
The following 30 QA developer requirements were tested for standalone QA tasks and QA pipelines. These pipelines integrate two, three, four, or five QA tasks. The link _QA orchestrations_ directs to the possible orchestrations that QAestro produces given the specific requirement.

### with one QA Task

__Q1__: `q(Z2,Z3) :- disambiguation(Z1,Z2,Z3,Z4)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_1.txt)

__Q2__: `q(Z1,Z2) :- recognition(Z1,Z2)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_2.txt)

__Q3__: `q(Z1,Z2) :- tokenization(Z1,Z2)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_3.txt)

__Q4__: `q(Z1,Z2) :- postagging(Z1,Z2)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_4.txt)

__Q5__: `q(Z1,Z2) :- dependencyparser(Z1,Z2,Z3,Z4)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_5.txt)

__Q6__: `q(Z4) :- syntacticparser(Z1,Z2,Z3,Z4)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_6.txt)

__Q7__: `q(Z2,Z7) :- triplegen(Z1,Z2,Z3,Z4,Z5,Z6,Z7)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_7.txt)

__Q8__: `q(Z5) :- datamapper(Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_8.txt)

__Q9__: `q(Z3,Z8) :- querygen(Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_9.txt)

__Q10__: `q(Z1,Z3) :- answergen(Z1,Z2,Z3)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_10.txt)

__Q11__: `q(Z1,Z3) :- answertypeid(Z1,Z2,Z3)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_11.txt)

### with two QA Tasks
__Q12__: `q(Z1,Z3) :- recognition(Z2,Z1), disambiguation(Z1,Z2,Z3,Z4)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_12.txt)

__Q13__: `q(Z2) :- recognition(Z5,Z6), disambiguation(Z1,Z2,Z3,Z4)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_13.txt)

__Q14__: `q(Z6,Z10) :- datamapper(Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13), answergen(Z10,Z14,Z15)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_14.txt)

__Q15__: `q(Z6) :- datamapper(Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13), answergen(Z10,Z14,Z15)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_15.txt)

__Q16__: `q(Z2) :- dependencyparser(Z2,Z8,Z9,Z10), triplegen(Z1,Z2,Z3,Z4,Z5,Z6,Z7)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_16.txt)

__Q17__: `q(Z2) :- triplegen(Z1,Z2,Z3,Z4,Z5,Z6,Z7), datamapper(Z2,Z8,Z9,Z0,Z10,Z11,Z12,Z13,Z14,Z15,Z16,Z17,Z18)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_17.txt)

__Q18__: `q(Z1,Z2) :- tokenization(Z1,Z2), postagging(Z1,Z2,Z3)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_18.txt)

__Q19__: `q(Z8) :- querygen(Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8), answergen(Z9,Z8,Z10)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_19.txt)

__Q20__: `q(Z3,Z8) :- querygen(Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8), answertypeid(Z9,Z8,Z10)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_20.txt)

### with three QA Tasks
__Q21__: `q(Z1,Z2) :- recognition(Z2,Z3), disambiguation(Z1,Z2,Z3,Z4), querygen(Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_21.txt)

__Q22__: `q(Z2,Z3) :- recognition(Z2,Z3), disambiguation(Z1,Z2,Z3,Z4), querygen(Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_22.txt)

__Q23__: `q(Z2,Z3) :- disambiguation(Z1,Z2,Z3,Z4), querygen(Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13), answergen(Z14,Z13,Z15)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_23.txt)

__Q24__: `q(Z1,Z2) :- disambiguation(Z1,Z2,Z3,Z4), querygen(Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13), answergen(Z14,Z13,Z15)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_24.txt)

__Q25__: `q(Z2,Z3) :- tokenization(Z2,Z5), recognition(Z2,Z3), disambiguation(Z1,Z2,Z3,Z4)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_25.txt)

__Q26__: `q(Z2,Z3) :- postagging(Z2,Z8,Z9),recognition(Z2,Z3), disambiguation(Z1,Z2,Z3,Z4)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_26.txt)

### with four QA Tasks
__Q27__: `q(Z2,Z3) :- tokenization(Z2,Z5), recognition(Z2,Z3), disambiguation(Z1,Z2,Z3,Z4), answertypeid(Z2,Z6,Z7)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_27.txt)

__Q28__: `q(Z2,Z3) :- tokenization(Z2,Z5), recognition(Z2,Z3), disambiguation(Z1,Z2,Z3,Z4), dependencyparser(Z2,Z1,Z6,Z7)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_28.txt)

### with five QA Tasks
__Q29__: `q(Z2,Z9,Z3) :- tokenization(Z2,Z5), recognition(Z2,Z3), disambiguation(Z1,Z2,Z3,Z4), dependencyparser(Z2,Z1,Z6,Z7), answergen(Z8,Z9,Z10)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_29.txt)

__Q30__: `q(Z2,Z3) :- tokenization(Z2,Z5), recognition(Z2,Z3), disambiguation(Z1,Z2,Z3,Z4), dependencyparser(Z2,Z1,Z6,Z7), answertypeid(Z2,Z8,Z9)` -> [QA orchestrations](https://github.com/WDAqua/QAestro/blob/master/qa/output/output_query_30.txt)
