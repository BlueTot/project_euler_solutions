# Python3 program for the above approach 
 
# Function to find number of ordered
# positive integer pairs (x,y) such
# that they satisfy the equation
def solve(n):
 
    # Initialize answer variable
    ans = 0
 
    # Iterate over all possible values of y
    y = n + 1
    while(y <= n * n + n):
 
        # For valid x and y,
        # (n*n)%(y - n) has to be 0
        if ((n * n) % (y - n) == 0):
             
            # Increment count of ordered pairs
            ans += 1
 
        y += 1
 
    # Print the answer
    print(ans)
 
# Driver Code
n = 120
 
# Function call 
solve(n)
 