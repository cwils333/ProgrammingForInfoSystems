#
# INF1340, Section L101
# Assignment 3 - Due 2018-12-07
# Wilson, Courtney
#
# MySQL Client Program
# v.1.3 - 2018-12-03
# Compatible with Python Version 3.7
# Source File: a3-courtney.py
#

import mysql.connector # Import MYSQL connector to allow for connection to Database
import tkinter as tk #Module to allow use for Tkinter GUI. <tk> will be the variable used to establish widgets throughout the program

def get_query():
    """ (None) -> str
    Returns the <query.get> that is inputted by the user. User can choose
    the default value ('show tables;') or input their own custom query
    @rtype: str
    >>>Input = 'Select * FROM gene LIMIT 15;'
    Select * FROM gene LIMIT 15;
    >>>Input = 'show tables;'
    show tables;
    """

    DEFAULT_QUERY_STRING = "show tables;" #The default query that will be used if user does not have a custom one

    root = tk.Tk() #Creation of the empty 'tk' GUI 
    query = tk.StringVar() #Variable that will store the chosen query; default or custom
    
    tk.Label(root, text="Enter Query").pack() #Label widget for the Tkinter GUI
    tk.Radiobutton(root,text="Default", variable=query, value = DEFAULT_QUERY_STRING).pack() #Radio button widget for the deafault query choice 
    tk.Label(root, text="Custom Query").pack() #Label widget for the entry box 
    tk.Entry(root,text="Custom Query", textvariable=query).pack() #Text entry box for if the user wants to submit a custom query
    tk.Button(root, text="Okay",command = root.destroy).pack() #Okay button; command will destroy the Tkinter GUI
 
    root.mainloop()
    query = query.get()
    return query #Returns the choosen query from the user 

def retrieve_data(query):
    """ str -> dictionary
    Returns the <table_data> that contains the row data, column names,
    and column types that are all retrieved from the <query> that was
    inputted previsouly be the user.
    @type query: str
    @rtype: dictionary
    >>> 'show tables;'
    {"ColNames" : [Tables_in_gorilla_gorilla_core_52_1] ColType: <class 'str'>, "RowData" : [alt_allele,analysis,analysis_description,assembly,assembly_exception,attrib_type,coord_system,density_feature,density_type,ditag]}
    >>> 'select * from gene limit 3'
    {"ColNames":[gene_id,biotype,analysis_id,seq_region_id,seq_region_start,seq_region_end,seq_region_strand,display_xref_id,source,status,description,is_current,canonical_transcript_id,canonical_annotation],
    "ColType":[<class 'int'>,<class 'str'>,<class 'int'>,<class 'int'>,<class 'int'>,<class 'int'>,<class 'int'>,<class 'NoneType'>,<class 'str'>,<class 'str'>,<class 'NoneType'>,<class 'int'>,<class 'int'>,<class 'NoneType'>],
    "RowData": [(1, 'protein_coding', 34, 1977660, 249, 3625, 1, None, 'ensembl', 'NOVEL', None, 1, 1, None),(2, 'protein_coding', 34, 1984141, 13024, 27781, 1, 213692, 'ensembl', 'KNOWN_BY_PROJECTION', 'RUN and FYVE domain-containing protein 4  [Source:UniProtKB/Swiss-Prot;Acc:Q6ZNE9]', 1, 2, None),(3, 'protein_coding', 34, 1984781, 25318, 299370, 1, 209026, 'ensembl', 'KNOWN_BY_PROJECTION', 'Dynein heavy chain 9, axonemal (Axonemal beta dynein heavy chain 9)(Ciliary dynein heavy chain 9) [Source:UniProtKB/Swiss-Prot;Acc:Q9NYC9]', 1, 3, None)] }
    """

    HOST = 'ensembldb.ensembl.org'
    USER = 'anonymous'
    PASSWORD = ''
    DATABASE = 'gorilla_gorilla_core_52_1'

    row_data = [] #List that will hold a list of each data row in the SQL table
    column_names = [] #List that will hold the names of each column in the SQL table
    column_types = [] #List that will hold the column types in the SQL table
    
    cnx  =  mysql.connector.connect( host = HOST,
                                         user = USER, password = PASSWORD,
                                         database = DATABASE)
    cursor = cnx.cursor(buffered=True)

    cursor.execute(query)

    for name in cursor.description: #Populates the column_names list
        column_names.append(name[0])

    for row in cursor: #Populates the row_data list
        row_data.append(row)

    for c_type in row_data[0]: #Populates the column_types list 
        column_types.append(type(c_type))
    
    table_data = {"ColNames" : column_names, "ColType" : column_types, "RowData" : row_data}
          
    cnx.close() #Closing the SQL database connection
    cursor.close() #Closing the SQL database connection
    return table_data #Return a dictionary with the colomn names, column types, and row data from the SQL table

def summarize_data(table_data):
    """ dictionary -> (None)
    Prints out the result summary from the query to the user. Prints out
    the number of rows that were retrieved, the number of columns,
    the name of all the columns, as well as the first ten rows of the table.
    @type table_data: dictionary
    @rtype: None
    """
    print("Result Summary")
    row_num = len(table_data["RowData"]) #Total number of rows that were retrieved 
    print("Total number of Rows: " + str(row_num))
    col_num = len(table_data["ColNames"]) #Total number of columns that were retrieved
    print("Total number of Columns: " + str(col_num))
    print("Column Names: ")

    for name in table_data["ColNames"]: #Printing the column names from the column name list
        print(name)
    print("\n")

    print("Column Types: ")

    for t in table_data["ColType"]: #Printing the column types from the column type list
        print(t)
    print("\n")
    
    print("First 10 Rows of Query Result:\n")
    if row_num < 10: #Checking if more then 10 rows were retrieved from the query result
    #If there are less then 10 rows from the query results, print all the rows to the user
           for row in table_data["RowData"]:
               print(row)
    else:
    #If there are more then 10 rows from the query result, only print the first 10 rows.
        count = 0
        while count < 10:
            for i in table_data["RowData"][count]:
                print(str(i) + " | ", end='')
            print("\n")
            count = count + 1

    
if __name__ == '__main__':
    try:                                    ##
        query = get_query()
        table_data = retrieve_data(query)
        summarize_data(table_data)
    except:                                 ##
        print("Connection Failed. Please Exit & Start Again")
        query = None
        table_data = None
        

   
    
    
    
