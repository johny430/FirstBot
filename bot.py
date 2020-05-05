import telebot
from telebot import types
import sqlite3
from random import randint
import requests
import json
from blockchain import util
import json
from enum import Enum
from past.builtins import basestring

QIWI_TOKEN = '4aaf64eba7fd752f2db969250d33d851'
QIWI_ACCOUNT = '+375444734398'
btcadress = '175Ebu7n1dCKGA87uDGxy8xLo4aMmMsWU'
bot = telebot.TeleBot("1114807745:AAFtAKULqMNuoP8OWRuwvE2P6WTvyD7Y0sk")

m = response = requests.get('https://blockchain.info/ticker')
c = m.json()
F = c['USD']['buy']

def get_balance(addresses, filter=None, api_code=None):
    global v
    if isinstance(addresses, basestring):
        resource = 'balance?active=' + addresses
    else:
        resource = 'balance?active=' + '|'.join(addresses)
    if filter is not None:
        if isinstance(filter, FilterType):
            resource += '&filter=' + str(filter.value)
        else:
            raise ValueError('Filter must be of FilterType enum')
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    a = json_response
    v = a[addresses]['final_balance']

s = requests.Session()
s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
parameters = {'rows': '10'}
h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ QIWI_ACCOUNT +'/payments', params = parameters)
req = json.loads(h.text)

markupkorzina = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupbacktomeny = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupprofile = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
markupwhentovarchosed = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupnomoney = types.ReplyKeyboardMarkup(resize_keyboard=True)
abc = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
markupamountchoose = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
markupadmin = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
markupposlectg = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
markuppaymentchoose = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
markupoplati = types.ReplyKeyboardMarkup(resize_keyboard=True,  row_width= 2)
markupadminnazad = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupotkr = types.ReplyKeyboardMarkup(resize_keyboard=True)
abcd = types.ReplyKeyboardMarkup(resize_keyboard=True)
ekrc = types.ReplyKeyboardMarkup(resize_keyboard=True)

item1 = types.KeyboardButton("💳 Выбор товаров для покупки 💳 ")
item2 = types.KeyboardButton("👤 Мой профиль")
item3 = types.KeyboardButton("💬Отзывы")
item4 = types.KeyboardButton("🆘 Тех Поддержка")
item5 = types.KeyboardButton("ℹ️ Правила")
item6 = types.KeyboardButton("⏪ Назад")
item7 = types.KeyboardButton("❌ Отмена")
item8 = types.KeyboardButton("💵 Пополнить баланс 💵")
item9 = types.KeyboardButton("🛒 Моя корзина")
item10 = types.KeyboardButton("💳 Мои покупки")
item11 = types.KeyboardButton("⏪ Вернуться в меню")
item12 = types.KeyboardButton("Потвердить")
item13 = types.KeyboardButton("🛒 Добавить в корзину")
item16 = types.KeyboardButton("✔ Потвердить")
item17 = types.KeyboardButton("Добавить в корзину")
item21 = types.KeyboardButton("Общая информация")
item22 = types.KeyboardButton("Список администраторов")
item23 = types.KeyboardButton("Изменить баланс пользователя")
item24 = types.KeyboardButton("Выдать админ права")
item25 = types.KeyboardButton("Лишить админ права")
item26 = types.KeyboardButton("Закрыть/Открыть продажи")
item27 = types.KeyboardButton("Посмотреть профиль")
item28 = types.KeyboardButton("Посмотреть профиль")
item29 = types.KeyboardButton("Посмотреть покупки")
item30 = types.KeyboardButton("Найти покупку по номеру заказа")
item31 = types.KeyboardButton("Рассылка всем пользователям")
item32 = types.KeyboardButton("Сообщение пользователю")
item33 = types.KeyboardButton("Добавить категорию")
item34 = types.KeyboardButton("Удалить категорию")
item35 = types.KeyboardButton("Тест")
item37 = types.KeyboardButton("BTC")
item38 = types.KeyboardButton("QIWI")
item39 = types.KeyboardButton("❌ Очистить корзину")
item40 = types.KeyboardButton("💵 Оплатить корзину")
item41 = types.KeyboardButton("✔️ Оплатил")
item42 = types.KeyboardButton("❌ Отменить")
item43 = types.KeyboardButton("Открыть")
item44 = types.KeyboardButton("Закрыть")
item45 = types.KeyboardButton("Добавить товар в категории")
item46 = types.KeyboardButton("Удалить товар в категории")
item47 = types.KeyboardButton("Добавить  содержимое для товара")
item48 = types.KeyboardButton("Отчистить содержимое для товара")
item49 = types.KeyboardButton("Увеличить цену товаров в процентах")
item50 = types.KeyboardButton("Уменшить цену товаров в процентах")
item51 = types.KeyboardButton("Изменить цену товара")

abcd.row(item16,item13)
abcd.row(item6,item7)
markupotkr.row(item43, item44)
markupadminnazad.add(item6)
markupoplati.add(item41,item42)
markupkorzina.row(item39,item40)
markupkorzina.add(item11)
markup.add(item1)
markup.row(item2, item3)
markup.row(item4, item5)
markupadmin.add(item21, item22, item23)
markupadmin.row(item24, item25)
markupadmin.add(item26)
markupadmin.row(item27, item28)
markupadmin.row(item29, item30)
markupadmin.row(item31,item32,)
markupadmin.row(item33,item34)
markupadmin.row(item45,item46)
markupadmin.row(item47,item48)
markupadmin.row(item49,item50)
markupadmin.add(item51)
markupnomoney.add(item6, item7)
markupprofile.add(item8)
markupprofile.row(item9, item10)
markupprofile.add(item11)
markupwhentovarchosed.add(item12, item13, item6, item7)
markupamountchoose.add(item6, item7)
markupbacktomeny.add(item11)
abc.add(item35, item7)
markuppaymentchoose.add(item37,item11)
ekrc.row(item6, item7)

@bot.message_handler(commands=['start'])
def welcome(message):
    id = int( message.from_user.id)
    imya = message.from_user.username
    dannie = [(id,imya,0,0,0,0)]
    connection = sqlite3.connect("Spisokproductov.db")
    cursor = connection.cursor()

    t = (id,)
    cursor.execute('SELECT * FROM Users WHERE id=?', t)
    a = cursor.fetchone()

    if not a == None:
        bot.send_message(message.chat.id, 'C возвращением, {0.first_name}'.format(message.from_user), reply_markup = markup)
    else:  bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы продовать тебе цифровые товары".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    cursor.executemany("INSERT OR IGNORE INTO Users VALUES (?,?,?,?,?,?)", dannie)
    connection.commit()

