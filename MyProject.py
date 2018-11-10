import tkinter as tk
import tkinter.messagebox as mb
import pickle as pk
import tkinter.font as tf
from termcolor import colored

class MyProject:
    def __init__(self):
        self.__user = ''
        self.__pass = ''
        self.__amt = 0.0
        self.__row = None
        with open('user.dat', 'rb') as file:
            self.__userdata = pk.load(file)
        self.signin()

    def signin(self):
        """signin function creates a simple signin window and asks the user for
            information to move forward."""
        self.sw = tk.Tk()
        self.sw.title('Signin')
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()       
        self.cb_txt_sign = tk.StringVar()
        self.cb_txt_sign.set('Show Password')
        self.cb_val_sign = tk.IntVar()
        self.cb_val_sign.set(1)
        mytitlefont = tf.Font(family='TimesNewRoman',size='15',weight='bold')
        myregfont = tf.Font(family='TimesNewRoman',size='13')

        self.swl1 = tk.Label(self.sw,width=20,text='Enter Signin data below',font=mytitlefont)
        self.swl1.grid(columnspan=3)
        self.swl2 = tk.Label(self.sw,width=20,text='Username: ',font=myregfont) # Jim_Tim1
        self.swl2.grid(row=1)
        self.swl3 = tk.Label(self.sw,width=20,text='Password: ',font=myregfont) # biscuit1
        self.swl3.grid(row=2)

        self.swe1 = tk.Entry(self.sw, width=25, textvariable=self.user_var)
        self.swe1.grid(row=1,column=1,columnspan=2)
        self.swe2 = tk.Entry(self.sw, width=25, show='*', textvariable=self.pass_var)
        self.swe2.grid(row=2,column=1,columnspan=2)

        def activate_check():
            if self.cb_val_sign.get() == 1:
                self.swe2.config(show='*')
                self.cb_txt_sign.set('Show Password')
            else:
                self.swe2.config(show='')
                self.cb_txt_sign.set('Hide Password')

        self.cb_signin = tk.Checkbutton(self.sw, font=myregfont, command=activate_check, textvariable=self.cb_txt_sign, variable=self.cb_val_sign)
        self.cb_signin.grid(row=3,column=2)

        self.swnu = tk.Button(self.sw, width=15, text='New User', command=self.new_user_page,font=myregfont)
        self.swnu.grid(row=3)
        self.swb1 = tk.Button(self.sw, width=15, text='Enter', command=self.signin_to_main,font=myregfont)
        self.swb1.grid(row=4,column=2)
        self.swb2 = tk.Button(self.sw, width=15, text='Quit', command=self.quit_program,font=myregfont)
        self.swb2.grid(row=4)

        self.sw.mainloop()

    def new_user_page(self):
        """Destroy's the signin window and calls function new_user_window"""
        self.sw.withdraw()
        self.new_user_window()

    def signin_to_main(self):
        """signin_to_main function determines if the users data is in the system
            before allowing them access to the data"""
        flag = self.find_user(self.swe1.get(), True)
        x = self.find_user(self.swe1.get(), False)
        if flag:
            if self.swe2.get() == self.__userdata[x][1]:
                self.__user = self.__userdata[x][0]
                self.__pass = self.__userdata[x][1]
                self.__amt = self.__userdata[x][2]
                self.__row = x
                self.sw.destroy()
                self.main_window()
            else:
                mb.showinfo('Error','Password is incorrect')
        else:
            mb.showinfo('Error','Username is incorrect')

    def find_user(self, user, flag):
        for x in range(len(self.__userdata)):
            if user == self.__userdata[x][0]:
                if flag:
                    return True
                else:
                    return x
            else:
                continue
        return False

    def quit_program(self):
        """quit_program determines if the user really wants to quit the program
            at which point it shuts down everything"""
        if mb.askokcancel('Quit','Are you sure you want to quit program?'):
            exit()

    def main_window(self):
        """main_window function creates the main window for the user to be
            able to adjust their funds as needed"""
        self.mw = tk.Tk()
        self.mw.title('Main Window')
        mytitlefont = tf.Font(family='TimesNewRoman',size='15',weight='bold')
        myregfont = tf.Font(family='TimesNewRoman',size='13')
        intro_txt = 'Hello ' + self.__user
        self.my_money_txt = format(self.__amt, ',.2f')
        self.value = tk.StringVar()
        self.value.set(self.my_money_txt)
        self.cb_var = tk.IntVar()
        self.cb_var.set(0)

        self.intro = tk.Label(self.mw, text=intro_txt, font=mytitlefont)
        self.intro.grid(columnspan=3)
        self.funds = tk.Label(self.mw, text='Money: ', font=myregfont)
        self.funds.grid(row=1)
        self.money = tk.Label(self.mw, textvariable=self.value, font=myregfont)
        self.money.grid(row=1,column=1,columnspan=2)
        self.cng_amt = tk.Label(self.mw, text='Increase/Decrease Money: ', font=myregfont)
        self.cng_amt.grid(row=2,columnspan=2)

        self.enter_amt = tk.Entry(self.mw, width=20)
        self.enter_amt.grid(row=2,column=2)

        self.cb1 = tk.Checkbutton(self.mw, font=myregfont, text='Select to Reduce Funds', variable=self.cb_var)
        self.cb1.grid(row=3,columnspan=2)

        self.accept = tk.Button(self.mw, font=myregfont, width=15, text='Update Funds', command=self.update_funds)
        self.accept.grid(row=3,column=2)
        self.quit_b = tk.Button(self.mw, font=myregfont, width=15, text='Sign-out', command=self.sign_out)
        self.quit_b.grid(row=4)
        self.profile_b = tk.Button(self.mw, text='Profile', font=myregfont, width=15, command=self.goto_profile)
        self.profile_b.grid(row=4,column=2)

        self.mw.mainloop()

    def goto_profile(self):
        self.mw.destroy()
        self.profile_window()

    def profile_window(self):
        self.pw = tk.Tk()
        my_title_txt = str(self.__user) + "'s Profile"
        self.pw.title(my_title_txt)
        mytitlefont = tf.Font(family='TimesNewRoman',size='15',weight='bold')
        myregfont = tf.Font(family='TimesNewRoman',size='13')
        my_intro_pw = "Hello " + str(self.__user) + " select box below to change data."
        uname_pw = str(self.__user)
        pword_pw = str(self.__pass)
        amountpw = str(self.__amt)

        self.intro_label_pw = tk.Label(self.pw, text=my_intro_pw, font=mytitlefont)
        self.intro_label_pw.grid(columnspan=3)
        self.uname_pwl = tk.Label(self.pw, text='Username: ', font=myregfont)
        self.uname_pwl.grid(row=1)
        self.pword_pwl = tk.Label(self.pw, text='Password: ', font=myregfont)
        self.pword_pwl.grid(row=2)
        self.amt_pwl = tk.Label(self.pw, text='Current Funds: ', font=myregfont)
        self.amt_pwl.grid(row=3)

        self.uname_pwl2 = tk.Label(self.pw, text=(colored(uname_pw, 'blue')), font=myregfont)
        self.uname_pwl2.grid(row=1,column=1,columnspan=2)
        self.pword_pwl2 = tk.Label(self.pw, text=(colored(pword_pw, 'blue')), font=myregfont)
        self.pword_pwl2.grid(row=2,column=1,columnspan=2)
        self.amt_pwl2 = tk.Label(self.pw, text=(colored(amountpw, 'blue')), font=myregfont)
        self.amt_pwl2.grid(row=3,column=1,columnspan=2)

        self.accept = tk.Button(self.pw, width=15, text='Change', command=self.goto_change)
        self.accept.grid(row=4,column=2)
        self.cancel = tk.Button(self.pw, width=15, text='Cancel', command=self.back_to_main)
        self.cancel.grid(row=4)
        self.delete = tk.Button(self.pw, width=15, text='Delete User', command=self.del_user)
        self.delete.grid(row=4,column=1)

        self.pw.mainloop()

    def back_to_main(self):
        self.pw.destroy()
        self.main_window()

    def goto_change(self):
        self.pw.destroy()
        self.change_profile_window()

    def change_profile_window(self):
        self.cpw = tk.Tk()
        my_title_txt = "Change " + str(self.__user) + "'s Profile"
        self.cpw.title(my_title_txt)
        my_intro_txt = 'Fillin the boxes you wish to change below.'
        mytitlefont = tf.Font(family='TimesNewRoman',size='15',weight='bold')
        myregfont = tf.Font(family='TimesNewRoman',size='13')
        
        self.cp_intro = tk.Label(self.cpw, text=my_intro_txt, font=mytitlefont)
        self.cp_intro.grid()
        self.cp_name = tk.Label(self.cpw, text='Username: ', font=myregfont)
        self.cp_name.grid()
        self.cp_psl1 = tk.Label(self.cpw, text='Password: ', font=myregfont)
        self.cp_psl1.grid()
        self.cp_psl2 = tk.Label(self.cpw, text='Re-Enter: ', font=myregfont)
        self.cp_psl2.grid()

        self.cp_name_e = tk.Entry(self.cpw, width=25)
        self.cp_name_e.grid()
        self.cp_pse1 = tk.Entry(self.cpw, width=25)
        self.cp_pse1.grid()
        self.cp_pse2 = tk.Entry(self.cpw, width=25)
        self.cp_pse2.grid()

        self.accept = tk.Button(self.cpw, width=15, text='Accept', command=self.change_userdata)
        self.accept.grid()
        self.cancel = tk.Button(self.cpw, width=15, text='Back', command=self.cancel_change)
        self.cancel.grid()

        self.cpw.mainloop()

    def cancel_change(self):
        self.cpw.destroy()
        self.profile_window()

    def change_userdata(self):
        if len(self.cp_name_e.get()) > 0:
            if not(self.find_user(self.cp_name_e.get(), True)):
                if len(self.cp_name_e.get()) >= 8:
                    self.__user = self.cp_name_e.get()
                    self.__userdata[self.__row][0] = self.__user
                    self.name_pw.set(self.__user)
                else:
                    mb.showinfo('Error','Username must be at least 8 characters long..')
            else:
                mb.showinfo('Error','Username is already taken..')
        if len(self.cp_pse1.get()) > 0 and len(self.cp_pse2.get()) > 0:
            if self.cp_pse1.get() == self.cp_pse2.get():
                if len(self.cp_pse1.get()) >= 8:
                    self.__pass = self.cp_pse1.get()
                    self.__userdata[self.__row][1] = self.__pass
                    self.pass_pw.set(self.__pass)
                else:
                    mb.showinfo('Error','Password must be at least 8 characters long..')
            else:
                mb.showinfo('Error',"Password's must match each other")
        elif (len(self.cp_pse1.get()) > 0 and len(self.cp_pse2.get()) == 0) or (len(self.cp_pse2.get()) > 0 and len(self.cp_pse1.get()) == 0):
            mb.showinfo('Error',"Password fields must both contain data")
        self.update_file()
        

    def del_user(self):
        if mb.askyesno('Delete User', 'Would you like to delete this account?'):
            self.pw.destroy()
            del self.__userdata[self.__row]
            self.update_file()
            self.signin()

    def sign_out(self):
        """sign_out function asks if user wants to signout then updates records
            of current financial changes"""
        if mb.askokcancel('Sign-out', 'Are you sure you want to sign-out?'):
            for x in range(len(self.__userdata)):
                if self.__user == self.__userdata[x][0]:
                    self.__userdata[x][2] = self.__amt
                    with open('user.dat', 'wb') as file:
                        pk.dump(self.__userdata, file)
            self.mw.destroy()
            self.signin()

    def update_funds(self):
        """update_funds function determines whether to add/subtract the amount
            entered by user depending on a checkbutton widgets data"""
        amount = float(self.enter_amt.get())
        total = float(self.__amt)
        if self.cb_var.get() == 1:
            total -= amount
        else:
            total += amount
        self.value.set(format(total, ',.2f'))
        self.__amt = total

    def new_user_window(self):
        self.nuw = tk.Tk()
        self.nuw.title('New User Window')
        intro_new_user = 'Please fill in all available entry fields below'
        mytitlefont_nw = tf.Font(family='TimesNewRoman',size='15',weight='bold')
        myregfont = tf.Font(family='TimesNewRoman',size='13')

        self.intro_new = tk.Label(self.nuw, text=intro_new_user, font=mytitlefont_nw)
        self.intro_new.grid(columnspan=3)
        self.username_l = tk.Label(self.nuw, width=20, text='Username: ', font=myregfont)
        self.username_l.grid(row=1)
        self.passw_l1 = tk.Label(self.nuw, width=20, text='Password: ', font=myregfont)
        self.passw_l1.grid(row=2)
        self.passw_l2 = tk.Label(self.nuw, width=20, text='Password: ', font=myregfont)
        self.passw_l2.grid(row=3)
        self.amt_label = tk.Label(self.nuw, width=20, text='Starting Funds: ', font=myregfont)
        self.amt_label.grid(row=4)

        self.username_e = tk.Entry(self.nuw, width=25)
        self.username_e.grid(row=1,column=1,columnspan=2)
        self.passw_e1 = tk.Entry(self.nuw, width=25)
        self.passw_e1.grid(row=2,column=1,columnspan=2)
        self.passw_e2 = tk.Entry(self.nuw, width=25)
        self.passw_e2.grid(row=3,column=1,columnspan=2)
        self.amt_entry = tk.Entry(self.nuw, width=25)
        self.amt_entry.grid(row=4,column=1,columnspan=2)

        self.accept_new = tk.Button(self.nuw, font=myregfont, width=15, text='Accept', command=self.acpt_new_user)
        self.accept_new.grid(row=5,column=2)
        self.cancel_new = tk.Button(self.nuw, font=myregfont, width=15, text='Cancel', command=self.cancel_new_user)
        self.cancel_new.grid(row=5)

        self.nuw.mainloop()

    def acpt_new_user(self):
        if not(self.find_user(self.username_e.get(), True)):
            if len(self.username_e.get()) >= 8:
                if self.passw_e1.get() == self.passw_e2.get():
                    if len(self.passw_e1.get()) >= 8:
                        if len(self.amt_entry.get()) > 0:
                            self.__userdata.append([self.username_e.get(),self.passw_e1.get(),float(self.amt_entry.get())])
                            self.update_file()
                            self.sw.deiconify()
                            self.user_var.set(self.username_e.get())
                            self.pass_var.set(self.passw_e1.get())
                            self.nuw.destroy()
                        else:
                            mb.showinfo('Error','Starting Funds data field must contain data')
                    else:
                        mb.showinfo('Error','Password must be at least 8 characters long')
                else:
                    mb.showinfo('Error','Password fields must equal each other')
            else:
                mb.showinfo('Error','Username field requires at least 8 characters.')
        else:
            mb.showinfo('Error','Username has already been taken please choose another.')

    def cancel_new_user(self):
        self.sw.deiconify()
        self.nuw.destroy()
    
    def update_file(self):
        with open('user.dat', 'wb') as file:
            pk.dump(self.__userdata,file)
        with open('user.dat', 'rb') as file:
            self.__userdata = pk.load(file)      

def main():
    mp = MyProject()
main()







        
    
