promit = "\nTell me something, and I will repeat it back to you:"
promit += "\nEnter quit to end the program. "
active = True
#while active:
 #   message = raw_input(promit)
  #  if message == 'quit':
   #     active = False
#    else:
 #       print(message)

#while True:
#    message = raw_input(promit)
 #   if message == 'quit':
  #      break
   # else:
    #    print(message)
unconfirmed_uesrs = ['lidong','ssss','bbbbbbbbb']
confirmed_users = []
print("unconfirmed_uesrs: ")
print(unconfirmed_uesrs)
print("confirmed_users: ")
print(confirmed_users)
while unconfirmed_uesrs:
    current_user = unconfirmed_uesrs.pop()
    print("verity user: "+current_user.title())
    confirmed_users.append(current_user)
print("unconfirmed_uesrs: ")
print(unconfirmed_uesrs)
print("confirmed_users: ")
print(confirmed_users)
