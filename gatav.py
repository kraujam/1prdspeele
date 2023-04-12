from tkinter import * #imports the tkinter library

#all the functions that are used

def computer_wait():
    root.after(2000, computer_turn)

def try_again():#for trying again
    global p1, p2, p1_turn, p2_turn, string, p1_turn_check, p2_turn_check, string_list, string_list_fail_safe, string_check

    string="11001010"
    string_list=[]

    string_check=""

    for x in string:
        string_list.append(x)

    string_list_fail_safe=string_list

    print(string)

    #resets the screen and the scores
    p1=5
    p2=5

    p1_turn_check=True
    p2_turn_check=False

    p1_turn=""
    p2_turn=""
    
    p1_score_label.config(text="Player score: "+str(p1))
    p2_score_label.config(text="Computer score: "+str(p2))

    bit_string_label.config(text=string)

    p1_input_text.delete("1.0","end")
    


    try_again_btn.place_forget()

    ask_label.place(x=150, y=350)

    choice_computer_btn.place(x=100, y=400)

    choice_player_btn.place(x=350, y=400)

    
def winner(): #determines the winner when only 1 number remaining
    global p1, p2

    if p1>p2:
        print("You win!")

        bit_string_label.configure(text="You win!")

    elif p1<p2:
        print("You lose!")

        bit_string_label.configure(text="You lose!")

    elif p1==p2:
        print("Draw")

        bit_string_label.configure(text="Draw")


    p1_input_btn.place_forget()

    try_again_btn.place(x=250, y=400)
    
def p1_check_move(): # function when the button corresponding is pressed
    
    global p1, p2, p1_turn, p2_turn, string, p1_turn_check, p2_turn_check, string_list, string_list_fail_safe, string_check
    p1_turn=p1_input_text.get("1.0", "end-1c")
    if len(string)>1: #checks is the turn of the player is true or not
        p1_turn_check=False
        p2_turn_check=True
        # checks if the length of the input string same as the string it should be after the move
        for i in range(len(string)-1):
            if string[i]+string[i+1]=="11":#these commands check sections of the string
                if p1_turn=="11":#this checks if the player entered the section of the string that was checked for
                    string_list[i+1]="0"
                    string_list.pop(i)
                    p2-=1
                    break
            elif string[i]+string[i+1]=="00":
                if p1_turn=="00":
                    string_list[i+1]="1"
                    string_list.pop(i)
                    p2-=1
                    break

            elif string[i]+string[i+1]=="10":
                    
                if p1_turn=="10":
                    string_list[i+1]="0"
                    string_list.pop(i)
                    p1-=2
                    break
            elif string[i]+string[i+1]=="01":
                if p1_turn=="01":
                    string_list[i+1]="1"
                    string_list.pop(i)
                    p1-=2
                    break

    #this happens even if nothing is put or something invalid is put
    p2_score_label.configure(text="Computer score: "+str(p2))
    p1_score_label.configure(text="Player score: "+str(p1))
    string=""
    for x in string_list:
        string+=x
    string_check=""
    string_list_fail_safe=string_list
    bit_string_label.configure(text=string)

    p1_input_btn.place_forget()
    p1_input_text.delete("1.0","end")

    #computer_wait()#adds delay so the changes can be seen
    if len(string)==1: # checks for the winner
        winner()
    else:
        computer_wait()

