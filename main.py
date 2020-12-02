import turtle

t = turtle.Pen()
turtle.bgcolor( "black" )

def numberCountSpiral():
    colors = [ "red", "yellow", "blue", "green" ]
    for i in range( 61 ):
        t.pencolor( colors[ i % 4 ] )
        t.penup()
        t.forward( i * 4 )
        t.pendown()
        t.write( i, font = ( "Arial", int( (i * 4) / 4 ), "bold" ) )
        t.left( 75 )
    print( "\nDone!" )

def coolShapes():
    sides = int(input( "\nEnter number of sides (2-6) for the shape " ))
    if 2 <= sides <= 6:
        colors = [ "red", "blue", "green", "orange", "yellow", "purple" ]
        for i in range(151):
            t.pencolor( colors[ i % sides ] )
            t.forward( i * 3 / sides + i )
            t.left( 360 / sides + 1 )
            t.width( int( i * sides / 200 ) )
        print( "\nDone!" )
    else:
        print( "\nPlease enter a number of sides that is between 2 - 6" )

def showMenuOptions():
    print( "\nOptions" )
    print( "-------" )
    print( "1. numberCountSpiral()" )
    print( "2. coolShapes()" )
    print( "0. Exit\n" )

def userChooseFunction():
    running = True
    while running:
        showMenuOptions()
        userChoice = input( "Which function would you like to run? " )

        if userChoice == "1":
            t.reset()
            numberCountSpiral()

        elif userChoice == "2":
            t.reset()
            coolShapes()

        elif userChoice == "0":
            print( "\nBye!\n" )
            running = False

        else:
            print( "\nInvalid choice." )


if __name__ == '__main__':
    userChooseFunction()
