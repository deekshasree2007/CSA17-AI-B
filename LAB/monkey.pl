% Monkey Banana Problem

% Initial state:
% Monkey = door
% Box = window
% Monkey is on floor
% Monkey does not have banana

% solve(State)
solve :-
    solve(state(door, window, floor, no)).

solve(state(_, _, _, yes)) :-
    write('Monkey has the bananas!'),
    nl.

solve(State) :-
    move(State, NewState),
    solve(NewState).

% Monkey moves
move(state(M, B, floor, H), state(P, B, floor, H)) :-
    M \= P,
    write('Monkey moves from '),
    write(M),
    write(' to '),
    write(P),
    nl.

% Monkey pushes the box
move(state(P, P, floor, H), state(P2, P2, floor, H)) :-
    write('Monkey pushes box from '),
    write(P),
    write(' to '),
    write(P2),
    nl.

% Monkey climbs onto the box
move(state(P, P, floor, H), state(P, P, onbox, H)) :-
    write('Monkey climbs onto the box'),
    nl.

% Monkey grabs bananas
move(state(middle, middle, onbox, no),
     state(middle, middle, onbox, yes)) :-
    write('Monkey grabs the bananas'),
    nl.
