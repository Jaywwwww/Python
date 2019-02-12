with open('show_version.txt') as file:
    #contents = file.read()
    #print(contents.rstrip())
    #for line in file:
    #    print(line.rstrip())
    pi_string = ''
    for line in file:
        pi_string += line.rstrip()
    print(pi_string)
    print(len(pi_string))
