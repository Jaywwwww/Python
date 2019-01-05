def display_message():
    print('I am learning No. 8 chapter')

def favorite_books(titles):
    print('One of my favorite books is: ' + titles.title())

def make_shirt(size, style='I love Python'):
    print('This shirt is ' + size.title() + ', ' + 'It is printed with ' + style.title())

def get_formated(first_name, last_name, middle_name=''):
    if middle_name:
        fullname = first_name + ' ' + middle_name + ' ' + last_name
    else:
        fullname = first_name + ' ' + last_name
    return fullname.title()

def city_country(name, country):
    print(
        '-----------------------------------------------------------\n' +
        name.title() + ' ' + country.title() +
        '\n-----------------------------------------------------------'
          )

def make_album(singer, album, song_amount=''):
    if song_amount:
        album_set = {'name':singer , 'album_name': album , 'song_amount': song_amount}
    else:
        album_set = {'name':singer , 'album_name': album}
    return album_set

#display_message()
#favorite_books('darkness')
#make_shirt(size='M')
#print(get_formated(input('please input first name: '),input('last name: '),input('middle name:')))
#print(city_country('beijing', 'china'))
print(make_album('Jay Chou', 'Yehuimei', 5))


