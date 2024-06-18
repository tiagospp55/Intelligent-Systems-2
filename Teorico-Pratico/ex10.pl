
instruction(move()) -->  [go,to], location(Loc).
instruction(load(Loc,Obj)) --> [load],loadable_object(Obj), [at], location(Loc).

location(oval_crater) --> [the],location_name(Loc), [station]
location(deep_crater) --> location_name(Loc).

location_name(oval_crater) --> [oval,crater].
location_name(deep_crater) --> [deep,crater].
location_name(lunar_valley) --> [lunar,valley].

loadable_object(barrel) --> [barrel].
loadable_object(food) --> [food,package].
