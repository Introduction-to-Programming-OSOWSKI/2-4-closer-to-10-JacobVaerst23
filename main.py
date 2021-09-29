#WRITE YOUR CODE IN THIS FILE

#define close10
def close10(x, y):
    if abs(x-10) < abs(y-10):
        return x

    elif abs(x-10) == abs(y-10):
        return 0

    else:
        return y

#Run the function
print(close10(16, 5))

    
        

