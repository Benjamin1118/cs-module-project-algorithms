'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n <= 1:
        return 1
    # two ways 1+1
    if n == 2:
        return 2
    # ways if he ate 1 @ a time, + 2@ a time, + 3@ a time...
    return eating_cookies(n-1), + eating_cookies(n-2), + eating_cookies(n-3)



    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
