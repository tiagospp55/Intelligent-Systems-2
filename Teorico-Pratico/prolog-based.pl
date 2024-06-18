%% exercicio 1

occurs(X,[X|T]).
occurs(X,[H|T]):-occurs(X,T).

%% Exercicio 2

concatenate([],L,L).
concatenate([H|T],L2,[H,L3]) :- concatenate(T,L2,L3)

%% exercicio 3
%% Altamente ra eu perceber o que fiz para aqui :))

invert([],[]).
invert([H|T], I) :- inverter(T,IT), append(IT, [H], I).  %% IT será a cauda do que é invertido 

%% exercicio 4

%% sem cut

count(_,[],0).
count(X,[X,T],N) :- count(X, T, N0), N is N0+1
count(X, [H|T], N) :- X \=H, count(X,T,N)

%% com cut


count(_,[],0).
count(X,[X,T],N) :- !,count(X, T, N0), N is N0+1
count(X, [H|T], N) :- X \=H, count(X,T,N)

%% exercicio 5

min([X], X)
min([H|T], H) :- min(T, M), H =< M
min([H|T], M) :- MIN(T,M), H > M



