import requests
import json

url = f'https://petstore.swagger.io/v2'

data_post = {'id': 19191919191919,'username': 'program_1','firstName': 'yuri','lastName': 'golovanov','email': '715@yandex.ru',\
                          'password': 'qwerty','phone': '88005553535','userStatus': 0}

res_post = requests.post(url + '/user', params={'status': 'available'},headers={'accept': 'application/json','Content-Type': 'application/json'}, data = json.dumps(data_post, ensure_ascii=False))
print('создание пользователя(post)')
print(res_post.status_code)
print(res_post.json())


res_get_1 = requests.get(url + '/user/'+data_post['username'], params={'status': 'available'})
print('проверка(get)')
print(res_get_1.status_code)
print(res_get_1.json())

data_put = {'id': 19191919191919,'username': 'program_1','firstName': 'vova','lastName': 'vedenkin','email': 'mstuca@yandex.ru',\
                          'password': 'admin','phone': '88586515050','userStatus': 0}

res_put = requests.put(url + '/user/'+data_post['username'],params={'status': 'available'},headers={'accept': 'application/json','Content-Type': 'application/json'}, data = json.dumps(data_put, ensure_ascii=False))
print('изменение данных пользователя(put)')
print(res_put.status_code)
print(res_put.json())

res_get_2 = requests.get(url + '/user/'+data_post['username'], params={'status': 'available'})
print('проверка(get)')
print(res_get_2.status_code)
print(res_get_2.json())

res_del = requests.delete(url + '/user/'+data_post['username'],params={'status': 'available'},headers={'accept': 'application/json'})
print('удаление пользователя(delete)')
print(res_del.status_code)
print(res_del.json())