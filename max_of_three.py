def max_of_two(n1,n2):
    if n1 > n2:
        return n1
    return n2

def max_of_three(n1,n2,n3):
    max_num = max_of_two(n1,n2)
    max_of_three = max_of_two(max_num,n3)
    return max_of_three

print(max_of_three(n1=4,n2=6,n3=8))
