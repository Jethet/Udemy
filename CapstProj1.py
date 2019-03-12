# Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile
# it would take to cover a floor plan of width and height, using a cost
# entered by the user.
import math

def cost_tile(width,height,price):
    w_tile = 0.30
    h_tile = 0.30
    tiles = (width*height) / 0.30
    print('The total cost of the tiles is:', math.ceil(price*tiles))

cost_tile(5,4,3.95)
