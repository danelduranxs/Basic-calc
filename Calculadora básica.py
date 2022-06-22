variable =float(input("Please enter a number:"))

operator =input("Please enter an operator -Do not write spaces- (+) or (-) or (*) or (/) or (exponent):")

variable2 = float(input("Please enter another number:"))


if operator == "+" : 
    print("The result of your choices =", variable + variable2 )
    
elif operator == "-" : 
    print("The result of your choices =", variable - variable2 )
    
elif operator == "*" :
    print("The result of your choices =", variable * variable2 )
    
elif operator == "/" :
     print("The result of your choices =", variable / variable2 )
     
elif operator == "exponent":
      print("The result of your choices =", variable ** variable2 )
      
elif operator != "+" or operator != "-" or operator != "*" or operator != "/" or operator !=  "exponent": 
    print()
    print("You clicked incorrectly!, Please enter one of these choices (copy paste them):")
    print("+")
    print("-")
    print("/")
    print("*")
    print("exponent")