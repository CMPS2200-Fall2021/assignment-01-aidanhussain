"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    ### TODO
    count = 0
    longest = 0
    for e in mylist:
        if e == key:
            count += 1
            if count > longest:
                longest = count
        else:
            count = 0
            
    return longest


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

    
def longest_run_recursive(mylist, key):
    ### TODO
    mid = len(mylist)/2
    
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1,1,1,True)
        else:
            return Result(0,0,0,False)
    
    else:
        left = longest_run_recursive(mylist[0,mid], key)
        right = longest_run_recursive(mylist[mid+1: len(mylist)-1], key)
        
        if left.is_entire_range and right.is_entire_range:
            return Result(left.longest_size+right.longest_size,left.longest_size+right.longest_size,left.longest_size+right.longest_size,True)
        elif left.is_entire_range:
            return Result(left.longest_size,0,max(left.longest_size,right.longest_size),False)
        elif right.is_entire_range:
            return Result(0,right.longest_size,max(left.longest_size,right.longest_size),False)  

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([12], 12) == 1



