from turtle import*

def dibujar_corazon():
    bgcolor("black")
    color("red")
    title("corazon")

    begin_fill()
    pensize(3)
    left(50)
    forward(133)
    circle(50,200)
    right(140)
    circle(50,200)
    forward(133)
    end_fill()


def texto_corazon(texto):
        penup()
        goto(0,-50)
        pendown()
        color("white")
        style= ("courier", 15, "bold")
        write(texto, align="center", font=style)


        hideturtle()
        done()
dibujar_corazon()
texto_corazon("hola")

