x="outside variable"
def func():
    print("global variabal is" + x)
func()
#global variable is created outside variable
#global keyword is used both inside and outside function are used
#to created global variable by using global keyword
def func():
    global x
    x="fantastic"
    print("python is" + x)
func()
#outside function are used by global keyword
x="awesome"
def fun():
    global x
    x="fantastic"
    print("python is " + x)
fun()
print("python is " + x)




