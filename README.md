# MySQL
This is a MySQL Package that allows for simple operations

# What is required
 - mysql-connector

# Package Installation
To install this package cd into the package and run
`python setup.py develop`

# Utilization

  - Create
      Args:
       Database: MySqlConnector Database Object
       Cursor: MySqlConnector Cursor Object
       table: String indicating what table to use
       dict: What information are we putting in (eg. {"ColumnName": "Data"})

   - Read
     Args:
       Database: MySqlConnector Database Object
       Cursor: MySqlConnector Cursor Object
       table: String indicating what table to use
       id: What id to pick from table - (default = 'All')
       columns: What columns to return - (default = 'All')

   - Update
       Args:
        Database: MySqlConnector Database Object
        Cursor: MySqlConnector Cursor Object
        table: String indicating what table to use
        id: What id are we using
        dict: What information are we putting in (eg. {"ColumnName": "Data"})

  - Delete
      Args:
       Database: MySqlConnector Database Object
       Cursor: MySqlConnector Cursor Object
       table: String indicating what table to use
       id: What id are we using - (default = 'All')
