users = {
    'wujin': {
        'first_name' : 'jin',
        'last_name' : 'wu',
        'password' : '123456',
        'email' : '297300526@qq.com',
        'location' : 'zhengzhou',
    },
    'liumengnan' : {
        'first_name' : 'mengnan',
        'last_name' : 'liu',
        'password' : '111111',
        'email' : '273101828@qq.com',
        'location' : 'henan',
    }
}
for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['last_name'] + ' ' + user_info['first_name'] + '.'
    localtion = user_info['location']
    email = user_info['email']
    print('\tFull name is ' + full_name.title())
    print('\tLocation is ' + localtion.title())
    print('\tThe contact is ' + email.title())