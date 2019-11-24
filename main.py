import requests
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
url = 'https://api.telegram.org/botxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


def getMe():
    r = requests.get(url + '/getMe')
    print(r.json())

def getUpdates():
    r = requests.get(url + '/getUpdates')
    print(r.json())
    r = r.json()
    if len(r['result']) == 0:
        print('Нових повідомлень немає')
    else:
        for i in r['result']:
            chat_id = i['message']['chat']['id']
            message_id = i['message']['message_id']
            text = i['message']['text']
            sendMessage(chat_id, text,message_id)
        print("Повідомлення успішно оброблені.")


def sendMessage(chat_id, text, message_id):
    answer = {'chat_id': chat_id, 'text': text, 'reply_to_message_id': message_id}
    r = requests.post(url+'/sendMessage', json=answer)


# getMe()
getUpdates()
