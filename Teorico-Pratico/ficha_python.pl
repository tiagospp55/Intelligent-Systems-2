%% Exercicio 1 %%
% Dada uma lista, retorna o seu comprimento 

comprimento([], 0).
comprimento([_|T], N) :- comprimento(T, N0), N is N0 + 1.

%% Exercicio 2 %%
% Dada uma lista de números, retorna a respetiva soma

soma([],0)
soma([H|T], S):- soma(T, S0), S is S0 + H1.


%% Exercicio 3 %%
% Dada uma lista e um elemento, verifica se o elemento ocorre na lista

ocorre(_, [], no).
ocorre(X, [X|_], yes) :- !, ocorre(X, [_|T], R) :- ocorre(X, T, R).
