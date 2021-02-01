def Fibonacci(n): 
    """
    int--->int
    OBJ: Calcula el n-ésimo término de la sucesión de Fibonacci. 
    PRE: Los términos de una sucesión son números enteros. 
    """
    if(n==0): 
        return 0
    elif(n==1): 
        return 1
    else: 
        return Fibonacci(n-2)+Fibonacci(n-1)