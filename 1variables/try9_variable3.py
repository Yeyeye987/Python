a, b, c = "The Story ", "of Vampire ", "Michaela."

def myfunc():
    global g
    g, h, j = "Guren ", "no ", "Chatastrophy."
    print ("Owari no Seraph: " + g + h + j)

myfunc()

print ("Owari no Seraph: " + a + b + c)
print ("Owari no Seraph: " + a + b + g+".")
