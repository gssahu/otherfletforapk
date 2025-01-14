from flet import *

def main(page:Page):
    T = Text('Hello world!')
    page.add(T)
    
    page.update()

app(main)
