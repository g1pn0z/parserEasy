#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import requests
import re

url = 'https://lenta.ru/news/2021/01/20/regions/'
r = requests.get(url, allow_redirects=True)
open('index.html', 'wb').write(r.content)
f = open("index.html", "r")
contents = f.read()
result = re.findall(r'class=\"b-text clearfix js-topic__text\" itemprop=\"articleBody\"', contents)
print(result)
result = re.search(r'class=\"b-text clearfix js-topic__text\" itemprop=\"articleBody\"', contents)

print(result.group(0))
mainwindow = tk.Tk()
mainwindow.title("Parser Internet Journals")
text1 = tk.Text(mainwindow, height=20, width=50)
text1.config(state="normal")
text1.insert(tk.INSERT,result.group(0))
text1.insert(tk.INSERT,"\nLine 2")
text1.config(state="disabled")

text1.pack()
button1 = tk.Button(mainwindow,text="Парсинг")
button1.pack()
mainwindow.mainloop()