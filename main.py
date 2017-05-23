# coding=utf-8
import vk
import vk.exceptions
import os
import urllib.request

while True:
    print('Логин:')
    user_login = input()

    print('Пароль:')
    user_password = input()
    try:
        session = vk.AuthSession('5932434', user_login, user_password, scope='wall, messages')
        vk_api = vk.API(session)
        break
    except vk.exceptions.VkAuthError:
        print('Авторизация не удалась: неверный логин или пароль')

while True:
    print('Полная ссылка на беседу:')
    link = input()
    dialog_id = link[link.find('=')+1:]

    print('Сколько фотографий?')
    num = int(input())

    links = []
    start = ''
    range_ = num // 100
    for i in range(range_):
        attachments = vk_api.messages.getHistoryAttachments(peer_id=dialog_id,media_type='photo',count='100',start_from=start)
        try:
            for o in range(1,len(attachments)-1):
                links.append(attachments[str(o)]['photo']['src_big'])
            print(attachments)
            start = attachments['next_from']
        except TypeError:
            break

    file_list = os.listdir('Photos')
    files_count = len(file_list)

    try:
        os.mkdir('Photos')
        os.chdir('Photos')
    except FileExistsError:
        os.chdir('Photos')

    file_num=0
    for href in links:
        urllib.request.urlretrieve(href, str(files_count))
        files_count += 1
        file_num += 1
        print ("Скачано " + str(file_num) + " файлов\n")

    print('Загрузка завершена')
    file_num = 0

    for file in file_list:
        if file[file.rfind('.')+1:] != 'jpg':
            os.rename(file,file+'.jpg')
            file_num += 1
            print("Переименовано " + str(file_num) + " файлов\n")

    print("Скачать фото из других диалогов? (Да/Нет)")
    answer = input().lower()
    if answer == "нет":
        break
