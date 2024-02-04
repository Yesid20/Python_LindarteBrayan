## -------------------------------------------
## ---- Ejercicio 3 ----
## -------------------------------------------
import math

def ball_collide(ball1, ball2):
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) <= (r1 + r2)

print(ball_collide((0, 0, 3), (5, 0, 4)))  
print(ball_collide((0, 0, 3), (8, 0, 2)))  
print(ball_collide((0, 0, 3), (3, 0, 3)))  
print(ball_collide((0, 0, 5), (2, 2, 2)))  

# Desarrollado por Brayan Yesid Lindarte Anaya - 1010120365
