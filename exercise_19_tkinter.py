from swampy.Gui import *

g = Gui()
g.title('Gui')


def make_button():
    g.bu(text='Press me too.', command=make_label)


def make_label():
    g.la(text='Nice Job!')


def make_circle():
    canvas.circle(coord=[0, 0], r=20, fill='blue', outline='red', width=2)


button = g.bu(text='Press me.', command=make_circle)
entry = g.en(text='Type your name: ')
text = g.te(width=10, height=5)
text.insert(END, 'A line of text.')
text.insert(1.1, 'nother')
print(text.get(0.0, END))
text.delete(1.1, END)
print(text.get(0.0, END))
canvas = g.ca(width=500, height=500, bg='cyan')
canvas.rectangle([[0, 0], [200, 100]], fill='blue', outline='orange', width=1)
canvas.oval([[0, 0], [200, 100]], outline='orange', width=1)
canvas.line([[0, 100], [100, 200], [200, 100]], width=1)
canvas.polygon([[0, 100], [100, 200], [200, 100]], fill='black', outline='orange', width=1)

g.mainloop()
