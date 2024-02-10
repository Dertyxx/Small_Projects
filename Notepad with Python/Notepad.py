#je veux coder un bloc note avec python

#faire les imports

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import ttk
from tkinter import colorchooser
from tkinter import font
from tkinter import simpledialog

#définir la fenêtre
fenetre = tk.Tk()
fenetre.title("Bloc note")
#fenetre.geometry("600x400")

#définir les variables
texte = ""
chemin = ""
#zone_texte = scrolledtext.ScrolledText(fenetre, width = 800, height = 600, wrap = tk.WORD)
#définir la fonction pour créer un nouveau fichier
def nouveau():
      global texte
      global chemin
      if texte == "":
         texte = ""
         chemin = ""
      else:
         if messagebox.askyesno("Bloc note", "Voulez-vous enregistrer les modifications apportées à " + chemin + " ?"):
               enregistrer()
         else:
               texte = ""
               chemin = ""
      zone_texte.delete(1.0, tk.END)

#définir la fonction pour ouvrir un fichier
def ouvrir():
      global texte
      global chemin
      if texte == "":
         chemin = filedialog.askopenfilename(title = "Ouvrir un fichier", filetypes = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
         if chemin != "":
               fichier = open(chemin, "r")
               texte = fichier.read()
               zone_texte.delete(1.0, tk.END)
               zone_texte.insert(1.0, texte)
               fichier.close()
      else:
         if messagebox.askyesno("Bloc note", "Voulez-vous enregistrer les modifications apportées à " + chemin + " ?"):
               enregistrer()
               chemin = filedialog.askopenfilename(title = "Ouvrir un fichier", filetypes = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
               if chemin != "":
                     fichier = open(chemin, "r")
                     texte = fichier.read()
                     zone_texte.delete(1.0, tk.END)
                     zone_texte.insert(1.0, texte)
                     fichier.close()
         else:
               chemin = filedialog.askopenfilename(title = "Ouvrir un fichier", filetypes = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
               if chemin != "":
                     fichier = open(chemin, "r")
                     texte = fichier.read()
                     zone_texte.delete(1.0, tk.END)
                     zone_texte.insert(1.0, texte)
                     fichier.close()

#définir la fonction pour enregistrer un fichier
def enregistrer():
      global texte
      global chemin
      if chemin == "":
         chemin = filedialog.asksaveasfilename(title = "Enregistrer un fichier", filetypes = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
         if chemin != "":
               fichier = open(chemin, "w")
               fichier.write(texte)
               fichier.close()
      else:
         fichier = open(chemin, "w")
         fichier.write(texte)
         fichier.close()

#définir la fonction pour enregistrer sous
'''def enregistrer_sous():
      global texte
      global chemin
      chemin = filedialog.asksaveasfilename(title = "Enregistrer un fichier", filetypes = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
      if chemin != "":
            fichier = open(chemin, "w")
            fichier.write(texte)
            fichier.close()'''

def enregistrer_sous():
    global texte
    chemin = filedialog.asksaveasfilename(title="Enregistrer sous", filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
    if chemin != "":
        with open(chemin, "w") as fichier:
            fichier.write(texte)


#définir la fonction pour quitter
def quitter():
      global texte
      global chemin
      if texte == "":
         fenetre.destroy()
      else:
         if messagebox.askyesno("Bloc note", "Voulez-vous enregistrer les modifications apportées à " + chemin + " ?"):
               enregistrer()
               fenetre.destroy()
         else:
               fenetre.destroy()

#définir la fonction pour copier
def copier():
      zone_texte.clipboard_clear()
      zone_texte.clipboard_append(zone_texte.selection_get())

#définir la fonction pour coller
def coller():
      zone_texte.insert(tk.INSERT, zone_texte.clipboard_get())

#définir la fonction pour couper
def couper():
      zone_texte.clipboard_clear()
      zone_texte.clipboard_append(zone_texte.selection_get())
      zone_texte.delete(tk.SEL_FIRST, tk.SEL_LAST)

"""#définir la fonction pour annuler  
def annuler():
      zone_texte.edit_undo()"""
# Fonction Undo
def annuler():
    try:
        zone_texte.edit_undo()
        #zone_texte.edit_reset()
        zone_texte.update()
    except tk.TclError:
        # Gère le cas où aucune action undo n'est possible
        messagebox.showwarning("Attention", "Aucune action Undo n'est possible.")

"""#définir la fonction pour rétablir
def retablir():
      zone_texte.edit_redo()"""
# Fonction Redo
def retablir():
    try:
        zone_texte.edit_redo()
        zone_texte.update()
    except tk.TclError:
         pass


#définir la fonction pour sélectionner tout
def tout_selectionner():
      zone_texte.tag_add(tk.SEL, "1.0", tk.END)
      zone_texte.mark_set(tk.INSERT, "1.0")
      zone_texte.see(tk.INSERT)

#définir la fonction pour rechercher
'''def rechercher():
    global texte
    global chemin
    if texte == "":
        messagebox.showwarning("Bloc note", "Vous n'avez pas encore ouvert de fichier.")
    else:
        recherche = simpledialog.askstring("Bloc note", "Rechercher :")
        if recherche is not None:
            start = "1.0"
            while True:
                start = texte.search(recherche, start, tk.END)
                if not start:
                    break
                end = f"{start}+{len(recherche)}c"
                texte.tag_add("selection", start, end)
                start = end
            if "selection" not in texte.tag_names():
                messagebox.showwarning("Bloc note", "La chaîne de caractères \"" + recherche + "\" n'a pas été trouvée.")
                texte.tag_remove("selection", "1.0", tk.END)
            else:
                texte.focus_set()
                texte.tag_configure("selection", background="yellow")
                messagebox.showinfo("Bloc note", "La chaîne de caractères \"" + recherche + "\" a été trouvée.")'''

#définir la fonction pour rechercher et selectionner toutes les occurences de la recherche a la fois de sorte que l'on puisse les remplacer toutes d'un coup sans utliser search
def rechercher():
      global texte
      global chemin
      if texte == "":
         messagebox.showwarning("Bloc note", "Vous n'avez pas encore ouvert de fichier.")
      else:
         recherche = simpledialog.askstring("Bloc note", "Rechercher :")
         if recherche is not None:
               start = "1.0"
               while True:
                  start = zone_texte.search(recherche, start, tk.END)
                  if not start:
                     break
                  end = f"{start}+{len(recherche)}c"
                  zone_texte.tag_add("selection", start, end)
                  start = end
               if "selection" not in zone_texte.tag_names():
                  messagebox.showwarning("Bloc note", "La chaîne de caractères \"" + recherche + "\" n'a pas été trouvée.")
                  zone_texte.tag_remove("selection", "1.0", tk.END)
               else:
                  zone_texte.focus_set()
                  zone_texte.tag_configure("selection", background="yellow")
                  #messagebox.showinfo("Bloc note", "La chaîne de caractères \"" + recherche + "\" a été trouvée.")
                  zone_texte.tag_configure("selection", background="white")
                  zone_texte.tag_add(tk.SEL, "1.0", tk.END)




#définir la fonction pour remplacer
def remplacer():
      global texte
      global chemin
      if texte == "":
         messagebox.showwarning("Bloc note", "Vous n'avez pas encore ouvert de fichier.")
      else:
         recherche = simpledialog.askstring("Bloc note", "Rechercher :")
         if recherche != None:
               if recherche in texte:
                     remplacement = simpledialog.askstring("Bloc note", "Remplacer par :")
                     if remplacement != None:
                           texte = texte.replace(recherche, remplacement)
                           zone_texte.delete(1.0, tk.END)
                           zone_texte.insert(1.0, texte)
               else:
                     messagebox.showwarning("Bloc note", "La chaîne de caractères \"" + recherche + "\" n'a pas été trouvée.")

#ajouter les widgets
barre_menu = tk.Menu(fenetre)

#créer le menu fichier
menu_fichier = tk.Menu(barre_menu, tearoff = 0)
menu_fichier.add_command(label = "Nouveau", command = nouveau)
menu_fichier.add_command(label = "Ouvrir", command = ouvrir)
menu_fichier.add_command(label = "Enregistrer", command = enregistrer)
menu_fichier.add_command(label = "Enregistrer sous", command = enregistrer_sous)
menu_fichier.add_separator()
menu_fichier.add_command(label = "Quitter", command = quitter)
barre_menu.add_cascade(label = "Fichier", menu = menu_fichier)

#créer le menu édition
menu_edition = tk.Menu(barre_menu, tearoff = 0)
menu_edition.add_command(label = "Annuler", command = annuler)
menu_edition.add_command(label = "Rétablir", command = retablir)
menu_edition.add_separator()
menu_edition.add_command(label = "Couper", command = couper)
menu_edition.add_command(label = "Copier", command = copier)
menu_edition.add_command(label = "Coller", command = coller)
menu_edition.add_separator()
menu_edition.add_command(label = "Sélectionner tout", command = tout_selectionner)
barre_menu.add_cascade(label = "Édition", menu = menu_edition)

#créer le menu rechercher
menu_rechercher = tk.Menu(barre_menu, tearoff = 0)
menu_rechercher.add_command(label = "Rechercher", command = rechercher)
menu_rechercher.add_command(label = "Remplacer", command = remplacer)
barre_menu.add_cascade(label = "Rechercher", menu = menu_rechercher)

#afficher la barre de menu
fenetre.config(menu = barre_menu)



#mettre a jour le texte
def mettre_a_jour_texte(event):
      global texte
      texte = event.widget.get(1.0, tk.END)



#créer la zone de texte
zone_texte = tk.Text(fenetre)
zone_texte.bind("<KeyRelease>", mettre_a_jour_texte)
zone_texte.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#créer la barre de défilement
barre_defilement = tk.Scrollbar(fenetre, command=zone_texte.yview)
barre_defilement.pack(side=tk.RIGHT, fill=tk.Y)
zone_texte.config(yscrollcommand=barre_defilement.set)

#faire disparaitre automatiquement apres 2 seconde s'il nest pas solicité et le remettre
"""def hide_scrollbar():
    barre_defilement.pack_forget()
    zone_texte.pack_configure(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, barre_defilement.winfo_width()))
    fenetre.update()"""

#faire apparaitre la barre de défilement
def show_scrollbar():
    zone_texte.pack_configure(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 0))
    barre_defilement.pack(side=tk.RIGHT, fill=tk.Y)
    zone_texte.yview_moveto(1)

#faire apparaitre la barre de défilement
def on_scroll(*args):
    show_scrollbar()
    #fenetre.after(2000, hide_scrollbar)

zone_texte.bind("<MouseWheel>", on_scroll)
zone_texte.bind("<Button-4>", on_scroll)
zone_texte.bind("<Button-5>", on_scroll)

#configurer la zone de texte
zone_texte.config(undo=True, maxundo=-1, autoseparators=True)

#definir main
def main():
   #afficher la fenêtre
   fenetre.mainloop()
     
#lancer le programme
if __name__ == "__main__":
      main()



         
      


