import telebot
from telebot import types

bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("English language")
    btn2 = types.KeyboardButton("Русский язык")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "👋 Choose language/Выберете язык", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "English language":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("burrito🌯")
        btn2 = types.KeyboardButton("sandwiches🥪")
        btn3 = types.KeyboardButton("breakfast☀")
        btn4 = types.KeyboardButton("main course🍽")
        btn5 = types.KeyboardButton("salad🥗")
        btn6 = types.KeyboardButton("soups🍲")
        btn7 = types.KeyboardButton("desserts🍩")
        btn8 = types.KeyboardButton("snacks🍿")
        btn9 = types.KeyboardButton("your suggestion")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)
    elif message.text == "burrito🌯":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Chicken burrito🌯🍗")
        btn2 = types.KeyboardButton("Beef burrito🌯🥩")
        btn3 = types.KeyboardButton("Fish burrito🌯🐟")
        btn4 = types.KeyboardButton("Tofu burrito🌯🧀")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)
    elif message.text == "sandwiches🥪":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Chicken sandwich🥪🍗")
        btn2 = types.KeyboardButton("Beef sandwich🥪🥩")
        btn3 = types.KeyboardButton("Fish sandwich🥪🐟")
        btn4 = types.KeyboardButton("Mushroom sandwich🥪🍄‍🟫")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)
    elif message.text == "breakfast☀":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Sweat oat breakfast🥣")
        btn2 = types.KeyboardButton("Smoothie breakfast🥤")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)
    elif message.text == "main course🍽":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Rice and chicken🍚🍗")
        btn2 = types.KeyboardButton("Rice and beef🍚🥩")
        btn3 = types.KeyboardButton("Rice and fish🍚🐟")
        btn4 = types.KeyboardButton("Rice and tofu🍚🧀")
        btn5 = types.KeyboardButton("Alfredo pasta🍗🧀🍝")
        btn6 = types.KeyboardButton("Bolonjeze pasta🥫🍝")
        btn7 = types.KeyboardButton("Cheese pasta🧀🍝")
        btn8 = types.KeyboardButton("Mushroom pasta🍄‍🟫🍝")
        btn9 = types.KeyboardButton("Mush potato with chicken🥔🍗")
        btn10 = types.KeyboardButton("Mush potato with beef🥔🥩")
        btn11 = types.KeyboardButton("Mush potato with fish🥔🐟")
        btn12 = types.KeyboardButton("Mush potato with tofu🥔🧀")
        btn13 = types.KeyboardButton("Lasagne🍝")
        btn14 = types.KeyboardButton("Ultimate stew🥘")
        btn15 = types.KeyboardButton("Curry🍛")
        btn16 = types.KeyboardButton("Ultimate bowl🥙")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)
    elif message.text == "salad🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Green salad🥗")
        btn2 = types.KeyboardButton("Italian salad🇮🇹🥗")
        btn3 = types.KeyboardButton("Summer vinaigrette salad🍀🥗")
        btn4 = types.KeyboardButton("Apple salad🍎🥗")
        btn5 = types.KeyboardButton("Broccoli salad🥦🥗")
        btn6 = types.KeyboardButton("Mexican salad🇲🇽🥗")
        btn7 = types.KeyboardButton("Mediterranean salad🫑🥗")
        btn8 = types.KeyboardButton("Warm salad🌤🥗")
        btn9 = types.KeyboardButton("Autumn salad🍁🥗")
        btn10 = types.KeyboardButton("Fish salad🐟🥗")
        btn11 = types.KeyboardButton("English salad🏴󠁧󠁢󠁥󠁮󠁧󠁿🥗")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)
    elif message.text == "soups🍲":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Creamy chicken soup🍜🍗")
        btn2 = types.KeyboardButton("Creamy fish soup🍜🐟")
        btn3 = types.KeyboardButton("Creamy mushroom soup🍜🍄‍🟫")
        btn4 = types.KeyboardButton("Cream soup🍜")
        btn5 = types.KeyboardButton("Ultimate ramen🍜")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)
    elif message.text == "desserts🍩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Iced yogurt and berry🍧")
        btn2 = types.KeyboardButton("Fruit pie🥧")
        btn3 = types.KeyboardButton("Sorbet🍨")
        btn4 = types.KeyboardButton("Sweet bread🍞")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)
    elif message.text == "snacks🍿":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Fritters🧇")
        btn2 = types.KeyboardButton("Flatbread🫓")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)
    elif message.text == "your suggestion":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'If you want to recommend a new recipe, give advice on how the bot works, support the project or contact the creator, you can do this by following the' + ' [link.](https://t.me/o2mooro)', parse_mode='Markdown')
        bot.send_message(message.from_user.id, "Go back to the main menu", reply_markup=markup)

    elif message.text == "Chicken burrito🌯🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Chicken burrito🌯🍗
♨️suitable for harvesting in the freezer 
Ingredients:
 • Chicken meat
 • Lavash
 • Pickles
 • Cabbage
 • Hard cheese 
 • Pickled beans
 • Onion 
 • Corn
 • Seasonings: curry, paprika, garlic 
Preparation:
 1. Fry the chicken meat in a frying pan, divide by fibers. 
 2. Add the beans, finely chopped onion, corn and seasonings to the pan. Cook over low heat. Mash with a fork to the consistency of mashed potatoes. 
 3. Put on the pita bread, add the remaining ingredients. Roll up. 
To defrost: preheat in a frying pan / microwave."""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Beef burrito🌯🥩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Beef burrito🌯🥩
♨️suitable for harvesting in the freezer 
Ingredients:
 • Beef/ ground beef
 • Lavash
 • Bell pepper 
 • Carrots in Korean
 • Hard cheese 
 • Pickled beans
 • Onion
 • Corn
 • Seasonings: curry, paprika, garlic 
Preparation:
 1. Fry the beef in a frying pan, divide by fibers / minced meat. 
 2. Add the beans, finely chopped onion, corn and seasonings to the pan. Cook over low heat. Mash with a fork to the consistency of mashed potatoes. 
 3. Put on the pita bread, add the remaining ingredients. Roll up. 
To defrost: preheat in a frying pan / microwave."""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Fish burrito🌯🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Fish burrito🌯🐟
♨️suitable for harvesting in the freezer 
Ingredients:
 • Pollock/cod/walleye/mackerel/pink salmon
 • Lavash
 • Avocado
 • Polka dots
 • Hard cheese 
 • Pickled beans
 • Onion
 • Corn
 • Seasonings: curry, paprika, garlic 
Preparation:
 1. Cook the fish in a frying pan / steamed. 
 2. Add the beans, finely chopped onion, corn and seasonings to the pan. Cook over low heat. Mash with a fork to the consistency of mashed potatoes. 
 3. Put on the pita bread, add the remaining ingredients. Roll up. 
To defrost: preheat in a frying pan / microwave."""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Tofu burrito🌯🧀":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Tofu burrito🌯🧀
♨️suitable for harvesting in the freezer 
Ingredients:
 • Tofu
 • Soy sauce
 • Pita bread
 • Pickles
 • Bell pepper
 • Hard cheese 
 • Pickled beans
 • Onion
 • Corn
 • Seasonings: curry, paprika, garlic 
Preparation:
 1. Fry finely chopped tofu with soy sauce and spices in a frying pan
 2. Add the beans, finely chopped onion and corn to the pan.  Cook over low heat. Mash with a fork to the consistency of mashed potatoes. 
 3. Put on the pita bread, add the remaining ingredients. Roll up. 
To defrost: preheat in a frying pan / microwave."""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Chicken sandwich🥪🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Chicken sandwich🥪🍗
♨️suitable for harvesting in the freezer 
Included:
 • Toast bread
 • Chicken meat
 • Avocado
 • Sour cream/mayonnaise/Greek yogurt 
 • Greens: onion, parsley, dill
