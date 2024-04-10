# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente
class studenteDao:
    def handle_cercaStudente(matricola) -> list[Studente] | None:
        """
            Funzione che data una matricola ricerca nel database lo studente corrispondente (se presente)
            :param matricola: la matricola dello studente da ricercare
            :return: uno studente, se presente
        """
        cnx = get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT * 
                        FROM studente 
                        WHERE matricola = %s """
            cursor.execute(query, (matricola,))
            row = cursor.fetchone()
            if row is not None:
                result = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
            else:
                result = None
            cursor.close()
            cnx.close()
            return result
        else:
            print("Nessuna connessione")
            return None

    # il prof l'ha inserita in corso_DAO
    def handle_cercaCorsi(matricola) -> list[Corso]:
        """
            Funzione che data una matricola ricerca nel database i corsi frequentati
            :param matricola: la matricola dello studente da ricercare
            :return: una lista di corsi
        """
        cnx = get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT * 
                        FROM studente s, iscrizione i, corso c
                        WHERE s.matricola = i.matricola and c.codins =i.codins and s.matricola = %s """
            cursor.execute(query, (matricola,))
            for row in cursor:
                result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Nessuna connessione")
