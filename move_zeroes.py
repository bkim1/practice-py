import time 


def move_zeroes(arr):
    zero = 0 # Holds place of leftmost '0' #
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[zero] = arr[zero], arr[i]
            zero += 1
            




if __name__ == "__main__":
    arr = [0,1,2,-1,5,0,7]
    print("Before: %s" % arr)
    t0 = time.time()
    move_zeroes(arr)
    t1 = time.time()
    print("After: %s" % arr)
    print("Time: %f" % (t1 - t0))

    arr = [0,0,0,0,5,0,7]
    print("Before: %s" % arr)
    t2 = time.time()
    move_zeroes(arr)
    t3 = time.time()
    print("After: %s" % arr)
    print("Time: %f" % (t3 - t2))

    arr = [1,3,5,72,3,5,0]
    print("Before: %s" % arr)
    t4 = time.time()
    move_zeroes(arr)
    t5 = time.time()
    print("After: %s" % arr)
    print("Time: %f" % (t5 - t4))

    arr = [1,3,0,72,3,5,2]
    print("Before: %s" % arr)
    t6 = time.time()
    move_zeroes(arr)
    t7 = time.time()
    print("After: %s" % arr)
    print("Time: %f" % (t7 - t6))
