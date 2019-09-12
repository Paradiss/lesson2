
aq_dict = {'Как дела?': "Хорошо!", "Что делаешь?": "Программирую","Что ты?": "Нечто", "й":"ц"}


def ask_user():
    question = ''
    dela = ''
    while question != aq_dict.get(question):
        question = input("Спроси что-нибудь.\n")
        print(aq_dict.get(question))
        print(question)
        if aq_dict.get(question) != None:
            dela = aq_dict[question]
            print(dela)

ask_user()