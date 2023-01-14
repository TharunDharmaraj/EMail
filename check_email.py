new_list = []
with open("unvisited.txt","r") as file:
    curr = file.readline()
    while(curr):
        mail_name = curr
        at_pos = mail_name.find('@')
        if("gmail" in mail_name):
            name = mail_name[0:at_pos]
        else:
            dot_pos = mail_name.find('.')
            name = mail_name[at_pos+1:dot_pos]
        new_list.append([name,curr])
        curr = file.readline()

with open("temp_mails_with_name.txt",'w') as new_file:
    for line in new_list:
        name = line[0]
        id = line[1]
        new_file.writelines(name+"#"+id)
        



