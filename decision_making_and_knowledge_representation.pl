/*
Experiment: Decision Making and Knowledge Representation
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
To implement decision making and knowledge representation using prolog tool.
*/

% ==========================================
% Part 1: Minimum and Maximum of Two Numbers
% ==========================================

% Rule to find the minimum of two numbers
minimum(X, Y, X) :- X =< Y. % If X is less than or equal to Y, X is the minimum.
minimum(X, Y, Y) :- X > Y.  % If X is greater than Y, Y is the minimum.

% Rule to find the maximum of two numbers
maximum(X, Y, X) :- X >= Y. % If X is greater than or equal to Y, X is the maximum.
maximum(X, Y, Y) :- X < Y.  % If X is less than Y, Y is the maximum.

% ==========================================
% Part 2: Simple Clauses & Relational Logic
% ==========================================

% Given facts
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% Rules based on the conditions:
% 1. John likes anything that Mary likes
likes(john, X) :- likes(mary, X).

% 2. John likes anyone who likes wine
likes(john, Y) :- likes(Y, wine).

% 3. John likes anyone who likes themselves
likes(john, Y) :- likes(Y, Y).

/*
Sample Queries and Expected Outputs:
1. To find the minimum of two numbers:
   ?- minimum(5, 10, Min).
   Output: Min = 5.

2. To find the maximum of two numbers:
   ?- maximum(5, 10, Max).
   Output: Max = 10.

3. Combined query:
   ?- minimum(8, 3, Min), maximum(8, 3, Max).
   Output: Min = 3, Max = 8.

4. Relational queries:
   ?- likes(mary, food).
   Output: yes.

   ?- likes(john, wine).
   Output: yes.

   ?- likes(john, food).
   Output: yes.

   ?- likes(john, Y).
   Output:
   Y = mary ;
   Y = john ;
   Y = wine ;
*/
