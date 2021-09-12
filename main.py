from yandex import YaUploader
from heroes import Hero
from tok import tok_ya, tok_hero


if __name__ == '__main__':
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    hero = Hero(tok_hero)
    hero.max_hero_int(hero_list)

    path_to_file = 'C:/PyProject/requests/1.txt'
    uploader = YaUploader(tok_ya)
    uploader.upload(path_to_file)
