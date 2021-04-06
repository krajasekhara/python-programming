x=int(input("enter first numb"))
if x>1:
    for i in range(2,x):
        if (x%i)==0:
            print("it is not prime numb")
            break
        else:
            print( "prime times")
            break
else:
    print("not prime")