def computer_turn():
    global p1, p2, p1_turn, p2_turn, string, p1_turn_check, p2_turn_check, string_list, string_list_fail_safe, string_check
    better=False #value given to the better, if 1 pointer found, it is given value true, so the code to find 2 pointers does not get executed
    
    for i in range(len(string)-1):#checks for the best possible outcomes first
        if string_list[i]=="1" and string_list[i+1]=="1": #if the 01 section available in the string it runs the code for it, next elif checks for 10 instead
            string_list[i+1]="0" #changes the second value of the section with the replacement
            string_list.pop(i) #remove the first bit of the section
            string=""
            for x in string_list:#makes the string for the next turn
                string+=x
            better=True
            p1-=1
            break

        elif string_list[i]=="0" and string_list[i+1]=="0":
            string_list[i+1]="1"
            string_list.pop(i)
            string=""
            for x in string_list:
                string+=x
            better=True
            p1-=1
            break

    if better==False: # if best possible 1 pointers are not availaible, the computer just playes the 2 pointer move
        for i in range(len(string)-1):#does exactly the same thing as the 1 pointer checking but is a fail safe option for 2 pointers is the 1 pointers are not available
            if string_list[i]=="0" and string_list[i+1]=="1":

                string_list[i+1]="1"
                string_list.pop(i)
                string=""
                for x in string_list:
                    string+=x
                better=True
                p2-=2
                break
            elif string_list[i]=="1" and string_list[i+1]=="0":
                string_list[i+1]="0"
                string_list.pop(i)
                string=""
                for x in string_list:
                    string+=x
                better=True
                p2-=2
                break

            break

    #runs no matter what outcome
    p1_score_label.configure(text="Player score: "+str(p1))#updates the scores
    p2_score_label.configure(text="Computer score: "+str(p2))
    string=""
    for x in string_list:
        string+=x
    string_check=""
    string_list_fail_safe=string_list
    bit_string_label.configure(text=string)
    p1_input_btn.place(x=120, y=350)

    p1_input_text.delete("1.0","end")
        
    if len(string)==1:
        winner()

#this is started whhen the player chooses who starts
def computer_start():
    computer_turn()#calls the function for computer's turn
    choice_computer_btn.place_forget()#removes the extra start choosing labels
    choice_player_btn.place_forget()
    ask_label.place_forget()

def Player_start():
    p1_input_btn.place(x=120, y=350)#places the enter button
    choice_computer_btn.place_forget()
    choice_player_btn.place_forget()
    ask_label.place_forget()

#_____________________defines the starting scores and GUI________________________________________

global p1, p2, p1_turn, p2_turn, string, p1_turn_check, p2_turn_check, string_list_fail_safe, string_check

string="11001010"
# Turns the string into a list for easier replacement of the items
string_list=[]

string_list_fail_safe=string#not used anymore
for x in string:#adds the value from the string to the list
    string_list.append(x)

string_check=""#not relevant
string_list_fail_safe=string_list#not relevant

print(string)#outputs the starting string into the terminal

#sets the starting scores
p1=5
p2=5

#not relevant
p1_turn_check=True
p2_turn_check=False

#sets the turn checker to string
p1_turn=""
p2_turn=""

#creates and changes the attributes of the window popup
root=Tk()
root.config(bg="Light Blue")
root.geometry("800x500")

#different labels on the window "root" which keep track of the score
p1_score_label=Label(root, text="Player score: "+str(p1), font=("", 30), bg="Blue", fg="Black")
p1_score_label.place(x=10, y=10)
p2_score_label=Label(root, text="Computer score: "+str(p2), font=("", 30), bg="Blue", fg="Black")
p2_score_label.place(x=400, y=10)

#displays the string on the window
bit_string_label=Label(root, text=string, font=("", 50), fg="Black", bg="Light Blue")
bit_string_label.place(x=170, y=170)

#the input area on the window is created
p1_input_label=Label(root, text="Player:", fg="Black", bg="Light Blue", font=("", 20))
p1_input_label.place(x=0, y=300)
p1_input_text=Text(root, height=1, width=8, font=("", 20))#text box for the player 1 move
p1_input_text.place(x=110, y=300)
p1_input_btn=Button(root, text="Enter", fg="Black", bg="Light Blue", font=("", 20), command=p1_check_move)

#labels to determine the starting player
ask_label=Label(root, text="Who shall start First?", font=("", 30), fg="Black", bg="Light Blue")
ask_label.place(x=150, y=350)

choice_computer_btn=Button(root, text="Computer", fg="Black", bg="Light Blue", font=("", 30), command=computer_start)
choice_computer_btn.place(x=100, y=400)

choice_player_btn=Button(root, text="Player", fg="Black", bg="Light Blue", font=("", 30), command=Player_start)
choice_player_btn.place(x=350, y=400)

#try again button
try_again_btn=Button(root, text="Play Again", fg="Black", bg="Light Blue", font=("", 30), command=try_again)

#don't delete this as this keeps the window open
root.mainloop()