Preparation:
 1. Fry the chicken meat in a frying pan, divide by fibers. 
 2. Add the remaining ingredients. Mash with a fork to the consistency of mashed potatoes. 
 3. Put a thick layer on the bread. 
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Beef sandwich🥪🥩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Beef sandwich🥪🥩
♨️suitable for harvesting in the freezer 
Included:
• Toast bread
 • Beef/ground beef
 • Pickles
 • Sour cream/mayonnaise/Greek yogurt 
 • Greens: onion, parsley, dill
Preparation:
 1. Fry the beef / minced meat in a frying pan. 
 2. Add the remaining ingredients. Mash with a fork to the consistency of mashed potatoes. 
 3. Put a thick layer on the bread. 
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Fish sandwich🥪🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Fish sandwich🥪🐟
♨️suitable for harvesting in the freezer 
Included:
 • Toast bread
 •Pollock/cod/walleye/mackerel/pink salmon/haddock/heck
 • Onion/celery/seaweed
 • Sour cream/mayonnaise/Greek yogurt 
 • Greens: onion, parsley, dill
Preparation:
 1. Cook the fish in a frying pan / steamed. 
 2. Add the remaining ingredients. Mash with a fork to the consistency of mashed potatoes. 
 3. Put a thick layer on the bread. 
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Mushroom sandwich🥪🍄‍🟫":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Mushroom sandwich🥪🍄‍🟫
♨️suitable for preparation in the freezer 
Included:
 • Toast bread
 • Champignons/porcini mushrooms
 • Cabbage 
 • Sour cream/mayonnaise/Greek yogurt 
 • Greens: onion, parsley, dill
Preparation:
 1. Cook mushrooms in a frying pan. 
 2. Add the remaining ingredients. Mash with a fork to the consistency of mashed potatoes. 
 3. Put a thick layer on the bread. 
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Sweat oat breakfast🥣":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Sweet breakfast🥣
♨️suitable for harvesting in the freezer 
Ingredients:
 • Oatmeal that does not require cooking/granola/chia seeds 
 • Yogurt
 • Berries/fruits
Preparation:
1. Mix all the ingredients. Leave to infuse for 10 minutes
To freeze: lay out the ingredients in layers, leaving the yogurt at the bottom. 
To defrost: leave in the refrigerator for an hour, stir.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Smoothie breakfast🥤":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Smoothies🥤
♨️suitable for harvesting in the freezer 
Ingredients:
 • Fruits/vegetables/berries
 • Yogurt/milk/juice
Preparation:
 1. Crush fruits / vegetables / berries with a fork / whisk with a blender. 
 2. Add yogurt/milk/juice. 
For defrosting: get it in an hour.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    
    elif message.text == "Rice and chicken🍚🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Rice and chicken🍚🍗
♨️suitable for harvesting in the freezer 
Ingredients:
 • Rice
 • Chicken meat
 • Broccoli/cauliflower
 • Butter/avocado oil 
 • Seasonings: basil, oregano, dill
Preparation:
 1. Cook the rice. 
 2. Chop the chicken meat, put it out in a frying pan in oil with spices. Remove from the pan. 
 3. Put out the vegetables and rice in the same pan. Add the meat. 
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Rice and beef🍚🥩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Rice and beef🍚🥩
♨️suitable for harvesting in the freezer 
Ingredients:
 • Rice
 • Beef
 • Carrots/bell peppers
 • Butter/avocado oil 
 • Seasonings: black pepper, parsley, rosemary
Preparation:
 1. Cook the rice. 
 2. Chop the beef, put it out in a frying pan in oil with spices.
 3. Mix meat, vegetables and rice.  
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Rice and fish🍚🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Rice and fish🍚🐟
♨️suitable for harvesting in the freezer 
Ingredients:
 • Rice
 • Pollock/cod/walleye/mackerel/pink salmon
 • Tomatoes/green beans
 • Butter/avocado oil 
 • Seasonings: lemon juice, basil, oregano
Preparation:
 1. Cook the rice. 
 2. Chop the fish, put it out in a frying pan in oil with spices and vegetables.
 3. Mix meat, vegetables and rice.  
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Rice and tofu🍚🧀":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Rice and tofu 🍚🧀
♨️suitable for harvesting in the freezer 
Ingredients:
 • Rice
 • Tofu
 • Corn/carrots in Korean
 • Butter/avocado oil 
 • Seasonings: soy sauce, sugar, paprika, red pepper
Preparation:
 1. Cook the rice. 
 2. Chop the fried tofu, put it out in a frying pan in oil with spices and vegetables.
 3. Mix meat, vegetables and rice.  
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Alfredo pasta🍗🧀🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Alfredo pasta🍗🧀🍝
♨️suitable for harvesting in the freezer 
Ingredients:
 • Pasta
 • Chicken meat/fish/tofu
 • Sour cream/cream 30%
 • Hard cheese 
 • Butter/avocado oil
 • Seasoning: garlic, parsley
Preparation:
 1. Boil the pasta until aldente. 
 2. Stew meat / fish / tofu in oil with sour cream / cream and seasoning. Add the water from under the cooking pasta. 
 3. Add the pasta to the sauce and simmer for another 3 minutes. Sprinkle with hard cheese. 
To freeze: put the sauce on the pasta aldente. 
To defrost: heat in a frying pan / microwave and mix.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Bolonjeze pasta🥫🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Pasta bolognese🥫🍝
♨️suitable for harvesting in the freezer 
Ingredients:
 • Pasta
 • Any minced meat
 • Tomato paste
 • Onion
 • Butter/avocado oil
 • Seasoning: paprika, black pepper
Preparation:
 1. Boil the pasta until aldente. 
 2. Put out the minced meat with finely chopped onion and tomato paste in oil. Add the water from under the cooking pasta. 
 3. Add the pasta to the sauce and simmer for another 3 minutes. 
To freeze: put the sauce on the pasta aldente. 
To defrost: heat in a frying pan / microwave and mix.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Cheese pasta🧀🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Cheese pasta🧀🍝
♨️suitable for harvesting in the freezer 
Ingredients:
 • Pasta
 • Sour cream/cream 30%
 • Cheese: mozzarella, tilsiter
 • Seasoning: paprika, garlic
Preparation:
 1. Boil the pasta until aldente. 
 2. Add cheese and seasonings to the sour cream / cream. Add the pasta and cook for another 3 minutes. 
To freeze: put the sauce on the pasta aldente. 
To defrost: heat in a frying pan / microwave and mix.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Mushroom pasta🍄‍🟫🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Mushroom paste🍄‍🟫🍝
♨️suitable for harvesting in the freezer 
Ingredients:
 • Pasta
 • Chicken meat/tofu
 • Champignons/porcini mushrooms
 • Sour cream/cream 30%
 • Hard cheese
 • Butter/avocado oil
 • Seasoning: garlic, basil
