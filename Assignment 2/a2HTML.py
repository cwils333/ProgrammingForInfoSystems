#
# INF1340, Section LEC0101
# Assingment 2 - Due 2018-11-19
# Wilson, Courtney
#
# HTML Table Extraction Program
# v.1.4 - 2018-11-18
# Compatibale with Python version 3.7
# Source File: a2HTML.py
#

import sys
import requests
import re #import statement for regular expressions

def get_HTML_lines(filename):
    """ (str) -> str
    Returns the <raw_string> that is retrieved from the browser via a 'get' request
    @type filename: str
    @rtype: str
    >>>Input = 'https://www.abc.com/example.html'
    https://www.abc.com/example.html
    """
    #Sends a 'get' request to get the HTML from the browser 
    http_object = requests.get(filename)  
    raw_html = http_object.content
    #Turns the 'raw_html' and decodes it to 'utf-8', making it readable and gives us the ability to work with it later on. 
    raw_string = raw_html.decode('utf-8')

    return raw_string

def extract_head(raw_string):
    """ (str) -> str
    Extracts the header from the <h.*?></h.*?> tags within the HTML mark up
    @type raw_string: str
    @rtype: str
    """
    #Using regular expressions, the header (located in <h1>,<h2>,... tags etc) is extracted from the the HTML.
    #re.findall takes advantage of a built in function from the 're' module, which finds all instances of a specified wildcard
    #<.h*?> </h.*?> is the wild card to find all 'header' tags within the HTML
    #(.+?) is the wild card to access the contents in between the two header tags

    header = re.findall(r"<h.*?>(.+?)</h.*?>",raw_string)[0]
    return header
                 
def extract_table(raw_string):
    """ (str) -> str
    Exgtracts the table from the <table></table> tags within the HTML mark up
    @type raw_string: str
    @rtype: str
    """
    #re.I : Short for 'IGNORECASE' in the re module. 
    #re.M : Short for 'MULTILINE' in the re module.
    #re.S : Short for 'DOTALL'
    #To read up on re.I, re.M, & re.S, visit the Python API (https://docs.python.org/2/library/re.html) for a better understanding of these! 

    #Similar to the extract_head, the re.findall uses the wildcard (.*?) to extract the content from the <table></table> tags
    table = re.findall(r"<table>(.*?)</table>",raw_string,re.M|re.I|re.S)
    return table
    
def extract_rows(table):
    """ (str) -> str
    Extracts the rows within the table, in the <tr></tr> tags in the HTML markup
    @type table: str
    @rtype: str
    """
    table_string = " " #A empty string, so each table row can be appended to as the 'table' variable is iterated through
    
    for i in table: #The for loop to go through the HTML table to access each row, and append it to 'table_str', making it a string
    #Making it into a string will make the rows easier to work with when using the re module        
        table_string = table_string + i
    row = re.findall(r"<tr>(.*?)</tr>",table_string,re.M | re.I | re.S) #Stripping the <tr></tr> tags, in the same way as the table and header 
    return row

def extract_cells(row):
    """ (str) -> str
    Extracts the data from the <td></td> in the HTML markup
    @type row: str
    @rtype: str
    >>> Input = 
    """
    row_list = [] #List to hold the data from each row 

    for i in row:
        cell = i.strip().replace("<td>","").replace("</td>","").splitlines() #Replace the <td></td> tags with empty spaces
        #The second for loop, is looping through the 'inner' list, extracting each cell that is within each row of the table
        for c in range(len(cell)):
            cell[c] = cell[c].strip() + " "
        row_list.append(cell)
    return row_list
        
    
def write_output_py_file(header,table_str,fileOutputName):
    """ (str, str, str) -> None
    Creates and write to a new .py, displaying the extracted HTML data
    @type header: str
    @type table_str: str
    @type fileOutputName: str
    @rtype: None
    """
    INDENT = "  " #Variable putting the proper indents in the written file 
    TABLE_ASSIGNMENT = table_str
    FILE_OUTPUT_NAME = fileOutputName + ".py" 
    
    py_file = open(FILE_OUTPUT_NAME,"w") #Opening/creating the file for writing 
    py_file.write("#\n")
    py_file.write("# INF1340, Section LEC0101\n") #Boilerplate comment
    py_file.write("# Assingment 2 - Due 2018-11-19\n") #Boilerplate comment
    py_file.write("#\n")
    py_file.write("# HTML Table Extraction Program - Output .py Program\n") #Boilerplate comment
    py_file.write("# Compatibale with Python version 3.7\n") #Boilerplate comment
    py_file.write("#\n")
    py_file.write("\n")

    py_file.write("if __name__ == '__main__':\n") #Creation of the 'main' function 
    py_file.write(INDENT + "print('" + header + "')\n") #Print statement for the header of the HTML file
    py_file.write(INDENT + "print(' ')\n")

    py_file.write(INDENT + 'print("""'+ TABLE_ASSIGNMENT + '""")') #Print statement for the table
    #Using the triple quotes, the table contents will be able to be printed on different lines   
    py_file.close()
      
def display_table(row_list):
    """ (str) -> str
    Displays the table data that was extracted from the HTML markup 
    @type row_list: str
    @rtype: str
    """
    table_str = "" #A string variable to append each cell and row onto for future use
    
    for row in row_list:
        row_str = ""
        for cell in range(len(row)):
            row_str = row_str + (row[cell])
        table_str = table_str + row_str + """\n"""

    return table_str

if __name__ == '__main__':
    filename = sys.argv[1]
    fileOutputName = filename.rsplit('/',1)[-1].replace('.html',"") #Stripping away the rest of the URL query string for the output filename
    raw_string = get_HTML_lines(filename)

    header = extract_head(raw_string)
    table = extract_table(raw_string)
    row = extract_rows(table)
    row_list = extract_cells(row)
    table_str = display_table(row_list)
    write_output_py_file(header,table_str,fileOutputName)
    

    
    
    
