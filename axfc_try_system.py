import requests, os

subdomains = [
    "pepper",
    "saffron",
    "mars",
    "taurus",
    "aquarius",
    "aries",
    "earth",
    "jupiter",
    "mercury",
    "venus",
    "emerald",
    "sapphire",
    "peridot",
    "opal",
    "ape",
    "gorilla",
    "monkey",
    "chimpanzee",
    "capricomus",
    "pisces",
    "capricornus",
    "gemini",
    "diamond",
    "pearl",
    "aquamarine"
]

print("Axfc DL Try System")
path = input("Axfc DL URLを入力してください : ").split("axfc.net")[-1]
filename = path.split("/")[-1]

for i in subdomains:
    url = "https://"+i+".axfc.net"+path
    print(url, end="")
    try:
        res = requests.get(url)
        res.raise_for_status()
        with open(filename, mode="wb") as f:
            f.write(res.content)
        print(" OK")
    except Exception as e:
        print(" Error "+str(e)[:11])
    if os.path.isfile(filename):
        break

if os.path.isfile(filename):
    print("ファイルがダウンロードできました")
else:
    print("ファイルがダウンロードできませんでした")