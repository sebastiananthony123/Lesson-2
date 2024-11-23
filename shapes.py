import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

from turtle import *

bgcolor("#cafcf5") #background color for screen

fillcolor("#009982")
begin_fill()

for i in range(4):
    forward(100)
    left(90)

end_fill()

mainloop() #keep the output window open