Preparation:
 1. Boil the pasta until it is completely dry.
 2. Put out meat / tofu with mushrooms, sour cream / cream and seasoning
 3. Add the pasta to the sauce and simmer for another 3 minutes. Sprinkle with grated cheese. 
 4. For freezing: put the sauce on the pasta and aldentee. 
 5. For defrosting: heat in a frying pan / microwave and mix.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Green salad🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Green salad🥗
Ingredients:
 • Tomatoes
 • Cabbage
 • Corn
 • Onion 
 • Olive/sunflower oil
 • Seasoning: garlic, paprika, rosemary
Preparation:
 1. Mix the oil and seasoning for dressing. 
 2. Mix the vegetables with the dressing
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Italian salad🇮🇹🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Italian salad🇮🇹🥗
Ingredients:
 • Spinach/salad
 • Olives
 • Brie cheese/fried tofu
 • Almonds
 • Honey
 • Olive/sunflower oil
 • Seasoning: oregano, rosemary 
Preparation:
 1. For dressing, mix the oil, seasoning and honey. 
 2. Mix the dressing and the rest of the ingredients.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Summer vinaigrette salad🍀🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Summer vinaigrette🍀🥗
Ingredients:
 • Adyghe cheese
 • Cabbage
 • Radish
 • * Roasted chickpeas/nuts
 • Lemon
• Sour cream/Greek yogurt
Preparation:
1. Mix all the ingredients. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Apple salad🍎🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Apple salad🍎🥗
Ingredients:
 • Apples
 • Onion
 • Hazelnut
 • Parsley
Preparation:
1. Mix all the ingredients. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Broccoli salad🥦🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Broccoli salad🥦🥗
Ingredients:
 • Boiled broccoli 
 • Boiled carrots
 • Almonds
 • Onion
 • Avocado
Preparation:
1. Mix all the ingredients. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Mexican salad🇲🇽🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Mexican salad🇲🇽🥗
Ingredients:
 • Corn
 • Adyghe cheese
 • Boiled egg
 • Green onions
 • Paprika
 • Parsley
 • Lemon juice
Preparation:
1. Mix all the ingredients.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Mediterranean salad🫑🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Mediterranean salad🫑🥗
Ingredients:
 • Cucumber
 • Salted tomatoes
 • Bell pepper
 • Adyghe cheese
 • Olive/sunflower oil
 • Seasoning: rosemary, oregano, basil
Preparation:
1. Mix the oil and seasoning for dressing. 
 2. Mix all the ingredients and the dressing.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Warm salad🌤🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Warm salad🌤️🥗
♨️suitable for harvesting in the freezer 
Ingredients:
 • Boiled carrots
 • Boiled chicken meat
 • Boiled broccoli 
 • Tomatoes
Preparation:
1. Mix all the ingredients. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Autumn salad🍁🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Autumn salad🍁🥗
♨️suitable for harvesting in the freezer 
Included:
 • Boiled pumpkin
 • Boiled carrots
 • Any nuts
 • Avocado
 • Onion
Preparation:
1. Mix all the ingredients. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Fish salad🐟🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Fish salad🐟🥗
♨️suitable for harvesting in the freezer 
In the composition:
 • Avocado
 • Cooked pollock/cod/walleye/mackerel/pink salmon
 • Onion
 • Adyghe cheese
Preparation:
 1. Mix all the ingredients. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "English salad🏴󠁧󠁢󠁥󠁮󠁧󠁿🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """English salad 🏴󠁧󠁢󠁥󠁮󠁧󠁿🥗
♨️suitable for preparation in the freezer 
Ingredients:
 • Beans in tomato sauce * Fried tofu
 • Onion
