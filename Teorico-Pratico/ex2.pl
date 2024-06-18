%    menor prioridade, 
:- op (800 , fx , when ) . % unary operator
:- op (700 , xfx , do ) . % non associative operator
:- op (300 , xfy , or ) . % righ associative operator
:- op (200 , xfy , and ) .
:- op (150 , fx , not ) .

when passengerFor(here) or CallFor(here) and door(closed) then open.
when door(timeToClose) then close
when passengerFor(above) and door(closed) then up.
when passengerFor(down) and door(closed) then down.
when passengerFor(here) and door(open) then close
when passengerFor(down) or passengerFor(up) then close.