@bot.message_handler(commands=['admin'])
def adminpannel(message):
    connection = sqlite3.connect("Spisokproductov.db")
    cursor = connection.cursor()

    t = (message.from_user.id,)
    cursor.execute('SELECT * FROM Users WHERE id=?', t)
    a = cursor.fetchone()
    if a[5] == 0:
        bot.send_message(message.chat.id, 'У вас нет прав администратора!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Общая информация")
def info(message):
    d = 0
    conn = sqlite3.connect("Spisokproductov.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Users")
    E = c.fetchall()
    c.execute("SELECT * FROM Vsepokupki3")
    s = c.fetchall()
    for i in range(len(E)):
        d = int(d) + int(E[i][4])
    bot.send_message(message.chat.id, 'Зарегистрированных пользователей в боте: '+ str(len(E))+'\nСумма всех пополнений: ' + str(d)+ ' $\nКол-во продаж: '+ str(len(s))+ ' шт.', reply_markup= markupadmin)

@bot.message_handler(func=lambda message: message.text == "Список администраторов")
def admini(message):
    conn = sqlite3.connect("Spisokproductov.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Users")
    E = c.fetchall()
    if len(E) > 0:
        bot.send_message(message.chat.id, 'Администраторы:', reply_markup= markupadmin)
    for i in range(len(E)):
        bot.send_message(message.chat.id, 'СhatId: '+ str(E[i][0]) + '\nЛогин: @'+str(E[i][1]))

@bot.message_handler(func=lambda message: message.text == "Изменить баланс пользователя")
def balancechng(message):
    msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg5, kek)

def kek(message):
    global i
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    elif message.text.isdigit():
        i = int(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (int(message.text),)
        c.execute('SELECT * FROM Users WHERE id=?', t)
        E = c.fetchone()
        if E == None:
            msg9 = bot.send_message(message.chat.id, 'Пользователь не найден!\nВведите id повторно', reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg9, kek)
        else:
            msg6 = bot.send_message(message.chat.id, 'Текущий баланс пользователя: '+ str(E[2])+ '\nУкажите новый баланс: ')
            bot.register_next_step_handler(msg6, ola)
    else:
        msg7 = bot.send_message(message.chat.id, 'Укажите Chatid:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg7, kek)

def ola(message):
    if message.text == '⏪ Назад':
        msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg5, kek)
    elif not message.text.isdigit():
        msg6 = bot.send_message(message.chat.id,'Укажите верное значение:')
        bot.register_next_step_handler(msg6, ola)
    else:
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        sql = """
        UPDATE Users 
        SET balance = ?
        WHERE id = ?
        """
        data = (int(message.text), i)
        c.execute(sql, data)
        conn.commit()
        bot.send_message(message.chat.id, 'Баланс успешно изменен!',reply_markup = markupadmin)

@bot.message_handler(func=lambda message: message.text == "Выдать админ права")
def admini(message):
    msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg5, lolo)
def lolo(message):
    if message.text.isdigit():
        o = int(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (o,)
        c.execute('SELECT * FROM Users WHERE id=?', t)
        E = c.fetchone()
        if E == None:
            msg9 = bot.send_message(message.chat.id, 'Пользователь не найден!\nВведите id повторно',reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg9, lolo)
        else:
            conn = sqlite3.connect("Spisokproductov.db")
            c = conn.cursor()
            sql = """
            UPDATE Users 
            SET admin = ?
            WHERE id = ?
            """
            data = (1, o)
            c.execute(sql, data)
            conn.commit()
            bot.send_message(message.chat.id, 'Права выданы', reply_markup=markupadmin)
    elif message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    else:
        msg6 = bot.send_message(message.chat.id, 'Укажите верное значение:')
        bot.register_next_step_handler(msg6, lolo)

@bot.message_handler(func=lambda message: message.text == "Лишить админ права")
def admini(message):
    msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg5, lolol)
def lolol(message):
    if message.text.isdigit():
        o = int(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (o,)
        c.execute('SELECT * FROM Users WHERE id=?', t)
        E = c.fetchone()
        if E == None:
            msg9 = bot.send_message(message.chat.id, 'Пользователь не найден!\nВведите id повторно',reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg9, lolol)
        else:
            conn = sqlite3.connect("Spisokproductov.db")
            c = conn.cursor()
            sql = """
            UPDATE Users 
            SET admin = ?
            WHERE id = ?
            """
            data = (0, o)
            c.execute(sql, data)
            conn.commit()
            bot.send_message(message.chat.id, 'Пользователь лишен прав', reply_markup=markupadmin)
    elif message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    else:
        msg6 = bot.send_message(message.chat.id, 'Укажите верное значение:')
        bot.register_next_step_handler(msg6, lolol)

@bot.message_handler(func=lambda message: message.text == "Закрыть/Открыть продажи")
def no(message):
    msg = bot.send_message(message.chat.id, 'Открыть или закрыть?:', reply_markup= markupotkr)
    bot.register_next_step_handler(msg, lololo)
def lololo(message):
    if message.text == 'Открыть':
        conn = sqlite3.connect('Spisokproductov.db')
        c = conn.cursor()
        sql = """
        UPDATE Statusprodag
        SET Status = 1 
        WHERE Status = 0
        """
        c.execute(sql)
        conn.commit()
        bot.send_message(message.chat.id, 'Продажи открыты', reply_markup=markupadmin)
    elif message.text == 'Закрыть':
        conn = sqlite3.connect('Spisokproductov.db')
        c = conn.cursor()
        sql = """
        UPDATE Statusprodag
        SET Status = 0 
        WHERE Status = 1
        """
        c.execute(sql)
        conn.commit()
        bot.send_message(message.chat.id, 'Продажи закрыты', reply_markup=markupadmin)
    else:
        msg = bot.send_message(message.chat.id, 'Открыть или закрыть?:', reply_markup= markupotkr)
        bot.register_next_step_handler(msg, lololo)

@bot.message_handler(func=lambda message: message.text == "Посмотреть профиль")
def pokazano(message):
    msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg5, lolopp)
