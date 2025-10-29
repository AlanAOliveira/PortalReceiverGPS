import DB
import json

def enviarListaYG(itens):
    for item in itens:
        print(item)
    dataResponse = {
        "Status":"1"
    }  
    return json.dumps(dataResponse)

def getYGBarcode(barcode):
    query = f'SELECT rc, yg , descricao, qtd, un , pedido , status from programacao where codBarras1 = "{barcode}"'
    response = DB.return_query(query)
    
    
    if response == None:
        dataResponse = {
            "rc": "falha"
        }
    else:
        dataResponse = {
            "rc": response[0],
            "yg": response[1],
            "descricao": response[2],
            "qtd": response[3],
            "un": response[4],
            "pedido": response[5],
            "status": response[6]
        }

    print(dataResponse)
    return json.dumps(dataResponse)