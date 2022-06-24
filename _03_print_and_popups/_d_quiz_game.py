from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    jk = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    #      // 2.  Ask the user a question 
    j = simpledialog.askstring('k', 'what is 2+2?')
    #      // 3.  Use an if statement to check if their answer is correct
    if j == 4:

    #      // 4.  if the user's answer was correct, add one to their score
        jk = jk+1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    i = simpledialog.askstring('g', 'what is 4+4?')
    jk
    n = simpledialog.askstring('f', 'what is 8+8?')
    jk
    # After all the questions have been asked, tell the user their final score
    messagebox.showinfo('lllll', 'your final score is 3')
    # remember to convert your variable to a string using the str() function 
    jk = str()
    # Run the window's .mainloop() method
