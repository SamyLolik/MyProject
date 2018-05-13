from time import sleep
import requests
import datetime
import const
#Установка адреса бота
url = 'https://api.telegram.org/bot' + const.TELEGRAM_API_TOKEN + '/'

class Bot:
    def __init__(self):
        pass
    #Поиск последнего сообщения из массива чата с пользователем Telegram.
    def lastUpdate(self, dataEnd):
        res = dataEnd['result']
        totalUpdates = len(res) - 1
        return res[totalUpdates]
    #Получение идентификатора чата Telegram
    def getChatID(self, update):
        chatID = update['message']['chat']['id']
        return chatID
    #отправка запроса sendMessage боту
    def sendResp(self, chat, value):
        settings = {'chat_id': chat, 'text': value}
        resp = requests.post(url + 'sendMessage', data=settings)
        return resp
    #Get-запрос на обновление информации к боту. Результат – строка json. Метод .json позволяет развернуть ее в массив
    def getUpdatesJson(self, request):
        settings = {'timeout': 100, 'offset': None}
        response = requests.get(request + 'getUpdates', data=settings)
        return response.json()
    #Главная функция
    def main(self):
        chatID = self.getChatID(self.lastUpdate(self.getUpdatesJson(url)))
        self.sendResp(chatID, 'Ваше сообщение')
        updateID = self.lastUpdate(self.getUpdatesJson(url))['update_id']
        #Бесконечный цикл, который отправляет запросы боту на получение обновлений
        while True:
        #Если обновление есть, отправляем сообщение
            if updateID == self.lastUpdate(self.getUpdatesJson(url))['update_id']:
                self.sendResp(self.getChatID(self.lastUpdate(self.getUpdatesJson(url))), 'проба')
                updateID += 1
                sleep(1)
#Запуск главной функции
if __name__ == '__main__':
    newBot = Bot()
