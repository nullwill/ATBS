import re

test = """http://google.com/Hello

https://www.google.com/search?q=valid+url+characters&rlz=1C1UEAD_enUS1129US1129&oq=valid+URL+characters&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMgoIBhAAGAoYFhgeMggIBxAAGBYYHjIICAgQABgWGB4yCAgJEAAYFhge0gEINDA2N2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8


IN the text we are trying to find http and https links!!

http://stackoverflow.com/questions/7109143/what-characters-are-valid-in-a-url


http://www.chess.com/analysis/game/live/139887189134?tab=analysis&move=67 Let's just randomly paste links to see what sticks and what doesnt

Ya hurd me??

http:/youhardme.com/1

testing all of it"""

http_re = re.compile(r'https?://\S+')
matches = http_re.findall(test)
for match in matches:
    print(match)