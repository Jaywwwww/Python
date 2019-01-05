magic = ['david', 'tony', 'harry']

def print_magic(magic_arg):
    print(magic_arg)

def make_great(magic_arg):
    magic_arg_temp = []
    while magic_arg:
        current = magic_arg.pop()
        current = 'the Great ' + current
        magic_arg_temp.append(current)
    for name in magic_arg_temp:
        magic_arg.append(name)
    magic_arg.reverse()
    return magic_arg

print_magic(magic)
#make_great(magic)
magic_copy = make_great(magic[:])
print_magic(magic)
print_magic(magic_copy)
