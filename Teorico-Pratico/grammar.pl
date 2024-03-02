
:- discontiguous np/2, vp/2, properNoun/2, commonNoun/2.
:- discontiguous pronoun/2, pp/2, preposition/2, adverb/2.
:- discontiguous article/2, verb/2, adjective/2.

:- discontiguous example/2.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(1,[the,breeze,is,smelly]).
example(2,[aveiro,is,beautiful]).
example(3,[aveiro,is,a,city]).
example(4,[peter,is,a,man]).
example(5,[the,cats,are,beautiful]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

sentence --> np, vp.

np --> properNoun.
np --> article, commonNoun.

vp --> verb, np.
vp --> verb, adjective.

commonNoun --> [breeze].
commonNoun --> [city].
commonNoun --> [man].
commonNoun --> [men].
commonNoun --> [cat].
commonNoun --> [cats].

properNoun --> [peter].
properNoun --> [aveiro].

verb --> [is].
verb --> [are].

adjective --> [smelly].
adjective --> [beautiful].

article --> [the].
article --> [a].
article --> [an].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(6,[peter,is,in,aveiro]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

vp --> verb, pp.

pp --> preposition, np.

preposition --> [in].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(7,[he,is,in,aveiro]).
example(8,[she,loves,him]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

np --> pronoun.

verb --> [love].
verb --> [loves].

pronoun --> [i].
pronoun --> [you].
pronoun --> [he].
pronoun --> [she].
pronoun --> [we].
pronoun --> [they].

pronoun --> [me].
pronoun --> [you].
pronoun --> [him].
pronoun --> [her].
pronoun --> [them].
pronoun --> [us].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example( 9,[you,give,the,gold,to,me]).
example(10,[you,give,me,the,gold]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

vp --> verb, np, np.
vp --> verb, np, pp.

verb --> [give].
verb --> [gives].

commonNoun --> [gold].

preposition --> [to].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(11,[they,smell,the,wumpus]).
example(12,[the,wumpus,smells,awful]).
example(13,[peter,smells,like,a,wumpus]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

verb --> [smell].
verb --> [smells].

adjective --> [awful].

preposition --> [like].

commonNoun --> [wumpus].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(14,[the,cat,is,here]).
example(15,[peter,is,there]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

vp --> verb, adverbe.

adverbe --> [here].
adverbe --> [there].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(16,[the,beautiful,cat,died]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

vp --> verb.

np --> article, adjective, commonNoun.


% =========================================

parse_all_examples(L)
:- findall(X,(example(X,Words),sentence(Words,[])),L).


