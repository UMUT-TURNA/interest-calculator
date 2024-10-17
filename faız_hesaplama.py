import tkinter as tk
from tkinter import messagebox

def print_money(para):
    return '${:,.1f}'.format(para)

class InterestCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Faiz Hesaplama Programı")
        self.root.geometry("400x500")
        self.root.configure(bg="#333333")
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, padx=10, pady=10, bg="#333333")
        self.frame.pack(pady=20)

        self.title_label = tk.Label(self.frame, text="FAIZ HESAPLAMA PROGRAMI", bg="#333333", fg="white", font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = tk.Label(self.frame, text="İsminiz:", bg="#333333", fg="white", font=("Helvetica", 12))
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.name_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.credit_label = tk.Label(self.frame, text="Kredi Miktarı:", bg="#333333", fg="white", font=("Helvetica", 12))
        self.credit_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        self.credit_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.credit_entry.grid(row=2, column=1, padx=10, pady=5)

        self.rate_label = tk.Label(self.frame, text="Faiz Oranı (%):", bg="#333333", fg="white", font=("Helvetica", 12))
        self.rate_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        self.rate_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.rate_entry.grid(row=3, column=1, padx=10, pady=5)

        self.years_label = tk.Label(self.frame, text="Kredi Vadesi (Yıl):", bg="#333333", fg="white", font=("Helvetica", 12))
        self.years_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        self.years_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.years_entry.grid(row=4, column=1, padx=10, pady=5)

        self.months_label = tk.Label(self.frame, text="Kredi Vadesi (Ay):", bg="#333333", fg="white", font=("Helvetica", 12))
        self.months_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
        self.months_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.months_entry.grid(row=5, column=1, padx=10, pady=5)

        self.iteration_label = tk.Label(self.frame, text="Yineleme Aralığı (Ay):", bg="#333333", fg="white", font=("Helvetica", 12))
        self.iteration_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        
        self.iteration_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.iteration_entry.grid(row=6, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.frame, text="Hesapla", command=self.calculate_interest, bg="#007acc", fg="white", font=("Helvetica", 12), width=20)
        self.calculate_button.grid(row=7, column=0, columnspan=2, pady=20)

        self.result_label = tk.Label(self.frame, text="", bg="#333333", fg="white", font=("Helvetica", 12))
        self.result_label.grid(row=8, column=0, columnspan=2, pady=10)

    def calculate_interest(self):
        try:
            name = self.name_entry.get()
            credit_amount = float(self.credit_entry.get())
            annual_rate = float(self.rate_entry.get())
            years = int(self.years_entry.get())
            months = int(self.months_entry.get())
            iteration = int(self.iteration_entry.get())

            total_months = (years * 12) + months
            monthly_interest = (credit_amount / 100) * (annual_rate / 12)
            current_months = 0
            total_paid = 0
            result = f"Merhaba, {name}!\n\n"

            while current_months < total_months:
                current_months += iteration
                total_paid += iteration * monthly_interest
                if current_months > total_months:
                    current_months = total_months
                result += f"{current_months // 12} yıl, {current_months % 12} ay:\n"
                result += f"Toplam Ödeme: {print_money(credit_amount + total_paid)}\n"
                result += f"Aylık Ödeme: {print_money((credit_amount + total_paid) / current_months)}\n\n"

            self.result_label.config(text=result)
        except ValueError:
            messagebox.showerror("Hata", "Lütfen tüm alanları doğru şekilde doldurun.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterestCalculator(root)
    root.mainloop()
