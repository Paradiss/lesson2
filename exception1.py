 
aq_dict = {'Как дела?': "Хорошо!", "Что делаешь?": "Программирую","Что ты?": "Нечто", "й":"ц"}

def ask_user():
    dela = ''
    
    while dela != 'хорошо':
        try:
            question = input("Спроси что-нибудь.\n")
            if aq_dict.get(question) != None:
                dela = aq_dict[question]
                print(dela)
            dela = (input('Как дела?\n')).lower()
        except(KeyboardInterrupt): 
            print("Пока")
            break        
ask_user()