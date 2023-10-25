# Basic python function
def MyFunction(name:str):
    print('Hello Mr.', name)
    
# MyFunction('Kolozuz') # Function Call


# Function with default/optional parameters
def orderItem(ItemName, Amount = 1, Color = 'blue'):
    print('    Item Ordered! \n    You ordered', Amount, ItemName, 'in', Color, 'Color' )
    
orderItem('Mouse')


# Crear programa que multiplique numeros pero solo usando sumas:

def Multiply(num, times):
    result = 0
    for i in range(times):
        result = result + num
        
    return result

# result = Multiply(2,5)
# print(result)
