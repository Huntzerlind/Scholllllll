import time

user_agreement = 0
IQ = 0
print("Hey there, welcome my IQ test. The only IQ test on the internet that's 100% accurate.")
print("If you want to know your real IQ, this is the test for you! Please read our user agreement")
print("before you start.")
print("Select an option: 1. Take the survey, 2. User agreement, 3. How it works.")
aput = input()
if aput == '2':
    print("By taking this survey, you agree to all of the following terms: We may collect, store, and use"
          "all of the answers you input. We may sell this data to any government, company, or really anybody"
          "if they say please. We may use your data to model and recreate a replica of you. We may use this "
          "replica for slavery, morbid curiosities, or to kill and replace you. The replica will then take over"
          "your job, life, and children. The replica may seduce and bed your wife/husband. ")
    user_agreement = 1
elif aput == '3':
    print("Magic")
elif aput == '1':
    name = input("What is your name:")
    Q1 = input("How old are you")
    Q2 = input("Arnold Schwarzenegger has a long one. Michael J. Fox has a short one. "
               "Madonna does not use hers. Bill Clinton always uses his. The Pope never "
               "uses his. What is it?")
    print("Their last names! You filthy bastard :(")
    Q3 = input("Your parents have six sons including you and each son has one sister."
               " How many people are in the family?")
    print("nine.")
    Q4 = input("Draw a line")
    age = Q2
    Q2 = int(Q2/2)
    Q2 = (Q2*Q2)
    Q2 = (Q2 + 5)
    math_age = Q2
    Q5 = input("If I divided your age by two, then squared it, then added five, what would I get?")
    print(math_age)
    Q6 = input("Are you smart?")
    print("Apparently not")
    Q7 = input("Do you watch Dangerous Damian?")
    if Q7 == "yes":
        print("Thanks mom")
    else:
        print("https://www.youtube.com/channel/UCK6vxVQUlTLVGq61nJ12A0A?feature=emb_ch_name_ex")
    Q8 = input("If I played you in Backgamon right now, who would win?")
    print("Nobody. If you're playing backgamon you've already lost")
    Q9 = input("Can you communicate telepathically with animals?")
    print("Cool!")
    Q10 = input("What is the fifth letter of alphabet?")
    print("E")
    if user_agreement == 1:
       Q11 = input("Hypothetically, if you were to be cloned, could the clone be pacified with any"
                   "specific tranquilizer? Also, can you fit through a 12 inch gap between cage bars?"
                   "And how is the quality of your skin? ")
    print("Okay that was the last question. Thank you for taking the test!")
    print("Processing results...")
    if Q2 == "last name":
        IQ + 30
    if Q3 == "nine":
        IQ + 45
    if Q4 == "-"
        IQ + 15
    if  Q5
    time.wait(3)