Preparation:
 1. Mix all the ingredients. Serve with bread."""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Ultimate bowl🥙":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Ultimate Bowl🥙
♨️suitable for harvesting in the freezer 
Ingredients:
 • Boiled carrots
 • Mashed potatoes
 • Boiled broccoli 
 • Boiled cauliflower
 • Any nuts
 • Hummus
 • Avocado
 • Bell pepper 
 • Fried zucchini
 • Olives/olives
 • Chicken meat/beef/fish/tofu
 • Fried string beans 
 • Corn
 • Canned beans
 • Peas
Preparation:
 1. Mix some of the ingredients. 
To defrost: heat in a frying pan / microwave and mix. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Mush potato with chicken🥔🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Mashed potatoes with chicken 🥔🍗
♨️suitable for harvesting in the freezer 
Ingredients:
 • Potatoes
 • Butter/avocado
 • Chicken meat
 • Carrots
 • Tomato paste
 • Seasoning: curry, paprika
Preparation:
 1. Boil potatoes, mash, add oil. 
 2. Fry grated carrots in oil, add tomato paste and seasoning. Add the chicken meat. 
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Mush potato with beef🥔🥩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Mashed potatoes with beef 🥔🥩
♨️suitable for harvesting in the freezer 
Ingredients:
 • Potatoes
 • Butter/avocado
 • Beef
 • Carrots
 • Marinade: soy sauce, garlic, tomato paste
 • Seasoning: curry, green onion 
Preparation:
 1. Marinate the sliced beef in advance.  
 2. Boil the potatoes, mash, add oil. 
 3. Fry grated carrots in oil, add seasoning and beef. 
To defrost: preheat in a frying pan / microwave. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Mush potato with fish🥔🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Mashed potatoes with fish 🥔🐟
♨️suitable for harvesting in the freezer 
Ingredients:
 • Potatoes
 • Butter/avocado
 • Canned tuna 
 • Carrots
 • Tomato paste
 • Seasoning: curry, paprika
Preparation:
 1. Boil potatoes, mash, add butter. 
 2. Fry grated carrots in oil, add tomato paste and seasoning. Add tuna. 
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Mush potato with tofu🥔🧀":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Mashed potatoes with tofu 🥔🧀
♨️suitable for harvesting in the freezer 
Ingredients:
 • Potatoes
 • Butter/avocado
 • Tofu
 • Carrots
 • Marinade: soy sauce, garlic, tomato paste
 • Seasoning: curry, green onion 
Preparation:
 1. Marinate the chopped tofu in advance. Fry it. 
 2. Boil the potatoes, mash, add oil. 
 3. Fry grated carrots in oil, add seasoning and tofu. 
To defrost: preheat in a frying pan / microwave. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Lasagne🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Lasagna 🍝
♨️suitable for harvesting in the freezer 
Ingredients:
 • Minced beef
 • Tomato sauce
 • Hard cheese
 • Onion
 • Lasagna sheets 
 • Seasoning: black pepper, paprika
Preparation:
 1. Preheat the oven to 180 degrees. 
 2. Fry the minced meat with seasoning, finely chopped onion, tomato sauce and water. 
 3. Spread in layers - minced meat, cheese, leaf. At the end, put the minced meat and sprinkle liberally with cheese. 
 4. Bake in the oven. 
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Ultimate stew🥘":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Stew 🥘
♨️suitable for harvesting in the freezer 
Ingredients:
 • Potatoes
 • Carrots
 • Eggplant
 • Zucchini
 • Onion
 • Peas
 • Beans
 • String beans
 • Chicken meat/beef/fish
 • Champignons/porcini mushrooms 
 • Tomato paste
 • Garlic
 • Oregano
Preparation:
 1. Mix some of the ingredients and simmer in a frying pan. Add tomato paste, water, garlic and oregano. 
To defrost: preheat in a frying pan / microwave. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Curry🍛":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Curry 🍛
♨️suitable for harvesting in the freezer 
Ingredients:
 • Boiled rice
 • Onion
 • Chicken meat
 • Potatoes
 • Carrots
 • Olive/sunflower oil
 • Tomato paste
 • Seasoning: curry, chili, garlic
Preparation:
 1. Fry vegetables (except onions) with meat, adding water. Simmer over low heat. 
 2. Prepare the sauce separately: tomato paste, seasoning, oil, finely chopped onion. 
 3. Add the sauce to the vegetables. Serve with rice. 
To defrost: preheat in a frying pan / microwave.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Creamy chicken soup🍜🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Creamy chicken soup 🍜🍗
♨️Suitable for harvesting in the freezer 
Ingredients:
 • Chicken meat
 • Carrots
 • Sour cream/cream 30%
 • Potatoes
 • Seasoning: garlic, paprika
Preparation:
 1. Put out the chicken and carrots in a frying pan. 
 2. Boil the potatoes in a saucepan. Add chicken, carrots, seasoning and sour cream/cream.  
For freezing: put chicken, carrots and seasoning on boiled potatoes.  
To defrost: Pour water and add sour cream / cream, bring to a boil. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Creamy fish soup🍜🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Creamy fish soup 🍜🐟
♨️Suitable for harvesting in the freezer 
Ingredients:
 • Pollock/cod/walleye/mackerel/pink salmon/haddock/heck
 • Carrots
 • Sour cream/cream 30%
 • Potatoes
 • Seasoning: garlic, paprika
Preparation:
 1. Put out the fish and carrots in a frying pan. 
 2. Boil the potatoes in a saucepan. Add fish, carrots, seasoning and sour cream/ cream.  
For freezing: put fish, carrots and seasoning on boiled potatoes.  
To defrost: Pour water and add sour cream / cream, bring to a boil. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Creamy mushroom soup🍜🍄‍🟫":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Creamy mushroom soup🍜🍄‍🟫
♨️Suitable for harvesting in the freezer 
Ingredients:
 • Champignons/porcini mushrooms
 • Carrots
 • Sour cream/cream 30%
 • Potatoes
 • Seasoning: garlic, paprika
Preparation:
 1. Put out the mushrooms and carrots in a frying pan. 
 2. Boil the potatoes in a saucepan. Add mushrooms, carrots, seasoning and sour cream/ cream.  
For freezing: put mushrooms, carrots and seasoning on boiled potatoes.  
To defrost: Pour water and add sour cream / cream, bring to a boil.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Cream soup🍜":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Cream soup 🍜
♨️Suitable for harvesting in the freezer 
Ingredients:
 • Main ingredient: chicken meat/fish/mushrooms/pumpkin/tomatoes/peas and broccoli/onions and white wine
 • Carrots
 • Sour cream/cream 30%
 • Potatoes
 • Seasoning: garlic, paprika
Preparation:
 1. Put out the main ingredient with carrots in a frying pan. 
 2. Boil the potatoes in a saucepan. Add the main ingredient, carrots, seasoning and sour cream/cream.  
 3. Beat with a blender. 
For defrosting: Boil. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Ultimate ramen🍜":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Ultimate ramen🍜
♨️Suitable for harvesting in the freezer 
Ingredients:
 • Chicken meat/beef/fish/tofu
 • String beans/mushrooms/corn/peas/bell peppers
 • Vermicelli 
 • Seasoning: garlic
Preparation:
 1. Put out meat / fish / tofu with vegetables with water, cook over low heat. 
 2. Add the noodles. 
For freezing: without adding vermicelli, freeze the broth. 
To defrost: Boil the broth, add the noodles. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Iced yogurt and berry🍧":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Frozen yogurt with berries🍧
♨️Suitable for harvesting in the freezer 
Ingredients:
 • Yogurt
 • Any berries
Preparation:
 1. Mix yogurt with berries.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Fruit pie🥧":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Fruit pie🥧
♨️Suitable for harvesting in the freezer 
In the composition:
 • Puff pastry
 • Any fruit
 • Sugar
Preparation:
 1. Preheat the oven to 180 degrees. 
 2. Put the fruits on the dough, sprinkle with sugar. Cover with dough. 
 3. Bake in the oven. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Sorbet🍨":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Sherbet 🍨
♨️Suitable for harvesting in the freezer 
Ingredients:
 • Any fruits/berries
 • Sugar syrup
Preparation:
 1. Beat fruits / berries in a blender, add sugar syrup. 
 2. Freeze in the freezer, stirring every hour, for 10-12 hours. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Sweet bread🍞":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Sweet bread 🍞
♨️Suitable for harvesting in the freezer 
Ingredients:
 • Banana/boiled pumpkin/boiled carrot/currant/chocolate
 • Eggs
 • Flour
 • Sugar
 • Butter/avocado
 • Baking powder
 • Seasoning: vanilla, walnut, cinnamon
Preparation:
 1. Preheat the oven to 180 degrees. 
 2. Mix banana / pumpkin / carrot / currant / chocolate, eggs and melted butter. Add dry flour, sugar, baking powder, seasoning. 
 3. Bake in the oven. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Fritters🧇":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Fritters🧇
♨️Suitable for harvesting in the freezer 
Ingredients:
 • Potatoes/squash
 • Eggs
 • Flour
Preparation:
 1. Grate the potatoes / zucchini, squeeze out the moisture. Mix with other ingredients. Bake in a frying pan.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Flatbread🫓":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Return to the main menu")
        markup.add(btn1)
        recipie = """Flatbread🫓
♨️suitable for harvesting in the freezer 
Ingredients:
 • Lavash
 • Cheese
 • Any vegetables/ready minced meat/ready meat/fish/sausages
