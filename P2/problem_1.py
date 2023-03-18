def sqrt(n):
    start = 0
    end = n

    while start <= end:
        mid = (start + end) // 2
        print(mid)
        mid_squared = mid * mid

        if mid_squared == n:
            return mid
        elif mid_squared < n:
            start = mid + 1
        else:
            end = mid - 1

    return end

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")