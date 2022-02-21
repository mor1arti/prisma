import requests
import os
import datetime
from bs4 import BeautifulSoup



print('Привет добро пожаловать в программу PRISMA, она предназначена для сбора информации исключительно о людях')





while True:
    a = int(input('Введите любую команду месье > '
                  '[1]-meta_data\n'
                  '[2]-pars_simcard\n'
                  '[3]-search\n'))







    def meta_data():
        image = input('Введите сам файла:')
        c = image.split('.')[-1]
        print('Вот расширения файла:', c)



        create_file = os.path.getctime(image)  # время создания файла
        create_file = datetime.fromtimestamp(create_file).strftime('%Y-%m-%d %H:%M:%S')  # конвертация
        print('Файл был создан:  {create_file}'.format(create_file=create_file))

        edit_file = os.path.getmtime(image)  # время последнего изменения файла
        edit_file = datetime.fromtimestamp(edit_file).strftime('%Y-%m-%d %H:%M:%S')
        print('Файл был изменен:  {edit_file}'.format(edit_file=edit_file))

        size_image = os.path.getsize(image)
        print('Размер файла', size_image)

        file = open(image, 'r')
        print('Вот содержимое файла - \n', file.read())

        # for index, images in image:
        file.close()



    def pars_simcard():
        phone = input("Номер: ")

        url = f'https://htmlweb.ru/geo/api.php?json&telcod={phone}'
        req = requests.get(url)
        src = req.json()

        posts = src["country"]["name"]
        postsr = src["region"]["name"]
        omg = src["region"]["okrug"]
        oper = src["0"]["oper"]
        operator = src["0"]["oper_brand"]
        locationtwo = src["0"]["latitude"]
        locationtree = src["0"]["longitude"]
        print(posts)
        print(postsr)
        print(omg)
        print(oper)
        print(operator)
        print(locationtwo)
        print(locationtree)


    # def ip_information():
    #
    #
    #     ip = input('Введите айпи адрес > ')
    #
    #     header = {
    #         'User-Agent: Mozilla/5.0 (X11; Linux i686; rv:69.0) Gecko/20100101 Firefox/69.0'
    #     }
    #
    #
    #     data = {
    #         'ip':'109.252.114.83',
    #         'token': '03AGdBq24-eoTUbbq_m-WNJsc1QkpHDIayc94XylTxsK0ytlLy9WNAWgyZJ0VUjbVCtfPe1xvFo7vRBYLXngXWG_gVmg06H9gByxAjkG14ogD8YExd_CjmbzhaeUqaIAcCczccwfJFbu6OeobSG0XTgSo4Wse6iUXy6p0D-eVms0xggoI3E6U1mvBMqpetNNoFibQXxH1w19Y3HFluc6VoiSRQCv7XFb-G8Tis1WmuHfgjXOJdyH-YfAyKYJRgyBWWfkhURx-hkGhcNe6ripScfDhrBZCJbTmJFmEPKE7rNW5QMWjHtOM6O-vv4GlXOtcIhgSJ15ysFPpHOqIryHG3vbd61lNOnruNUAE32RozRtxOhFoxv_6SAr3ch0jeZAGk3ZrhKUdX-OGCkn0t-SiYrhNAHTjKU9wtD5O3gl4XVFcOYE0hdcrhGyUIN3oOyIdr1MMowYmwTCtVQC0vREHqvfZX4LsiLriIzshCX5_OfnsgTIFbl-U54RF4HDcbRFX8kW5v5uA4nIQQ'
    #     }
    #
    #
    #     url = f'https://ipstack.com/ipstack_api.php?ip={ip}&token=03AGdBq24-eoTUbbq_m-WNJsc1QkpHDIayc94XylTxsK0ytlLy9WNAWgyZJ0VUjbVCtfPe1xvFo7vRBYLXngXWG_gVmg06H9gByxAjkG14ogD8YExd_CjmbzhaeUqaIAcCczccwfJFbu6OeobSG0XTgSo4Wse6iUXy6p0D-eVms0xggoI3E6U1mvBMqpetNNoFibQXxH1w19Y3HFluc6VoiSRQCv7XFb-G8Tis1WmuHfgjXOJdyH-YfAyKYJRgyBWWfkhURx-hkGhcNe6ripScfDhrBZCJbTmJFmEPKE7rNW5QMWjHtOM6O-vv4GlXOtcIhgSJ15ysFPpHOqIryHG3vbd61lNOnruNUAE32RozRtxOhFoxv_6SAr3ch0jeZAGk3ZrhKUdX-OGCkn0t-SiYrhNAHTjKU9wtD5O3gl4XVFcOYE0hdcrhGyUIN3oOyIdr1MMowYmwTCtVQC0vREHqvfZX4LsiLriIzshCX5_OfnsgTIFbl-U54RF4HDcbRFX8kW5v5uA4nIQQ'
    #     responce = requests.get(url,headers=header,data=data)


    def search():
        email = input('write emails:')

        headers = {
            'authority': 'account.mail.ru',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://account.mail.ru',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://account.mail.ru/recovery?email={email}',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'accept-language': 'ru',
        }

        mailruMail = "{}@mail.ru".format(email)
        data = {'email': mailruMail}

        response = requests.post(
            'https://account.mail.ru/api/v1/user/password/restore',
            headers=headers,
            data=data)

        reqd = response.json()
        print(reqd["body"])
        print(reqd["body"]["phones"])
        print(reqd['body']["id"])














    def main():
        if a == '1':
            meta_data()
        elif a == '2':
            pars_simcard()
        elif a == '3':
            search()












    if __name__ == '__main__':
        main()











