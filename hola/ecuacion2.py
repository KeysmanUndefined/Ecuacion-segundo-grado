def ecuacion2():

    import math

    a= float (input("introduce a"))
    b= float (input("introduce b"))
    c= float (input("introduce c"))
    discriminante = b ** 2 - 4* a* c

    if (discriminante <=0):
        print ("no hay solucion")

    if (discriminante > 0):

        x1 = (( -b + (math.sqrt(discriminante)))/ (2*a))
        x2 = ((-b - (math.sqrt(discriminante)))/(2*a))

        print ("x1=   ", int(x1), "x2=   ", int(x2))

ecuacion2()