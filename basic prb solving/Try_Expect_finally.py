def sum(number1,number2):
    try:
        result=number1+number2
    except Exception as e:
        print("number type is not matched")
    
    except:
        print("error is not defined")
        
    finally:
        print("programme is on going")


sum(2,"limon")