/*
Experiment: Find Minimum and Maximum of Two Numbers
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
To find the minimum and maximum of two numbers using Prolog.
*/

% Rule to find the minimum of two numbers
minimum(X, Y, X) :- X =< Y. % If X is less than or equal to Y, X is the minimum.
minimum(X, Y, Y) :- X > Y.  % If X is greater than Y, Y is the minimum.

% Rule to find the maximum of two numbers
maximum(X, Y, X) :- X >= Y. % If X is greater than or equal to Y, X is the maximum.
maximum(X, Y, Y) :- X < Y.  % If X is less than Y, Y is the maximum.

/*
Sample Queries:
?- minimum(5, 10, Min).
Output: Min = 5.

?- maximum(5, 10, Max).
Output: Max = 10.

?- minimum(8, 3, Min), maximum(8, 3, Max).
Output: Min = 3, Max = 8.
*/
