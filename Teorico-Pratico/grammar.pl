
:- discontiguous np/4, vp/4, properNoun/4, commonNoun/4.
:- discontiguous pronoun/4, pp/3, preposition/3, adverb/3.
:- discontiguous article/4, verb/4, adjective/3.

:- discontiguous example/2.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(1,[the,breeze,is,smelly]).
example(2,[aveiro,is,beautiful]).
example(3,[aveiro,is,a,city]).
example(4,[peter,is,a,man]).
example(5,[the,cats,are,beautiful]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

sentence(s(NP,VP)) --> np(Num,NP,subj), vp(Num,VP).

np(Num,np(Noun)) --> properNoun(Num,Noun).
np(Num,np(Art,Noun)) --> article(Num,Art), commonNoun(Num, Noun).

vp(Num, vp(Verb,NP)) --> verb(Num,Verb), np(_,NP,obj).
vp(Num, vp(Verb,Adj)) --> verb(Num,Verb), adjective(Adj).

commonNoun(sing,cnoun(breeze)) --> [breeze].
commonNoun(sing,cnoun(city)) --> [city].
commonNoun(sing,cnoun(man)) --> [man].
commonNoun(sing,cnoun(men)) --> [men].
commonNoun(sing,cnoun(cat)) --> [cat].
commonNoun(sing,cnoun(cats)) --> [cats].

properNoun(sing, pnoun(peter)) --> [peter].
properNoun(sing, pnoun(aveiro)) --> [aveiro].

verb(sing, verb(is)) --> [is].
verb(plur, verb(are)) --> [are].

adjective(adj(smelly)) --> [smelly].
adjective(adj(beatiful)) --> [beautiful].

%%% Falta daqui
article(sing, art(the)) --> [the].
article(sing, art(a)) --> [a].
article(sing, art(an)) --> [an].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(6,[peter,is,in,aveiro]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Awui
vp(Num, vp(Verb,PP)) --> verb(Num,Verb), pp(PP).

pp(pp(Prep,Np)) --> preposition(Prep), np(_,NP, obj).

preposition(prep(in)) --> [in].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(7,[he,is,in,aveiro]).
example(8,[she,loves,him]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

np(Num,np(Pron)) --> pronoun(Num,Pron).

verb(sing,verb(love)) --> [love].
verb --> [loves].

pronoun(sing,pron(i)) --> [i].
pronoun(sing, pron(you)) --> [you].
pronoun(sing, pron(he)) --> [he].
pronoun(sing, pron(she)) --> [she].
pronoun(sing, pron(we)) --> [we].
pronoun(sing, pron(they)) --> [they].

pronoun(sing, pron(me)) --> [me].
pronoun(sing, pron(you)) --> [you].
pronoun(sing, pron(him)) --> [him].
pronoun(sing, pron(her)) --> [her].
pronoun(sing, pron(them)) --> [them].
pronoun(sing, pron(us)) --> [us].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example( 9,[you,give,the,gold,to,me]).
example(10,[you,give,me,the,gold]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

vp(Num,vp(Verb, NP1,NP2)) --> verb(Num,Verb), np(_,NP1,obj), np(_,NP2,obj).
vp(Num,vp(Verb, NP,PP)) --> verb(Num,Verb), np(_,NP,obj), pp(PP).

verb(sing, verb(give)) --> [give].
verb(sing, verb(gives)) --> [gives].

commonNoun(sing(cnoun(gold))) --> [gold].

preposition(prep(to)) --> [to].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(11,[they,smell,the,wumpus]).
example(12,[the,wumpus,smells,awful]).
example(13,[peter,smells,like,a,wumpus]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

verb(sing, verb(smell)) --> [smell].
verb(sing,verb(smeels)) --> [smells].

adjective(adj(awful)) --> [awful].

preposition(prep(like)) --> [like].

commonNoun(sing, cnoun(wumpus)) --> [wumpus].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(14,[the,cat,is,here]).
example(15,[peter,is,there]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

vp(Num, vp(Verb, Adv)) --> verb(Num,Verb), adverbe(Adv).

adverbe(adv(here)) --> [here].
adverbe(adv(there)) --> [there].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
example(16,[the,beautiful,cat,died]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

vp(Num,vp(Verb)) --> verb(Num, Verb).

np(Num) --> article(Num,Art), adjective(Adj), commonNoun(Num,Noun).


% =========================================

parse_all_examples(L)
:- findall(X,(example(X,Words),sentence(ST,Words,[],writeln(X/ST))),L).


