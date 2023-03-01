# Organizador de XMLs

Este é um script em Python que organiza arquivos XMLs de notas fiscais eletrônicas (NF-e) de acordo com o tipo de pagamento.

**Atenção:** Este script foi desenvolvido para funcionar somente com a versão 4.00 da NF-e.

## Setup

1. Certifique-se de ter o Python 3 instalado em seu computador.
2. Clone este repositório ou faça o download do código-fonte.
3. Instale a biblioteca `xml.etree.ElementTree` com o comando `pip install xml`.
4. Execute o arquivo `app.py`.


## Como usar

1. Abra o arquivo `app.py` em um editor de texto.
2. Altere o valor da constante `DIRETORIO` para o diretório onde estão os arquivos XMLs que deseja organizar.
3. Execute o arquivo `app.py`.
4. Verifique o diretório de destino especificado pelo script para garantir que as pastas foram criadas e que os arquivos XMLs foram movidos corretamente.

## Como funciona

O script percorre o diretório especificado pela constante `DIRETORIO` em busca de arquivos com extensão `.xml`. Para cada arquivo encontrado, o script lê o valor do elemento `tPag` do XML para determinar o tipo de pagamento da nota fiscal.

Se o valor de `tPag` for igual a `01`, o script move o arquivo para o diretório especificado pela constante `DESTINO` com path para sua pasta dinheiro. Caso contrário, o script move o arquivo para o diretório especificado pela constante `DESTINO`com path para sua pasta de cartão.

## Autor

Este script foi desenvolvido por thiago gentil.
