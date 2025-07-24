from tkinter import *
from tkinter import messagebox
import random

class Bill_App:
    def __init__(self, root):
        # Variables
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width=1280, height=700)
        self.root.minsize(width=1280, height=700)
        self.root.title("Grocery Billing System")

        self.cus_name = StringVar()
        self.c_phone = StringVar()
        x = random.randint(1000, 9999)
        self.c_bill_no = StringVar()
        self.c_bill_no.set(str(x))

        # Product variables
        self.bread = IntVar()
        self.candy = IntVar()
        self.hamburger = IntVar()
        self.hotdog = IntVar()
        self.sandwich = IntVar()
        self.wheat = IntVar()
        self.food_oil = IntVar()
        self.salt = IntVar()
        self.rice = IntVar()
        self.suger = IntVar()
        self.gatorade = IntVar()
        self.juice_oil = IntVar()
        self.coke = IntVar()
        self.waffer = IntVar()
        self.biscuits = IntVar()

        self.total_food = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()

        bg_color = "green"
        fg_color = "white"
        ibl_color = 'white'

        # Title of app
        title = Label(self.root, text="Grocery Billing System", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
                      font=("times new roman", 30, "bold"), pady=3)
        title.pack(fill=X)

        F1 = LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color, relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)
        # Customer Name
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold"))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, textvariable=self.cus_name, bg=bg_color, fg=fg_color,
                         font=("times new roman", 15, "bold"))
        cname_en.grid(row=0, column=1, padx=10, pady=5)
        # Customer Phone Number
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=2, ipady=4, ipadx=4, pady=5)
        # Customer Bill Number
        cbill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=3, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=4, ipadx=30, ipady=4, pady=5)

        #=======================Food Frame========================
        F2 = LabelFrame(self.root, text="Food", bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 15, "bold"))
        F2.place(x=5, y=180, width=380, height=380)

        # ========Frame Content==========
        bath_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Bread")
        bath_ibl.grid(row=0, column=0, ipady=5, ipadx=5)
        bath_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.bread)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)
        # Candy
        face_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Candy")
        face_ibl.grid(row=1, column=0, ipady=5, ipadx=5)
        face_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.candy)
        face_en.grid(row=1, column=1, ipady=5, ipadx=5)
        # Hamburger
        wash_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Hamburger")
        wash_ibl.grid(row=2, column=0, ipady=5, ipadx=5)
        wash_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.hamburger)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=5)
        # Hotdog
        hair_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Hotdog")
        hair_ibl.grid(row=3, column=0, ipady=5, ipadx=5)
        hair_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.hotdog)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=5)
        # Sandwich
        lot_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Sandwich")
        lot_ibl.grid(row=4, column=0, ipady=5, ipadx=5)
        lot_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.sandwich)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=5)
        # Wheat
        wheat_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Wheat")
        wheat_ibl.grid(row=5, column=0, ipady=5, ipadx=5)
        wheat_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.wheat)
        wheat_en.grid(row=5, column=1, ipady=5, ipadx=5)
        # Food Oil
        food_oil_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Food Oil")
        food_oil_ibl.grid(row=6, column=0, ipady=5, ipadx=5)
        food_oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.food_oil)
        food_oil_en.grid(row=6, column=1, ipady=5, ipadx=5)
        # Salt
        salt_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Salt")
        salt_ibl.grid(row=7, column=0, ipady=5, ipadx=5)
        salt_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.salt)
        salt_en.grid(row=7, column=1, ipady=5, ipadx=5)
        # Rice
        rice_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Rice")
        rice_ibl.grid(row=8, column=0, ipady=5, ipadx=5)
        rice_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.rice)
        rice_en.grid(row=8, column=1, ipady=5, ipadx=5)
        # Suger
        suger_ibl = Label(F2, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Suger")
        suger_ibl.grid(row=9, column=0, ipady=5, ipadx=5)
        suger_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.suger)
        suger_en.grid(row=9, column=1, ipady=5, ipadx=5)

        #=======================Grocery Frame========================
        F3 = LabelFrame(self.root, text='Others', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F3.place(x=400, y=180, width=325, height=380)

        #========Frame Content==========
        maza_ibl = Label(F3, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Gatorade")
        maza_ibl.grid(row=0, column=0, ipady=10, ipadx=20)
        maza_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.gatorade)
        maza_en.grid(row=0, column=1, ipady=5, ipadx=5)
        # Juice Oil
        juice_ibl = Label(F3, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Juice Oil")
        juice_ibl.grid(row=1, column=0, ipady=10, ipadx=20)
        juice_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.juice_oil)
        juice_en.grid(row=1, column=1, ipady=5, ipadx=5)
        # Coke
        cock_ibl = Label(F3, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Coke")
        cock_ibl.grid(row=2, column=0, ipady=10, ipadx=20)
        cock_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.coke)
        cock_en.grid(row=2, column=1, ipady=5, ipadx=5)
        # Waffer
        cold_ibl = Label(F3, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Waffer")
        cold_ibl.grid(row=3, column=0, ipady=10, ipadx=20)
        cold_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.waffer)
        cold_en.grid(row=3, column=1, ipady=5, ipadx=5)
        # Biscuits
        bis_ibl = Label(F3, font=("times new roman", 15, "bold"), fg=ibl_color, bg=bg_color, text="Biscuits")
        bis_ibl.grid(row=4, column=0, ipady=10, ipadx=20)
        bis_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.biscuits)
        bis_en.grid(row=4, column=1, ipady=5, ipadx=5)

        #=======================Bill Area========================
        F4 = Label(self.root, bd=10, relief=GROOVE)
        F4.place(x=960, y=180, width=325, height=380)
        #========
        bill_title = Label(F4, text="Bill Area", font=("Lucida", 15, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        #=======
        scroll_y = Scrollbar(F4, orient=VERTICAL)
        self.txt = Text(F4, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        #==============Buttons Frame================
        F5 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                       font=("times new roman", 13, "bold"))
        F5.place(x=0, y=560, relwidth=1, height=145)

        #========Buttons==========
        cosm_ibl = Label(F5, font=("times new roman", 15, "bold"), fg=ibl_color, text="Total Food")
        cosm_ibl.grid(row=0, column=0, padx=10, pady=0)
        cosm_en = Entry(F5, bd=8, relief=GROOVE, textvariable=self.total_food)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        gro_ibl = Label(F5, font=("times new roman", 15, "bold"), fg=ibl_color, text="Total Grocery")
        gro_ibl.grid(row=1, column=0, ipady=10, ipadx=5)
        gro_en = Entry(F5, bd=8, relief=GROOVE, textvariable=self.total_grocery)
        gro_en.grid(row=1, column=1, ipady=2, ipadx=5)
        #======oth========
        oth_ibl = Label(F5, font=("times new roman", 15, "bold"), fg=ibl_color, text="Others Total")
        oth_ibl.grid(row=2, column=0, ipady=10, ipadx=5)
        oth_en = Entry(F5, bd=8, relief=GROOVE, textvariable=self.total_other)
        oth_en.grid(row=2, column=1, ipady=2, ipadx=5)
        #======cosmt========
        cosmt_ibl = Label(F5, font=("times new roman", 15, "bold"), fg=ibl_color, text="Food Tax")
        cosmt_ibl.grid(row=0, column=2, ipady=10, ipadx=5)
        cosmt_en = Entry(F5, bd=8, relief=GROOVE, textvariable=self.tax_cos)
        cosmt_en.grid(row=0, column=3, ipady=2, ipadx=5)

        #======grot========
        grot_ibl = Label(F5, font=("times new roman", 15, "bold"), fg=ibl_color, text="Grocery Tax")
        grot_ibl.grid(row=1, column=2, ipady=10, ipadx=5)
        grot_en = Entry(F5, bd=8, relief=GROOVE, textvariable=self.tax_groc)
        grot_en.grid(row=1, column=3, ipady=2, ipadx=5)
        #====================
        otht_ibl = Label(F5, font=("times new roman", 15, "bold"), fg=ibl_color, text="Others Tax")
        otht_ibl.grid(row=2, column=2, ipady=10, ipadx=5)
        otht_en = Entry(F5, bd=8, relief=GROOVE, textvariable=self.tax_other)
        otht_en.grid(row=2, column=3, ipady=2, ipadx=5)
        #======================
        total_btn = Button(F5, text="Total", bg=bg_color, fg=fg_color, font=("Lucida", 12, "bold"), bd=7,
                         relief=GROOVE, command=self.total)
        total_btn.grid(row=1, column=4, ipadx=20, padx=30)
        #================================
        genbill_btn = Button(F5, text="Generate Bill", bg=bg_color, fg=fg_color, font=("Lucida", 12, "bold"), bd=7,
                         relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=5, ipadx=20)
        #================================
        clear_btn = Button(F5, text="Clear", bg=bg_color, fg=fg_color, font=("Lucida", 12, "bold"), bd=7,
                         relief=GROOVE, command=self.clear)
        clear_btn.grid(row=1, column=6, ipadx=20, padx=30)
        #================================
        exit_btn = Button(F5, text="Exit", bg=bg_color, fg=fg_color, font=("Lucida", 12, "bold"), bd=7,
                         relief=GROOVE, command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=20, padx=20)

        self.welcome_soft()

    def total(self):
        self.total_food_prices = (
            (self.bread.get() * 1) +
            (self.candy.get() * 3) +
            (self.hamburger.get() * 8) +
            (self.hotdog.get() * 6) +
            (self.sandwich.get() * 4)
        )
        self.total_food.set("$" + str(self.total_food_prices))
        self.tax_cos.set("$" + str(round(self.total_food_prices * 0.05)))
        self.total_grocery_prices = (
            (self.wheat.get() * 1) +
            (self.food_oil.get() * 5) +
            (self.salt.get() * 1) +
            (self.rice.get() * 3) +
            (self.suger.get() * 2)
        )
        self.total_grocery.set("$" + str(self.total_grocery_prices))
        self.tax_groc.set("$" + str(round(self.total_grocery_prices * 0.05)))
        self.total_other_prices = (
            (self.gatorade.get() * 4) +
            (self.juice_oil.get() * 2) +
            (self.coke.get() * 2) +
            (self.waffer.get() * 2) +
            (self.biscuits.get() * 2)
        )
        self.total_other.set("$" + str(self.total_other_prices))
        self.tax_other.set("$" + str(round(self.total_other_prices * 0.05)))

    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "Welcome To Store's Retail\n")
        self.txt.insert(END, f"\nBill No. :{str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name. :{str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n=====================================")
        self.txt.insert(END, "\nProduct    Qty   Price")
        self.txt.insert(END, "\n=====================================")

    def clear(self):
        self.txt.delete('1.0', END)
        self.cus_name.set("")
        self.c_phone.set("")
        self.c_bill_no.set(str(random.randint(1000, 9999)))
        for var in [self.bread, self.candy, self.hamburger, self.hotdog, self.sandwich, self.wheat, self.food_oil, self.salt, self.rice, self.suger, self.gatorade, self.juice_oil, self.coke, self.waffer, self.biscuits]:
            var.set(0)
        self.total_food.set("")
        self.total_grocery.set("")
        self.total_other.set("")
        self.tax_cos.set("")
        self.tax_groc.set("")
        self.tax_other.set("")
        self.welcome_soft()

    def bill_area(self):
        if self.cus_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Please Fill Customer Details")
        else:
            self.welcome_soft()
            if self.bread.get() != 0:
                self.txt.insert(END, f"\nBread    {self.bread.get()}   {self.bread.get() * 1}")
            if self.candy.get() != 0:
                self.txt.insert(END, f"\nCandy    {self.candy.get()}   {self.candy.get() * 3}")
            if self.hamburger.get() != 0:
                self.txt.insert(END, f"\nHamburger    {self.hamburger.get()}   {self.hamburger.get() * 8}")
            if self.hotdog.get() != 0:
                self.txt.insert(END, f"\nHotdog    {self.hotdog.get()}   {self.hotdog.get() * 6}")
            if self.sandwich.get() != 0:
                self.txt.insert(END, f"\nSandwich    {self.sandwich.get()}   {self.sandwich.get() * 4}")
            # Grocery
            if self.wheat.get() != 0:
                self.txt.insert(END, f"\nWheat    {self.wheat.get()}   {self.wheat.get() * 1}")
            if self.food_oil.get() != 0:
                self.txt.insert(END, f"\nFood Oil    {self.food_oil.get()}   {self.food_oil.get() * 5}")
            if self.salt.get() != 0:
                self.txt.insert(END, f"\nSalt    {self.salt.get()}   {self.salt.get() * 1}")
            if self.rice.get() != 0:
                self.txt.insert(END, f"\nRice    {self.rice.get()}   {self.rice.get() * 3}")
            if self.suger.get() != 0:
                self.txt.insert(END, f"\nSuger    {self.suger.get()}   {self.suger.get() * 2}")
            # Other
            if self.gatorade.get() != 0:
                self.txt.insert(END, f"\nGatorade    {self.gatorade.get()}   {self.gatorade.get() * 4}")
            if self.juice_oil.get() != 0:
                self.txt.insert(END, f"\nJuice Oil    {self.juice_oil.get()}   {self.juice_oil.get() * 2}")
            if self.coke.get() != 0:
                self.txt.insert(END, f"\nCoke         {self.coke.get()}      {self.coke.get() * 2}")
            if self.waffer.get() != 0:
                self.txt.insert(END, f"\nWaffer    {self.waffer.get()}      {self.waffer.get() * 2}")
            if self.biscuits.get() != 0:
                self.txt.insert(END, f"\nBiscuits    {self.biscuits.get()}      {self.biscuits.get() * 2}")
            self.txt.insert(END, "\n========================================")
            total_sum = self.total_food_prices + self.total_grocery_prices + self.total_other_prices + round(self.total_food_prices * 0.05) + round(self.total_grocery_prices * 0.05) + round(self.total_other_prices * 0.05)
            self.txt.insert(END, f"\nTotal: ${total_sum}")

    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()


