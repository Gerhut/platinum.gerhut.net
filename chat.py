from time import time

__all__ = ['chat_content', 'add']

chat_content = ''
chats = []

def add(name, content):
    chats.insert(0, '(%s)[%s]%s' % (strftime('%H:%M:%S', localtime(time()))
        , name, content))
    chats = chats[:50]
    chat_content = '\n'.join(chats)