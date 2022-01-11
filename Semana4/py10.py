# 
# Miguel Ravagnani de Carvalho
# 

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

import os

print(dir(os))

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

os.chdir('/home/miguel/Documents/UFU/SEMBII/SEII-MiguelRavagnaniDeCarvalho/')

os.makedirs('osdirs/Demo/Sub-dir')

print(os.listdir())


#------------------------------------------------#
print("\n#------------------------------------------------#\n")

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))