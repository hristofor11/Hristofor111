import telebot
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token)

# Обработчик стартового сообщения
@bot.message_handler(commands=['start'])
def start_command(message):
    username = message.from_user.username
    
    # Проверяем, существует ли уже созданный покемон для пользователя
    if username not in Pokemon.pokemons.keys():
        # Создаем нового покемона для пользователя
        pokemon = Pokemon(username)
        
        # Отправляем сообщение с информацией о покемоне
        bot.send_message(message.chat.id, pokemon.info())
        
        # Отсылаем фотографию покемона
        photo_path = pokemon.show_img()
        # with open(photo_path, 'rb') as f:
        bot.send_photo(message.chat.id, photo_path)
            
    else:
        bot.reply_to(message, "Ты уже создал себе покемона.")

# Обработчик команды /info
@bot.message_handler(commands=['info'])
def info_command(message):
    username = message.from_user.username
    
    # Проверяем существование покемона для текущего пользователя
    if username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[username]
        bot.send_message(message.chat.id, pokemon.info())
    else:
        bot.reply_to(message, "Покемон ещё не создан. Используй команду /start.")

if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
