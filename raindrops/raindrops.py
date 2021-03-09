def convert(number):
    result = ""    

    divisibleBy3 = number % 3 == 0
    divisibleBy5 = number % 5 == 0
    divisibleBy7 = number % 7 == 0

    if divisibleBy3:
        result = result + "Pling"
    
    if divisibleBy5:
        result = result + "Plang"
    
    if divisibleBy7:
        result = result + "Plong"

    if not divisibleBy3 and not divisibleBy5 and not divisibleBy7:
        result = str(number)

    return result
