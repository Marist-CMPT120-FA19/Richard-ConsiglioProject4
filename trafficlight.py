from graphics import * 
def main():
    win = GraphWin("h",500,500)
    white = Rectangle(Point(100,30), Point(400,470)) 
    red = Circle(Point (250,120) ,50)
    yellow = Circle(Point (250,240) , 50)
    green = Circle(Point (250,360) , 50)
   

    white.setFill("white")
    green.setFill("green")
    red.setFill("red")
    yellow.setFill("yellow")

    white.draw(win)
    green.draw(win)
    red.draw(win)
    yellow.draw(win)
    win.getMouse()
main() 
