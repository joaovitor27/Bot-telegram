import telebot

CHAVE_API = "5187133043:AAE0rYWXDGDDKdNjplGAchQ9abj7fw9GyIA"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pedido"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "oi")


@bot.message_handler(commands=["reclamar"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Para fazer uma reclamação mande uma email para: falecom@revgas.com")


@bot.message_handler(commands=["endereco"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, '''
Av. Jóquei Clube, 299 - Jóquei, Teresina - PI, 64048-110
Localizado em: Edificio Euro Business
Maps: https://goo.gl/maps/oSYy4BTDn6ax6osv8
''')


@bot.message_handler(commands=["redessociais"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, '''
Instagram: https://www.instagram.com/revgas.br/
Linkdin: https://www.linkedin.com/company/revgas/about/
Twitter: https://twitter.com/revgas_br
Site: https://revgas.com/
    ''')


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, '''
Olá, seja bem vindo ao Atendimento da RevGás!
Escolha uma das opções para continuar(Clique no Item):
    - /pedido (Fazer um Pedido)
    - /reclamar (Fazer Reclamação de Produtos ou atentimento)
    - /endereco (Emdereço da Rev Gás)
    - /redessociais (intagram, linkdin, twitter, site)
''')

bot.polling()