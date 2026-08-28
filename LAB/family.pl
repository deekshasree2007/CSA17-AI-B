% Family Tree Database

% Facts
male(ravi).
male(rajesh).
male(amit).
male(rohit).
male(arjun).

female(priya).
female(sita).
female(anjali).
female(neha).
female(kavya).

% Parent relationships
parent(ravi, amit).
parent(priya, amit).

parent(ravi, anjali).
parent(priya, anjali).

parent(rajesh, ravi).
parent(sita, ravi).

parent(rajesh, rohit).
parent(sita, rohit).

parent(amit, arjun).
parent(neha, arjun).

% Rules

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

brother(X, Y) :-
    male(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.

sister(X, Y) :-
    female(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandfather(X, Y) :-
    male(X),
    parent(X, P),
    parent(P, Y).

grandmother(X, Y) :-
    female(X),
    parent(X, P),
    parent(P, Y).
