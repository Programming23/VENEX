import requests

token = [
    "5405896266:AAEJ3ys5YGYnsZH2mbwCibyBN-jUz7sVGho",
    "5303895970:AAFlIyXZq35p1lCxPo_IoowAE6Xm-SfIOqg",
    "5450989550:AAHfsadyn2xTODBBiEy5g_q_xxlsmzHDDjg",
    "5531348667:AAGKb1St2T08GWlVMOHUb8NjQEP8It1ADQc",
    "5556787750:AAF_9pxWxbXhIWIkBvpFiN6eV3Q62xq3Cy0",
    "5440466832:AAGzaynhUcs3Dya2dBn5Rh7F7JlgU3eLkK4",
    "5405405877:AAEN6fY5PLRSSb65TW2Z0rKoFUoAv2CQiM4",
    "5546222396:AAH8WXedd5oR68MXH_-KVJNTvt_UyhTMcBs",
    "5531373084:AAFiT-e4xy0HU9nTYjtWuPrfObjTqYCwdD4",
    "5480738265:AAF49PL9TNloRh0Rb1Z7vttpAD9AmF2jfF8",
    "5304240815:AAEquvG-bl8nCs4ymZnDt9_KSLvaXOPBJiA",
    "5342964211:AAFYHd0_3EAgzwvMhqT0G9VyvaFCYp5KvN8",
    "5490039097:AAF2BhAgd2LSMZLZmJ2lvv4zCHWYDBSW-DI",
    "5218058146:AAHNzZ61dF5qTlG8jc-sEg76AUlBoEWKb7o",
    "5576383918:AAGztY782Ot5MHxP3N1ndNEeDnO9EkH6WKU",
    "5408775017:AAGAbLDgtC0dMEJxtGk3DZSeYOxY9eJoDJA",
    "5429265538:AAGCh2Dqw-5gOeZiIqFbMyvJr8HRXPFPUas",
    "5581246233:AAGNA2grYAg2jOZwYtqry5_41HLo8LdWW9U",
    "5464259533:AAHzna4GDzVHXKZzjXQPXZKJcG5Tux4vao8",
    "5549123021:AAEVNsziiAltOVCqTsSi7mi87tLimHL8a14",
    "5558611579:AAHw5ZnkzftCwjBQDfmG76YPa6QOv4X37qY",
]

group = 'WIZCHECKER10'
cmd = '/ch'

file = open('output.txt', 'r')

index = 0
mx = len(token)
num = 1
max_req = 5

for line in file:
    if num == max_req:
        index += 1
    url = f'https://api.telegram.org/bot{token[index]}/sendMessage?chat_id=@{group}&text={cmd}{line}'
    r = requests.get(url)
    if index == mx:
        index = 0

file.close()
