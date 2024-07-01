def send_email(message, recipient,*,sender = 'university.help@gmail.com'):
    a=0
    b=0
    c=0
    const_sender='university.help@gmail.com'
    wrong_sender='urban.info@gmail.com'
    list = ('@','.com','.ru','.net')
    for element in list:
        if element in recipient:
            a+=1
    for element in list:
        if element in sender:
            b+=1
    if a<2 or b<2:
        print ("Невозможно отправить письмо с адреса",sender,"на адрес",recipient)
    if recipient == sender:
        print ('Нельзя отправить письмо самому себе!')
    if sender == const_sender:
        print(message, sender, 'на адрес', recipient)
    if sender == wrong_sender:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender,'на адрес', recipient)


send_email('Письмо успешно отправлено с адреса', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')