# -*- coding: utf-8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import message_list
import random
from datetime import datetime
import time

token = ''

vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

permitted_user = []
mailing_list = []
week_info = []

elder_id = 408637275
mailing_flag = 0
message_flag = 0


id_list = open('id_list.txt', 'r')
id_l = id_list.readlines()
count_person = id_l[0]
for num in range(1, int(count_person)+1):
    permitted_user.append(int(id_l[num]))
id_list.close()

id_board = open('id_board.txt', 'r')
id_b = id_board.readlines()
count_person_board = id_b[0]
for num in range(1, int(count_person_board)+1):
    mailing_list.append(int(id_b[num]))
id_board.close()

def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, 2147483648), "attachment": attachment, 'keyboard': keyboard})

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'default_1':
        keyboard.add_button('Расписание на сегодня', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Расписание на завтра', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        #keyboard.add_button('Подписаться на рассылку расписания', color=VkKeyboardColor.PRIMARY)
        #keyboard.add_line()
        keyboard.add_button('Материал', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Преподаватели', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Закрыть', color=VkKeyboardColor.NEGATIVE)


    elif response == 'default_2':
        keyboard.add_button('Расписание на сегодня', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Расписание на завтра', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        #keyboard.add_button('Отписаться от рассылки расписания', color=VkKeyboardColor.NEGATIVE)
        #keyboard.add_line()
        keyboard.add_button('Материал', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Преподаватели', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Закрыть', color=VkKeyboardColor.NEGATIVE)

    elif response == 'elder_1':
        keyboard.add_button('Отправить сообщение группе', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Расписание на сегодня', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Расписание на завтра', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        #keyboard.add_button('Подписаться на рассылку расписания', color=VkKeyboardColor.PRIMARY)
        #keyboard.add_line()
        keyboard.add_button('Материал', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Преподаватели', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Закрыть', color=VkKeyboardColor.NEGATIVE)

    elif response == 'elder_2':
        keyboard.add_button('Отправить сообщение группе', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Расписание на сегодня', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Расписание на завтра', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        #keyboard.add_button('Отписаться от рассылки расписания', color=VkKeyboardColor.NEGATIVE)
        #keyboard.add_line()
        keyboard.add_button('Материал', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Преподаватели', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Закрыть', color=VkKeyboardColor.NEGATIVE)

    elif response == 'закрыть':
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard

def numberweek():
    numberw = (datetime.utcnow().isocalendar()[1])
    return int(numberw)

def get_board(day):
    if numberweek() % 2 == 0:
        ch = 1
    else:
        ch = 0
    dayweek = (time.strftime('%w', time.localtime()))
    if day == 0:
        dw = int(dayweek)
        if ch == 1:
            if dw == 0:
                mes = 'Выходной'
            elif dw == 1:
                mes = message_list.msg1_monday
            elif dw == 2:
                mes = message_list.msg1_tuesday
            elif dw == 3:
                mes = message_list.msg1_wednesday
            elif dw == 4:
                mes = message_list.msg1_thursday
            elif dw == 5:
                mes = message_list.msg1_friday
            elif dw == 6:
                mes = message_list.msg1_saturday
        if ch == 0:
            if dw == 0:
                mes = 'Выходной'
            elif dw == 1:
                mes = message_list.msg2_monday
            elif dw == 2:
                mes = message_list.msg2_tuesday
            elif dw == 3:
                mes = message_list.msg2_wednesday
            elif dw == 4:
                mes = message_list.msg2_thursday
            elif dw == 5:
                mes = message_list.msg2_friday
            elif dw == 6:
                mes = message_list.msg2_saturday
    elif day == 1:
        dw = int(dayweek) + 1
        if dw > 6:
            dw = 0
        if ch == 1:
            if dw == 0:
                mes = 'Выходной'
            elif dw == 1:
                mes = message_list.msg1_monday
            elif dw == 2:
                mes = message_list.msg1_tuesday
            elif dw == 3:
                mes = message_list.msg1_wednesday
            elif dw == 4:
                mes = message_list.msg1_thursday
            elif dw == 5:
                mes = message_list.msg1_friday
            elif dw == 6:
                mes = message_list.msg1_saturday
        if ch == 0:
            if dw == 0:
                mes = 'Выходной'
            elif dw == 1:
                mes = message_list.msg2_monday
            elif dw == 2:
                mes = message_list.msg2_tuesday
            elif dw == 3:
                mes = message_list.msg2_wednesday
            elif dw == 4:
                mes = message_list.msg2_thursday
            elif dw == 5:
                mes = message_list.msg2_friday
            elif dw == 6:
                mes = message_list.msg2_saturday
    return mes


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.from_user and not (event.from_me):
                    response = event.text.lower()
                    if (response != 'закрыть') and (int(event.user_id) != elder_id) and (mailing_list.count(event.user_id) == 0):
                        key_base = 'default_1'
                    elif (response != 'закрыть') and (int(event.user_id) != elder_id) and (mailing_list.count(event.user_id) == 1):
                        key_base = 'default_2'
                    elif (int(event.user_id) == elder_id) and (response != 'закрыть') and (mailing_list.count(event.user_id) == 0):
                        key_base = 'elder_1'
                    elif (int(event.user_id) == elder_id) and (response != 'закрыть') and (mailing_list.count(event.user_id) == 1):
                        key_base = 'elder_2'
                    else:
                        key_base = 'закрыть'
                    keyboard = create_keyboard(key_base)
                    if (permitted_user.count(event.user_id) == 0):
                        if response == "привет":
                            send_message(vk_session, 'user_id', event.user_id, message=message_list.msg1, keyboard=keyboard)
                            permitted_user.append(event.user_id)
                        else:
                            send_message(vk_session, 'user_id', event.user_id, message=message_list.msg1, keyboard=keyboard)
                            permitted_user.append(event.user_id)
                    elif (permitted_user.count(event.user_id) == 1):
                        if response == "расписание на сегодня":
                            send_message(vk_session, 'user_id', event.user_id, message=get_board(0), keyboard=keyboard)
                        elif (event.user_id == elder_id) and (response == 'отправить сообщение группе'):
                            send_message(vk_session, 'user_id', event.user_id, message=message_list.msg8, keyboard=keyboard)
                            mailing_flag = 1
                        elif (event.user_id == elder_id) and (mailing_flag == 1):
                            mailing_message = event.text
                            week_info.append(mailing_message)
                            message_flag = 1
                            send_message(vk_session, 'user_id', event.user_id, message = message_list.msg9, keyboard=keyboard)
                        elif response == "расписание на завтра":
                            send_message(vk_session, 'user_id', event.user_id, message=get_board(1), keyboard=keyboard)
                        elif response == "подписаться на рассылку расписания":
                            if mailing_list.count(event.user_id) == 0:
                                if event.user_id == elder_id:
                                    keyboard = create_keyboard('elder_2')
                                else:
                                    keyboard = create_keyboard('default_2')
                                send_message(vk_session, 'user_id', event.user_id, message=message_list.msg4, keyboard=keyboard)
                                mailing_list.append(event.user_id)
                            else:
                                send_message(vk_session, 'user_id', event.user_id, message=message_list.msg6, keyboard=keyboard)
                        elif response == "отписаться от рассылки расписания":
                            if mailing_list.count(event.user_id) == 1:
                                if event.user_id == elder_id:
                                    keyboard = create_keyboard('elder_1')
                                else:
                                    keyboard = create_keyboard('default_1')
                                send_message(vk_session, 'user_id', event.user_id, message=message_list.msg5, keyboard=keyboard)
                                mailing_list.remove(event.user_id)
                            else:
                                send_message(vk_session, 'user_id', event.user_id, message=message_list.msg7, keyboard=keyboard)
                        elif response == "материал":
                            send_message(vk_session, 'user_id', event.user_id, message=message_list.msg3, keyboard=keyboard)
                        elif response == "преподаватели":
                            send_message(vk_session, 'user_id', event.user_id, message=message_list.msg10, keyboard=keyboard)
                        elif response == "закрыть":
                            send_message(vk_session, 'user_id', event.user_id, message='Ok', keyboard=keyboard)
                        else:
                            send_message(vk_session, 'user_id', event.user_id, message=message_list.msg2, keyboard=keyboard)
            if (mailing_flag == 1) and (message_flag == 1):
                for num in range(len(permitted_user)):
                    send_message(vk_session, 'user_id', permitted_user[num], message=mailing_message)
                mailing_flag = 0
                message_flag = 0

            id_list = open("id_list.txt", 'w')
            id_list.write(str(len(permitted_user)) + "\n")
            for num in range(len(permitted_user)):
                id_list.write(str(permitted_user[num]) + "\n")
            id_list.close()
    except Exception as e:
        print('error', e)
