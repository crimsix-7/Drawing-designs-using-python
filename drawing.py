from turtle import*

#The main background shape

def shape(size,t):

  for i in range(6):

    t.forward(size)

    t.left(360/6)

def draw(t):

#defining the colors list

  colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

#setting the speed for pen

t.speed(0)

for i in range(60):

  t.pencolor("grey")

  shape(5*i,t)

  t.left(i)

#for Spiral Helix Pattern

for i in range(600):

  t.pencolor(colors[i%6])

#increase width sequentially

t.width(i/80 + 1)

t.forward(i)

t.left(59)

done()

def main():

#setting window size to 800 X 800

  setup(800, 800)

#setting background color to black

bgcolor('black')

t = Pen()

draw(t)

main()
