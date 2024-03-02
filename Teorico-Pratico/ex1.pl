%% Exercicio A %%
occurs(X, [X|_]). % X occurs in the list if it is the first element
occurs(X, [_|T]) :- occurs(X, T). % X occurs in the list if it occurs in the tail

:- occurs(3, [1,2,3,4,5]), writeln(yes); writeln(no).
:- occurs(6, [1,2,3,4,5]), writeln(yes); writeln(no).




%% Exercicio B  %%

concatenar([], L, L). % concatenating an empty list with another list results in the same list
concatenar([X|L1], L2, [X|L3]) :- concatenar(L1, L2, L3). % concatenating a list with another list results in a list with the first element of the first list and the concatenation of the rest of the first list with the second list

:- concatenar([1, 2, 3], [4, 5, 6], Resultado), writeln(Resultado).



%% Exercicio C  %%

inverter([], []).                                                                 % inverting an empty list results in an empty list
inverter([H|T],I) :- inverter(T,IT), append(IT,[H],I).                           % inverting a list results in the concatenation of the inverted tail with the head

:- inverter([1, 2, 3, 4, 5], Resultado), writeln(Resultado).


%% Exercicio D  %%

% counting the number of appearences of an element in a list
conta(_, [], 0). % counting the number of appearences of an element in an empty list results in 0
conta(X,[X|T], N) :- contar(X,T,N0), N is N0+1.
conta(X,[H|T], N) :- X \= H, contar(X,T,N). % if the head of the list is different from the element we are counting, we continue counting in the tail



% Com cut
conta(_, [], 0). % counting the number of appearences of an element in an empty list results in 0
conta(X,[X|T], N) :- !, contar(X,T,N0), N is N0+1.
conta(X,[H|T], N) :- contar(X,T,N). % if the head of the list is different from the element we are counting, we continue counting in the tail

minimum(X, [H|])

%% Exercicio E  %%

% finding the minimum element in a list
minimo([X], X).                                    % the minimum element in a list with only one element is the element itself
minimo([H|T], H) :- minimo(T, M), H =< M.          % the minimum element in a list is the head if it is less than or equal to the minimum of the tail
minimo([H|T], M) :- minimo(T, M), H > M.           % the minimum element in a list is the minimum of the tail if the head is greater than the minimum of the tail

:- minimo([1, 2, 3, 4, 5], Resultado), writeln(Resultado).
:- minimo([5, 4, 3, 2, 1], Resultado), writeln(Resultado).

%% Exercicio F  %%
% finding the maximum element in a list

%% Exercicio G  %%
% Merge: return a sorted list containing all the elements of two sorted lists

merge_sorted([], L, L).
merge_sorted(L, [], L)
merge_sorted([H1|T1], [H2|T2], [H1|T3]) :- H1 =< H2, !, merge_sorted(T1, [H2|T2], [H1| MergedTail])
merge_sorted([H1|T1], [H2|T2], [H2|T2]) :- merge_sorted([H1|T1], T2, [H2| MergedTail])

%% Exercicio H  %%
% Set all subsets of a given element - produce a list of list representing all subsets of the input subsets

subsets([], [[]]).
subsets([H|T]) :- subsets(T,SS) :- subsets(T, SST1), distribute(H, SST1, SST2), append(H, SST1, SST2, SS).

distribute(X,[],[X])
distribute([],X,[X])
distribute(X, [H|T], [[X|H]|T2]) :- distribute(X, T, T2). 

%%%%%%%%%%%% ou utilizando o findall para acrescentar a todos os subsets ao conjunto  %%%%%%%%%

subsets([], [[]]).
subsets([H|T]) :- subsets(T,SS) :- subsets(T, SST1), findall([H|T], SST, SST2), append(H, SST1, SST2, SS).

distribute(X,[],[X])
distribute([],X,[X])
distribute(X, [H|T], [[X|H]|T2]) :- distribute(X, T, T2). 

%% Exercicio I  %%
% Produce a list of pairs formed by elements in equal positions in the input lists
equal_position([], [], []).
equal_position([H1|T1], [H|T2], [[H1, H2]|T3]) :- equal_position(T1, T2, T3).