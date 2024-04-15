print("**Welcome**")

def max_of_three(a,b,c):
    if a > b:
        if b > c:
            return b
        else:
            return c
    return a

num = int(input(f"Enter number: "))

print(max_of_three(1,3,5))
