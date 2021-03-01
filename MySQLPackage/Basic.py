def Create(Database, Cursor, table, dict):
    columns = []
    values = []
    for column, value in dict.items():
        columns += [column]
        values += [f"'{value}'"]

    SQLStatement = f"INSERT INTO {table} ({','.join(columns)}) VALUES ({','.join(values)})"
    Cursor.execute(SQLStatement)

def Read(Database, Cursor, table, id='All', columns='All'):
    if columns == 'All':
        if id == 'All':
            SQLStatement = f"SELECT * FROM {table}"
        elif type(id) == int:
            SQLStatement = f"SELECT * FROM {table} WHERE id={id}"
        else:
            raise ValueError()
    else:
        if id == 'All':
            SQLStatement = f"SELECT ({','.join(columns)}) FROM {table}"
        elif type(id) == int:
            SQLStatement = f"SELECT ({','.join(columns)}) FROM {table} WHERE id={id}"
        else:
            raise ValueError()

    Cursor.execute(SQLStatement)
    Resp = Cursor.fetchall()

    return Resp

def Update(Database, Cursor, table, id, dict):
    items = []
    for column, value in dict.items():
        items += [f"{column} = '{value}',"]
    if type(id) == int:
        SQLStatement = f"UPDATE {table} {','.join(items)} WHERE id={id}"
    else:
        raise ValueError()

    Cursor.execute(SQLStatement)

def Delete(Database, Cursor, table, id):
    if type(id) == int:
        SQLStatement = f"DELETE FROM {table} WHERE id={id}"
    else:
        raise ValueError()

    Cursor.execute(SQLStatement)
