today_list = []
with open("unvisited.txt","r")as file:
    curr = file.readline()
    while(curr):
        mail = curr
        hash_pos = mail.find("#")
        at_pos = mail.find("@")
        mail_id = mail[hash_pos+1:len(mail)]
        name = mail[at_pos+1:hash_pos-6]
        today_list.append([name,mail_id])
        curr = file.readline()
        
with open("today.txt","w") as f:
    for line in today_list:
        name = line[0]
        id = line[1]
        f.writelines(name+"#"+id)
    
