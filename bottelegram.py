import telebot
import random

#chave dev CHAVE_API = "5158551785:AAFITirBNUOAA2YFQGrrnDJFk2lAPriOuUM"
CHAVE_API = "5187133043:AAE0rYWXDGDDKdNjplGAchQ9abj7fw9GyIA"

bot = telebot.TeleBot(CHAVE_API)



@bot.message_handler(commands=["gas5"])
def responder(mensagem):

    id_cliente = mensagem.from_user.id + random.randint(0, 1000000)
    nome_cliente = mensagem.from_user.first_name
    is_bot = mensagem.from_user.is_bot

    bot.send_message(mensagem.chat.id, f'''
    Seu pedido foi encaminhado para a central!

    Detalhes do pedido:
        - Id do Pedido: {id_cliente}
        - Cliente: {nome_cliente}
        - Pedido: Botijão de Gás de 5kg
        - Quantidade: 1
        - Cliente é um BOT? {is_bot}
    ''')


@bot.message_handler(commands=["gas8"])
def responder(mensagem):

    id_cliente = mensagem.from_user.id + random.randint(0, 1000000)
    nome_cliente = mensagem.from_user.first_name
    is_bot = mensagem.from_user.is_bot

    bot.send_message(mensagem.chat.id, f'''
    Seu pedido foi encaminhado para a central!

    Detalhes do pedido:
        - Id do Pedido: {id_cliente}
        - Cliente: {nome_cliente}
        - Pedido: Botijão de Gás de 8kg
        - Quantidade: 1
        - Cliente é um BOT? {is_bot}
    ''')


@bot.message_handler(commands=["gas13"])
def responder(mensagem):

    id_cliente = mensagem.from_user.id + random.randint(0, 1000000)
    nome_cliente = mensagem.from_user.first_name
    is_bot = mensagem.from_user.is_bot

    bot.send_message(mensagem.chat.id, f'''
    Seu pedido foi encaminhado para a central!

    Detalhes do pedido:
        - Id do Pedido: {id_cliente}
        - Cliente: {nome_cliente}
        - Pedido: Botijão de Gás de 13kg
        - Quantidade: 1
        - Cliente é um BOT? {is_bot}
    ''')


@bot.message_handler(commands=["gas20"])
def responder(mensagem):

    id_cliente = mensagem.from_user.id + random.randint(0, 1000000)
    nome_cliente = mensagem.from_user.first_name
    is_bot = mensagem.from_user.is_bot

    bot.send_message(mensagem.chat.id, f'''
    Seu pedido foi encaminhado para a central!

    Detalhes do pedido:
        - Id do Pedido: {id_cliente}
        - Cliente: {nome_cliente}
        - Pedido: Botijão de Gás de 20kg
        - Quantidade: 1
        - Cliente é um BOT? {is_bot}
    ''')


@bot.message_handler(commands=["gas45"])
def responder(mensagem):

    id_cliente = mensagem.from_user.id + random.randint(0, 1000000)
    nome_cliente = mensagem.from_user.first_name
    is_bot = mensagem.from_user.is_bot

    bot.send_message(mensagem.chat.id, f'''
    Seu pedido foi encaminhado para a central!

    Detalhes do pedido:
        - Id do Pedido: {id_cliente}
        - Cliente: {nome_cliente}
        - Pedido: Botijão de Gás de 45kg
        - Quantidade: 1
        - Cliente é um BOT? {is_bot}
    ''')


@bot.message_handler(commands=["gas90"])
def responder(mensagem):

    id_cliente = mensagem.from_user.id + random.randint(0, 1000000)
    nome_cliente = mensagem.from_user.first_name
    is_bot = mensagem.from_user.is_bot

    bot.send_message(mensagem.chat.id, f'''
    Seu pedido foi encaminhado para a central!

    Detalhes do pedido:
        - Id do Pedido: {id_cliente}
        - Cliente: {nome_cliente}
        - Pedido: Botijão de Gás de 90kg
        - Quantidade: 1
        - Cliente é um BOT? {is_bot}
    ''')


@bot.message_handler(commands=["pedido"])
def responder(mensagem):
    
    bot.send_message(mensagem.chat.id, '''
    Escolha o produto:

        - /gas5 Botijão de 5Kg
        - /gas8 Botijão de 8Kg
        - /gas13 Botijão de 13Kg
        - /gas20 Botijão de 20Kg
        - /gas45 Botijão de 45Kg
        - /gas90 Botijão de 90kg

    ''')
           

@bot.message_handler(commands=["reclamacao"])
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
Linkedin: https://www.linkedin.com/company/revgas/about/
Twitter: https://twitter.com/revgas_br
Site: https://revgas.com/
''')


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    print(mensagem)
    nome_cliente = mensagem.from_user.first_name
    bot.send_message(mensagem.chat.id, f'''
Olá {nome_cliente}, seja bem vindo ao Atendimento da RevGás!
Escolha uma das opções para continuar(Clique no Item):
    - /pedido (Fazer um Pedido)
    - /reclamacao (Fazer Reclamação de Produto ou atentimento)
    - /endereco (Endereço da RevGás)
    - /redessociais (Instagram, Linkedin, Twitter, Site)
''')

bot.polling()