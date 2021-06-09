import mailbox


data = mailbox.mbox("Takeout/Mail/All mail Including Spam and Trash.mbox")

for i in data.keys():
    print([j for j in data[i].items()[0]])
    exit()