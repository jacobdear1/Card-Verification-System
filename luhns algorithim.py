import tkinter

def validate_credit_card_number(card_number):
    temp_list=list(str(card_number))
    my_list=[]
    list1 = temp_list[-2::-2]
    list2=temp_list[::-2]
    list2 = [int (n) for n in list2]
    my_list=[int(n) for n in list1]
    list1 = [int(n)*2 for n in list1]
    t_list=list1

    for i in list1:
        sum_res=0

        if i>9:
            idx = list1.index(i)
            t_list.pop(idx)

            while i:
                rem = i%10
                sum_res+=rem
                i = i//10
            t_list.insert(idx, sum_res)

    list1_sum=sum(t_list)
    list2_sum = sum(list2)
    final_sum = list1_sum+ list2_sum

    if final_sum%10==0:
        return True
    return False


def cardcheck():

    cardnumber = ccnumber.get()

    if len(cardnumber) > 16:
        print("Please enter a 16 digit card number, the number you have enter is too long ")

    if len(cardnumber) < 16:
        print("Please enter a 16 digit card number, the number you have entered is too short")

    else:
        result = validate_credit_card_number(cardnumber)

        if (result):
            print("Your credit card is valid")
            cardnumber = int(cardnumber)
            first_digit = cardnumber
            while (first_digit >= 10):
                first_digit = first_digit // 10
            if first_digit == 4:
                print("Your card is a Visa credit card")
            elif first_digit == 5:
                print("Your card is a Mastercard credit card")
            else:
                print("The card is invalid, this system only validates Visa or Mastercard credit cards")
        else:
            print("Your credit card is invalid")

window = tkinter.Tk()
canvas1 = tkinter.Canvas(window, width=400, height=300, relief="raised")
canvas1.pack()
label1 = tkinter.Label(window, text="Card Verfication System")
label1.config(font=("helvetica", 14))
canvas1.create_window(200, 25, window=label1)
label2 = tkinter.Label(window, text="Type your card number:")
label2.config(font=("helvetica", 10))
canvas1.create_window(200, 100, window=label2)
ccnumber = tkinter.StringVar()
entry1 = tkinter.Entry(window, textvariable = ccnumber)
canvas1.create_window(200, 140, window=entry1)
button1 = tkinter.Button(window, text="Continue", command = cardcheck)
canvas1.create_window(200, 180, window=button1)

window.mainloop()

cardcheck()