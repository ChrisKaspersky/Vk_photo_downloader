import vk
import os
import urllib.request

print('Vvedite login')
login_ = input()
print('Vvedite parol')
parol_ = input()
print('Vvedite ssilku na besedu:')
id_ = input()
print('Skolko fotok?')
num = int(input())
links = []
session = vk.AuthSession('5932434', login_, parol_, scope='wall, messages')
vk_api = vk.API(session)
start = ''
range_ = num // 100
for i in range(range_):
    attachments = vk_api.messages.getHistoryAttachments(peer_id=id_,media_type='photo',count='100',start_from=start)
    try:
        for o in range(1,len(attachments)-1):
            links.append(attachments[str(o)]['photo']['src_big'])
        print(attachments)
        start = attachments['next_from']
    except TypeError:
        break
#attachments = vk_api.messages.getHistoryAttachments(peer_id=id_,media_type='photo',count=str(num % 100),start_from=start)
#for i in range(1,len(attachments)-1):
#    links.append(attachments[str(i)]['photo']['src_big'])


os.mkdir('Photos')

os.chdir('Photos')

file_num=0
for href in links:
    urllib.request.urlretrieve(href, str(file_num))
    file_num += 1
    print ("Skachano " + str(file_num) + " failov\n")
