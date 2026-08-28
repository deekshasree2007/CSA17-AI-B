% Bird Database

bird(eagle).
bird(parrot).
bird(pigeon).
bird(sparrow).
bird(ostrich).
bird(penguin).

% Birds that can fly
can_fly(eagle).
can_fly(parrot).
can_fly(pigeon).
can_fly(sparrow).

% Birds that cannot fly
cannot_fly(ostrich).
cannot_fly(penguin).

% Function to check whether a bird can fly or not

check_bird(Bird) :-
    can_fly(Bird),
    write(Bird),
    write(' can fly.').

check_bird(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    write(' cannot fly.').
