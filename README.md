
# Leitura código de barras 

Ese projeto foi motivado pela POC PF-1228 e tem o objetivo de ler codigos de barras em arquivos PDF e retornar os valores dos mesmos, atomatizando o processo de obter o numero das notas fiscais na plataforma 




## Instalação

Para rodar este projeto instale as bibliotecas necessárias com

```bash
pip install pyzbar
pip install opencv-python
pip install pdf2image

``` 


## Uso/Exemplos
#### Informe o path do arquivo PDF: pdf/NF42884.pdf

```JSON

retorno: {
   "locate":(2376, 560, 1359,345),
   "value":"b""41210501924271000104550030000428841785288097",
   "type":"CODE128"
}

```