def lolopp(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    elif not message.text.isdigit():
        msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg5, lolopp)
    else:
        o = int(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (o,)
        c.execute('SELECT * FROM Users WHERE id=?', t)
        E = c.fetchone()
        if E == None:
            msg7 = bot.send_message(message.chat.id, 'Пользователь не найден!\nВведите id повторно:', reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg7, lolopp)
        else:
            bot.send_message(message.chat.id,"ChatID: " + str(E[0]) + "\nЛогин: " + '@' + str(E[1]) + "\nТекущий баланс: " + str(E[2]) + " $." + "\nКоличество всех заказов: " + str(E[3]) + " шт." + "\nСумма всех пополнений: " + str(E[4]) + " $.", reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Посмотреть покупки")
def pokupku(message):
    msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg5, loloppo)
def loloppo(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    elif not message.text.isdigit():
        msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg5, loloppo)
    else:
        o = int(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (o,)
        c.execute('SELECT * FROM VSEPOKUPKI3 WHERE id=?', t)
        E = c.fetchall()
        if E == []:
            msg7 = bot.send_message(message.chat.id, 'Пользователь не найден или у него отсутствуют покупки!\nВведите id повторно:',reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg7, loloppo)
        else:
            for i in range(len(E)):
                bot.send_message(message.chat.id, 'Категория: '+str(E[i][1])+ '\nТовар: '+ str(E[i][2])+'\nКоличество: '+str(E[i][3])+'шт.', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Найти покупку по номеру заказа")
def pokupku(message):
    msg5 = bot.send_message(message.chat.id, 'Укажите номер покупки:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg5, loloppol)
def loloppol(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    elif not message.text.isdigit():
        msg5 = bot.send_message(message.chat.id, 'Укажите номер покупки', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg5, loloppol)
    else:
        o = int(message.text)
        o = o - 1
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        c.execute('SELECT * FROM VSEPOKUPKI3')
        E = c.fetchall()
        if o > len(E):
            msg5 = bot.send_message(message.chat.id, 'Покупки с таким номером не существуюе.\nПоследння покупка имеет номер: '+ str(len(E))+'\nВведите номер покупки заново:', reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg5, loloppol)
        else:
             bot.send_message(message.chat.id,'Категория: ' + str(E[o][1]) + '\nТовар: ' + str(E[o][2]) + '\nКоличество: ' + str(E[o][3]) + 'шт.', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Рассылка всем пользователям")
def pokupkus(message):
    msg5 = bot.send_message(message.chat.id, 'Введите сообщение:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg5, loloppols)
def loloppols(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    else:
        g = str(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        c.execute('SELECT * FROM Users')
        E = c.fetchall()
        for i in range(len(E)):
            bot.send_message(E[i][0], g)
        bot.send_message(message.chat.id, 'Рассылка отправлена успешно!', reply_markup = markupadmin)

@bot.message_handler(func=lambda message: message.text == "Сообщение пользователю")
def pokupkusf(message):
    msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg5,kish)

def kish(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    elif not message.text.isdigit():
        msg5 = bot.send_message(message.chat.id, 'Укажите id пользователя:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg5, kish)
    else:
        global p
        p = int(message.text)
        t = (p,)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        c.execute('SELECT * FROM Users WHERE id = ?', t)
        E = c.fetchone()
        if E == None:
            msg6 = bot.send_message(message.chat.id, 'Пользователь не зарегистрирован в боте.\nВведите id повторно:', reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg6, kish)
        else:
            msg6 = bot.send_message(message.chat.id , 'Ваше сообщение:', reply_markup= markupadminnazad)
            bot.register_next_step_handler(msg6, von)
def von(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    else:
        bot.send_message(p, message.text)
        bot.send_message(message.chat.id, 'Отправлено успешно', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Изменить цену товара")
def izmcnpokupkusf(message):
    msg5 = bot.send_message(message.chat.id, 'Укажите название товара:', reply_markup= markupadminnazad)
    bot.register_next_step_handler(msg5, lslsl)
def lslsl(message):
    global e
    e = str(message.text)
    conn = sqlite3.connect("Spisokproductov.db")
    c = conn.cursor()
    t = (e,)
    c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie = ?', t)
    k = c.fetchone()
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора!', reply_markup=markupadmin)
    elif k == None:
        msg5 = bot.send_message(message.chat.id, 'Такого товара нет!\nУкажите название товара:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg5, lslsl)
    else:
        bot.send_message(message.chat.id, 'Категория: '+str(k[1])+ '\nТовар: '+ str(k[0])+'\nКоличество: '+str(k[2])+'шт.'+'\nЦена за единицу товара: '+ str(k[3])+' $')
        msg6 = bot.send_message(message.chat.id, 'Укажите цену товара:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg6, pppp)

def pppp(message):
    if message.text == '⏪ Назад':
        msg5 = bot.send_message(message.chat.id, 'Укажите название товара:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg5, lslsl)
    elif not message.text.isdigit():
        msg6 = bot.send_message(message.chat.id, 'Укажите цену товара:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg6, pppp)
    else:
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        sql = """
        UPDATE Vsetovari2
        SET  zena = ? 
        WHERE Nazvanie = ?
        """
        f = (str(message.text), e)
        c.execute(sql, f)
        conn.commit()
        t = (e,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie = ?', t)
        E = c.fetchone()
        bot.send_message(message.chat.id, 'Цена товара изменена!\nНовая цена:'+str(E[3])+'$', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Добавить категорию")
def izmcnpokupkusf(message):
    msg6 = bot.send_message(message.chat.id, 'Укажите название категории:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg6, ppppp)
def ppppp(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    else:
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        k = str(message.text)
        f = (k,)
        c.execute('SELECT * FROM Categorii2 WHERE Categoria=?', f)
        d = c.fetchone()
        if d == None:
            c.execute("INSERT INTO Categorii2 VALUES (?)", f)
            conn.commit()
            bot.send_message(message.chat.id, 'Добавлена категория: ' + str(message.text), reply_markup=markupadmin)
        else:
            bot.send_message(message.chat.id, 'Категория существует!',reply_markup = markupadmin)

@bot.message_handler(func=lambda message: message.text == "Удалить категорию")
def izmcnpokupkusfs(message):
    msg6 = bot.send_message(message.chat.id, 'Укажите название категории:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg6, pppppp)
def pppppp(message):
    k = str(message.text)
    conn = sqlite3.connect("Spisokproductov.db")
    c = conn.cursor()
    t = (str(message.text),)
    c.execute('SELECT * FROM Categorii2 WHERE Categoria=?', t)
    E = c.fetchone()
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    elif E == None:
        msg6 = bot.send_message(message.chat.id, 'Категория не найдена!\nУкажите категорию:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg6, pppppp)
    else:
        f = str(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        sql = "DELETE FROM Categorii2 WHERE Categoria = ?"
        c.execute(sql, (f,))
        conn.commit()
        bot.send_message(message.chat.id, 'Удалена категория: '+str(message.text),reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Добавить товар в категории")
def izmcnpokupkusfss(message):
    msg6 = bot.send_message(message.chat.id, 'Укажите название категории:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg6, pppppppp)
def pppppppp(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    else:
        global f
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        f = str(message.text)
        t = (f,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Categoria = ?', t)
        E = c.fetchall()
        c.execute('SELECT * FROM Categorii2 WHERE Categoria = ?', t)
        F = c.fetchall()
        if E == [] and F == []:
            msg6 = bot.send_message(message.chat.id, 'Категория не найдена!\nВведите категорию:', reply_markup = markupadminnazad)
            bot.register_next_step_handler(msg6, pppppppp)
        else:
            msg6 = bot.send_message(message.chat.id, 'Введите название товара:', reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg6, Nazvanietvr)
def Nazvanietvr(message):
    global o
    o = str(message.text)
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    else:
        msg7 = bot.send_message(message.chat.id, 'Укажите количество:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg7, colvotovara)
def colvotovara(message):
    global l
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    elif not message.text.isdigit():
        msg7 = bot.send_message(message.chat.id, 'Укажите количество:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg7, colvotovara)
    else:
        l = int(message.text)
        msg7 = bot.send_message(message.chat.id, 'Укажите цену за штуку:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg7, cenatovara)
def cenatovara(message):
    global k
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    elif not message.text.isdigit():
        msg7 = bot.send_message(message.chat.id, 'Укажите цену за штуку:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg7, cenatovara)
    else:
        k = int(message.text)
        msg7 = bot.send_message(message.chat.id, 'Укажите ссылку:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg7, cenatovaras)
def cenatovaras(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    else:
        v = str(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        m = str(message.text)
        data = [o, f, l, k, v]
        c.execute("INSERT INTO Vsetovari2 VALUES (?,?,?,?,?)", data)
        conn.commit()
        bot.send_message(message.chat.id, 'Добавлен товар :'+str(o)+'\nКатегория: '+str(f)+'\nКоличество: '+str(l)+' шт.'+'\nЦена за штуку: '+str(k)+' $\nСсылка: '+str(m),parse_mode = 'html', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Удалить товар в категории")
def dobavitnet(message):
    msg6 = bot.send_message(message.chat.id, 'Укажите название категории:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg6, pppppppppp)
def pppppppppp(message):
    global f
    conn = sqlite3.connect("Spisokproductov.db")
    c = conn.cursor()
    f = str(message.text)
    t = (f,)
    c.execute('SELECT * FROM Vsetovari2 WHERE Categoria = ?', t)
    E = c.fetchall()
    c.execute('SELECT * FROM Categorii2 WHERE Categoria = ?', t)
    F = c.fetchall()
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    elif E == [] and F == []:
        msg6 = bot.send_message(message.chat.id, 'Категория не найдена!\nВведите категорию:',reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg6, pppppppp)
    else:
        ms = bot.send_message(message.chat.id, 'Укажите название товара:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(ms, ldld)

def ldld(message):
    conn = sqlite3.connect("Spisokproductov.db")
    c = conn.cursor()
    k = str(message.text)
    t = (k,)
    c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie = ?', t)
    E = c.fetchone()
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadminnazad)
    elif E == None:
        msg6 = bot.send_message(message.chat.id, 'Товар не найден!\nВведите название товара:', reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg6, pppppppppp)
    else:
        b = str(message.text)
        f = (b,)
        sql = "DELETE FROM Vsetovari2 WHERE Nazvanie = ?"
        c.execute(sql, f)
        conn.commit()
        bot.send_message(message.chat.id, 'Удалено успешно!', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Добавить  содержимое для товара")
def dobavits(message):
    msg = bot.send_message(message.chat.id, 'Укажите название товара:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg, dobavitsoder)
def dobavitsoder(message):
    global b, h
    b = str(message.text)
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    else:
        conn = sqlite3.connect('Spisokproductov.db')
        c = conn.cursor()
        h = str(message.text)
        h = (h,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie=?', h)
        h = c.fetchone()
        if h == None:
            msg = bot.send_message(message.chat.id, 'Товар не найден!\nВведите товар заново:')
            bot.register_next_step_handler(msg, dobavitsoder)
        else:
            msg2 = bot.send_message(message.chat.id, 'Укажите количество добавляемых ссылок:',reply_markup = markupadminnazad)
            bot.register_next_step_handler(msg2, ssilkeadds)
def ssilkeadds(message):
    global o
    if message.text == '⏪ Назад':
        msg = bot.send_message(message.chat.id, 'Укажите название товара:')
        bot.register_next_step_handler(msg, dobavitsoder)
    elif not message.text.isdigit():
        msg2 = bot.send_message(message.chat.id, 'Укажите количество добавляемых ссылок:',reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg2, ssilkeadds)
    else:
        o = int(message.text)
        msg2 = bot.send_message(message.chat.id, 'Укажите добавляеме ссылки(через пробел):',reply_markup=markupadminnazad)
        bot.register_next_step_handler(msg2, ssilkeadd)
def ssilkeadd(message):
    if message.text == '⏪ Назад':
        msg = bot.send_message(message.chat.id, 'Укажите название товара:')
        bot.register_next_step_handler(msg, dobavitsoder)
    else:
        m = str(message.text)
        conn = sqlite3.connect('Spisokproductov.db')
        c = conn.cursor()
        t = b
        t = (t,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie=?', t)
        h = c.fetchone()
        v = h[4]
        n = v +'\n'+ m
        sql = """
        UPDATE Vsetovari2 
        SET link = ? 
        WHERE Nazvanie = ?
        """
        data = (n, b)
        c.execute(sql, data)
        conn.commit()
        k = int(o) + int(h[2])
        sql = """
        UPDATE Vsetovari2 
        SET colvo = ? 
        WHERE Nazvanie = ?
        """
        datas = (k, b)
        c.execute(sql, datas)
        conn.commit()
        bot.send_message(message.chat.id, 'Содержимое обновлено!', reply_markup = markupadmin)

@bot.message_handler(func=lambda message: message.text == "Отчистить содержимое для товара")
def popolnenies(message):
    msg = bot.send_message(message.chat.id, 'Укажите название товара:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg, ydalitsoder)
def ydalitsoder(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    else:
        conn = sqlite3.connect('Spisokproductov.db')
        c = conn.cursor()
        h = str(message.text)
        b = h
        h = (h,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie=?', h)
        h = c.fetchone()
        if h  ==  None:
            msg = bot.send_message(message.chat.id, 'Товар не найден!\nВведите товар заново:')
            bot.register_next_step_handler(msg, dobavitsoder)
        else:
            conn = sqlite3.connect('Spisokproductov.db')
            c = conn.cursor()
            sql = """
            UPDATE Vsetovari2 
            SET link = ? 
            WHERE Nazvanie = ?
            """
            data = (None, b)
            c.execute(sql, data)
            conn.commit()
            sql = """
            UPDATE Vsetovari2 
            SET colvo = ? 
            WHERE Nazvanie = ?
            """
            data = (0, b)
            c.execute(sql, data)
            conn.commit()
            bot.send_message(message.chat.id, 'Содержимое удалено!', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Увеличить цену товаров в процентах")
def popolnenies(message):
    msg6 = bot.send_message(message.chat.id, 'Укажите название категории:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg6, persentplus)
def persentplus(message):
    global d
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    else:
        e = str(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (e,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Categoria = ?', t)
        E = c.fetchall()
        c.execute('SELECT * FROM Categorii2 WHERE Categoria = ?', t)
        F = c.fetchall()
        if E == [] or F == []:
            msg6 = bot.send_message(message.chat.id, 'Категория не найдена или в ней нет сейчас товаров!\nВведите категорию:',reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg6, persentplus)
        else:
            d = str(message.text)
            mk = bot.send_message(message.chat.id, 'Укажите процент увеличения(без знака %):', reply_markup=markupadminnazad)
            bot.register_next_step_handler(mk, loshara)
def loshara(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    elif not message.text.isdigit():
        mk = bot.send_message(message.chat.id, 'Укажите процент увеличения(без знака %):', reply_markup=markupadminnazad)
        bot.register_next_step_handler(mk, loshara)
    else:
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (d,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Categoria = ?', t)
        E = c.fetchall()
        for i in range(len(E)):
            u = E[i][3]
            u = u * float(message.text) / 100 + u
            sql = """
            UPDATE Vsetovari2
            SET zena = ? 
            WHERE Nazvanie = ?
            """
            e = (u, E[i][0])
            c.execute(sql, e)
            conn.commit()
        bot.send_message(message.chat.id, 'Цены увеличены!', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "Уменшить цену товаров в процентах")
def popolnenies(message):
    msg6 = bot.send_message(message.chat.id, 'Укажите название категории:', reply_markup=markupadminnazad)
    bot.register_next_step_handler(msg6, persentpluss)
def persentpluss(message):
    global d
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    else:
        e = str(message.text)
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (e,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Categoria = ?', t)
        E = c.fetchall()
        c.execute('SELECT * FROM Categorii2 WHERE Categoria = ?', t)
        F = c.fetchall()
        if E == [] or F == []:
            msg6 = bot.send_message(message.chat.id, 'Категория не найдена или в ней нет сейчас товаров!\nВведите категорию:',reply_markup=markupadminnazad)
            bot.register_next_step_handler(msg6, persentpluss)
        else:
            d = str(message.text)
            mk = bot.send_message(message.chat.id, 'Укажите процент увеличения(без знака %):', reply_markup=markupadminnazad)
            bot.register_next_step_handler(mk, losharas)
def losharas(message):
    if message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Меню администратора', reply_markup=markupadmin)
    elif not message.text.isdigit():
        mk = bot.send_message(message.chat.id, 'Укажите процент увеличения(без знака %):', reply_markup=markupadminnazad)
        bot.register_next_step_handler(mk, losharas)
    else:
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (d,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Categoria = ?', t)
        E = c.fetchall()
        for i in range(len(E)):
            u = E[i][3]
            u = u - u * float(message.text) / 100
            sql = """
            UPDATE Vsetovari2
            SET zena = ? 
            WHERE Nazvanie = ?
            """
            e = (u, E[i][0])
            c.execute(sql, e)
            conn.commit()
        bot.send_message(message.chat.id, 'Цены уменьшены!', reply_markup=markupadmin)

@bot.message_handler(func=lambda message: message.text == "💵 Пополнить баланс 💵")
def popolnenie(message):
    msg2 = bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=markuppaymentchoose)
    bot.register_next_step_handler(msg2 , lol)

def lol(message):
    if message.text == '⏪ Вернуться в меню':
        bot.send_message(message.chat.id, 'Пополнение баланса отменено!', reply_markup = markup)
    elif message.text == 'BTC':
        msg4 = bot.send_message(message.chat.id, 'Введите нужную сумму в долларах для пополнения (минимум - 1 $):', reply_markup = markupnomoney)
        bot.register_next_step_handler(msg4, next)
    else:
        msg2 = bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=markuppaymentchoose)
        bot.register_next_step_handler(msg2, lol)

def next(message):
    get_balance(btcadress)
    global d
    d = v
    if message.text == '❌ Отмена':
        bot.send_message(message.chat.id, 'Пополнение баланса отменено!', reply_markup=markup)
    elif message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=markuppaymentchoose)
    elif not message.text.isdigit():
        msg4 = bot.send_message(message.chat.id, 'Ошибка при считывании суммы пополнения, введите сумму, которая больше 0:', reply_markup = markupnomoney)
        bot.register_next_step_handler(msg4, next)
    else:
        global j, o
        j = int(message.text)
        o = j/F
        bot.send_message(message.chat.id, 'Для пополнения баланса, оплати счет по ссылке ниже.\n\n💰 Сумма: '+str(j)+ ' $❗️ Время на оплату платежа: 30 минут')
        bot.send_message(message.chat.id, '<a href="https://blockchain.com/btc/payment_request?address=1LjBjcCXTf2KigGJC72jaFQFTkXDmhuuTf&amount='+str(o)+'&message=Оплатите для пополнения баланса!">Приступить к оплате</a>', parse_mode= html, reply_markup = markupoplati)
        bot.send_message(message.chat.id, '👾 После оплаты, нажмите на кнопку "Оплатил')

@bot.message_handler(func=lambda message: message.text == "❌ Отменить")
def otmenit(message):
    bot.send_message(message.chat.id, 'Пополнение баланса отменено!', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "BTC")
def a(message):
    msg4 = bot.send_message(message.chat.id, 'Введите нужную сумму в доллорах для пополнения (минимум - 1 $):', reply_markup = markupnomoney)
    bot.register_next_step_handler(msg4, next)

def next(message):
    get_balance(btcadress)
    global d
    d = v
    if message.text == '❌ Отмена':
        bot.send_message(message.chat.id, 'Пополнение баланса отменено!', reply_markup=markup)
    elif message.text == '⏪ Назад':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=markuppaymentchoose)
    elif not message.text.isdigit():
        msg4 = bot.send_message(message.chat.id,'Ошибка при считывании суммы пополнения, введите сумму, которая больше 0:',reply_markup=markupnomoney)
        bot.register_next_step_handler(msg4, next)
    else:
        global j, o
        j = int(message.text)
        o = j / F
        bot.send_message(message.chat.id, 'Для пополнения баланса, оплати счет по ссылке ниже.\n\n💰 Сумма: ' + str(j) + ' $❗️ Время на оплату платежа: 30 минут')
        bot.send_message(message.chat.id,'<a href="https://blockchain.com/btc/payment_request?address=1LjBjcCXTf2KigGJC72jaFQFTkXDmhuuTf&amount=' + str(o) + '&message=Оплатите для пополнения баланса!">Приступить к оплате</a>', parse_mode='html',reply_markup=markupoplati)
        bot.send_message(message.chat.id, '👾 После оплаты, нажмите на кнопку "Оплатил')

@bot.message_handler(func=lambda message: message.text == "✔️ Оплатил")
def proverkaoplati(message):
    id = int(message.from_user.id)
    bot.send_message(message.chat.id, 'Проверяем оплату(10 сек.)')
    conn = sqlite3.connect("Spisokproductov.db")
    c = conn.cursor()
    t = (id,)
    c.execute('SELECT * FROM Users WHERE id = ?', t)
    E = c.fetchone()
    k = int(j) + int(E[2])
    f = int(j) + int(E[4])
    get_balance(btcadress)
    n = o + d
    if v == n:
        sql ="""
        UPDATE Users 
        SET balance = ? 
        WHERE id = ?
        """
        f = (k, message.from_user.id)
        c.execute(sql, f)
        conn.commit()
        sql = """
        UPDATE Users 
        SET summavsexpopolnenii = ?
        WHERE id = ?
        """
        data = (f, id)
        c.execute(sql, data)
        conn.commit()
        bot.send_message(message.chat.id, 'Оплачено успешно!\nВаш новый баланс: ' + str(f) + ' $', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '📱 Оплата не найдена\n🔔 Произошла ошибка? Напишите нам!', reply_markup = markupoplati)
@bot.message_handler(func=lambda message: message.text == "🆘 Тех Поддержка")
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Опишите вашу проблему (изображения и документы, если это требуется, отправляйте внешней ссылкой!):', reply_markup = markupbacktomeny )
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    if message.text == '⏪ Вернуться в меню':
        bot.send_message(message.chat.id, 'Обращение в Тех Поддержку отменено!', reply_markup = markup)
    else:
        bot.send_message(message.chat.id, 'Ваше сообщение отправлено, в ближайшее время вам ответят, ожидайте!', reply_markup = markup)

@bot.message_handler(func=lambda message: message.text == "💬Отзывы")
def otzivi(message):
    bot.send_message(message.chat.id, "Отзывы вы можете найти в нашем канале:\nhttps://t.me/joinchat/AAAAAFXDTuzwmalEd9_sbQ",parse_mode='html', reply_markup = markup)

@bot.message_handler(func=lambda message: message.text == "ℹ️ Правила")
def pravila(message):
    bot.send_message(message.chat.id,"Правила таковы:Можно купить товар и продать,но нельзя его потрогать.Если у вас есть вопросы ,то ответы на них вы можете получить нигде",reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "👤 Мой профиль")
def profilecommands(message):
    id = str(message.from_user.id)
    imya = str(message.from_user.username)
    connection = sqlite3.connect("Spisokproductov.db")
    cursor = connection.cursor()
    t = (id,)
    cursor.execute('SELECT * FROM Users WHERE id=?', t)
    a = cursor.fetchone()
    bot.send_message(message.chat.id,"Ваш ChatID: " + id + "\nВаш логин: " + '@' + imya + "\nВаш текущий баланс: " + str(a[2]) + " $." + "\nКоличество всех заказов: " + str(a[3]) + " шт." + "\nСумма всех пополнений: " + str(a[4]) + " $.", reply_markup=markupprofile)

@bot.message_handler(func=lambda message: message.text == "⏪ Вернуться в меню")
def bacttomeny(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "💳 Мои покупки")
def pokupki(message):
    connection = sqlite3.connect("Spisokproductov.db")
    cursor = connection.cursor()
    id = int(message.from_user.id)
    t = (id,)
    cursor.execute('SELECT * FROM VSEPOKUPKI3 WHERE id=?', t)
    k = cursor.fetchall()
    if k == []:
        bot.send_message(message.chat.id, 'Вы не совершали покупок!', reply_markup = markupprofile)
    else:
        for i in range(len(k)):
            bot.send_message(message.chat.id, 'Категория: '+str(k[i][1])+ '\nТовар: '+ str(k[i][2])+'\nКоличество: '+str(k[i][3])+'шт.'+'\nЦена за единицу товара: '+ str(k[i][4])+' $', reply_markup=markupprofile)
            u = k[i][5]
            u = u.split('\n')
            for c in range(len(u)-1):
                bot.send_message(message.chat.id, 'Ссылка:\n'+str(u[c]), parse_mode = 'html')

@bot.message_handler(func=lambda message: message.text == "🛒 Моя корзина")
def korzina(message):
    global b
    b = 0
    c = 0
    connection = sqlite3.connect("Spisokproductov.db")
    cursor = connection.cursor()
    id = int(message.from_user.id)
    t = (id,)
    cursor.execute('SELECT * FROM Polzovatelakorzina WHERE id=?', t)
    k = cursor.fetchall()
    if k == []:
        bot.send_message(message.chat.id, 'Вы ничего не добавляли в корзину!', reply_markup=markupprofile)
    else:
        for i in range(len(k)):
            c = int(k[i][3]) * int(k[i][4])
            bot.send_message(message.chat.id, 'Категория: '+str(k[i][1])+ '\nТовар: '+ str(k[i][2])+'\nКоличество: '+str(k[i][3])+'шт.'+ '\nК оплате: '+ str(c)+ '$' )
            b = b + int(k[i][3]) * int(k[i][4])
        bot.send_message(message.chat.id, 'Общая стоимость корзины: ' + str(b)+ '$',reply_markup =markupkorzina)

@bot.message_handler(func=lambda message: message.text == "💵 Оплатить корзину")
def oplatitikorziny(message):
    id = int(message.from_user.id)
    conn = sqlite3.connect("Spisokproductov.db")
    c = conn.cursor()
    t = (id,)
    c.execute('SELECT * FROM Users WHERE id=?', t)
    a = c.fetchone()
    c.execute('SELECT * FROM Polzovatelakorzina WHERE id=?', t)
    f = c.fetchall()
    b = 0
    for i in range(len(f)):
        b = b + int(f[i][4]) * int(f[i][3])
    if int(a[2]) < int(b):
        bot.send_message(message.chat.id, 'На вашем балансе недостаточно средств для данной покупки!', reply_markup = markup)
    else:
        connection = sqlite3.connect("Spisokproductov.db")
        cursor = connection.cursor()
        e = a[2] - b
        sql = """
        UPDATE Users 
        SET balance = ?
        WHERE id = ?
        """
        data = (e, id)
        cursor.execute(sql, data)
        connection.commit()
        conn = sqlite3.connect("Spisokproductov.db")
        c = conn.cursor()
        t = (id,)
        c.execute('SELECT * FROM Polzovatelakorzina WHERE id=?', t)
        k = c.fetchall()
        sql = """
        UPDATE Users 
        SET kolvopokupok = ?
        WHERE id = ?
        """
        p = 0
        for i in range(len(k)):
            p = p + int(k[i][3])
        Y = int(a[3]) + int(p)
        data = (Y, id)
        c.execute(sql, data)
        conn.commit()
        for i in range(len(k)):
            bot.send_message(message.chat.id, 'Товар: ' + str(k[i][2]) )
            n = k[i][5]
            n = n.split('\n')
            for qw in range(len(n)-1):
                bot.send_message(message.chat.id, 'Заберите товар здесь:\n'+n[qw], parse_mode = 'html')
        sql2 = "DELETE FROM Polzovatelakorzina WHERE id = id"
        c.execute(sql2)
        conn.commit()
        bot.send_message(message.chat.id, 'Корзина успешно оплачена, ваш новый баланс:'+str(e)+'.\nНаслаждайтесь вашими товарами!', reply_markup= markup)

@bot.message_handler(func=lambda message: message.text == "❌ Очистить корзину")
def ochistka(message):
    id = int(message.from_user.id)
    conn = sqlite3.connect("Spisokproductov.db")
    c = conn.cursor()
    id = (id,)
    c.execute('SELECT * FROM Polzovatelakorzina WHERE id=?', id)
    d = c.fetchall()
    sql = "DELETE FROM Polzovatelakorzina WHERE id = id"
    c.execute(sql)
    conn.commit()
    for i in range(len(d)):
        try:
            t = d[i][2]
            t = (t,)
            c.execute('SELECT * FROM Vsetovari2 WHERE nazvanie=?', t)
            e = c.fetchone()
            p = e[4] +'\n'+ d[i][5]
            sql = """
            UPDATE Vsetovari2
            SET link = ? 
            WHERE Nazvanie = ?
            """
            data = (p, d[i][2])
            c.execute(sql, data)
            conn.commit()
            sql = """
            UPDATE Vsetovari2
            SET colvo = ? 
            WHERE Nazvanie = ?
            """
            a = int(e[2]) + int(d[i][3])
            data = (a, d[i][2])
            c.execute(sql, data)
            conn.commit()
        except:
            dannie = (d[i][2], d[i][1], d[i][3], d[i][4],d[i][5])
            c.execute("INSERT INTO Vsetovari2 VALUES (?,?,?,?,?)", dannie)
            conn.commit()
    bot.send_message(message.chat.id, 'Корзина успешно отчищена!', reply_markup = markupprofile)

@bot.message_handler(func=lambda message: message.text == "💳 Выбор товаров для покупки 💳")
def pokupri(message):
    global E, markupsctg
    conn = sqlite3.connect('Spisokproductov.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Statusprodag')
    e = c.fetchone()
    c.execute('SELECT * FROM Categorii2')
    E = c.fetchall()
    markupsctg = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for i in range(len(E)):
        a = types.KeyboardButton(E[i][0])
        markupsctg.add(a)
    markupsctg.add(item7)
    if e[0] == 1:
        msg7 = bot.send_message(message.chat.id, 'Выберите категорию.', reply_markup=markupsctg)
        bot.register_next_step_handler(msg7, tovarselect)
    else:
        bot.send_message(message.chat.id, 'Продажи закрыты!\nПриходите позже!', reply_markup=markup)

def tovarselect(message):
    global markupselecttovar
    conn = sqlite3.connect('Spisokproductov.db')
    c = conn.cursor()
    j = str(message.text)
    j = (j,)
    conn = sqlite3.connect('Spisokproductov.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Vsetovari2 WHERE categoria = ?', j)
    b = c.fetchall()
    markupselecttovar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for i in range(len(b)):
        a = types.KeyboardButton(b[i][0] + ' | ' + str(b[i][3]) + ' $ ' + ' | ' + ' В наличии: ' + str(b[i][2]) + ' шт.')
        if not b[i][2] == 0:
            markupselecttovar.add(a)
    markupselecttovar.row(item6, item7)
    if j in E:
        msg = bot.send_message(message.chat.id, 'Выберите товар для покупки.', reply_markup=markupselecttovar)
        bot.register_next_step_handler(msg, vibrantovar)
    elif message.text == '❌ Отмена':
        bot.send_message(message.chat.id, 'Меню', reply_markup = markup)
    else:
        msg = bot.send_message(message.chat.id, 'Выберите категорию.', reply_markup=markupsctg)
        bot.register_next_step_handler(msg, tovarselect)
def vibrantovar(message):
    global g,x
    if message.text == '⏪ Назад':
        msg = bot.send_message(message.chat.id, 'Выберите категорию.', reply_markup=markupsctg)
        bot.register_next_step_handler(msg, tovarselect)
    elif message.text == '❌ Отмена':
        bot.send_message(message.chat.id, 'Меню', reply_markup=markup)
    else:
        m = str(message.text)
        k = m.find('|')
        if not k == -1:
            e = ''
            for i in range(0, k - 1):
                e = e + m[i]
            g = e
            e = (e,)
            conn = sqlite3.connect('Spisokproductov.db')
            c = conn.cursor()
            c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie = ?', e)
            x = c.fetchone()
            msg7 = bot.send_message(message.chat.id,'🏷 ВЫБРАН ТОВАР «' + str(x[0]) + ' | ' + str(x[3]) + ' $ | В наличии: ' + str(x[2]) + ' шт.»\n\nВведите нужное количество для покупки:',reply_markup=markupamountchoose)
            bot.register_next_step_handler(msg7, lopster)
        else:
            msg = bot.send_message(message.chat.id, 'Выберите товар для покупки.', reply_markup=markupselecttovar)
            bot.register_next_step_handler(msg, vibrantovar)
def lopster(message):
    global m,f
    if message.text == '⏪ Назад':
        msg = bot.send_message(message.chat.id, 'Выберите товар для покупки.', reply_markup=markupselecttovar)
        bot.register_next_step_handler(msg, vibrantovar)
    elif message.text == '❌ Отмена':
        bot.send_message(message.chat.id, 'Меню', reply_markup=markup)
    elif not message.text.isdigit():
        msg = bot.send_message(message.chat.id, 'Не корректные данные, введите количество снова:', reply_markup=markupsctg)
        bot.register_next_step_handler(msg, lopster)
    else:
        f = message.text
        e = (g,)
        conn = sqlite3.connect('Spisokproductov.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie = ?', e)
        x = c.fetchone()
        k = int(message.text)
        if k > x[2] or k == 0 :
            msg = bot.send_message(message.chat.id, 'Такое количество товаров недоступно!\nВ данный момент можно купить только: '+str(x[2])+' шт.\nВведите количество снова:',reply_markup=ekrc )
            bot.register_next_step_handler(msg, lopster)
        else:
            m = int(message.text) * int(x[3])
            msg = bot.send_message(message.chat.id, 'Товар: '+str(x[0])+'\nКоличество: '+str(f)+' шт.\nК оплате: '+str(m)+' $\nПодтвердить покупку или добавить товар в корзину?', reply_markup=abcd)
            bot.register_next_step_handler(msg, potchi)
def potchi(message):
    if message.text == '⏪ Назад':
        msg = bot.send_message(message.chat.id, 'Выберите товар для покупки.', reply_markup=markupselecttovar)
        bot.register_next_step_handler(msg, vibrantovar)
    elif message.text == '❌ Отмена':
        bot.send_message(message.chat.id, 'Меню', reply_markup=markup)
    elif message.text == '✔ Потвердить':
        conn = sqlite3.connect('Spisokproductov.db')
        c = conn.cursor()
        z = message.chat.id
        v = z
        z = (z,)
        c.execute('SELECT * FROM Users WHERE id = ?', z)
        n = c.fetchone()
        if n[2] < m:
            bot.send_message(message.chat.id, 'На вашем балансе недостаточно средств для данной покупки!', reply_markup=markup)
        else:
            r = x[2] - int(f)
            sql = """
            UPDATE Vsetovari2
            SET colvo = ? 
            WHERE nazvanie = ?
            """
            data = (r, x[0])
            c.execute(sql, data)
            conn.commit()
            d = int(n[2]) - int(m)
            conn = sqlite3.connect('Spisokproductov.db')
            c = conn.cursor()
            sql = """
            UPDATE Users
            SET balance = ? 
            WHERE id = ?
            """
            data = (d, int(message.from_user.id))
            c.execute(sql, data)
            conn.commit()
            conn = sqlite3.connect('Spisokproductov.db')
            c = conn.cursor()
            sql = """
            UPDATE Users
            SET kolvopokupok = ? 
            WHERE id = ?
            """
            y = int(n[3])+int(f)
            datas = (y,v)
            c.execute(sql, datas)
            conn.commit()
            bot.send_message(message.chat.id, 'Наслаждайтесь вашими товарами!', reply_markup=markup)
            w = x[4]
            d = w.split('\n')
            u = ''
            for i in range(0, int(f)):
                bot.send_message(message.chat.id, 'Заберите ваш товар здесь:\n' + str(d[i]),parse_mode = 'html', reply_markup=markup)
                u = u + d[i]+'\n'
            p = x[4]
            p = p.replace(u, '')
            sql = """
            UPDATE Vsetovari2
            SET link = ? 
            WHERE nazvanie = ?
            """
            data = (p, x[0])
            c.execute(sql, data)
            conn.commit()
            dannie = [(int(message.from_user.id), x[1], x[0], int(f), x[3], u)]
            c.executemany("INSERT INTO VSEPOKUPKI3 VALUES (?,?,?,?,?,?)", dannie)
            conn.commit()
            d = x[0]
            d = (d,)
            c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie = ?', d)
            a = c.fetchone()
            if a[2] == 0:
                sql = "DELETE FROM Vsetovari2 WHERE Nazvanie = ?"
                c.execute(sql, d)
                conn.commit()
    elif message.text == '🛒 Добавить в корзину':
        conn = sqlite3.connect('Spisokproductov.db')
        c = conn.cursor()
        r = x[2] - int(f)
        sql = """
        UPDATE Vsetovari2
        SET colvo = ? 
        WHERE nazvanie = ?
        """
        data = (r, x[0])
        c.execute(sql, data)
        conn.commit()
        w = x[4]
        d = w.split('\n')
        u = ''
        for i in range(0, int(f)):
            u = u + d[i] + '\n'
        p = x[4]
        p = p.replace(u, '')
        sql = """
        UPDATE Vsetovari2
        SET link = ? 
        WHERE nazvanie = ?
        """
        data = (p, x[0])
        c.execute(sql, data)
        conn.commit()
        d = x[0]
        d = (d,)
        c.execute('SELECT * FROM Vsetovari2 WHERE Nazvanie = ?', d)
        a = c.fetchone()
        if a[2] == 0:
            sql = "DELETE FROM Vsetovari2 WHERE Nazvanie = ?"
            c.execute(sql, d)
            conn.commit()
        dannie = [(int(message.from_user.id), x[1], x[0], int(f), x[3], u)]
        try:
            t = x[0]
            t = (t,)
            c.execute('SELECT * FROM Polzovatelakorzina WHERE nazvanie=?', t)
            e = c.fetchone()
            p = e[5] +'\n'+ u
            sql = """
            UPDATE Polzovatelakorzina
            SET link = ? 
            WHERE nazvanie = ?
            """
            data = (p, x[0])
            c.execute(sql, data)
            conn.commit()
            sql = """
            UPDATE Polzovatelakorzina
            SET colichestvo = ? 
            WHERE nazvanie = ?
            """
            a = int(e[3]) + int(f)
            data = (a, x[0])
            c.execute(sql, data)
            conn.commit()
        except:
            c.executemany("INSERT INTO Polzovatelakorzina VALUES (?,?,?,?,?,?)", dannie)
            conn.commit()
        bot.send_message(message.chat.id, 'Товар успешно добавлен в корзину!', reply_markup=markup)
    else:
        msg = bot.send_message(message.chat.id,'Товар: ' + str(x[0]) + '\nКоличество: ' + str(f) + ' шт.\nК оплате: ' + str(m) + ' $\nПодтвердить покупку или добавить товар в корзину?', reply_markup=abcd)
        bot.register_next_step_handler(msg, potchi)

@bot.message_handler(func=lambda message: message.text == "❌ Отмена")
def otmena(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup = markup)

@bot.message_handler(func=lambda message: message.text == "❌ Отменить")
def otmenit(message):
    bot.send_message(message.chat.id, 'Пополнение баланса отменено!', reply_markup = markup)

@bot.message_handler(func=lambda message: message.text == "⏪ Назад")
def otmena(message):
    bot.send_message(message.chat.id, 'Меню адиминистратора', reply_markup = markupadmin)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def nettakoicmd(message):
    bot.send_message(message.chat.id, 'Такой команды не существует!')

bot.polling(none_stop=True)
