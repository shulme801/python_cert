def sum(num1, num2):
    num1_type = type(num1)
    if ( (num1_type != int) and (num1_type != float) and (num1_type != complex) ):
        print("First param is not an integer")
        return(-1)
    
    num2_type = type(num2)
    if ( (not(num2_type == int)) and (not(num2_type == float)) and (not(num2_type == complex)) ):
        print("Second param is not an integer")
        return(-1)
    
    return(num1+num2)
    
in_num = int(input('Enter a number: '))
# in_num = input('Enter a number: ')
print(sum(in_num, 42))
