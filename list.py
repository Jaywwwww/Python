invitation = ['wujin', 'liumengnan', 'mum',
              'dad', 'grandfather', 'grandmother']
print(invitation)
for attendee in invitation:
    print(attendee.title() + ' will be invited')
unattendee = 'mum'
replacement = 'uncle'
invitation.remove('mum')
print(unattendee + ' is not able to attend' + ',' +
      ' so we will replace ' + unattendee + ' with ' + replacement + "\n")
print(invitation)
invitation.insert(2, replacement)
print(invitation)
print('Since we have a larger table, we will invite 3 more people\n')
invitation.insert(0, 'aunt')
invitation.insert(4, 'son')
invitation.append('nephew')
print(invitation)
invitation.sort()
print(invitation)
for updatedattendee in invitation:
    print(updatedattendee.title() + ' will be invited')
print('The last invitation is been sent to ' + invitation[-1] + '\n')
print('Since the bigger table is not available yet, we need to fire someone\n')
for i in range(len(invitation)):
    r = invitation.pop()
    print('Dear ' + r + ', due to unexpected circumstance we have to cancel the invitation, thanks for understanding')
    if len(invitation) == 2:
        print(invitation)
        break
for latestattendee in invitation:
    print(latestattendee + ' will be invited')
del invitation[1]
del invitation[0]
print(invitation)
