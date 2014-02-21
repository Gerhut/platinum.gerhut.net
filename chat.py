from time import time

__all__ = ['content', 'add']

content = ''
chats = []

def add(name, content):
    chats.insert(0, '(%s)[%s]%s' % (strftime('%H:%M:%S', localtime(time()))
        , name, content))
    chats = chats[:50]
    content = '\n'.join(chats)