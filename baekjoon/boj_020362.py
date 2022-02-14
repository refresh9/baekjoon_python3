from collections import Counter
n, s = input().split()
chat_list = []
for _ in range(int(n)):
    nick, chat = input().split()
    if nick == s:
        print(Counter(chat_list)[chat])
        break
    chat_list.append(chat)