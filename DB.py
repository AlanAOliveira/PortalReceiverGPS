import json
import sqlite3
from sqlite3 import Error
import os

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

#connection = create_connection(".\\sm_app.sqlite")

def execute_query(query):
    connection = create_connection(".\\sm_app.sqlite")
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    connection.close()

def return_query(query):
    row = []
    connection = create_connection(".\\sm_app.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        row = cursor.fetchone()
    except Error as e:
        print(f"The error '{e}' occurred")
    
    connection.close()
    
    
    return row

def startDB():
    connection = create_connection(".\\sm_app.sqlite")
    f = open(r"tables.json")
 
    data = json.load(f)
 
    for tabela in data:
        nome = tabela['Nome']
        fields = "("
        for campo in tabela["Campos"]:
            if(campo == "ID"):
                fields = fields + "ID INTEGER PRIMARY KEY ASC ON CONFLICT ABORT AUTOINCREMENT"
            else:
                fields = fields + ", " + campo + " " + tabela["Campos"][campo]
        
        fields = fields + ")"
        query = f"CREATE TABLE IF NOT EXISTS {nome} " 
        query = query + fields
        execute_query(query)

            
    f.close()    
    connection.close()
    
    f = open(r"programacaoteste.json", encoding="utf8")
    data = json.load(f)
    keys_list = list(data[0].keys())
    colunas = "codBarras1"
    for key in keys_list[1:67]:
        colunas += f", {key}" 
    
    
    values = ""
    for item in data[1:140]:  
        value = f'''("{item["codBarras1"]}",
        "{item["codBarras2"]}",
        "{item["codBarras3"]}",
        "{item["ni"]}",
        "{item["divsao"]}",
        "{item["rc"]}",
        "{item["seqRc"]}",
        "{item["dataRc"]}",
        "{item["pl"]}",
        "{item["secao"]}",
        "{item["comprador"]}",
        "{item["yg"]}",
        "{item["descricao"]}",
        "{item["texto"]}",
        "{item["qtd"]}",
        "{item["un"]}",
        "{item["bm"]}",
        "{item["limite"]}",
        "{item["ultFornec"]}",
        "{item["ultPreco"]}",
        "{item["apr"]}",
        "{item["dataAprov"]}",
        "{item["tc"]}",
        "{item["bmct"]}",
        "{item["transp"]}",
        "{item["etdPlan"]}",
        "{item["pedido"]}",
        "{item["seqPedido"]}",
        "{item["dataPedido"]}",
        "{item["nopo"]}",
        "{item["status"]}",
        "{item["noRingi"]}",
        "{item["texto3"]}",
        "{item["requisitante"]}",
        "{item["reqPedido"]}",
        "{item["obs"]}",
        "{item["fornecRc"]}",
        "{item["nome"]}",
        "{item["nomeAtualFornece"]}",
        "{item["dataRecebimento"]}",
        "{item["qtdRecebida"]}",
        "{item["statusRecebimento"]}",
        "{item["obsRecebimento"]}",
        "{item["dataPo"]}",
        "{item["ltDias"]}",
        "{item["novaPrevPosPo"]}",
        "{item["novaPrevEntrega"]}",
        "{item["planta"]}",
        "{item["plantaYgRcSeqRc"]}",
        "{item["dataInicioFollow"]}",
        "{item["dataRetornoFollow"]}",
        "{item["qtdFollowRealizado"]}",
        "{item["respFollow"]}",
        "{item["tipoSolicitacao"]}",
        "{item["itemAtendido"]}",
        "{item["motivoAtraso"]}",
        "{item["motivoNaoAtendido"]}",
        "{item["descontinuado"]}",
        "{item["novaPrevEntrega2"]}",
        "{item["podeReenviar"]}",
        "{item["temProntaEntrega"]}",
        "{item["numNfEntregue"]}",
        "{item["dataEntregueMat"]}",
        "{item["emailGps"]}",
        "{item["faturamentoMinimo"]}",
        "{item["outrasSituacaoes"]}",
        "{item["familia"]}"),'''
        values += value
        
    values += f'''("{data[141]["codBarras1"]}",
        "{data[141]["codBarras2"]}",
        "{data[141]["codBarras3"]}",
        "{data[141]["ni"]}",
        "{data[141]["divsao"]}",
        "{data[141]["rc"]}",
        "{data[141]["seqRc"]}",
        "{data[141]["dataRc"]}",
        "{data[141]["pl"]}",
        "{data[141]["secao"]}",
        "{data[141]["comprador"]}",
        "{data[141]["yg"]}",
        "{data[141]["descricao"]}",
        "{data[141]["texto"]}",
        "{data[141]["qtd"]}",
        "{data[141]["un"]}",
        "{data[141]["bm"]}",
        "{data[141]["limite"]}",
        "{data[141]["ultFornec"]}",
        "{data[141]["ultPreco"]}",
        "{data[141]["apr"]}",
        "{data[141]["dataAprov"]}",
        "{data[141]["tc"]}",
        "{data[141]["bmct"]}",
        "{data[141]["transp"]}",
        "{data[141]["etdPlan"]}",
        "{data[141]["pedido"]}",
        "{data[141]["seqPedido"]}",
        "{data[141]["dataPedido"]}",
        "{data[141]["nopo"]}",
        "{data[141]["status"]}",
        "{data[141]["noRingi"]}",
        "{data[141]["texto3"]}",
        "{data[141]["requisitante"]}",
        "{data[141]["reqPedido"]}",
        "{data[141]["obs"]}",
        "{data[141]["fornecRc"]}",
        "{data[141]["nome"]}",
        "{data[141]["nomeAtualFornece"]}",
        "{data[141]["dataRecebimento"]}",
        "{data[141]["qtdRecebida"]}",
        "{data[141]["statusRecebimento"]}",
        "{data[141]["obsRecebimento"]}",
        "{data[141]["dataPo"]}",
        "{data[141]["ltDias"]}",
        "{data[141]["novaPrevPosPo"]}",
        "{data[141]["novaPrevEntrega"]}",
        "{data[141]["planta"]}",
        "{data[141]["plantaYgRcSeqRc"]}",
        "{data[141]["dataInicioFollow"]}",
        "{data[141]["dataRetornoFollow"]}",
        "{data[141]["qtdFollowRealizado"]}",
        "{data[141]["respFollow"]}",
        "{data[141]["tipoSolicitacao"]}",
        "{data[141]["itemAtendido"]}",
        "{data[141]["motivoAtraso"]}",
        "{data[141]["motivoNaoAtendido"]}",
        "{data[141]["descontinuado"]}",
        "{data[141]["novaPrevEntrega2"]}",
        "{data[141]["podeReenviar"]}",
        "{data[141]["temProntaEntrega"]}",
        "{data[141]["numNfEntregue"]}",
        "{data[141]["dataEntregueMat"]}",
        "{data[141]["emailGps"]}",
        "{data[141]["faturamentoMinimo"]}",
        "{data[141]["outrasSituacaoes"]}",
        "{data[141]["familia"]}")'''
        

    query = f"insert into programacao ({colunas}) VALUES {values}"
    query = query.strip()   
    print(query)
    execute_query(query)

    
    f.close()

file_path = "sm_app.sqlite"


if os.path.isfile(file_path):
    print(f"O banco '{file_path}' já existe.")
else:
    print(f"O Banco '{file_path}' não existe e sera iniciado agora")
    startDB()

print("DB Started")
