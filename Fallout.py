import random

#Словарь с информацией о различных локациях.
locations = {
    "пустошь": {
        "описание": "Вы находитесь в бескрайней пустоши. Вокруг вас находятся развалины и остатки былой цивилизации.",
        "соседние_локации": ["лагерь", "завод", "пивоварня"],
        "враги": ["радскорпион", "дикий гуль"],
        "ресурсы": ["мясо радскорпиона", "грязная вода", "заколка"]
    },
    "лагерь": {
        "описание": "Вы пришли к лагерю рейдеров. Здесь царит хаос и анархия.",
        "соседние_локации": ["пустошь", "пещера"],
        "враги": ["рейдер"],
        "ресурсы": ["оружие", "стимулятор", "антирадин"]
    },
    "завод": {
        "описание": "Перед вами расположен огромный завод по производству протектронов. Видно несколько охранных патрулей роботов.",
        "соседние_локации": ["пустошь", "убежище"],
        "враги": ["протектрон"],
        "ресурсы": ["радиоактивные материалы", "металолом", "болты"]
    },
    "убежище": {
        "описание": "Вы входите в убежище под номером 108. Похоже оно давно заброшено, но из соседней комнаты слышно, как кто-то произносит имя 'Гэри'.",
        "соседние_локации": ["завод"],
        "враги": ["Клон Гэри", "радтаракан"],
        "ресурсы": ["комбенизон убежища 108","10-мм пистолет", "мясо радтаракана"]
    },
    "пещера": {
        "описание": "Вы вошли в темную пещеру, полную тайн и опасностей.",
        "соседние_локации": ["лагерь"],
        "враги": ["Супермутант"],
        "ресурсы": ["кости", "бутылочные крышки", "металолом"]
    },
    "пивоварня": {
        "описание": "Вы зашли в пивоварню 'Сансет саспарилла'. На удивление здесь довольно тихо и видно лишь несколько радтараканов и кротокрысов.",
        "соседние_локации": ["пустошь"],
        "враги": ["радтаракан", "кротокрыс"],
        "ресурсы": ["Пиво 'Сансет саспарилла'", "Крышки от 'Сансет саспарилла' со звездой", "пустая бутылка"]
    }
}

#Сражение с врагами.
def сражение(враги, ресурсы):
    while враги:
        выбранный_враг = random.choice(враги)
        print(f"Вы сражаетесь с {выбранный_враг}!")        
        if random.random() < 0.5:
            print(f"Вы победили {выбранный_враг}!")
            враги.remove(выбранный_враг)
        else:
            print(f"{выбранный_враг} нанес вам урон!")
        
        if not враги:
            print("Вы победили всех врагов!")
            полученный_предмет = random.choice(ресурсы)
            print(f"Осмотрев тела врагов вы нашли: {полученный_предмет}")
        else:
            print("Остались другие враги:")
            for враг in враги:
                print(f"- {враг}")

#Перемещение между локациями и столкновение с врагами.
def перемещение(локация):
    print(locations[локация]["описание"])
    print("Вы видите следующие доступные локации:")
    for соседняя_локация in locations[локация]["соседние_локации"]:
        print(f"- {соседняя_локация}")
    
    if locations[локация]["враги"]:
        print("Вы столкнулись с врагами!")
        сражение(locations[локация]["враги"], locations[локация]["ресурсы"])

    выбор = input("Выберите локацию для перемещения или введите 'выход' для выхода из игры: ")
    if выбор == "выход":
        print("Спасибо за игру! До свидания!")
        return
    elif выбор in locations[локация]["соседние_локации"]:
        перемещение(выбор)
    else:
        print("Вы выбрали недопустимую локацию.")

#Начало игры.
print("Добро пожаловать в мир Fallout!")
print("Вы очнулись в бескрайней пустоши...")
перемещение("пустошь")