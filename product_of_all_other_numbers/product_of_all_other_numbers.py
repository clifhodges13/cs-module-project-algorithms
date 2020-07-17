'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    products = []

    # loop over arr
    for i in range(len(arr)):
        # pop off the current item
        popped = arr.pop(i) # save it for later
        # create a running total
        running_total = 1
        for j in arr:
            # multiply all the remaining items together
            running_total = running_total * j
        # put each of them into the products list
        products.append(running_total)
        # reinsert the popped off item
        arr.insert(i,popped)

    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
