'''
Count fruit drops from trees that rollover to house
'''

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    a_drop = 0
    o_drop = 0
    
    apple_pos = [i + a for i in apples]
    orange_pos = [j + b for j in oranges]
    
    for a in apple_pos:
        if s <= a <= t:
            a_drop += 1
            
    for o in orange_pos:
        if s <= o <= t:
            o_drop += 1
            
    return a_drop, o_drop


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    a, o = countApplesAndOranges(s, t, a, b, apples, oranges)
    
    print(a)
    print(o)