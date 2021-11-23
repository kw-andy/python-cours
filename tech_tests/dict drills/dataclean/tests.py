import unittest

from dataclean import data_csv_opener
from dataclean import data_add_dictionaries
from dataclean import change_string_date


class TestCleaning(unittest.TestCase):
    def test_csv_opener(self):
        headers, final_liste = data_csv_opener("data.csv")
        self.assertEqual(
            headers,
            [
                "emp id",
                "emp_first_name",
                "emp_last_name",
                "emp_job_title",
                "emp_salary",
                "hiredate",
                "departdate",
                "grade",
            ])

        self.assertEqual(final_liste, 
            [['1', 'Joe', 'Bradigan', 'Recruter', '10000', '12/12/01', '10/09/20', 'A'], 
            ['2', 'Joe', 'Justice', 'PO', '10001', '13/12/01', '', 'B'], 
            ['3', 'Brad', 'Dourif', 'Actor', '10002', '14/12/01', '02/07/07', 'A'], 
            ['4', 'Gisèle', 'Chabir', 'Lawyer', '10003', '15/12/01', '', 'A'], 
            ['5', 'Caroline', 'Makanen', 'Linguist', '10004', '16/12/01', '', 'D'], 
            ['6', 'Vladimir', 'Doey', 'Builder', '10005', '17/12/01', '', 'A'], 
            ['7', 'Basile', 'Hervé', 'Geek', '10006', '18/12/01', '14/06/03', 'B'], 
            ['8', 'Voyager', 'Opodo', 'Traveler', '10007', '19/12/01', '', 'E'], 
            ['9', 'Céline', 'Dion', 'Dev', '10008', '20/12/01', '', 'C'], 
            ['10', 'René', 'Canado', 'Designer', '10009', '21/12/01', '25/10/12', 'A'], 
            ['11', 'Vans', 'Land of the Free', 'Graphist', '10010', '22/12/01', '', 'C']])    


    def test_add_dictionaries(self):
                add_dict_dictio = data_add_dictionaries(data_csv_opener("data.csv"))    
                self.assertEqual(add_dict_dictio,
                [{'emp id': '1', 'emp_first_name': 'Joe', 'emp_last_name': 'Bradigan', 'emp_job_title': 'Recruter', 'emp_salary': '10000', 'hiredate': '12/12/01', 'departdate': '10/09/20', 'grade': 'A'}, 
                {'emp id': '2', 'emp_first_name': 'Joe', 'emp_last_name': 'Justice', 'emp_job_title': 'PO', 'emp_salary': '10001', 'hiredate': '13/12/01', 'departdate': '', 'grade': 'B'}, 
                {'emp id': '3', 'emp_first_name': 'Brad', 'emp_last_name': 'Dourif', 'emp_job_title': 'Actor', 'emp_salary': '10002', 'hiredate': '14/12/01', 'departdate': '02/07/07', 'grade': 'A'}, 
                {'emp id': '4', 'emp_first_name': 'Gisèle', 'emp_last_name': 'Chabir', 'emp_job_title': 'Lawyer', 'emp_salary': '10003', 'hiredate': '15/12/01', 'departdate': '', 'grade': 'A'}, 
                {'emp id': '5', 'emp_first_name': 'Caroline', 'emp_last_name': 'Makanen', 'emp_job_title': 'Linguist', 'emp_salary': '10004', 'hiredate': '16/12/01', 'departdate': '', 'grade': 'D'}, 
                {'emp id': '6', 'emp_first_name': 'Vladimir', 'emp_last_name': 'Doey', 'emp_job_title': 'Builder', 'emp_salary': '10005', 'hiredate': '17/12/01', 'departdate': '', 'grade': 'A'}, 
                {'emp id': '7', 'emp_first_name': 'Basile', 'emp_last_name': 'Hervé', 'emp_job_title': 'Geek', 'emp_salary': '10006', 'hiredate': '18/12/01', 'departdate': '14/06/03', 'grade': 'B'}, 
                {'emp id': '8', 'emp_first_name': 'Voyager', 'emp_last_name': 'Opodo', 'emp_job_title': 'Traveler', 'emp_salary': '10007', 'hiredate': '19/12/01', 'departdate': '', 'grade': 'E'}, 
                {'emp id': '9', 'emp_first_name': 'Céline', 'emp_last_name': 'Dion', 'emp_job_title': 'Dev', 'emp_salary': '10008', 'hiredate': '20/12/01', 'departdate': '', 'grade': 'C'}, 
                {'emp id': '10', 'emp_first_name': 'René', 'emp_last_name': 'Canado', 'emp_job_title': 'Designer', 'emp_salary': '10009', 'hiredate': '21/12/01', 'departdate': '25/10/12', 'grade': 'A'}, 
                {'emp id': '11', 'emp_first_name': 'Vans', 'emp_last_name': 'Land of the Free', 'emp_job_title': 'Graphist', 'emp_salary': '10010', 'hiredate': '22/12/01', 'departdate': '', 'grade': 'C'}]
                )

    def test_change_string_to_date(self):
        string_to_date = change_string_date(data_add_dictionaries(data_csv_opener("data.csv")))    
        date_to_pick = string_to_date
        hiredate = ''
        for key,elt in date_to_pick[0].items():
            if key == 'hiredate':
                hiredate = elt
        self.assertEqual(hiredate,'12-12-2001')             


if __name__ == "__main__":
    unittest.main()



