import customtkinter as ctk

from . import theme


class NavBar(ctk.CTkFrame):
    def __init__(self, master, sur_changement):
        super().__init__(
            master,
            fg_color=theme.CARTE,
            corner_radius=0,
            border_width=1,
            border_color=theme.BORDURE,
            height=56,
        )
        self._sur_changement = sur_changement
        self._boutons = {}
        self.grid_propagate(False)

        entrees = (
            ("utilisateurs", "👤  Utilisateurs"),
            ("livres", "📖  Livres"),
            ("parametres", "⚙  Paramètres"),
        )

        self.grid_rowconfigure(0, weight=1)
        for index, (cle, texte) in enumerate(entrees):
            colonne = index * 2
            self.grid_columnconfigure(colonne, weight=1)
            bouton = ctk.CTkButton(
                self,
                text=texte,
                height=54,
                corner_radius=0,
                fg_color="transparent",
                hover_color=theme.BOUTON_SURVOL,
                text_color=theme.TEXTE,
                font=theme.police(14),
                command=lambda valeur=cle: self._sur_changement(valeur),
            )
            bouton.grid(row=0, column=colonne, sticky="nsew")
            self._boutons[cle] = bouton

            if index < len(entrees) - 1:
                separateur = ctk.CTkFrame(
                    self,
                    width=1,
                    fg_color=theme.BORDURE,
                    corner_radius=0,
                )
                separateur.grid(row=0, column=colonne + 1, sticky="ns")

    def activer(self, cle):
        for nom, bouton in self._boutons.items():
            actif = nom == cle
            bouton.configure(
                fg_color=theme.ACTIF if actif else "transparent",
                font=theme.police(14, "bold") if actif else theme.police(14),
            )


class BookCard(ctk.CTkFrame):
    def __init__(
        self,
        master,
        livre,
        sur_emprunter,
        sur_retourner,
        sur_supprimer,
    ):
        super().__init__(
            master,
            fg_color=theme.CARTE,
            corner_radius=6,
            border_width=1,
            border_color=theme.BORDURE,
        )

        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=3)
        self.grid_columnconfigure(3, weight=3)

        disponible = livre.getAvailability()
        statut = "Disponible" if disponible else f"Emprunté par {livre.getBorrowerId()}"
        colonnes = (
            ("Titre", livre.getTitle(), 0),
            ("Auteur", livre.getAuthor(), 1),
            ("ISBN", livre.getISBN(), 2),
            ("Statut", statut, 3),
        )

        for entete, valeur, colonne in colonnes:
            ctk.CTkLabel(
                self,
                text=entete,
                font=theme.police(12),
                text_color=theme.TEXTE_SECONDAIRE,
                anchor="w",
            ).grid(
                row=0,
                column=colonne,
                sticky="ew",
                padx=(16 if colonne == 0 else 8, 8),
                pady=(12, 2),
            )
            ctk.CTkLabel(
                self,
                text=valeur,
                font=theme.police(13),
                text_color=theme.TEXTE,
                anchor="w",
                justify="left",
                wraplength=240 if colonne == 0 else 180,
            ).grid(
                row=1,
                column=colonne,
                sticky="ew",
                padx=(16 if colonne == 0 else 8, 8),
                pady=(0, 4),
            )

        ctk.CTkButton(
            self,
            text="🗑",
            width=32,
            height=28,
            corner_radius=4,
            fg_color="transparent",
            hover_color=theme.BOUTON_SURVOL,
            text_color=theme.TEXTE,
            font=theme.police(15),
            command=lambda: sur_supprimer(livre),
        ).grid(row=0, column=4, rowspan=2, sticky="ne", padx=(4, 10), pady=(8, 0))

        action = sur_emprunter if disponible else sur_retourner
        ctk.CTkButton(
            self,
            text="Emprunter" if disponible else "Retourner",
            width=110,
            height=28,
            corner_radius=4,
            fg_color=theme.BOUTON,
            hover_color=theme.BOUTON_SURVOL,
            text_color=theme.TEXTE,
            border_width=1,
            border_color=theme.BORDURE,
            font=theme.police(12),
            command=lambda: action(livre),
        ).grid(row=2, column=3, sticky="e", padx=(8, 10), pady=(2, 12))


class PlaceholderView(ctk.CTkFrame):
    def __init__(
        self,
        master,
        titre,
        message,
        action_texte=None,
        action=None,
    ):
        super().__init__(master, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        entete = ctk.CTkFrame(self, fg_color="transparent")
        entete.grid(row=0, column=0, sticky="ew", padx=24, pady=(18, 10))
        ctk.CTkLabel(
            entete,
            text="Bibliothèque",
            font=theme.police(30),
            text_color=theme.TEXTE,
            anchor="w",
        ).pack(anchor="w")
        ctk.CTkLabel(
            entete,
            text=titre,
            font=theme.police(13),
            text_color=theme.TEXTE,
            anchor="w",
        ).pack(anchor="w")

        corps = ctk.CTkFrame(self, fg_color="transparent")
        corps.grid(row=1, column=0, sticky="nsew")
        ctk.CTkLabel(
            corps,
            text=message,
            font=theme.police(16),
            text_color=theme.TEXTE_SECONDAIRE,
        ).pack(expand=True)

        if action_texte and action:
            ctk.CTkButton(
                corps,
                text=action_texte,
                width=200,
                height=36,
                corner_radius=4,
                fg_color=theme.BOUTON,
                hover_color=theme.BOUTON_SURVOL,
                text_color=theme.TEXTE,
                border_width=1,
                border_color=theme.BORDURE,
                font=theme.police(13),
                command=action,
            ).pack(pady=(0, 60))
