# Подключаем библиотеки
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import telebot
import config
import datetime
date = datetime.datetime.now()
bot = telebot.TeleBot(config.token)
credentials = ServiceAccountCredentials.from_json_keyfile_name(config.CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http=httpAuth)
def getfood(message):
    ranges = ["Лист номер один!B3:B3"]  #
    results = service.spreadsheets().values().batchGet(spreadsheetId=config.spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    sheet_values = results['valueRanges'][0]['values']
    bot.send_message(message.chat.id, f'Информация аткуальна на {date.strftime("%d.%m")} \n{sheet_values[0][0]}')

def getplan(message):
    ranges = ["Лист номер один!C3:C3"]  #
    results = service.spreadsheets().values().batchGet(spreadsheetId=config.spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    sheet_values = results['valueRanges'][0]['values']
    bot.send_message(message.chat.id, f'Информация аткуальна на {date.strftime("%d.%m")} \n{sheet_values[0][0]}')
print('https://docs.google.com/spreadsheets/d/' + config.spreadsheetId)