Preparation:
 1. Cut a strip of pita bread (considering that one strip is about 10x25 cm)
 2. Put any filling on the edge in the shape of a triangle and sprinkle with cheese. Wrap the triangle. 
 3. Fry in a frying pan/toaster.
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Return to the main menu":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("burrito🌯")
        btn2 = types.KeyboardButton("sandwiches🥪")
        btn3 = types.KeyboardButton("breakfast☀")
        btn4 = types.KeyboardButton("main course🍽")
        btn5 = types.KeyboardButton("salad🥗")
        btn6 = types.KeyboardButton("soups🍲")
        btn7 = types.KeyboardButton("desserts🍩")
        btn8 = types.KeyboardButton("snacks🍿")
        btn9 = types.KeyboardButton("your suggestion")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "Choose a dish", reply_markup=markup)


    if message.text == "Русский язык":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("буррито🌯")
        btn2 = types.KeyboardButton("сэндвичи🥪")
        btn3 = types.KeyboardButton("завтрак☀")
        btn4 = types.KeyboardButton("основные блюда🍽")
        btn5 = types.KeyboardButton("салаты🥗")
        btn6 = types.KeyboardButton("супы🍲")
        btn7 = types.KeyboardButton("дессерты🍩")
        btn8 = types.KeyboardButton("перекусы🍿")
        btn9 = types.KeyboardButton("ваши предложения")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)
    elif message.text == "буррито🌯":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Куриное буррито🌯🍗")
        btn2 = types.KeyboardButton("Говяжье буррито🌯🥩")
        btn3 = types.KeyboardButton("Рыбное буррито🌯🐟")
        btn4 = types.KeyboardButton("Тофу буррито🌯🧀")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)
    elif message.text == "сэндвичи🥪":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Куриный сэндвич🥪🍗")
        btn2 = types.KeyboardButton("Говяжий сэндвич🥪🥩")
        btn3 = types.KeyboardButton("Рыбный сэндвич🥪🐟")
        btn4 = types.KeyboardButton("‍Грибной сэндвич🥪🍄‍🟫")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)
    elif message.text == "завтрак☀":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сладкий завтрак🥣")
        btn2 = types.KeyboardButton("Смузи🥤")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)
    elif message.text == "основные блюда🍽":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Рис и курица🍚🍗")
        btn2 = types.KeyboardButton("Рис и говядина🍚🥩")
        btn3 = types.KeyboardButton("Рис и рыба🍚🐟")
        btn4 = types.KeyboardButton("Рис и тофу🍚🧀")
        btn5 = types.KeyboardButton("Паста альфредо🍗🧀🍝")
        btn6 = types.KeyboardButton("Паста болоньезе🥫🍝")
        btn7 = types.KeyboardButton("Паста сырная🧀🍝")
        btn8 = types.KeyboardButton("Паста грибная🍄‍🟫🍝")
        btn9 = types.KeyboardButton("Пюре с курицей🥔🍗")
        btn10 = types.KeyboardButton("Пюре с говядиной🥔🥩")
        btn11 = types.KeyboardButton("Пюре с рыбой🥔🐟")
        btn12 = types.KeyboardButton("Пюре с тофу🥔🧀")
        btn13 = types.KeyboardButton("Лазанья🍝")
        btn14 = types.KeyboardButton("Рагу🥘")
        btn15 = types.KeyboardButton("Карри🍛")
        btn16 = types.KeyboardButton("Ультимейт Боул🥙")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)
    elif message.text == "салаты🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Зеленый салат🥗")
        btn2 = types.KeyboardButton("Итальянский салат🇮🇹🥗")
        btn3 = types.KeyboardButton("Летний винегрет🍀🥗")
        btn4 = types.KeyboardButton("Яблочный салат🍎🥗")
        btn5 = types.KeyboardButton("Салат брокколи🥦🥗")
        btn6 = types.KeyboardButton("Мексиканский салат🇲🇽🥗")
        btn7 = types.KeyboardButton("Средиземноморский салат🫑🥗")
        btn8 = types.KeyboardButton("Теплый салат🌤🥗")
        btn9 = types.KeyboardButton("Осенний салат🍁🥗")
        btn10 = types.KeyboardButton("Рыбный салат🐟🥗")
        btn11 = types.KeyboardButton("Английский салат🏴󠁧󠁢󠁥󠁮󠁧󠁿🥗")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)
    elif message.text == "супы🍲":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сливочный куриный суп🍜🍗")
        btn2 = types.KeyboardButton("Сливочный рыбный суп🍜🐟")
        btn3 = types.KeyboardButton("Сливочный грибной суп🍜🍄‍🟫")
        btn4 = types.KeyboardButton("Крем суп🍜")
        btn5 = types.KeyboardButton("Абсолютный рамен🍜")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)
    elif message.text == "дессерты🍩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Замороженный йогурт с ягодами🍧")
        btn2 = types.KeyboardButton("Фруктовый пирог🥧")
        btn3 = types.KeyboardButton("Щербет🍨")
        btn4 = types.KeyboardButton("Сладкий хлеб🍞")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)
    elif message.text == "перекусы🍿":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оладьи🧇")
        btn2 = types.KeyboardButton("Лепешка🫓")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)
    elif message.text == "ваши предложения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Если хотите посоветовать новый рецепт, дать совет по работе бота, поддержать проект или связаться с создателем, это можно сделать по' + ' [ссылке.](https://t.me/o2mooro)', parse_mode='Markdown')
        bot.send_message(message.from_user.id, "Вернитесь в главное меню", reply_markup=markup)

    elif message.text == "Куриное буррито🌯🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Куриное буррито🌯🍗
♨️Подходит для заготовки в морозильнике 
В составе:
 • Куриное мясо
 • Лаваш
 • Соленые огурцы
 • Капуста
 • Сыр твердый 
 • Фасоль маринованная
 • Лук 
 • Кукуруза
 • Приправы: карри, паприка, чеснок 
Приготовление:
 1. На сковороде пожарить куриное мясо, разделить по волокнам. 
 2. В сковороду добавить фасоль, мелко нарезанный лук, кукурузу и приправы. Готовить на медленном огне. Размять вилкой до консистенции пюре. 
 3. Выложить на лаваш, добавить остальные ингредиенты. Свернуть. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Говяжье буррито🌯🥩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Говяжье буррито🌯🥩
♨️Подходит для заготовки в морозильнике 
В составе:
 • Говядина/ говяжий фарш
 • Лаваш
 • Болгарский перец 
 • Морковь по-корейски
 • Сыр твердый 
 • Фасоль маринованная
 • Лук
 • Кукуруза
 • Приправы: карри, паприка, чеснок 
Приготовление:
 1. На сковороде пожарить говядину, разделить по волокнам/фарш. 
 2. В сковороду добавить фасоль, мелко нарезанный лук, кукурузу и приправы. Готовить на медленном огне. Размять вилкой до консистенции пюре. 
 3. Выложить на лаваш, добавить остальные ингредиенты. Свернуть. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Рыбное буррито🌯🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Рыбное буррито🌯🐟
♨️Подходит для заготовки в морозильнике 
В составе:
 • Минтай/треска/судак/скумбрия/горбуша
 • Лаваш
 • Авокадо
 • Горошек
 • Сыр твердый 
 • Фасоль маринованная
 • Лук
 • Кукуруза
 • Приправы: карри, паприка, чеснок 
Приготовление:
 1. На сковороде/на пару приготовить рыбу. 
 2. В сковороду добавить фасоль, мелко нарезанный лук, кукурузу и приправы. Готовить на медленном огне. Размять вилкой до консистенции пюре. 
 3. Выложить на лаваш, добавить остальные ингредиенты. Свернуть. 
Для разморозки: разогреть на сковороде / в микроволновке.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Тофу буррито🌯🧀":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Тофу буррито🌯🧀
♨️Подходит для заготовки в морозильнике 
В составе:
 • Тофу
 • Соевый соус 
 • Лаваш
 • Соленые огурцы
 • Болгарский перец
 • Сыр твердый 
 • Фасоль маринованная
 • Лук
 • Кукуруза
 • Приправы: карри, паприка, чеснок 
Приготовление:
 1. На сковороде пожарить мелко нарезанный тофу с соевым соусом и специями
 2. В сковороду добавить фасоль, мелко нарезанный лук и кукурузу.  Готовить на медленном огне. Размять вилкой до консистенции пюре. 
 3. Выложить на лаваш, добавить остальные ингредиенты. Свернуть. 
Для разморозки: разогреть на сковороде / в микроволновке.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Куриный сэндвич🥪🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Куриный сэндвич🥪🍗
♨️Подходит для заготовки в морозильнике 
В составе:
 • Хлеб тостовый
 • Куриное мясо
 • Авокадо
 • Сметана/майонез/греческий йогурт 
 • Зелень: лук, петрушка, укроп
Приготовление:
 1. На сковороде пожарить куриное мясо, разделить по волокнам. 
 2. Добавить остальные ингредиенты. Размять вилкой до консистенции пюре. 
 3. Выложить на хлеб толстым слоем. 
