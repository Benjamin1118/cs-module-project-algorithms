'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    count = arr.count(0)
    zeros_list = [0 for i in range(count)]
    print(zeros_list)
    #iterate array
    x = [i for i in arr if i != 0]
    print(x)
    arr = x + zeros_list
    return arr

    # i = 0
    # k = len(arr)
    # for i in arr:
    #     print(arr[i])
    #     if i == 0:
    #         zero = arr.pop(i)
    #         arr.insert(0, zero)
    #         i += 1
    # return arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")