import sqlite3 as sq


from aiogram import types

import admins
from create_bot import dp, bot

def db_start():
    global base, cur
    base = sq.connect("cafe.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY)')
    base.execute('CREATE TABLE IF NOT EXISTS master_at_work(master_id TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS bron(user TEXT, time TEXT, user_name TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS all_masters(id TEXT, photo TEXT, about TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS spam(text TEXT, photo TEXT)')
    base.execute("CREATE TABLE IF NOT EXISTS tells(id INTEGER, words TEXT, code TEXT, oke TEXT)")
    base.execute("CREATE TABLE IF NOT EXISTS korzina(id INTEGER, tov TEXT, price INTEGER)")
    base.commit()


async def user_add(message):
    try:
        cur.execute("INSERT INTO users VALUES (?)", (message.from_user.id,))
    except:
        pass
    base.commit()

async def set_master(message):
    try:
        cur.execute("INSERT INTO master_at_work VALUES (?)", (message.from_user.id,))
    except:
        pass
    base.commit()

async def master():
    nobr = cur.execute("SELECT MAX(ROWID) FROM master_at_work").fetchall()
    tobr = cur.execute(f"SELECT master_id FROM master_at_work WHERE ROWID == {nobr[0][0]}").fetchall()
    return (tobr[0][0])

async def bron(message):
    cur.execute("INSERT INTO bron VALUES (?, ?, ?)", (message.from_user.id, message.text, message.from_user.username))
    base.commit()
    nobr = cur.execute("SELECT MAX(ROWID) FROM bron").fetchall()
    tobr = cur.execute(f"SELECT time FROM bron WHERE ROWID == {int(nobr[0][0])} ").fetchall()
    uobr = cur.execute(f"SELECT user FROM bron WHERE ROWID == {int(nobr[0][0])} ").fetchall()
    name = cur.execute(f"SELECT user_name FROM bron WHERE ROWID == {int(nobr[0][0])} ").fetchall()
    return (nobr, tobr, uobr, name)

async def bronselect(message):
    user = cur.execute(f"SELECT user FROM bron WHERE ROWID == {message.text} ").fetchall()
    return user

async def spam(data):
    cur.execute("INSERT INTO spam VALUES (?, ?)", (data["text"], data["photo"]))
    base.commit()
    last_spam_num = int(cur.execute("SELECT MAX(ROWID) FROM spam").fetchall()[0][0])
    sp_t = cur.execute(f"SELECT text FROM spam WHERE ROWID == {last_spam_num} ").fetchall()[0][0]
    sp_ph = cur.execute(f"SELECT photo FROM spam WHERE ROWID == {last_spam_num} ").fetchall()[0][0]
    users = cur.execute("SELECT * FROM users").fetchall()
    for i in users:
        try:
            await bot.send_message(int(i[0]), sp_t)
            await bot.send_photo(int(i[0]), sp_ph)
        except:
            pass


async def add_photo(message):
    cur.execute("INSERT INTO all_masters VALUES (?, ?, ?)",
                (message.from_user.id, message.photo[0].file_id, None))
    base.commit()


async def add_name(message):
    last_master_num = int(cur.execute("SELECT MAX(ROWID) FROM all_masters").fetchall()[0][0])
    cur.execute(f"UPDATE all_masters SET about == ? WHERE ROWID == {last_master_num}", (f"{message.text}",))
    base.commit()


async def tells_to_base(message: types.Message):
    cur.execute("INSERT INTO tells VALUES (?, ?, ?, ?)",
                (message.from_user.id, message.text, None, None))
    base.commit()



async def get_max_tell() -> int:
    return int(cur.execute("SELECT MAX(ROWID) FROM tells").fetchall()[0][0])


async def get_user_tell(code: int):
    return cur.execute(f"SELECT id FROM tells WHERE ROWID == {code}").fetchall()[0][0]


async def tells_of_another():
    bad = "bad"
    words: list = [i[1] for i in cur.execute(f"SELECT * FROM tells").fetchall() if i[3] != "bad"]
    return words


async def change_to_bad(number, user):
    cur.execute(f"UPDATE tells SET oke == ? WHERE ROWID == {number}", ("bad",))
    base.commit()
    await bot.send_message(user, "Added to trash")


async def get_all_users_with_code_tell() -> list:
    users: list = [i[0] for i in cur.execute("SELECT * FROM tells").fetchall() if i[2]]
    return users


async def give_code(user: int, promo: str):
    cur.execute(f"UPDATE tells SET code == ? WHERE id == {user}", (f"{promo}",))
    base.commit()

"""async def add_zak(user: int, tov: str):
    real_tov = goods.gods[tov]
    cur.execute("INSERT INTO korzina VALUES (?, ?, ?)",
                (user, real_tov[0], real_tov[1]))
    base.commit()"""


async def get_tov_from_korzina(user: int):
    return cur.execute(f"SELECT ROWID, * FROM korzina WHERE id== {user}").fetchall()


async def clear_korzinu(user: int):
    cur.execute(f"DELETE FROM korzina WHERE id == {user}")
    base.commit()