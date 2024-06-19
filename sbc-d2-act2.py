from random import randint

ako = input(" hayang to  1 kulob: ")
C2 = randint(0,1)
C3 = randint(0,1)

hayang = 0
kulob = 1

if ako == kulob:
    print("Ako:kulob")
elif ako == hayang:
    print("Ako:hayang")
if C2 == 1:
    print("C2:kulob")
elif C2 == 0:
    print("C2:hayang")
if C3 == 1:
    print("C3:kulob")
elif C3 == 0:
    print("C3:hayang")
    


if ako == 0 and C2 == 1 and C3 == 1 or ako == 1 and C2 == 0 and C3 == 0 :
    print("you win")
elif ako == 1 and C2 == 0 and C3 == 1 or ako == 0 and C2 == 1 and C3 == 0:
    print("C2 win")
elif ako == 1 and C2 == 1 and C3 == 0 or ako == 0 and C2 == 0 and C3 == 1:
    print("C2 win")
else:
    print("draw")