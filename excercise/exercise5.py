new_member = input("Enter new member: ")

file = open("../files/members.txt", 'r')
members = file.readlines()
file.close()

members.append(new_member + "\n")
file = open("../files/members.txt", 'w')
members = file.writelines(members)

Dfile.close()




