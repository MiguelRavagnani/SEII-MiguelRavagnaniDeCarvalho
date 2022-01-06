# 
# Miguel Ravagnani de Carvalho
# 

#------------------------------------------------#
print("\n#------------------------------------------------#\n")
message = 'Hello World'

message = message.replace('World', 'Universe')

print(message)
#------------------------------------------------#
print("\n#------------------------------------------------#\n")
name = 'Michael'
greeting = 'Hello'

message = greeting + ', ' + name + '. Welcome!'

print(message)
#------------------------------------------------#
print("\n#------------------------------------------------#\n")
message = '{}, {}. Welcome!'.format(greeting, name)

print(message)
#------------------------------------------------#
print("\n#------------------------------------------------#\n")
message = f'{greeting}, {name.upper()}. Welcome!'

print(message)
#------------------------------------------------#
print("\n#------------------------------------------------#\n")

print(dir(name))
#------------------------------------------------#