from time import time, strftime, localtime

__all__ = ['content', 'add']

content = ''
chats = []

def add(name, says):
    global chats, content
    chats.insert(0, '(%s)[%s]%s' % (strftime('%H:%M:%S', localtime(time()))
        , name, says))
    chats = chats[:50]
    content = '\n'.join(chats)