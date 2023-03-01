''' 
O código é responsável por ler arquivos XML em um diretório
específico, verificar o valor do elemento tPag em cada arquivo e, 
em seguida, mover os arquivos para um dos dois diretórios, 
dependendo do valor do elemento tPag. Se o valor for '01', 
o arquivo será movido para a pasta 'dinheiro', caso contrário, 
será movido para a pasta 'cartoes' ou 'outros'.
'''
import shutil
import os
import xml.etree.ElementTree as ET

# Especifica o diretório onde estão os arquivos XML
DIRETORIO = r"C:\Users\Downloads\codes\python\organizadorXml\Emitidas"

# Loop pelos arquivos no diretório
for arquivo in os.listdir(DIRETORIO):
    if arquivo.endswith('.xml'):  # Verifica se é um arquivo XML
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(DIRETORIO, arquivo)

        # Lê o arquivo XML
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()

        # Obtém o nome do arquivo
        nome_arquivo = 'NFe' + \
            root.find(
                ".//{http://www.portalfiscal.inf.br/nfe}nNF").text + '.xml'

        # Verifica o valor do elemento tPag
        tPag = root.find(".//{http://www.portalfiscal.inf.br/nfe}tPag").text
        if tPag == '01':
            DESTINO = r"C:\Users\Downloads\codes\python\organizadorXml\notas separadas\dinheiro"
        elif tPag == '03':
            DESTINO = r"C:\Users\Downloads\codes\python\organizadorXml\notas separadas\cartoes\credito"
        elif tPag == '04':
            DESTINO = r"C:\Users\Downloads\codes\python\organizadorXml\notas separadas\cartoes\debito"
        else:
            DESTINO = r"C:\Users\Downloads\codes\python\organizadorXml\notas separadas\outros"

        # Move o arquivo para o destino correto
        shutil.move(caminho_arquivo, os.path.join(DESTINO, nome_arquivo))
# Exibe uma mensagem de conclusão quando a tarefa é finalizada
print("Tarefa concluída!")
