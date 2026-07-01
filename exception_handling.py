try:
    a,b=12,3
    print(a/b)
except ZeroDivisionError:
    print("You cannot divide by zero")
except TypeError:
    print("Can divide only by integer")
except NameError:
    print("Please provide values for a and b")
except Exception as e:
    print("Error occured",e)
else:
    print("Program executed without any errors")
finally:
    print("Program executed")