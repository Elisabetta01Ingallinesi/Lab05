import flet as ft
from model.corso import Corso

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # self dizionario corsi
        self._id_map_corsi = {}
        # il corso selezionato nel menù a tendina
        self.corso_selezionato = None


    def leggi_corso(self, e):
        self.corso_selezionato = self._view._ddCorsi.value

    # per popolare un menù a tendina prendendo le informazioni da un database
    def populate_ddCorsi(self):
        for corso in self._model.get_corsi():
            self._id_map_corsi[corso.codins] = corso
            self._view._ddCorsi.options.append(ft.dropdown.Option(key = corso.codins, text = corso))
        self._view.update_page()

    def handle_CercaIscritti(self, e):
        if self.corso_selezionato is None:
            self._view.create_alert("Selezionare un corso")
            return
        iscritti = self._model.handle_cerca_iscritti(self.corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problema nella connessione!")
            return
        self._view.txt_result.controls.clear()
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti al corso"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{studente}"))
            self._view.update_page()

    def handle_cercaStudente(self,e):
        self._view.txt_result.controls.clear()
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            return
        studente = self._model.handle_cercaStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente!")
        else:
            self._view.txt_nome.value = f"{studente.nome}"
            self._view.txt_cognome.value = f"{studente.cognome}"

        self._view.update_page()

    def handle_cercaCorsi(self,e):
        self._view.txt_result.controls.clear()
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            return
        corsi = self._model.handle_cercaCorsi(matricola)
        numCorsi = len(corsi)
        self._view.txt_result.controls.append(ft.Text(f"Risultano {numCorsi} corsi"))
        for corso in corsi:
            self._view.txt_result.controls.append(ft.Text(f"{corso.nome} {corso.codins}"))
        self._view.update_page()

    def handle_Iscrivi(self,e):
        codiceCorso = self._view._ddCorsi.value
        if codiceCorso is None:
            self._view.create_alert("Selezionare un corso")
            return
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            return
        studente = self._model.handle_cercaStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente!")
            return

        newIscrizione = self._model.handle_iscrivi(matricola, codiceCorso)
        if newIscrizione:
            self._view.txt_result.controls.append(ft.Text("Iscrizione avvenuta con successo"))
        else:
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))
        self._view.update_page()

