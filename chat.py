from time import time, strftime, localtime

__all__ = ['content', 'add', 'flood_limit']

content = ''
chats = []
flood_limit = 5

name_lastsays = dict()

def add(name, says):
    global chats, content
    
    current_time = time()

    if current_time - name_lastsays.get(name, 0) > flood_limit:
        name_lastsays[name] = current_time
        chats.insert(0, '(%s)[%s]%s' % (strftime('%H:%M:%S', localtime(time()))
            , name, says))
        chats = chats[:50]
        content = '\n'.join(chats)