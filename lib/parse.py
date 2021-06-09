file = open("lib/main.py.cs", "r")
lines = file.readlines()
lines = 'using System;\n' + ''.join(lines)
file.close()

file = open("lib/main.py.cs", "w")
file.write(lines)
file.close()
