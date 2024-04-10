# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from model.studente import Studente
from database.DB_connect import get_connection

import mysql.connector

class corsoDao:
    @staticmethod
    def get_corsi() -> list[Corso] | None:
        """
        Funzione che legge tutti i corsi nel database
        :return: una lista con tutti i corsi presenti
        """
        cnx = get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT *
                        FROM corso """
            cursor.execute(query)
            for row in cursor:
                result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Nessuna connessione")
            return None

    def handle_cerca_iscritti(codins) -> list[Studente] | None:
        """
            Funzione che recupera una lista con tutti gl istudenti iscritti al corso selezionato
            :param corso: il corso di cui recuperare gli iscritti
            :return: una lista con tutti gli studenti iscritti
            """
        cnx = get_connection()
        result = []

        query = """ select studente.* 
                    from iscrizione, studente
                    where iscrizione.matricola = studente.matricola AND iscrizione.codins = %s  """
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, (codins,))
            for row in cursor:
                result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Could not connect")
            return None

    def handle_iscrivi(matricola, codins) ->bool:
        """
            Funzione che aggiunge uno studente agli iscritti di un corso
            :param matricola: la matricola dello studente
            :param codins: il codice del corso
            :return: True se l-operazione va a buon fine, False altrimenti
        """
        cnx = get_connection()
        query = """ INSERT IGNORE INTO `iscritticorsi`.`iscrizione` 
                    (`matricola`, `codins`) 
                    VALUES(%s,%s) """
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, (matricola,codins,))
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        else:
            print("Could not connect")
            return False