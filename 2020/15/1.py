# whens = {}
whens = [None] * 30000
spokens = []
current_turn = 1

def speak(n):
    print("speaking", n)
    spokens.append(n)
    if n in whens:
        if len(whens[n]) > 1:
            whens[n] = [whens[n][-1], current_turn]
        else:
            whens[n].append(current_turn)
    else:
        whens[n] = [current_turn]

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        
        for n in l.split(","):
            speak(int(n))
            current_turn += 1
            
def play_turn():
    last_spoken = spokens[-1]

    if len(whens[last_spoken]) == 1:
        speak(0)
    else:
        speak(whens[last_spoken][-1] - whens[last_spoken][-2])

while True:
    print("playing turn", current_turn)
    play_turn()
    if current_turn == 30000000:
        exit()
    current_turn += 1