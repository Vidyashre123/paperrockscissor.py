import random
print("********************************")
print("* * PAPER * ROCK * SCISSOR * *")
print("********************************")
print(" Lets start the game!!....")
point=0
ai=0
hs=0
cs=0
ma=0
while(True):
    if(ma>5):
        print("######################")
        print("Total Match: ",ma)
        print("Human score: ",hs)
        print("AI score : ",cs)
        if(hs>cs):
            print("Congrats you won")
        elif(cs>hs):
            print("AI won...... Better luck next time")
        else:
            print("MATCH DRAW")
        print("######################")
        break
    c=input("Choose the option: paper->p Rock->r Scissor->s stop->stop: ")
    if(c=="p"):
        print("papper")
        point=10+random.randint(1,3)
        match point:
            case 11:
                ma=ma+1
                hs+hs+1
                print("Human:paper", "AI: rock")
                print("match: ",ma,"human score: ",hs,"AI score: ",cs)
                print("human: wins","AI: lost the Match")
                print("-----------------------")
            case 12:
                ma=ma+1
                cs=cs+1
                print("Human:paper","AI:scissor")
                print("match: ",ma,"human score: ",hs,"AI score: ",cs)
                print("human:lost ","AI: won the Match")
                print("-----------------------")
            case 13:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human:paper", "AI: paper")
                print("match: ",ma,"human score: ",hs,"AI score: ",cs)
                print("Match Draw")
                print("-----------------------")
    elif(c=="r"):
        print("rock")
        point=10+random.randint(1,3)
        match point:
            case 21:
                ma=ma+1
                hs+hs+1
                print("Human:rock", "AI: paper")
                print("match: ",ma,"human score: ",hs,"AI score: ",cs)
                print("human: wins","AI: lost the Match")
                print("-----------------------")
            case 22:
                ma=ma+1
                cs=cs+1
                print("Human:rock","AI:scissor")
                print("match: ",ma,"human score: ",hs,"AI score: ",cs)
                print("human:lost ","AI: won the Match")
                print("-----------------------")
            case 23:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human:rock", "AI: paper")
                print("match: ",ma,"human score: ",hs,"AI score: ",cs)
                print("Match Draw")
                print("-----------------------")
    elif(c=="s"):
        print("scissor")
        point=10+random.randint(1,3)
        match point:
            case 31:
                ma=ma+1
                hs+hs+1
                print("Human:paper", "AI: rock")
                print("match: ",ma,"human score: ",hs,"AI score: ",cs)
                print("human: wins","AI: lost the Match")
                print("-----------------------")
            case 32:
                ma=ma+1
                cs=cs+1
                print("Human:scissor","AI:rock")
                print("match: ",ma,"human score: ",hs,"AI score: ",cs)
                print("human:lost ","AI: won the Match")
                print("-----------------------")
            case 33:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human:scissor", "AI:scissor")
                print("match: ",ma,"human score: ",hs,"AI score: ",cs)
                print("Match Draw")
                print("-----------------------")
    elif(c=="stop"):
        break
print("program End")
