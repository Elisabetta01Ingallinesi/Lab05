from database.corso_DAO import corsoDao
from database.studente_DAO import studenteDao
class Model:
    def __init__(self):
        pass

    def get_corsi(self):
        return corsoDao.get_corsi()

    def handle_cerca_iscritti(self, corso):
        return corsoDao.handle_cerca_iscritti(corso)

    def handle_cercaStudente(self, matricola):
        return studenteDao.handle_cercaStudente(matricola)

    def handle_cercaCorsi(self, matricola):
        return studenteDao.handle_cercaCorsi(matricola)

    def handle_iscrivi(self, matricola, codins):
        return corsoDao.handle_iscrivi(matricola, codins)