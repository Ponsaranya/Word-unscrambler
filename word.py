import random

def choose():
    words=['time', 'people', 'world', 'water', 'man', 'woman', 'child', 'family', 'house', 'food', 'money', 'work', 'love', 'friend', 'day', 'night', 'sun', 'moon', 'earth', 'air', 'fire', 'tree', 'animal', 'dog', 'cat', 'bird', 'flower', 'music', 'book', 'school', 'teacher', 'student', 'car', 'road', 'city', 'country', 'government', 'war', 'peace', 'health', 'heart', 'mind', 'hope', 'dream', 'idea', 'problem', 'solution', 'light', 'dark', 'color', 'time', 'space', 'year', 'month', 'week', 'day', 'hour', 'minute', 'second', 'age', 'life', 'death', 'birth', 'history', 'future', 'past', 'present', 'way', 'door', 'window', 'hand', 'foot', 'head', 'body', 'face', 'eye', 'ear', 'nose', 'mouth', 'hair', 'voice', 'smile', 'food', 'drink', 'sleep', 'dream', 'name', 'number', 'letter', 'word', 'sentence', 'story', 'picture', 'question', 'answer', 'problem', 'idea', 'job', 'business', 'money']
    pick=random.choice(words)
    return pick

def jumble (word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print (p1n, 'Your score is :',p1)
    print (p2n, 'Your score is :',p2)
    print('Thanks for playing')
    print('Have a nice day')

def play():
    p1name=input('Player 1, Please enter your name')
    p2name=input('Player 2, Please enter your name')
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose() #computers choice
        qn=jumble(picked_word)
        print(qn)
        #player1
        if turn%2==0:
            print(p1name, 'Your turn. ')
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp1=pp1+1
                print('Your score is:', pp1)
            else:
                print('Better luck next time. I thought:',picked_word)
            c=input('Press 1 to continue and 0 to quit:')
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break

        #player 2
        else :
            print(p2name, 'Your turn. ')
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp2=pp2+1
                print('Your score is:', pp2)
            else:
                print('Better luck next time. I thought:',picked_word)
            c=input('Press 1 to continue and 0 to quit:')
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1

play()



