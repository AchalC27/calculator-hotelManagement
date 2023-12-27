import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image,ImageTk
import random

class HotelManagementSystem:
    def Table(self):
        self.conn = sqlite3.connect('Hotel.db')
        self.cursor= self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, table_ID INTEGER PRIMARY KEY, item TEXT NOT NULL,quantity INTEGER NOT NULL,total_price REAL NOT NULL)''')
        self.conn.commit()
        self.conn.close()
    
    def fetch_customer(self):
        self.conn = sqlite3.connect('Hotel.db')
        self.cursor= self.conn.cursor()
        self.cursor('SELECT * FROM Hotel')
        self.customer = self.cursor.fetchall()
        self.conn.close()
        return self.customer
    
    def insert_customer (item, quantity, Cost):
        conn = sqlite3.connect('Hotel.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Customer (item, quantity, Cost) VALUES (?,?,?,?,?)', (item, quantity, Cost))
        conn.commit()
        conn.close()
         
    def __init__(hotel,root):
        hotel.root=root
        hotel.root.title("Hotel-Management-System")
        hotel.menu_list = {"Pizza - 250/-": 250.00,"Burger - 200/-": 200.00,"Toast - 150/-": 150.00,"Drink - 100/-": 100.00,"Ice-Cream - 50/-": 50.00 }
        hotel.payment_method = {"CASH", "UPI", "CARD", "WALLET"}
        hotel.Table_items = []
        hotel.total_price_variable = tk.StringVar()
        hotel.display_image()
        hotel.Table()
        hotel.total_price_label = tk.Label(root, textvariable=hotel.total_price_variable, bg="AntiqueWhite1",font=("Libre Baskerville", 15))
        hotel.total_price_label.place(x=1050, y=740)
        
    def generate_customer_id(self):
        return random.randint(100000, 999999)
    
    def display_image(self):
        self.hotel_management_text = tk.Label(root, text='HOTEL MANAGEMENT ', fg="White", bg="DodgerBlue4",padx=2, relief=tk.GROOVE,width=65, font=("Libre Baskerville", 30, "bold")).place(x=0, y=0)
        #menu frame me ke componenets
        self.menu_section = tk.Label(root, text='', fg="black", bg="AntiqueWhite1", relief=tk.GROOVE, width=60,height=100).place(x=0, y=50)
        
        #image wala section
        self.logo_path = "calculator-hotelManagement/Hotel_Management/Sources/PythonRestaurant.png"
        self.original_logo = Image.open(self.logo_path)
        self.resized_logo = self.original_logo.resize((300, 300), Image.BILINEAR)
        self.antique_white_background = Image.new("RGBA", (300, 300), (250, 235, 215, 255))
        self.antique_white_background.paste(self.resized_logo, (0, 0), self.resized_logo)
        self.photo = ImageTk.PhotoImage(self.antique_white_background)
        self.lab = tk.Label(root, image=self.photo)
        self.lab.place(x=55, y=50)
        
        #menu wala section
        self.menu_label = tk.Label(root, text="Menu Card", bg="AntiqueWhite1", font=("Libre Baskerville", 15)).place(x=10, y=325)
        self.menu_item=tk.StringVar()
        self.menu_scrollbar = ttk.Combobox(root, width=20, textvariable=self.menu_item,  font=("Libre Baskerville", 15), values=list(self.menu_list))
        self.menu_scrollbar.place(x=130, y=325)
        self.menu_scrollbar.set("Select Item")
        
        #quantity wala section
        self.quantity_label = tk.Label(root, text="Quantity", bg="AntiqueWhite1", font=("Libre Baskerville", 15)).place(x=10, y=375)
        self.menu_quantity = tk.IntVar()
        self.quantity_spinbox = tk.Spinbox(self.root, from_=1, to=100, width=20, font=("Libre Baskerville", 15), textvariable=self.menu_quantity).place(x=130, y=375)
        self.add_button = tk.Button(self.root, text ="ADD",width=36,fg="White", bg="DodgerBlue4",activeforeground="AntiqueWhite1", activebackground="DodgerBlue2", relief=tk.GROOVE, font=("Libre Baskerville", 15, ), command= self.add_function).place(x=0,y=425)
        
        #order information frame 
        self.order_section = tk.Label(root, text='', fg="black", bg="AntiqueWhite1", relief=tk.GROOVE, width=157,height=100).place(x=400, y=50)
        
        #order information components
        self.order_information_label = tk.Label(root, text="Order Information", bg="AntiqueWhite1", font=("Libre Baskerville", 15)).place(x=410,y=52)
        self.order_date_label= tk.Label(root, text="Date: ", bg="AntiqueWhite1", font=("Libre Baskerville", 15)).place(x=440,y=100)
        self.order_date = tk.Label(root, text=datetime.now().strftime('%A, %d %b %Y, %H:%M:%S'), bg="AntiqueWhite1", font=("Libre Baskerville", 15))
        self.order_date.place(x=1125, y=100)
        self.order_CustomerID_label= tk.Label(root, text="Customer ID:  ", bg="AntiqueWhite1", font=("Libre Baskerville", 15)).place(x=440,y=150)
        self.order_CustomerID = tk.Label(root, text=str(self.generate_customer_id()), bg="AntiqueWhite1", font=("Libre Baskerville", 15)).place(x=1125, y=150)
        self.order_TableNumber_label= tk.Label(root, text="Table Number:  ", bg="AntiqueWhite1", font=("Libre Baskerville", 15)).place(x=440,y=200)
        self.TableNumber = tk.IntVar()
        self.order_tableNumber_entry = tk.Entry(root, textvariable=self.TableNumber, width=32, font=("Libre Baskerville", 15)).place(x=1125,y=200)
        self.order_PaymentMethod_label= tk.Label(root, text="Payment Method:  ", bg="AntiqueWhite1", font=("Libre Baskerville", 15)).place(x=440,y=250)
        self.menu_scrollbar = ttk.Combobox(root, width=30, font=("Libre Baskerville", 15), values=list(self.payment_method))
        self.menu_scrollbar.place(x=1125, y=250)
        self.menu_scrollbar.set("Select Payment Method")
        
        #cost table
        self.Tables = ttk.Treeview(root, columns= ('Table ID','Items', "Quantity", "Cost") , show = 'headings' )
        self.Tables.heading('Table ID', text = "Table ID")
        self.Tables.heading('Items', text = "Items")
        self.Tables.heading('Quantity', text = "Quantity")
        self.Tables.heading('Cost', text = "Cost")
        self.Tables.tag_configure('Treeview', font=("Libre Baskerville", 15))
        self.Tables.place(x=445, y=325, width=1000, height=400)
        self.total_price = tk.Label(root, text="Total Price: Rs 00.00 ", bg="AntiqueWhite1", font=("Libre Baskerville", 15)).place(x=1200,y=740)
        
        #upgrade button
        self.upgrade_button = tk.Button(self.root, text ="UPGRADE",width=50,fg="White", bg="DodgerBlue4",activeforeground="AntiqueWhite1", activebackground="DodgerBlue2", relief=tk.GROOVE, font=("Libre Baskerville", 15, )).place(x=650,y=800)
        
    def add_function(self):
        item = self.menu_item.get()
        quantity = self.menu_quantity.get()
        table_ID = self.TableNumber.get()
        if item != "Select Item" and quantity > 0:
            cost = self.menu_list[item]
            total_cost = quantity * cost
            self.Table_items.append((table_ID, item, quantity, total_cost))
            self.Tables.insert("", tk.END, value=(table_ID, item, quantity, total_cost))
            self.total_price = sum(item[3] for item in self.Table_items)
            self.total_price_variable.set(f"Total Price: Rs {self.total_price:.2f}")
            
        
                 
    
if __name__ == "__main__":
    root = tk.Tk()
    hotel1 = HotelManagementSystem(root)
    root.geometry('1500x1000')
    root.mainloop()
    


