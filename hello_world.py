volume = 17
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
# Change vol if too loud/quiet
if volume <20 or volume > 80:
    volume = 50
    print("That's better")

# Define a function
def hi(name):
    if name == "Alice":
        print("hi there, Alice")
    elif name == "Louis":
        print("hi there, Louis")
    else:
        print("Hello, " + name.capitalize() + ", and World!")
    
hi("oleg")

# For In loops

people = ["alice", "louis", "robin", "nubi"]
for name in people:
    hi(name)
    print ('aaaand')
