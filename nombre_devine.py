import tkinter as tk
from tkinter import messagebox
from random import randrange
from time import sleep
from math import ceil

class GuessTheNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess The Numbers")
        self.number_to_guess = randrange(1, 11)
        self.attempts_left = 5
        self.money = 20
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Devinez un nombre entre 1 et 10")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Devinez", command=self.check_guess)
        self.button.pack()

        self.money_label = tk.Label(self.root, text=f"Argent: {self.money}€")
        self.money_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 0 or guess > 10:
                messagebox.showerror("Erreur", "Le nombre doit être entre 0 et 10.")
                return

            self.attempts_left -= 1

            if guess == self.number_to_guess:
                winnings = self.money * 3
                messagebox.showinfo("Résultat", f"Félicitations ! Vous obtenez {winnings}€!")
                self.money += winnings
                self.number_to_guess = randrange(1, 11)
                self.attempts_left = 5
            elif guess % 2 == self.number_to_guess % 2:
                winnings = ceil(self.money * 0.5)
                messagebox.showinfo("Résultat", f"Le nombre choisi est pair ou impair. Vous obtenez {winnings}€.")
                self.money += winnings
            else:
                messagebox.showinfo("Résultat", "Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
                self.money -= self.money

            self.money_label.config(text=f"Argent: {self.money}€")

            if self.money <= 0:
                messagebox.showinfo("Fin de Partie", "Vous êtes ruiné ! C'est la fin de la partie.")
                self.root.quit()
            elif self.attempts_left <= 0:
                messagebox.showinfo("Fin de Partie", "Vous avez épuisé vos tentatives. C'est la fin de la partie.")
                self.root.quit()

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()