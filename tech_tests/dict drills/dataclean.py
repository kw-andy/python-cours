data = """
all that stuff that does not matter but it is good title though
emp id,emp_first_name,emp_last_name,emp_job_title,emp_salary,hiredate,departdate,grade
1,Joe,Bradigan,Recruter,10000,12/12/01,10/09/20,A
2,Joe,Justice,PO,10001,13/12/01,,B
3,Brad,Dourif,Actor,10002,14/12/01,02/07/07,A
4,Gisèle,Chabir,Lawyer,10003,15/12/01,,A
5,Caroline,Makanen,Linguist,10004,16/12/01,,D
6,Vladimir,Doey,Builder,10005,17/12/01,,A
7,Basile,Hervé,Geek,10006,18/12/01,14/06/03,B
8,Voyager,Opodo,Traveler,10007,19/12/01,,E
9,Céline,Dion,Dev,10008,20/12/01,,C
10,René,Canado,Designer,10009,21/12/01,25/10/12,A
11,Vans,Land of the Free,Graphist,10010,22/12/01,,C
"""

from datetime import datetime

def data_cleaning(data):
    raw_data = data.split("\n")
    fin_raw_data = raw_data[1:]
    headers = fin_raw_data[1].split(',')
    liste = []
    dictio = {}
    final_liste = []
    for line in fin_raw_data[2:]:
        data_line = line.split(',')
        liste.append(data_line)
    for things in liste:
        for idx,value in enumerate(things):
            dictio[headers[idx]] = value
        final_liste.append(dictio.copy())
    return final_liste              

def change_string_date(data):
    input = data
    for idx,values in enumerate(input):
        for keys, val in values.items():
            if (keys == 'hiredate' or keys == 'departdate'):
                if values[keys] not in ['',None]:
                    values[keys] = datetime.strptime(val,'%d/%m/%y').strftime('%d-%m-%Y')
    return input            


if __name__ == "__main__":
    change_string_date(data_cleaning(data))    



    


