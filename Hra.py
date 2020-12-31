# Jenda Razák 
# 31.12 2020
# Freeware, můžete si s tím dělat co chcete, jen zachovat credit 
# (je to uděláno pomoci tutorialu na Youtube)
# Verze 2.0.0

import turtle
import os
import math
import random

pocet_nepratel = 30

# Vytvoření okna
obrazovka = turtle.Screen()
obrazovka.bgcolor("black")
obrazovka.title("Ničitel Ufounů")
obrazovka.bgpic("nicitelufonuPozadi.gif")
obrazovka.tracer(0)

# Registrování tvarů
obrazovka.register_shape("mimozemstan.gif")
obrazovka.register_shape("kulka.gif")

# Hranice Plochy
hranice = turtle.Turtle()
hranice.speed = 0
hranice.color("white")
hranice.penup()
hranice.setposition(-300,-300)
hranice.pendown()
hranice.pensize(3)

for strany in range(4):
    hranice.fd(600)
    hranice.lt(90)  

hranice.hideturtle()
 
# Skóre

skore = 0

skorepen = turtle.Turtle()
skorepen.speed = 0
skorepen.color("white")
skorepen.penup()
skorepen.setposition(-290,275)
skorestring = "Skóre: {}" .format(skore)
skorepen.write(skorestring, False, align="left", font = ("Arial", 14, "normal"))
skorepen.hideturtle()

# Konec hry

konechry = turtle.Turtle()
konechry.speed = 0
konechry.color("white")
konechry.penup()
konechry.setposition(-165,-10)
konechrystring = "Konec hry, vaše skóre: {}".format(skore)
konechry.write(konechrystring, False, align="left", font = ("Arial",25,"normal"))
konechry.hideturtle()

# Hráč   
hrac = turtle.Turtle() 
hrac.color("green")
hrac.shape("triangle")
hrac.penup()
hrac.speed = 0
hrac.setposition(0,-250)
hrac.setheading(90)
hrac.speed = 0

# Funkce Hráče
def doLeva():
    hrac.speed = -1


def doPrava():
    hrac.speed = 1
    x = hrac.xcor()
    x += hrac.speed
    hrac.setx(x)

def pohyb_hrace():
    x = hrac.xcor()
    x += hrac.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    hrac.setx(x)
    

def vystrel():
    global stavKulky

    if stavKulky == "ready":    
        stavKulky = "fire"
        x = hrac.xcor()
        y = hrac.ycor() + 10
        kulka.setposition(x,y )
        kulka.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


# Klávesy
obrazovka.listen() 
obrazovka.onkeypress(doLeva, "a")
obrazovka.onkeypress(doPrava, "d")
obrazovka.onkeypress(vystrel, "w")

# Nepřátelé

nepratele = []

for i in range(pocet_nepratel):
    nepratele.append(turtle.Turtle())

nepritel_start_x = -225
nepritel_start_y = 250
nepritel_cislo = 0
pocetnepratel = 0

for nepritel in nepratele:
    nepritel.color("red")
    nepritel.shape("mimozemstan.gif")
    nepritel.penup()
    nepritel.speed = 0
    x = nepritel_start_x + (50 * nepritel_cislo)
    y = nepritel_start_y
    nepritel.setposition(x, y)   
    nepritel_cislo += 1
    pocetnepratel += 1
    if nepritel_cislo == 10:
        nepritel_start_y -= 50
        nepritel_cislo = 0



rychlost_nepritele = 0.1

# Zbraň hráče(kulka)

kulka = turtle.Turtle()
kulka.color("yellow")
kulka.shape("kulka.gif")
kulka.penup()
kulka.speed = 0
kulka.setheading(90)
kulka.shapesize(0.5, 0.5)
kulka.hideturtle()

rychlost_kulky = 2.5

stavKulky = "ready"

# "while loop" hry

while True:
    obrazovka.update()
    pohyb_hrace()
    
    for nepritel in nepratele: 
        
       # Pohyb nepřátel
        x = nepritel.xcor()
        x += rychlost_nepritele
        nepritel.setx(x)

        if nepritel.xcor() > 280:
            for e in nepratele:
                y = e.ycor()
                y -= 40
                e.sety(y)
            rychlost_nepritele *= -1

        if nepritel.xcor() < -280:
            for e in nepratele:
                y = e.ycor()
                y -= 40
                e.sety(y)     
            rychlost_nepritele *= -1
 
        if isCollision(kulka, nepritel):
            kulka.hideturtle()
            stavKulky = "ready"
            kulka.setposition(0, -400)
        

            nepritel.setposition(0, 10000)   

            pocetnepratel -= 1
            skore += 5
            skorestring = "Skóre: {}" .format(skore)          
            skorepen.clear()
            skorepen.write(skorestring, False, align="left", font = ("Arial", 14, "normal"))
    
        if isCollision(hrac, nepritel):
            hrac.hideturtle()
            nepritel.hideturtle()
            print("Konec hry")
            break
  
    # Eliminace po konci

    if pocetnepratel < 1:
        konechry.clear()   
        konechrystring = "Konec hry, vaše skóre: {}".format(skore)
        konechry.write(konechrystring, False, align="left", font = ("Arial",25,"normal"))
    else:
        konechry.clear()

    # Výstřel kulky    
    if stavKulky == "fire":
        y = kulka.ycor()
        y += rychlost_kulky
        kulka.sety(y)

    if kulka.ycor() > 275:
        kulka.hideturtle()
        stavKulky = "ready"

#dealy = input("Enter pro opuštění")
