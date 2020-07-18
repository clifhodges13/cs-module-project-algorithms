'''
Input: an integer
Returns: an integer
'''
def eat_cookies(current,desired):
    # Your code here
    if current > desired:
        return 0
    elif current == desired:
        return 1
    return eat_cookies(current+1, desired) + eat_cookies(current+2, desired) + eat_cookies(current+3, desired)

def eating_cookies(n):
    return eat_cookies(0,n)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
