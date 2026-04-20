% Facts 
 
male(shivsagar). 
male(krishna). 
male(harshit). 
 
female(sharda). 
female(sunita). 
female(janhvi). 
parent(shivsagar, krishna). 
parent(shivsagar, sunita). 
parent(shardha, krishna). 
parent(shardha, sunita). 
parent(krishna, harshit). 
parent(janhvi, harshit). 
 
% Rules 
 
father(X, Y) :- 
parent(X, Y), 
male(X). 
 
mother(X, Y) :- 
parent(X, Y), 
female(X). 
sibling(X, Y) :- 
parent(Z, X), 
parent(Z, Y), 
X \= Y. 
grandparent(X, Y) :- 
parent(X, Z), 
parent(Z, Y). 
 
ancestor(X, Y) :- 
parent(X, Y). 
 
ancestor(X, Y) :- 
parent(X, Z), 
ancestor(Z, Y). 
