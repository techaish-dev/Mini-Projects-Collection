import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random

class ReWearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ReWear - Circular Fashion Marketplace")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f8f9fa')
        
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#f8f9fa')
        style.configure('Header.TFrame', background='#2d3e50')
        style.configure('Header.TLabel', background='#2d3e50', foreground='white', font=('Arial', 16, 'bold'))
        style.configure('Nav.TButton', font=('Arial', 12), background='#18a558', foreground='white')
        style.configure('Nav.TButton:hover', background='#128b4a')
        style.configure('Card.TFrame', background='white', relief='raised', borderwidth=1)
        style.configure('Title.TLabel', font=('Arial', 14, 'bold'), background='white')
        style.configure('Desc.TLabel', font=('Arial', 11), background='white', wraplength=280)
        style.configure('Action.TButton', font=('Arial', 10, 'bold'), background='#2d3e50', foreground='white')
        
        # Header
        self.header = ttk.Frame(root, style='Header.TFrame', height=80)
        self.header.pack(side='top', fill='x')
        self.header.pack_propagate(False)
        
        ttk.Label(self.header, text="ReWear", style='Header.TLabel').pack(side='left', padx=20)
        
        # Navigation buttons
        nav_frame = ttk.Frame(self.header, style='Header.TFrame')
        nav_frame.pack(side='right', padx=20)
        
        ttk.Button(nav_frame, text="Rent", style='Nav.TButton', command=self.show_rent).pack(side='left', padx=5)
        ttk.Button(nav_frame, text="Resell", style='Nav.TButton', command=self.show_resell).pack(side='left', padx=5)
        ttk.Button(nav_frame, text="Recycle", style='Nav.TButton', command=self.show_recycle).pack(side='left', padx=5)
        ttk.Button(nav_frame, text="About", style='Nav.TButton', command=self.show_about).pack(side='left', padx=5)
        
        # Main content area
        self.main_content = ttk.Frame(root, style='TFrame')
        self.main_content.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Welcome section
        self.show_welcome()
        
    def clear_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
    
    def show_welcome(self):
        self.clear_content()
        
        # Welcome message
        welcome_frame = ttk.Frame(self.main_content, style='TFrame')
        welcome_frame.pack(fill='x', pady=(0, 30))
        
        ttk.Label(welcome_frame, text="Welcome to ReWear", 
                 font=('Arial', 24, 'bold'), background='#f8f9fa').pack()
        ttk.Label(welcome_frame, text="Rent • Resell • Recycle", 
                 font=('Arial', 16), background='#f8f9fa', foreground='#18a558').pack(pady=10)
        ttk.Label(welcome_frame, text="Join the circular fashion movement and extend the life cycle of your clothing", 
                 font=('Arial', 12), background='#f8f9fa', wraplength=600).pack()
        
        # Stats frame
        stats_frame = ttk.Frame(self.main_content, style='Card.TFrame')
        stats_frame.pack(fill='x', pady=(0, 30))
        
        stats = [
            ("2.1M", "Items kept in circulation"),
            ("15K", "Active community members"),
            ("3.2K", "Tons of waste prevented")
        ]
        
        for stat, desc in stats:
            stat_frame = ttk.Frame(stats_frame, style='Card.TFrame')
            stat_frame.pack(side='left', expand=True, padx=20, pady=20)
            ttk.Label(stat_frame, text=stat, style='Title.TLabel', foreground='#18a558').pack()
            ttk.Label(stat_frame, text=desc, font=('Arial', 10), background='white').pack()
        
        # Features section
        ttk.Label(self.main_content, text="How ReWear Works", 
                 font=('Arial', 18, 'bold'), background='#f8f9fa').pack(anchor='w', pady=(20, 10))
        
        features_frame = ttk.Frame(self.main_content, style='TFrame')
        features_frame.pack(fill='x')
        
        features = [
            ("Rent", "Access designer fashion without the commitment. Rent for events or daily wear."),
            ("Resell", "Give your pre-loved items a new home. List your quality second-hand clothes."),
            ("Recycle", "Responsibly recycle garments that are beyond repair. We ensure proper processing.")
        ]
        
        for i, (title, desc) in enumerate(features):
            card = ttk.Frame(features_frame, style='Card.TFrame')
            card.pack(side='left', expand=True, fill='both', padx=(0, 20) if i < 2 else 0, pady=10)
            
            # Placeholder for icon
            icon_frame = ttk.Frame(card, width=60, height=60, style='Card.TFrame')
            icon_frame.pack(pady=20)
            icon_frame.pack_propagate(False)
            ttk.Label(icon_frame, text=title[0], font=('Arial', 18, 'bold'), 
                     background='white', foreground='#18a558').pack(expand=True)
            
            ttk.Label(card, text=title, style='Title.TLabel').pack()
            ttk.Label(card, text=desc, style='Desc.TLabel').pack(padx=20, pady=(0, 20))
            
            ttk.Button(card, text=f"Explore {title}", style='Action.TButton', 
                      command=lambda t=title: self.navigate_to(t)).pack(pady=(0, 15))
    
    def navigate_to(self, section):
        if section == "Rent":
            self.show_rent()
        elif section == "Resell":
            self.show_resell()
        elif section == "Recycle":
            self.show_recycle()
    
    def show_rent(self):
        self.clear_content()
        ttk.Label(self.main_content, text="Rent Fashion Items", 
                 font=('Arial', 20, 'bold'), background='#f8f9fa').pack(anchor='w', pady=(0, 20))
        
        # Filter section
        filter_frame = ttk.Frame(self.main_content, style='TFrame')
        filter_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Label(filter_frame, text="Filter by:", background='#f8f9fa').pack(side='left', padx=(0, 10))
        
        categories = ["All", "Dresses", "Suits", "Accessories", "Casual", "Formal"]
        category_var = tk.StringVar(value="All")
        
        for cat in categories:
            ttk.Radiobutton(filter_frame, text=cat, variable=category_var, 
                           value=cat, background='#f8f9fa').pack(side='left', padx=5)
        
        # Items grid
        items_frame = ttk.Frame(self.main_content, style='TFrame')
        items_frame.pack(fill='both', expand=True)
        
        # Sample rental items
        rental_items = [
            ("Designer Evening Gown", "$45/week", "Size M", "★ 4.8 (120 reviews)"),
            ("Business Suit", "$35/week", "Size L", "★ 4.7 (85 reviews)"),
            ("Summer Dress", "$25/week", "Size S", "★ 4.9 (64 reviews)"),
            ("Leather Jacket", "$40/week", "Size M", "★ 4.6 (92 reviews)")
        ]
        
        for i, (name, price, size, rating) in enumerate(rental_items):
            row, col = divmod(i, 2)
            card = ttk.Frame(items_frame, style='Card.TFrame')
            card.grid(row=row, column=col, padx=(0, 20), pady=(0, 20), sticky='nsew')
            
            # Placeholder for item image
            img_placeholder = ttk.Frame(card, height=150, width=150, style='Card.TFrame')
            img_placeholder.pack(pady=10)
            img_placeholder.pack_propagate(False)
            ttk.Label(img_placeholder, text="👗", font=('Arial', 40), background='white').pack(expand=True)
            
            ttk.Label(card, text=name, style='Title.TLabel').pack()
            ttk.Label(card, text=price, font=('Arial', 12, 'bold'), background='white', foreground='#18a558').pack()
            ttk.Label(card, text=size, font=('Arial', 10), background='white').pack()
            ttk.Label(card, text=rating, font=('Arial', 9), background='white').pack(pady=(0, 10))
            
            ttk.Button(card, text="Rent Now", style='Action.TButton').pack(pady=(0, 10))
        
        items_frame.columnconfigure(0, weight=1)
        items_frame.columnconfigure(1, weight=1)
        items_frame.rowconfigure(0, weight=1)
        items_frame.rowconfigure(1, weight=1)
    
    def show_resell(self):
        self.clear_content()
        ttk.Label(self.main_content, text="Resell Pre-Loved Items", 
                 font=('Arial', 20, 'bold'), background='#f8f9fa').pack(anchor='w', pady=(0, 20))
        
        # Two column layout
        resell_frame = ttk.Frame(self.main_content, style='TFrame')
        resell_frame.pack(fill='both', expand=True)
        
        # Left column - List an item
        list_frame = ttk.Frame(resell_frame, style='Card.TFrame')
        list_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        ttk.Label(list_frame, text="List an Item for Sale", style='Title.TLabel').pack(pady=20)
        
        # Form elements
        form_elements = [
            ("Item Name", "Enter item name"),
            ("Description", "Describe your item"),
            ("Size", "Select size"),
            ("Condition", "Select condition"),
            ("Price", "$0.00")
        ]
        
        for label, placeholder in form_elements:
            ttk.Label(list_frame, text=label, background='white').pack(anchor='w', padx=20, pady=(10, 0))
            entry = ttk.Entry(list_frame)
            entry.insert(0, placeholder)
            entry.pack(fill='x', padx=20, pady=(5, 0))
        
        ttk.Button(list_frame, text="Upload Images", style='Action.TButton').pack(pady=10)
        ttk.Button(list_frame, text="List Item", style='Action.TButton').pack(pady=20)
        
        # Right column - How it works
        info_frame = ttk.Frame(resell_frame, style='Card.TFrame')
        info_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        ttk.Label(info_frame, text="How Reselling Works", style='Title.TLabel').pack(pady=20)
        
        steps = [
            ("1. List", "Take photos and describe your item"),
            ("2. Sell", "We handle promotion and secure payments"),
            ("3. Ship", "Use our prepaid shipping labels"),
            ("4. Earn", "Get paid when your item sells")
        ]
        
        for step, desc in steps:
            step_frame = ttk.Frame(info_frame, style='Card.TFrame')
            step_frame.pack(fill='x', padx=20, pady=10)
            
            ttk.Label(step_frame, text=step, font=('Arial', 12, 'bold'), 
                     background='white', foreground='#18a558').pack(anchor='w')
            ttk.Label(step_frame, text=desc, background='white').pack(anchor='w')
    
    def show_recycle(self):
        self.clear_content()
        ttk.Label(self.main_content, text="Recycle Old Garments", 
                 font=('Arial', 20, 'bold'), background='#f8f9fa').pack(anchor='w', pady=(0, 20))
        
        # Impact section
        impact_frame = ttk.Frame(self.main_content, style='Card.TFrame')
        impact_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Label(impact_frame, text="Your Recycling Impact", style='Title.TLabel').pack(pady=20)
        
        facts = [
            ("~700 gallons", "of water saved per recycled cotton shirt"),
            ("95% reduction", "in water pollution compared to new production"),
            ("5.7 lbs", "of CO2 emissions avoided per recycled garment")
        ]
        
        for fact, desc in facts:
            fact_frame = ttk.Frame(impact_frame, style='Card.TFrame')
            fact_frame.pack(side='left', expand=True, padx=20, pady=20)
            ttk.Label(fact_frame, text=fact, style='Title.TLabel', foreground='#18a558').pack()
            ttk.Label(fact_frame, text=desc, font=('Arial', 10), background='white', wraplength=200).pack()
        
        # Process section
        ttk.Label(self.main_content, text="How to Recycle with Us", 
                 font=('Arial', 16, 'bold'), background='#f8f9fa').pack(anchor='w', pady=(20, 10))
        
        process_frame = ttk.Frame(self.main_content, style='TFrame')
        process_frame.pack(fill='x')
        
        steps = [
            ("1. Request", "a free recycling kit from your account"),
            ("2. Fill", "the kit with unwearable clothing and textiles"),
            ("3. Schedule", "a pickup or drop at a nearby location"),
            ("4. Earn", "reward points for future purchases")
        ]
        
        for i, (step, desc) in enumerate(steps):
            step_card = ttk.Frame(process_frame, style='Card.TFrame')
            step_card.pack(side='left', expand=True, fill='both', padx=(0, 20) if i < 3 else 0, pady=10)
            
            ttk.Label(step_card, text=step, style='Title.TLabel', foreground='#18a558').pack(pady=(20, 5))
            ttk.Label(step_card, text=desc, style='Desc.TLabel').pack(padx=20, pady=(0, 20))
        
        # CTA
        ttk.Button(self.main_content, text="Request Recycling Kit", style='Action.TButton', 
                  width=20).pack(pady=30)
    
    def show_about(self):
        self.clear_content()
        
        about_text = """
ReWear is a circular fashion marketplace dedicated to extending the life cycle of clothing 
and reducing textile waste. We believe in a sustainable future for fashion where items are 
rented, resold, and recycled rather than discarded.

Our mission is to transform the fashion industry by creating a closed-loop system that:
- Reduces the environmental impact of clothing production
- Makes fashion more accessible through rental options
- Provides a trusted platform for buying and selling pre-loved items
- Ensures responsible recycling of textiles that can no longer be worn

Join us in creating a more sustainable fashion future!
        """
        
        ttk.Label(self.main_content, text="About ReWear", 
                 font=('Arial', 20, 'bold'), background='#f8f9fa').pack(anchor='w', pady=(0, 20))
        
        ttk.Label(self.main_content, text=about_text, background='#f8f9fa', 
                 wraplength=700, justify='left').pack(anchor='w', pady=(0, 30))
        
        # Impact stats
        stats_frame = ttk.Frame(self.main_content, style='TFrame')
        stats_frame.pack(fill='x', pady=(0, 30))
        
        impacts = [
            ("12,500+", "Tons of clothing saved from landfills"),
            ("8.3M+", "Gallons of water conserved"),
            ("45,000+", "Active community members")
        ]
        
        for stat, desc in impacts:
            impact_card = ttk.Frame(stats_frame, style='Card.TFrame')
            impact_card.pack(side='left', expand=True, padx=10, pady=10)
            
            ttk.Label(impact_card, text=stat, style='Title.TLabel', foreground='#18a558').pack(pady=10)
            ttk.Label(impact_card, text=desc, background='white').pack(pady=(0, 10))
        
        # Team section
        ttk.Label(self.main_content, text="Our Commitment", 
                 font=('Arial', 16, 'bold'), background='#f8f9fa').pack(anchor='w', pady=(20, 10))
        
        commitments = [
            ("Transparency", "We openly share our environmental impact and processes"),
            ("Quality", "We ensure all items meet our quality standards before listing"),
            ("Innovation", "We continuously improve our technology to enhance sustainability"),
            ("Community", "We build a supportive community of conscious fashion lovers")
        ]
        
        for title, desc in commitments:
            commitment_frame = ttk.Frame(self.main_content, style='TFrame')
            commitment_frame.pack(fill='x', pady=5)
            
            ttk.Label(commitment_frame, text=title, font=('Arial', 12, 'bold'), 
                     background='#f8f9fa', foreground='#2d3e50').pack(anchor='w')
            ttk.Label(commitment_frame, text=desc, background='#f8f9fa').pack(anchor='w')

if __name__ == "__main__":
    root = tk.Tk()
    app = ReWearApp(root)
    root.mainloop()