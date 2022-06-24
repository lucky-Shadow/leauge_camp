from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    hi = random.randint(0, 3)
    # 2. Print your variable to the console
    print(hi)
    # 3. Get the user to enter something that they think is awesome
    t = simpledialog.askstring('fg', 'enter something you think is awsome')
    # 4. If your variable is  0
    if hi == 0:
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo('ljlkjlk', 'lego land is awsome!')
    # 5. If your variable is  1
    if hi == 1:
        # -- tell the user whatever they entered is ok.
        messagebox.showinfo('ff', 'lego land is ok')
    # 6. If your variable is  2
    if hi == 2:
        # -- tell the user whatever they entered is boring.
        messagebox.showinfo('gg', 'lego land is boring')
    # 7. If your variable is  3
    if hi == 3:
        # -- invent your own message to give to the user (be nice).
        messagebox.showinfo('kk', 'lego land is not fun but it does have good food')
    # Run the window's .mainloop() method
