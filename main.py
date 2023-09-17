import requests
from art import *
from datetime import datetime

token = ''
version = 5.131
art = text2art('SocialScript', 'big')
print(art)
id = ''
domain = ''
name = ''
bdate = ''
last_seen = ''
phone = ''
city = ''
home_city = ''
schools = ''
status = ''
sex = ''
result = '# Результат #'

while True:
    print('Введите ID или короткое имя')
    user_id = input(">> ")

    response = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'user_ids': user_id,
                                'fields': "city, schools, first_name, last_name, about, bdate, career, common_count. connections, contacts, domain, followers_count, home_town, last_seen, nickname, personal, universities, status, sex, verified, relation, relatives, photo_max_orig",
                                'access_token': token,
                                'v': 5.131
                            })
    try:
        data = response.json()['response'][0]
        if data['last_seen']['platform'] == 1:
            platform = 'Мобильная версия'
        elif data['last_seen']['platform'] == 2:
            platform = 'Iphone'
        elif data['last_seen']['platform'] == 3:
            platform = 'Ipad'
        elif data['last_seen']['platform'] == 4:
            platform = 'Android'
        elif data['last_seen']['platform'] == 5:
            platform = 'Windows Phone'
        elif data['last_seen']['platform'] == 6:
            platform = 'Приложение для Windows 10'
        elif data['last_seen']['platform'] == 7:
            platform = 'Полная версия сайта'


        id = f"\nID - {data['id']}"
        result += id
        domain = f"\nDomain - {data['domain']}"
        result += domain
        name = f"\nИмя - {data['first_name']} {data['last_name']}"
        result += name
        photo = f"\nФото - {data['photo_max_orig']}"
        result += photo
        bdate = f"\nДата рождения - {data['bdate']}"
        result += bdate
        if data['sex'] == 1:
            sex = '\nПол - Женский'
            result += sex
        if data['sex'] == 2:
            sex = '\nПол - Мужской'
            result += sex
        if data['sex'] == 0:
            sex = '\nНе указано'
            result += sex
        last_seen = f"\nПоследний вход - {platform} | {datetime.utcfromtimestamp(data['last_seen']['time']).strftime('%Y-%m-%d %H:%M:%S')}"
        result += last_seen
        try:
            if data['mobile_phone']:
                phone = f"\nМобильный телефон - {data['mobile_phone']}"
                result += phone
        except:
            pass
        try:
            if data['city']['title']:
                city = f"\nГород - {data['city']['title']}"
                result += city
        except:
            pass
        try:
            if data['home_town']:
                home_city = f"\nРодной город - {data['home_town']}"
                result += home_city
        except:
            pass
        try:
            schools = f"\nШкола - {data['schools'][0]['name']}"
            result += schools
        except:
            pass
        if data['status']:
            status = f"\nСтатус - {data['status']}"
            result += status
        try:
            for relative in data['relatives']:
                result1 = ''
                if relative['type'] == 'parent':
                    r_type = 'Родитель'
                if relative['type'] == 'sibling':
                    r_type = 'Сестра/брат'
                result1 = f'\n{r_type} - {relative["id"]}'
                result += result1
        except:
            pass

        print()
        print(result)
        print()


    except:
        print("Пользователь не найден")

# with open('l1berty.csv', 'w') as file:
#     pen = csv.writer(file)
#     pen.writerow(('user_id', 'city', 'school',
#                   ))
#     pen.writerow((data['id'], data['city']['title'], data['schools'][0]['name']))
