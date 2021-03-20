# pip install Pyrogram TgCrypto

from pyrogram import Client

api_id = 3094422

api_hash = "78feeeaf96a36b19b55ab100836b0400"

with Client(":memory:", api_id, api_hash) as app, open("session.txt", "w+") as s_file:

    session_string = app.export_session_string()

    s_file.write(session_string)

    print("Session string has been saved to session.txt")

    print(session_string)
