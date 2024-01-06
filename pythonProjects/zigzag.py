import sys, time
indents = 0
indent = " "
try:
    while True:


        while indents != 20:
            print(indents * indent + "i love you Dilshoda")
            indents += 1
            time.sleep(0.1)

        if indents == 20:

            while indents != 0:
                indents -= 1
                print(indents * indent + "I love you Dilshoda" )
                time.sleep(0.1)
except KeyboardInterrupt:
    print("you stopped the programm")
    sys.exit()