Для разморозки: разогреть на сковороде / в микроволновке.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Говяжий сэндвич🥪🥩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Говяжий сэндвич🥪🥩
♨️Подходит для заготовки в морозильнике 
В составе:
 • Хлеб тостовый
 • Говядина/говяжий фарш
 • Соленые огурцы
 • Сметана/майонез/греческий йогурт 
 • Зелень: лук, петрушка, укроп
Приготовление:
 1. На сковороде пожарить говядину/фарш. 
 2. Добавить остальные ингредиенты. Размять вилкой до консистенции пюре. 
 3. Выложить на хлеб толстым слоем. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Рыбный сэндвич🥪🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Рыбный сэндвич🥪🐟
♨️Подходит для заготовки в морозильнике 
В составе:
 • Хлеб тостовый
•Минтай/треска/судак/скумбрия/горбуша/пикша/хек
 • Лук репчатый/сельдерей/водоросли
 • Сметана/майонез/греческий йогурт 
 • Зелень: лук, петрушка, укроп
Приготовление:
 1. На сковороде/на пару приготовить рыбу. 
 2. Добавить остальные ингредиенты. Размять вилкой до консистенции пюре. 
 3. Выложить на хлеб толстым слоем. 
Для разморозки: разогреть на сковороде / в микроволновке.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Грибной сэндвич🥪🍄‍🟫":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Грибной сэндвич🥪🍄‍🟫
♨️Подходит для заготовки в морозильнике 
В составе:
 • Хлеб тостовый
 • Шампиньоны/белые грибы
 • Капуста 
 • Сметана/майонез/греческий йогурт 
 • Зелень: лук, петрушка, укроп
Приготовление:
 1. На сковороде приготовить грибы. 
 2. Добавить остальные ингредиенты. Размять вилкой до консистенции пюре. 
 3. Выложить на хлеб толстым слоем. 
Для разморозки: разогреть на сковороде / в микроволновке.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Сладкий завтрак🥣":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Сладкий завтрак🥣
♨️Подходит для заготовки в морозильнике 
В составе:
 • Овсянка не требующая варки/гранола/семена чиа 
 • Йогурт
 • Ягоды/фрукты
Приготовление:
 1. Смешать все ингредиенты. Оставить настояться на 10 минут
Для заморозки: выложить ингредиенты слоями, оставив йогурт внизу. 
Для разморозки: оставить в холодильнике на час, перемешать.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Смузи🥤":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Смузи🥤
♨️Подходит для заготовки в морозильнике 
В составе:
 • Фрукты/овощи/ягоды
 • Йогурт/молоко/сок
Приготовление:
 1. Раздавить вилкой/взбить блендером фрукты/овощи/ягоды. 
 2. Добавить йогурт/молоко/сок. 
Для разморозки: достать за час.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Рис и курица🍚🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Рис и курица🍚🍗
♨️Подходит для заготовки в морозильнике 
В составе:
 • Рис
 • Куриное мясо
 • Броколли/цветная капуста
 • Сливочное/авокадовое масло 
 • Приправы: базилик, орегано, укроп
Приготовление:
 1. Сварить рис. 
 2. Куриное мясо нарезать, потушить на сковороде на масле с приправами. Убрать со сковороды. 
 3. На той же сковороде потушить овощи с рисом. Добавить мясо. 
Для разморозки: разогреть на сковороде / в микроволновке. 
"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Рис и говядина🍚🥩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Рис и говядина🍚🥩
♨️Подходит для заготовки в морозильнике 
В составе:
 • Рис
 • Говядина
 • Морковь/болгарский перец
 • Сливочное/авокадовое масло 
 • Приправы: черный перц, петрушка, розмарин
Приготовление:
 1. Сварить рис. 
 2. Говядину нарезать, потушить на сковороде на масле с приправами.
 3. Смешать мясо, овощи и рис.  
Для разморозки: разогреть на сковороде / в микроволновке.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Рис и рыба🍚🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Рис и рыба🍚🐟
♨️Подходит для заготовки в морозильнике 
В составе:
 • Рис
 • Минтай/треска/судак/скумбрия/горбуша
 • Помидора/зеленая фасоль
 • Сливочное/авокадовое масло 
 • Приправы: лимонный сок, базилик, орегано
Приготовление:
 1. Сварить рис. 
 2. Рыбу разделать, потушить на сковороде на масле с приправами и овощами.
 3. Смешать мясо, овощи и рис.  
Для разморозки: разогреть на сковороде / в микроволновке.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Рис и тофу🍚🧀":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Рис и тофу 🍚🧀
♨️Подходит для заготовки в морозильнике 
В составе:
 • Рис
 • Тофу
 • Кукуруза/морковь по корейски
 • Сливочное/авокадовое масло 
 • Приправы: соевый соус, сахар, паприка, красный перец
Приготовление:
 1. Сварить рис. 
 2. Жаренный тофу нарезать, потушить на сковороде на масле с приправами и овощами.
 3. Смешать мясо, овощи и рис.  
Для разморозки: разогреть на сковороде / в микроволновке.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Паста альфредо🍗🧀🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Паста альфредо🍗🧀🍝
♨️Подходит для заготовки в морозильнике 
В составе:
 • Макароны
 • Куриное мясо/рыба/тофу
 • Сметана/сливки 30%
 • Твердый сыр 
 • Сливочное/авокадовое масло
 • Приправа: чеснок, петрушка
Приготовление:
 1. Отворить макароны до состояния альденте. 
 2. Потушить мясо/рыбу/тофу на масле с добавлением сметаны/сливок и приправы. Добавить воду из под варки макарон. 
 3. Добавить в соус макароны и тушить еще 3 минуты. Посыпать твердым сыром. 
Для заморозки: на макароны альденте положить соус. 
Для разморозки: разогреть на сковороде / в микроволновке и перемешать. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Паста болоньезе🥫🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Паста болоньезе🥫🍝
♨️Подходит для заготовки в морозильнике 
В составе:
 • Макароны
 • Любой фарш
 • Томатная паста
 • Лук
 • Сливочное/авокадовое масло
 • Приправа: паприка, черный перец
Приготовление:
 1. Отворить макароны до состояния альденте. 
 2. Потушить фарш с мелко нарезанным луком и томатной пастой на масле. Добавить воду из под варки макарон. 
 3. Добавить в соус макароны и тушить еще 3 минуты. 
Для заморозки: на макароны альденте положить соус. 
Для разморозки: разогреть на сковороде / в микроволновке и перемешать.  """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Паста сырная🧀🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Паста сырная🧀🍝
♨️Подходит для заготовки в морозильнике 
В составе:
 • Макароны
 • Сметана/сливки 30%
 • Сыр: моцарелла, тильзитер
 • Приправа: паприка, чеснок
Приготовление:
 1. Отворить макароны до состояния альденте. 
 2. В сметану/сливки добавить сыр и приправы. Добавить макароны и варить еще 3 минуты. 
Для заморозки: на макароны альденте положить соус. 
Для разморозки: разогреть на сковороде / в микроволновке и перемешать. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Паста грибная🍄‍🟫🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Паста грибная🍄‍🟫🍝
♨️Подходит для заготовки в морозильнике 
В составе:
 • Макароны
 • Куриное мясо/тофу
 • Шампиньоны/белые грибы
 • Сметана/сливки 30%
 • Твердый сыр
 • Сливочное/авокадовое масло
 • Приправа: чеснок, базилик
Приготовление:
1. Отворить макароны до состояния альденте.
2. Потушить мясо/тофу с грибами сметаной/сливками и приправой.
3. Добавить в соус макароны и тушить еще 3 минуты. Посыпать натертым сыром. 
4. Для заморозки: на макароны альденте положить соус. 
5. Для разморозки: разогреть на сковороде / в микроволновке и перемешать. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Зеленый салат🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Зеленый салат🥗
В составе:
 • Помидора
 • Капуста
 • Кукуруза
 • Лук 
 • Масло оливковое/подсолнечное
 • Приправа: чеснок, паприка, розмарин
Приготовление:
 1. Для заправки смешать масло и приправу. 
 2. Смешать овощи с заправкой"""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Итальянский салат🇮🇹🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Итальянский салат🇮🇹🥗
