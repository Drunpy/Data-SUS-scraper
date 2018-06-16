from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

driver = webdriver.Chrome()
site = 'http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinasc/cnv/nvuf.def'
driver.get(site)

seletor_anos= Select(driver.find_element_by_id('A'))

#Laço pra criar o nome dos arquivos que vão guardar os textos
for i in seletor_anos.options:
    year = i.text
    with open(year[:-5]+'.csv', 'w') as txt:
        pass
    txt.close()

for i in seletor_anos.options:
    try:
        ano = i.text
        print('Obtendo dados de {}'.format(ano))
    except:
        pass

    #Seleciona "Conteudo"  
    seletorc = Select(driver.find_element_by_id('I'))
    seletorc.deselect_all()
    selec = seletorc.select_by_visible_text('Nascim p/ocorrênc')

    #Seleciona "Linha"
    seletorl = Select(driver.find_element_by_id('L'))
    selecl = seletorl.select_by_visible_text('Instrução da mãe')

    #Seleciona "Coluna"
    seletorj = Select(driver.find_element_by_id('C'))
    selecj = seletorj.select_by_visible_text('Idade da mãe')

    #Seleciona a opção "separar por ';'"
    seletorop = driver.find_element_by_xpath("//input[@value = 'prn']")
    seletorop.click() 

    #Abre a página com os dados
    dar_input = driver.find_element_by_name('mostre')
    dar_input.click()

    #Copiando e salvando o text
    copiador = driver.find_element_by_tag_name('pre')
    with open('{}.csv'.format(ano[:-5]), 'w') as txt:
        txt.write(copiador.text)

    print('Compilação do ano {} ... OK'.format(ano))
    
    

    
