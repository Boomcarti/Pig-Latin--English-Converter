def to_pig_latin(sentence):
    ans=""
    words= sentence.split(" ")
    count=0;
    for word in words:
        if word.startswith("a") or word.startswith("e") or word.startswith("i") or word.startswith("o") or word.startswith("u"):
            words[count] = word+"way"
        else:
            words[count] = consonants(word)
        ans = ans+(words[count]+" ")
        count += 1
    return ans

def consonants(word):
    wordstobemoved=""
    ans=""
    wordarray = []
    for i in range(len(word)):
        wordarray.append(word[i:i+1])

    for i in range(len(wordarray)):
        if not (wordarray[i] == "a" or wordarray[i] == "e" or wordarray[i] =="i" or wordarray[i] =="o" or wordarray[i] =="u"):
            wordstobemoved= wordstobemoved+wordarray[i]
        if (wordarray[i] == "a" or wordarray[i] == "e" or wordarray[i] =="i" or wordarray[i] =="o" or wordarray[i] =="u"):
            break
           
    
    wordstobemoved="a"+wordstobemoved+"ay"
    for index in range(i , len(wordarray)):
        ans=ans+wordarray[index]
    return ans+wordstobemoved


def to_english(sentence):
    words=sentence.split(" ")
    count=0
    ans=""
    for word in words:
        words[count] = word[:-2]
        word = word[:-2]
        lastindex = word.rindex("a")
        firstpart = word[lastindex+1:]
        words[count]=word[:lastindex]
        word = word[:lastindex]
        ans = ans+firstpart+word+" "
    return ans

def main():
    prompt = input("(E)nglish or (P)ig Latin? \n")
    if prompt =="E" or prompt == "e":
        print("Enter an English sentence:")
        phrase= input()
        print("Pig-Latin:")
        print(to_pig_latin(phrase))
    else:
        print("Enter a Pig Latin sentence:")
        phrase= input()
        print("Pig-Latin:")
        print(to_english(phrase))

if __name__=='__main__':
    main() 



