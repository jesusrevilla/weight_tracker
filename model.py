import sqlite3
from sqlite3 import Error


def get_weight(user_id):
    results_lst = []
    try:
        con = sqlite3.connect("wtracker.db")
        cursorObj = con.cursor()
        cursorObj.execute(
            "SELECT * FROM weights where user_id = :user_id", {"user_id": user_id}
        )
        rows = cursorObj.fetchall()
        for row in rows:
            results_dict = {}
            results_dict["weight"] = row[2]
            results_dict["time_stamp"] = row[3]
            results_lst.append(results_dict)
    except Error:
        print(Error)
    finally:
        con.close()
    return results_lst


def get_user(username):
    results_lst = []
    try:
        con = sqlite3.connect("wtracker.db")
        cursorObj = con.cursor()
        cursorObj.execute(
            "SELECT * FROM users where username = :username", {"username": username}
        )
        rows = cursorObj.fetchall()
        for row in rows:
            results_dict = {}
            results_dict["id"] = row[0]
            results_dict["username"] = row[1]
            results_dict["hash"] = row[2]
            results_lst.append(results_dict)
    except Error:
        print(Error)
    finally:
        con.close()
    return results_lst


def register_user(username, hash):
    try:
        con = sqlite3.connect("wtracker.db")
        cursorObj = con.cursor()
        sql_str = "INSERT INTO users(username, hash) VALUES (:username, :hash)"

        cursorObj.execute(sql_str, {"username": username, "hash": hash})
        con.commit()
    except Error:
        print(Error)
    finally:
        con.close()
