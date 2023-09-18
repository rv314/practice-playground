'''
Given an empty list perform operations provided as input

insert i e: Insert integer  at position.
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the values of commands provided.
Iterate through each command in order and perform the corresponding operation on your list.

'''

commands = list()
arr = list()
if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        command = list()
        command = input().split()
        commands.append(command)
    
    for command in commands:
        if command[0] == 'insert':
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == 'append':
            arr.append(int(command[1]))
        elif command[0] == 'remove':
            arr.remove(int(command[1]))
        elif command[0] == 'sort':
            arr.sort()
        elif command[0] == 'reverse':
            arr.reverse()
        elif command[0] == 'pop':
            arr.pop()
        elif command[0] == 'print':
            print(arr)