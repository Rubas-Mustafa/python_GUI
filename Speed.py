from time import time 

#! Error
def typingErrors(prompt):
    global iwords 

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors+=1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1]==words[i+1]) & (iwords[i+1]==words[i+1]):
                    continue
                else:
                    errors+=1
            else:
                errors+=1
    return errors 


#! Speed
def typingSpeed(iprompt, stime, etime): #start time and end time
    global time
    global iwords 
    
    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / time

    return speed 


#! Time Taken

def timeElapsed(stime, etime):
    time =  etime - stime

    return time 

if __name__ == "__main__":
    prompt = "Hi, my name is Rubas Mustafa."
    print("Type This:-", prompt)

# THE INPUT
    input("Press Enter to Start.")

# ALL THE INFO FOR TIME LAPSE
    stime = time()
    iprompt = input()
    etime = time()

# ALL TRHE FUNCTIONS 

    time = round(timeElapsed(stime, etime), 2)
    speed = round(typingSpeed(iprompt, stime, etime), 4)
    errors = typingErrors(prompt)


    print(time ,"seconds")
    print(speed, "words per minute")
    print(errors, "errors")

if errors==0:
    print("Good Job")
else:
    print("Try Again")