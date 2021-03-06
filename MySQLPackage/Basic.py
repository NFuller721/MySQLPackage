def Create(Database, Cursor, table, dict, log=False):
    SQLStatement = ""
    columns = []
    values = []
    for column, value in dict.items():
        columns += [column]
        values += [f"'{value}'"]

    SQLStatement = f"INSERT INTO {table} ({','.join(columns)}) VALUES ({','.join(values)})"
    if log:
        print(SQLStatement)
    Cursor.execute(SQLStatement)
    Database.commit()

def Read(Database, Cursor, table, id='All', columns='All', log=False):
    SQLStatement = ""
    if columns == 'All':
        if id == 'All':
            SQLStatement = f"SELECT * FROM {table}"
        elif type(id) == int:
            SQLStatement = f"SELECT * FROM {table} WHERE id={id}"
        else:
            raise ValueError()
    else:
        if id == 'All':
            SQLStatement = f"SELECT {','.join(columns)} FROM {table}"
        elif type(id) == int:
            SQLStatement = f"SELECT {','.join(columns)} FROM {table} WHERE id={id}"
        else:
            raise ValueError()
    if log:
        print(SQLStatement)
    Cursor.execute(SQLStatement)
    Resp = Cursor.fetchall()

    return Resp

def Update(Database, Cursor, table, id, dict, log=False):
    SQLStatement = ""
    items = []
    for column, value in dict.items():
        items += [f"{column} = '{value}'"]
    if type(id) == int:
        SQLStatement = f"UPDATE {table} SET {', '.join(items)} WHERE id={id}"
    else:
        raise ValueError()

    if log:
        print(SQLStatement)

    Cursor.execute(SQLStatement)
    Database.commit()

def Delete(Database, Cursor, table, id='All', log=False):
    SQLStatement = ""

    if id == 'All':
        SQLStatement = f"DELETE FROM {table}"
    elif type(id) == list:
        ids = []
        for i in id:
            ids += [i]
        SQLStatement = f"DELETE FROM {table} WHERE id IN ({', '.join([str(i) for i in id])})"
    elif type(id) == int:
        SQLStatement = f"DELETE FROM {table} WHERE id={id}"
    else:
        raise ValueError()

    if log:
        print(SQLStatement)

    Cursor.execute(SQLStatement)
    Database.commit()

    ResetId(Database=Database, Cursor=Cursor, table=table)

def ResetId(Database, Cursor, table):
    ResetIdQuery = [
        "set @autoid :=0",
        f"update {table} set id = @autoid := (@autoid+1)",
        f"alter table {table} Auto_Increment = 1"
    ]

    for ResetLine in ResetIdQuery:
        Cursor.execute(ResetLine)
    Database.commit()
