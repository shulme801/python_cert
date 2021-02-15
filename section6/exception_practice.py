def sum(num1, num2):
    # 
    
    try:
        return(num1 + num2)
    except ValueError:
        print('One of the parameters is the wrong type: ValueError! ')
     
        
    
in_num = int(input('Enter a number: '))
print(sum(in_num, 42))
