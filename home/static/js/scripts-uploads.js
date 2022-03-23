let tipoArquivo = 'nome';
let valor;

let inputValor = document.querySelector('.inputValor');
let btnPesquisar = document.getElementById('btnPesquisar');
let arquivos_table = document.querySelector('.arquivos-table');
let modalDelete = document.getElementById('modalDelete');
let input_id_arquivo = document.getElementById('input-id-arquivo');
let arquivo_nome = document.getElementById('arquivo-nome');
let labelFiltro = document.getElementById('labelFiltro');
let id_usuario = document.getElementById('id_usuario');


function criarTabela(dados) {

    arquivos_table.innerHTML = '';

    dados.forEach((arquivo) => {

        let tr = document.createElement('tr');
        let td1 = document.createElement('td');
        let td2 = document.createElement('td');
        let td3 = document.createElement('td');
        let td4 = document.createElement('td');
        let td5 = document.createElement('td');

        let btnDownload = document.createElement('a');
        let btnExcluir = document.createElement('button');




        btnDownload.classList.add('btn');
        btnDownload.classList.add('btn-success');
        btnDownload.href = arquivo[3];
        btnDownload.download = '';

        console.log(arquivo);
        let j = document.createElement('i');

        j.classList.add('fas');
        j.classList.add('fa-download');

        btnDownload.appendChild(j);

        btnExcluir.classList.add("btn");
        btnExcluir.classList.add("btn-outline-danger");
        btnExcluir.classList.add("ml-2");

        btnExcluir.type = 'button';
        btnExcluir.setAttribute('data-toggle', 'modal');
        btnExcluir.setAttribute('id', arquivo[0]);

        btnExcluir.addEventListener('click', () => {

            let id = btnExcluir.id;

            input_id_arquivo.value = id;


        })


        let idModal = '#modalDelete';
        btnExcluir.setAttribute('data-target', idModal);



        let i = document.createElement('i');

        i.classList.add('fas');
        i.classList.add('fa-trash');


        btnExcluir.appendChild(i);

        td1.classList.add('text-center');
        td2.classList.add('text-center');
        td3.classList.add('text-center');
        td4.classList.add('text-center');
        td5.classList.add('text-center');




        let iicon = document.createElement('i');
        iicon.classList.add('fas');
        iicon.style.fontSize = '24px';

        if (arquivo[2] == 'pdf') {

            iicon.classList.add('fa-file-pdf');

        } else if (arquivo[2] == 'doc' || arquivo[2] == 'docx') {

            iicon.classList.add('fa-file-word');

        } else {


            iicon.classList.add('fa-file-image');

        }

        td1.appendChild(iicon); //Aqui vai o tipo do arquivo

        td2.innerText = arquivo[1]; //Nome do arquivo
        td2.style = "max-width: 15ch; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;";
        td3.innerText = arquivo[5]; //data de criação
        td4.innerText = arquivo[7]; //usuario que cadastro
        td5.appendChild(btnDownload);
        td5.appendChild(btnExcluir);



        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        tr.appendChild(td4);
        tr.appendChild(td5);


        arquivos_table.appendChild(tr);

    });

}



function definirTipo(label, valor) {

    if (valor == 'data_criacao') {

        inputValor.setAttribute('type', 'date');
    } else {

        inputValor.setAttribute('type', 'text');
        inputValor.value = "";

    }

    tipoArquivo = valor;

    labelFiltro.innerHTML = label;

}

function buscarDados(tipo, valor) {

    let req = new XMLHttpRequest();

    let data = new FormData();

    data.append('tipo', tipo);
    data.append('valor', valor);
    data.append('id_usuario', id_usuario.value)


    req.open('POST', '../../backend/filtrarArquivos.php');


    req.onreadystatechange = function() {

        if (this.readyState == 4 && this.status == 200) {

            let dados = JSON.parse(this.responseText);
            console.log(dados);
            criarTabela(dados);
        }

    }

    req.send(data);

}





this.addEventListener('load', () => {


    buscarDados('', '');
})