# -*- coding: utf-8 -*-

# FRAME
#verificaciones
import unittest
from src.functions.Functions import Functions as Selenium


class Test_013(Selenium, unittest.TestCase):


    def setUp(self):
        
        self.CURSOR = Selenium.pyodbc_query(self, "SELECT * FROM usuarios")
        
        Selenium.abrir_navegador(self, "https://www.google.com/?hl=es")
        Selenium.get_json_file(self, "google")

    def test_013(self):
            
        fecha = Selenium.textDateEnvironmentReplace(self, "today")
    
        
        Selenium.get_elements(self, "txt_buscar").send_keys(fecha)
        
        
        Selenium.esperar(5)
                  
      

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    