В составе:
 • Шпинат/салат
 • Оливки
 • Сыр бри/обжаренный тофу
 • Миндаль
 • Мед
 • Масло оливковое/подсолнечное
 • Приправа: орегано, розмарин 
Приготовление:
 1. Для заправки смешать масло, приправу и мед. 
 2. Смешать заправку и остальные ингредиенты. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Летний винегрет🍀🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Летний винегрет🍀🥗
В составе:
 • Адыгейский сыр
 • Капуста
 • Редиска
 • Жаренный нут/орехи
 • Лимон
 • Сметана/греческий йогурт
Приготовление:
 1. Смешать все ингредиенты. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Яблочный салат🍎🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Яблочный салат🍎🥗
В составе:
 • Яблоки
 • Лук
 • Орех лесной
 • Петрушка
Приготовление:
 1. Смешать все ингредиенты. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Салат брокколи🥦🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Салат брокколи🥦🥗
В составе:
 • Варенные брокколи 
 • Варенная морковь
 • Миндаль
 • Лук
 • Авокадо
Приготовление:
 1. Смешать все ингредиенты. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Мексиканский салат🇲🇽🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Мексиканский салат🇲🇽🥗
В составе:
 • Кукуруза
 • Адыгейский сыр
 • Варенное яйцо
 • Зеленый лук
 • Паприка
 • Петрушка
 • Лимонный сок
Приготовление:
 1. Смешать все ингредиенты. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Средиземноморский салат🫑🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Средиземноморский салат🫑🥗
В составе:
 • Огурец
 • Соленая помидора
 • Болгарский перец
 • Адыгейский сыр
 • Масло оливковое/подсолнечное
 • Приправа: розмарин, орегано, базилик
Приготовление:
 1. Для заправки смешать масло и приправу. 
 2. Смешать все ингредиенты и заправку. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Теплый салат🌤🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Теплый салат🌤️🥗
♨️Подходит для заготовки в морозильнике 
В составе:
 • Варенная морковь
 • Отваренное куриное мясо
 • Отваренные брокколи 
 • Помидора
Приготовление:
 1. Смешать все ингредиенты. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Осенний салат🍁🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Осенний салат🍁🥗
♨️Подходит для заготовки в морозильнике 
В составе:
 • Варенная тыква
 • Варенная морковь
 • Орехи любые
 • Авокадо
 • Лук
