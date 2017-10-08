# The-Pyramid-Game
Implementing the A* Algorithm in Python for implementing an intelligent AI computer to play against a human in The Pyramid Game.

## Note:
```
Source code: "Juego de la Piramide.py"
```

## Objective of the Artificial Intelligence Project
Implementing the A* Algorithm in Python for implementing an intelligent computer to play against a human in The Pyramid Game (a variation of the checkers game).

## Description of the Game (Reference: San Diego State University)
```
Original description link: http://www.eli.sdsu.edu/courses/fall95/cs596_1/project/Checkers.html
```
```
1  1 ▓ 1 ▓ 1 ▓ 1 ▓  
2  ▓ 1 ▓ 1 ▓ 1 ▓ ░  
3  ░ ▓ 1 ▓ 1 ▓ ░ ▓  
4  ▓ ░ ▓ 1 ▓ ░ ▓ ░  
5  ░ ▓ ░ ▓ 2 ▓ ░ ▓  
6  ▓ ░ ▓ 2 ▓ 2 ▓ ░  
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓  
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2  
```

Ten checkers are set up on each side, in the form of a pyramid. The Black pieces are on 1, 2, 3, 4, 6, 7, 8, 10, 11, 15. All men move only forward, do not crown, jump as in regular Checkers, but do not capture. That is, no pieces are removed from the board. It is compulsory to jump when able, and as far as able. The object of play is to maneuver one's own pieces to the squares originally occupied by the adverse pyramid. The first to do so wins. If in the course of play some pieces of one color are moved into a formation such that not all of them can get within the objective area, that color loses at once. For example, if White has moved pieces 3, 4, 8, and then is forced to jump 19-12, he loses, since the man on 12 cannot get inside the pyramid.

## Sample Game
 
Juego de la Pirámide
Tablero Inicial:
   1 2 3 4 5 6 7 8

1  1 ▓ 1 ▓ 1 ▓ 1 ▓ 
2  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 
3  ░ ▓ 1 ▓ 1 ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
6  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  1 ▓ 1 ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
6  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 5

 y1 = 5

 Destino:

 x2 = 8

 y2 = 3
Movimiento no válido
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 5

 y1 = 5

 Destino:

 x2 = 6

 y2 = 4
   1 2 3 4 5 6 7 8

1  1 ▓ 1 ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 2 ▓ ░ 
5  ░ ▓ ░ ▓ ░ ▓ ░ ▓ 
6  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  1 ▓ 1 ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 
3  ░ ▓ 1 ▓ ░ ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 2 ▓ ░ 
5  ░ ▓ 1 ▓ ░ ▓ ░ ▓ 
6  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 6

 y1 = 6

 Destino:

 x2 = 7

 y2 = 5
   1 2 3 4 5 6 7 8

1  1 ▓ 1 ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 
3  ░ ▓ 1 ▓ ░ ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 2 ▓ ░ 
5  ░ ▓ 1 ▓ ░ ▓ 2 ▓ 
6  ▓ ░ ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 2 ▓ ░ 
5  ░ ▓ 1 ▓ ░ ▓ 2 ▓ 
6  ▓ ░ ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 7

 y1 = 5

 Destino:

 x2 = 8

 y2 = 4
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 2 ▓ 2 
5  ░ ▓ 1 ▓ ░ ▓ ░ ▓ 
6  ▓ ░ ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ ░ ▓ 2 ▓ 2 
5  ░ ▓ 1 ▓ ░ ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 55

 y1 = 99

 Destino:

 x2 = 44

 y2 = 5555
Ingrese coordenadas válidas
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 4

 y1 = 6

 Destino:

 x2 = 8

 y2 = 3
Movimiento no válido
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 4

 y1 = 6

 Destino:

 x2 = 8

 y2 = 2
Movimiento no válido
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 6

 y1 = 4

 Destino:

 x2 = 8

 y2 = 3
Movimiento no válido
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 6

 y1 = 4

 Destino:

 x2 = 8

 y2 = 2
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ 1 ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ ░ ▓ ░ ▓ 2 
5  ░ ▓ 1 ▓ ░ ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 1 ▓ ░ ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 7

 y1 = 7

 Destino:

 x2 = 6

 y2 = 7
Movimiento no válido
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 7

 y1 = 7

 Destino:

 x2 = 6

 y2 = 6
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 1 ▓ ░ ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 2 ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 1 ▓ ░ ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 2 ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 6

 y1 = 6

 Destino:

 x2 = 5

 y2 = 5
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 1 ▓ 2 ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ ░ ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
6  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 3

 y1 = 7

 Destino:

 x2 = 1

 y2 = 5
   1 2 3 4 5 6 7 8

