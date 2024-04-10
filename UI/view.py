import flet as ft
from database import corso_DAO

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # Riga0 Dropdown
        self._ddCorsi = ft.Dropdown(label="Corso", width= 500, hint_text= "Seleziona un corso")
        self.fill_ddCorsi()

        self._btnCercaIscritti = ft.ElevatedButton(text = "Cerca iscritti", on_click= self._controller.handle_CercaIscritti)
        row0 = ft.Row([self._ddCorsi, self._btnCercaIscritti], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row0)

        # Riga1 matricola nome cognome
        # text field for the name
        self.txt_matricola = ft.TextField (label = "matricola", width = 200)
        self.txt_nome = ft.TextField( label="name", width=200, read_only=True)
        self.txt_cognome = ft.TextField(label="cognome", width=200, read_only=True)

        # self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        row1 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)

        # Riga2 bottoni per cerca studente, cerca corsi, iscrivi
        self._btnCercaStudente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_cercaStudenti)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_cercaCorsi)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_Iscrivi)

        row2 = ft.Row([self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def fill_ddCorsi(self):
        corso = corso_DAO.CorsoDao()
        nomi = corso.get_NomeCorso()
        for nome in nomi:
            self._ddCorsi.options.append(ft.dropdown.Option(nome))

