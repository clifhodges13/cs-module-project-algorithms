'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # set a start and endpoint for the window, and increment it as we go
    start,end = 0,k
    # set up a list to hold all maximum values
    max_vals = []

    while end-1 < len(nums):
        max_vals.append(max(nums[start:end]))

        # increment start and end points
        start,end = start+1,end+1

    return max_vals

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