1  1 ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ ░ ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  2 ▓ 1 ▓ 2 ▓ 1 ▓ 
6  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ ░ ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  2 ▓ 1 ▓ 2 ▓ 1 ▓ 
6  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 1

 y1 = 5

 Destino:

 x2 = 2

 y2 = 4
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ ░ ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
6  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 
7  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ ░ ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 1 ▓ 2 ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 5

 y1 = 7

 Destino:

 x2 = 7

 y2 = 5
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ ░ ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 1 ▓ 2 ▓ 2 ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ ░ ▓ ░ ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ ░ ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ ░ ▓ 2 ▓ 2 ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ ░ ▓ 1 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 7

 y1 = 5

 Destino:

 x2 = 5

 y2 = 3
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ ░ ▓ 1 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  1 ▓ ░ ▓ 2 ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ ░ ▓ 1 ▓ ░ ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ 2 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 8

 y1 = 8

 Destino:

 x2 = 7

 y2 = 7
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  1 ▓ ░ ▓ 2 ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ ░ ▓ 1 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 2 ▓ 2 ▓ 2 ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 2

 y1 = 8

 Destino:

 x2 = 1

 y2 = 7
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ 1 ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  2 ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  2 ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 1

 y1 = 7

 Destino:

 x2 = 3

 y2 = 5
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
6  ▓ 1 ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
6  ▓ ░ ▓ 2 ▓ 1 ▓ ░ 
7  1 ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 2

 y1 = 4

 Destino:

 x2 = 4

 y2 = 2
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
6  ▓ ░ ▓ 2 ▓ 1 ▓ ░ 
7  1 ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ ░ ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
6  ▓ ░ ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 2 ▓ 2 ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 4

 y1 = 2

 Destino:

 x2 = 3

 y2 = 1
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
6  ▓ ░ ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 2 ▓ 2 ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
6  ▓ ░ ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 2 ▓ 2 ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 6

 y1 = 8

 Destino:

 x2 = 8

 y2 = 6
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 1 ▓ 
4  ▓ ░ ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
6  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
6  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 2 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 3

 y1 = 8

 Destino:

 x2 = 2

 y2 = 6
Movimiento no válido
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 4

 y1 = 8

 Destino:

 x2 = 2

 y2 = 6
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ 2 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ ░ ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ 2 
7  ░ ▓ 1 ▓ ░ ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 5

 y1 = 5

 Destino:

 x2 = 7

 y2 = 3
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ 1 ▓ 2 ▓ 2 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ ░ ▓ 1 ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ 2 
7  ░ ▓ 1 ▓ ░ ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ ░ ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ 2 ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ 2 
7  ░ ▓ 1 ▓ ░ ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 7

 y1 = 3

 Destino:

 x2 = 5

 y2 = 1
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ 2 
7  ░ ▓ 1 ▓ ░ ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ ░ ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ 2 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 8

 y1 = 6

 Destino:

 x2 = 7

 y2 = 5
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 2 ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ ░ 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
2  ▓ ░ ▓ ░ ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 2 ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 5

 y1 = 3

 Destino:

 x2 = 4

 y2 = 2
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 1 ▓ 
2  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ ░ ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 2 ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
2  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 1 ▓ ░ ▓ 
4  ▓ ░ ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 2 ▓ 
6  ▓ 2 ▓ 2 ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 4

 y1 = 6

 Destino:

 x2 = 2

 y2 = 4
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
2  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 1 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 2 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
2  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ ░ ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 2 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 7

 y1 = 5

 Destino:

 x2 = 5

 y2 = 3
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
2  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ ░ ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
2  ▓ ░ ▓ 2 ▓ 1 ▓ 2 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 8

 y1 = 2

 Destino:

 x2 = 7

 y2 = 1
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 1 ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ ░ ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ ░ ▓ 2 
5  ░ ▓ 2 ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 8

 y1 = 4

 Destino:

 x2 = 6

 y2 = 2
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ 1 ▓ 
4  ▓ 2 ▓ 1 ▓ ░ ▓ ░ 
5  ░ ▓ 2 ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ ░ 
5  ░ ▓ 2 ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 3

 y1 = 5

 Destino:

 x2 = 1

 y2 = 3
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  2 ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ 1 ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  2 ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ 1 ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 1

 y1 = 3

 Destino:

 x2 = 2

 y2 = 2
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ 2 ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ 1 ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ ░ ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  ░ ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ 2 ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 2

 y1 = 2

 Destino:

 x2 = 1

 y2 = 1
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 1 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ ░ ▓ ░ ▓ ░ 
5  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
6  ▓ 2 ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 2

 y1 = 6

 Destino:

 x2 = 4

 y2 = 4
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 2 ▓ ░ ▓ ░ 
5  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
6  ▓ ░ ▓ ░ ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ ░ ▓ 2 ▓ ░ ▓ 
4  ▓ 2 ▓ 2 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ ░ ▓ 1 ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 2

 y1 = 4

 Destino:

 x2 = 3

 y2 = 3
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 2 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ ░ ▓ 1 ▓ 1 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ ░ 

Jugador 1:
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 2 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ ░ ▓ 1 ▓ ░ ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 2 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ 1 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 7

 y1 = 7

 Destino:

 x2 = 6

 y2 = 6
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 2 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ ░ ▓ 1 ▓ 2 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ ░ ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ 1 

Jugador 1:
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ ░ ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 2 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ ░ ▓ 1 ▓ 2 ▓ ░ 
7  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ 1 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 4

 y1 = 4

 Destino:

 x2 = 2

 y2 = 2
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ 2 ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ ░ ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ 1 ▓ 
6  ▓ ░ ▓ 1 ▓ 2 ▓ ░ 
7  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ 1 

Jugador 1:
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ 2 ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ ░ ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ ░ ▓ 
6  ▓ ░ ▓ 1 ▓ 2 ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ 1 

Jugador 2:
Ingrese las coordenadas origen y meta de la ficha que desea mover:

 Origen:

 x1 = 6

 y1 = 6

 Destino:

 x2 = 4

 y2 = 4
   1 2 3 4 5 6 7 8

1  2 ▓ 2 ▓ 2 ▓ 2 ▓ 
2  ▓ 2 ▓ 2 ▓ 2 ▓ ░ 
3  ░ ▓ 2 ▓ 2 ▓ ░ ▓ 
4  ▓ ░ ▓ 2 ▓ ░ ▓ ░ 
5  ░ ▓ ░ ▓ 1 ▓ ░ ▓ 
6  ▓ ░ ▓ 1 ▓ ░ ▓ 1 
7  ░ ▓ 1 ▓ 1 ▓ 1 ▓ 
8  ▓ 1 ▓ 1 ▓ 1 ▓ 1 

GANADOR: JUGADOR 2 (TÚ)
```