Приготовление:
 1. Смешать все ингредиенты."""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Рыбный салат🐟🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Рыбный салат🐟🥗
♨️Подходит для заготовки в морозильнике 
В составе:
 • Авокадо
 • Приготовленный минтай/треска/судак/скумбрия/горбуша
 • Лук
 • Адыгейский сыр
Приготовление:
 1. Смешать все ингредиенты. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Английский салат🏴󠁧󠁢󠁥󠁮󠁧󠁿🥗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Английский салат🏴󠁧󠁢󠁥󠁮󠁧󠁿🥗
♨️Подходит для заготовки в морозильнике 
В составе:
 • Фасоль в томатном соусе
 • Жаренный тофу
 • Лук
Приготовление:
 1. Смешать все ингредиенты. Подавать с хлебом. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Ультимейт Боул🥙":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Ультимейт Боул🥙
♨️Подходит для заготовки в морозильнике 
В составе:
 • Варенная морковь
 • Картофельное пюре
 • Варенное брокколи 
 • Варенная цветная капуста
 • Любые орехи
 • Хумус
 • Авокадо
 • Болгарский перец 
 • Жаренный кабачок
 • Оливки/маслины
 • Куриное мясо/говядина/рыба/тофу
 • Жаренная стручковая фасоль 
 • Кукуруза
 • Фасоль консирвированная
 • Горошек
Приготовление:
 1. Смешать некоторые из ингредиентов. 
Для разморозки: разогреть на сковороде / в микроволновке и перемешать. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Пюре с курицей🥔🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Пюре с курицей🥔🍗
♨️Подходит для заготовки в морозильнике 
В составе:
 • Картофель
 • Масло сливочное/авокадовое
 • Куриное мясо
 • Морковь
 • Томатная паста
 • Приправа: карри, паприка
Приготовление:
 1. Отворить картофель, размять, добавить масло. 
 2. Натертую морковь пожарить на масле, добавить томатную пасту и приправу. Добавить куриное мясо. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Пюре с говядиной🥔🥩":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Пюре с говядиной🥔🥩
♨️Подходит для заготовки в морозильнике 
В составе:
 • Картофель
 • Масло сливочное/авокадовое
 • Говядина
 • Морковь
 • Маринад: соевый соус, чеснок, томатная паста
 • Приправа: карри, зеленый лук 
Приготовление:
 1. Заранее замариновать нарезанную говядину.  
 2. Отворить картофель, размять, добавить масло. 
 3. Натертую морковь пожарить на масле, добавить приправу и говядину. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Пюре с рыбой🥔🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Пюре с рыбой🥔🐟
♨️Подходит для заготовки в морозильнике 
В составе:
 • Картофель
 • Масло сливочное/авокадовое
 • Тунец консервированный 
 • Морковь
 • Томатная паста
 • Приправа: карри, паприка
Приготовление:
 1. Отворить картофель, размять, добавить масло. 
 2. Натертую морковь пожарить на масле, добавить томатную пасту и приправу. Добавить тунец. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Пюре с тофу🥔🧀":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Пюре с тофу🥔🧀
♨️Подходит для заготовки в морозильнике 
В составе:
 • Картофель
 • Масло сливочное/авокадовое
 • Тофу
 • Морковь
 • Маринад: соевый соус, чеснок, томатная паста
 • Приправа: карри, зеленый лук 
Приготовление:
 1. Заранее замариновать нарезанный тофу. Пожарить. 
 2. Отворить картофель, размять, добавить масло. 
 3. Натертую морковь пожарить на масле, добавить приправу и тофу. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Лазанья🍝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Лазанья🍝
♨️Подходит для заготовки в морозильнике 
В составе:
 • Фарш говяжий
 • Томатный соус
 • Твердый сыр
 • Лук
 • Листы для лазаньи 
 • Приправа: черный перец, паприка
Приготовление:
 1. Разогреть духовку до 180 градусов. 
 2. Пожарить фарш с добавлением приправы, мелко нарезанного лука, томатного соуса и воды. 
 3. Выкладывать слоями - фарш, сыр, лист. В конце выложить фарш и обильно посыпать сыром. 
 4. Выпекать в духовке. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Рагу🥘":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Рагу🥘
♨️Подходит для заготовки в морозильнике 
В составе:
 • Картофель
 • Морковь
 • Баклажан
 • Кабачок
 • Лук
 • Горох
 • Фасоль
 • Фасоль стручковая
 • Куриное мясо/говядина/рыба
 • Шампиньоны/белые грибы 
 • Томатная паста
 • Чеснок
 • Орегано
Приготовление:
 1. Смешать некоторые из ингредиентов и тушить на сковороде. Добавить томатную пасту, воду, чеснок и орегано. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Карри🍛":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Карри🍛
♨️Подходит для заготовки в морозильнике 
В составе:
 • Отварной рис
 • Лук
 • Куриное мясо
 • Картофель
 • Морковь
 • Оливковое/подсолнечное масло
 • Томатная паста
 • Приправа: карри, чили, чеснок
Приготовление:
 1. Пожарить овощи(кроме лука) с мясом, добавив воду. Тушить на небольшом огне. 
 2. Отдельно приготовить соус: томатная паста, приправа, масло, мелко нарезанный лук. 
 3. Добавить соус к овощам. Подавать с рисом. 
Для разморозки: разогреть на сковороде / в микроволновке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Сливочный куриный суп🍜🍗":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Сливочный куриный суп🍜🍗
♨️Подходит для заготовки в морозильнике 
В составе:
 • Куриное мясо
 • Морковь
 • Сметана/сливки 30%
 • Картофель
 • Приправа: чеснок, паприка
Приготовление:
 1. Потушить курицу с морковью на сковороде. 
 2. В кастрюле отварить картошку. Добавить курицу, морковь, приправу и сметану/сливки.  
Для заморозки: на вареную картошку выложить курицу, морковь и приправу.  
Для разморозки: Залить водой и добавить сметану/сливки, довести до кипения. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Сливочный рыбный суп🍜🐟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Сливочный рыбный суп🍜🐟
♨️Подходит для заготовки в морозильнике 
В составе:
 • Минтай/треска/судак/скумбрия/горбуша/пикша/хек
 • Морковь
 • Сметана/сливки 30%
 • Картофель
 • Приправа: чеснок, паприка
Приготовление:
 1. Потушить рыбу с морковью на сковороде. 
 2. В кастрюле отварить картошку. Добавить рыбу, морковь, приправу и сметану/сливки.  
Для заморозки: на вареную картошку выложить рыбу, морковь и приправу.  
Для разморозки: Залить водой и добавить сметану/сливки, довести до кипения. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Сливочный грибной суп🍜🍄‍🟫":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Сливочный грибной суп🍜🍄‍🟫
♨️Подходит для заготовки в морозильнике 
В составе:
 • Шампиньоны/белые грибы
 • Морковь
 • Сметана/сливки 30%
 • Картофель
 • Приправа: чеснок, паприка
Приготовление:
 1. Потушить грибы с морковью на сковороде. 
 2. В кастрюле отварить картошку. Добавить грибы, морковь, приправу и сметану/сливки.  
Для заморозки: на вареную картошку выложить грибы, морковь и приправу.  
Для разморозки: Залить водой и добавить сметану/сливки, довести до кипения. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Крем суп🍜":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Крем суп🍜
♨️Подходит для заготовки в морозильнике 
В составе:
 • Основной ингредиент: куриное мясо/рыба/грибы/тыква/помидора/горох и брокколи/лук и белое вино
 • Морковь
 • Сметана/сливки 30%
 • Картофель
 • Приправа: чеснок, паприка
Приготовление:
 1. Потушить основной ингредиент с морковью на сковороде. 
 2. В кастрюле отварить картошку. Добавить основной ингредиент, морковь, приправу и сметану/сливки.  
 3. Взбить блендером. 
Для разморозки: Прокипятить. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Абсолютный рамен🍜":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Абсолютный рамен🍜
♨️Подходит для заготовки в морозильнике 
В составе:
• Куриное мясо/говядина/рыба/тофу
 • Стручковая фасоль/грибы/кукуруза/горох/болгарский перец
 • Вермишель 
 • Приправа: чеснок
Приготовление:
 1. Потушить мясо/рыбу/тофу с овощами с водой, варить на медленном огне. 
 2. Добавить вермишель. 
Для заморозки: не добавляя вермишель, заморозить бульон. 
Для разморозки: Прокипятить бульон, добавить вермишель. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Замороженный йогурт с ягодами🍧":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Замороженный йогурт с ягодами🍧
♨️Подходит для заготовки в морозильнике 
В составе:
 • Йогурт
 • Любые ягоды
Приготовление:
 1. Перемешать йогурт с ягодами. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Фруктовый пирог🥧":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Фруктовый пирог🥧
♨️Подходит для заготовки в морозильнике 
В составе:
 • Слоенное тесто
 • Любые фрукты
 • Сахар
Приготовление:
 1. Разогреть духовку до 180 градусов. 
 2. На тесто выложить фрукты, посыпать сахаром. Накрыть тестом. 
 3. Выпекать в духовке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Щербет🍨":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Щербет🍨
♨️Подходит для заготовки в морозильнике 
В составе:
 • Любые фрукты/ягоды
 • Сахарный сироп
Приготовление:
 1. В блендере взбить фрукты/ягоды, добавить сахарный сироп. 
 2. Заморозить в морозилке, перемешивая каждый час, на протяжении 10-12 часов. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Сладкий хлеб🍞":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Сладкий хлеб🍞
♨️Подходит для заготовки в морозильнике 
В составе:
 • Банан/вареная тыква/вареная морковь/смородина/шоколад
 • Яйца
 • Мука
 • Сахар
 • Масло сливочное/авокадовое
 • Разрыхлитель
 • Приправа: ваниль, грецкий орех, корица
Приготовление:
 1. Разогреть духовку до 180 градусов. 
 2. Смешать банан/тыкву/морковь/смородину/шоколад, яйца и растопленное масло. Добавить сухие муку, сахар, разрыхлитель, приправу. 
 3. Выпекать в духовке. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Оладьи🧇":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Оладьи🧇
♨️Подходит для заготовки в морозильнике 
В составе:
 • Картофель/кабачок
 • Яйца
 • Мука
Приготовление:
 1. Натереть картофель/кабачок, выжать от влаги. Смешать с другими ингредиентами. Выпекать на сковороде. """
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Лепешка🫓":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернутся в главное меню")
        markup.add(btn1)
        recipie = """Лепешка🫓
♨️Подходит для заготовки в морозильнике 
В составе:
 • Лаваш
 • Сыр
 • Любые овощи/готовый фарш/готовое мясо/рыба/колбасы
Приготовление:
 1. Отрезать полоску лаваша (учитывая, что одна полоса около 10х25 см)
 2. С краю в форме треугольника выложить любую начинку и посыпать сыром. Завернуть треугольник. 
 3. Пожарить на сковороде/тостере."""
        bot.send_message(message.from_user.id, recipie, reply_markup=markup)
    elif message.text == "Вернутся в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("буррито🌯")
        btn2 = types.KeyboardButton("сэндвичи🥪")
        btn3 = types.KeyboardButton("завтрак☀")
        btn4 = types.KeyboardButton("основные блюда🍽")
        btn5 = types.KeyboardButton("салаты🥗")
        btn6 = types.KeyboardButton("супы🍲")
        btn7 = types.KeyboardButton("дессерты🍩")
        btn8 = types.KeyboardButton("перекусы🍿")
        btn9 = types.KeyboardButton("ваши предложения")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "Выберете блюдо", reply_markup=markup)




bot.polling(none_stop=True, interval=0)
        
