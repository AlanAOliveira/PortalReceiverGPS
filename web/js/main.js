var listaEntradasYG = []
const form = document.getElementById('formEntrada');


function testget() {
  aoba = "https://toyotabrasil.sharepoint.com/:u:/s/Order/ETzg0FcEwBVJvDkFGBapRQUBuu6US9FHw0WUsqTTZGiqyw?e=XlXJ4F"
  lista = "https://toyotabrasil.sharepoint.com/sites/memorial_dwg_materiais_gps/_api/web/lists"
  querry_pdf = "https://toyotabrasil.sharepoint.com/sites/memorial_dwg_materiais_gps/_api/search/query?querytext=%27YG79140013*.pdf%27&querytemplatepropertiesurl=%27spfile://webroot/queryparametertemplate.xml%27"

   linke = "YG74987422"
   ahaha ="YG73690009"
   vish = "https://toyotabrasil.sharepoint.com/sites/memorial_dwg_materiais_gps/Documentos%20Compartilhados/Forms/AllItems.aspx?id=%2Fsites%2Fmemorial%5Fdwg%5Fmateriais%5Fgps%2FDocumentos%20Compartilhados%2FMemorial%20%26%20DWG%5FYG%27s%20TDB&viewid=c2407a7f%2D2467%2D4be7%2Da8b2%2D886b8720acda&view=7&q=YG74987422"

  fetch(querry_pdf, {
    method: 'GET',
    headers: {
      //'Access-Control-Allow-Origin': '*',
      'Accept': 'application/json;odata=verbose',      
      //'Authorization': 'Bearer YOUR_ACCESS_TOKEN' // Include if using OAuth
    },
    mode:'cors',
    credentials: 'same-origin' // If relying on browser's existing authentication
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Error fetching SharePoint data:', error);
    });
}

function openYG(yg) {
  link = `https://toyotabrasil.sharepoint.com/sites/memorial_dwg_materiais_gps/Documentos%20Compartilhados/Forms/AllItems.aspx?id=%2Fsites%2Fmemorial%5Fdwg%5Fmateriais%5Fgps%2FDocumentos%20Compartilhados%2FMemorial%20%26%20DWG%5FYG%27s%20TDB&viewid=c2407a7f%2D2467%2D4be7%2Da8b2%2D886b8720acda&view=7&q=${yg}`
  window.open(link, "_blank").focus();
}


function getYGBarcode(barcode) {
  yourUrl = ""
  value = "getYGBarcode"
  var xhr = new XMLHttpRequest();
  xhr.open("POST", yourUrl, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({
    function: value,
    dados: barcode
  }));
  xhr.onreadystatechange = function () {
    if (xhr.readyState == XMLHttpRequest.DONE) {
      try {
        info = JSON.parse(xhr.response)
        console.log(info)
        if (info.rc != "falha") {
          // RC / YG / Descrição / qty / un / pedido / status
          listaEntradasYG.push(barcode)
          document.getElementById("listaEntradas").innerHTML +=
            `<li id="pn_${listaEntradasYG.length}" class="list-group-item">
                    RC: ${info.rc} 
                    YG: ${info.yg} 
                    Desc: ${info.descricao} 
                    QTD: ${info.qtd} 
                    UN: ${info.un} 
                    Pedido: ${info.pedido} 
                    Status: ${info.status}
                    <button onclick="openYG('${info.yg}')" type="button" class="btn btn-success">Mem</button>
                    <button onclick="itemDelete('pn_${listaEntradasYG.length}',${listaEntradasYG.length})" type="button" class="btn btn-danger">X</button></li>`
        } else {
          alert("YG não encontradas")
        }

      } catch (error) {
      }
    }
  }
}

function itemDelete(id, index) {
  item = document.getElementById(id)
  item.remove()
  listaEntradasYG.splice(index - 1, 1)
}

form.addEventListener('submit', function (event) {
  event.preventDefault();
  var campo = document.getElementById('inputCodBarra');


  getYGBarcode(campo.value)
  //var lista = document.getElementById('listaEntradas')
  //if (campo.value != "") {
  //  lista.innerHTML = `<li class="list-group-item">${campo.value}</li>` + lista.innerHTML
  //  listaEntradasYG.push(campo.value)
  //}
  campo.value = "";
});

const form2 = document.getElementById('formListaEntrada');

form2.addEventListener('submit', function (event) {
  event.preventDefault();

  if (listaEntradasYG.length == 0) {
    alert("Lista vazia")
    return
  }
  yourUrl = ""
  value = "enviarListaYG"
  var xhr = new XMLHttpRequest();
  xhr.open("POST", yourUrl, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({
    function: value,
    dados: listaEntradasYG
  }));
  xhr.onreadystatechange = function () {
    if (xhr.readyState == XMLHttpRequest.DONE) {
      info = JSON.stringify(xhr.response)
      console.log(info)
      listaEntradasYG = []
      document.getElementById('listaEntradas').innerHTML = ""
    }
  }


});


function pamonha(){
  fetch("https://toyotabrasil.sharepoint.com/sites/memorial_dwg_materiais_gps/_api/search/query?querytext=%27YG79140013*.pdf%27&querytemplatepropertiesurl=%27spfile://webroot/queryparametertemplate.xml%27", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
  },
  "body": null,
  "method": "GET",
  "mode": "cors",
  "credentials": "include"
});
}