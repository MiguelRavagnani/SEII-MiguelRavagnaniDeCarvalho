# 
# Miguel Ravagnani de Carvalho
# 

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

import os

os.chdir('/home/miguel/Documents/UFU/SEMBII/SEII-MiguelRavagnaniDeCarvalho/')

for f in os.listdir():
    
    if f == '.DS_Store':
        continue
    file_name, file_ext = os.path.splitext(f)
    print(file_name)
    
    f_title, f_course, f_number = file_name.split('-')

    print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_number = f_number.strip()

    print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

    os.rename(fn, new_name)
print(len(os.listdir()))