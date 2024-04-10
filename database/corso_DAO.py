# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection

import mysql.connector

class CorsoDao:


    def get_NomeCorso(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = """ SELECT *
            FROM corso """
        cursor.execute(query)
        result = []
        for row in cursor:

            result.append(f" {row["nome"]} ({row["codins"]})")
        cursor.close()
        cnx.close()
        return result
