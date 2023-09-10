from selenium.webdriver.common.by import By
from selenium import webdriver
import db as conec
libro_consultado = input("Ingrese el tema del libro--> ")
driver = webdriver.Chrome()
driver.get("https://www.scielo.org/")
cuadro_busqueda=driver.find_element(by=By.CSS_SELECTOR, value="#searchForm > div > input[type=text]")
cuadro_busqueda.send_keys(libro_consultado)
boton_busqueda=driver.find_element(by=By.CSS_SELECTOR, value="#searchForm > div > a.btn.btn-default.btn-input")
boton_busqueda.click()
base=conec.cadena()
print("Libros Extraidos de www.scielo.org")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
lista=driver.find_elements(by=By.CSS_SELECTOR, value="#ResultArea > div.results>div")
for i in lista:
    try:
        nombre=i.find_element(By.CSS_SELECTOR, value="#ResultArea > div.results>div>div>div>a>strong").text
        autor= i.find_element(By.CSS_SELECTOR, value="#ResultArea > div.results>div>div>div>a.author").text
        revista=i.find_element(By.CSS_SELECTOR, value="#ResultArea > div.results>div>div>div>span.dropdown").text
        print("Nombre: ",nombre)
        print("Autor: ", autor)
        print("Revista: ", revista)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        libro = {
            "name": nombre,
            "author": autor,
            "magazine": revista}
        j = base.get_collection(libro_consultado)
        j.insert_one(libro)
    except Exception as e:
        print("Error al exraer datos de www.scielo.org")
print("Todos los Libros se subieron a Mongo")
driver.close()