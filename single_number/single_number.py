'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    oddball = None

    for i in range(len(arr)-1):
        popped = arr.pop(i) # pull off the item in question
        if popped in arr: # if the item exists in the remaining array, that means it was in there twice to begin with, so
            arr.insert(i,popped) # put it back, because it's not the oddball.
        else: # otherwise,
            oddball = popped # we've found the oddball!

    return oddball


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")