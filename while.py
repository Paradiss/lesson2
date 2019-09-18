
aq_dict = {'Как дела?': "Хорошо!", "Что делаешь?": "Программирую","Что ты?": "Нечто", "й":"ц"}

def ask_user():
    dela = ''
    while dela != 'хорошо':
        question = input("Спроси что-нибудь.\n")
        if question in aq_dict:
            print(aq_dict[question])
        dela = (input('Как дела?\n')).lower()

ask_user()
