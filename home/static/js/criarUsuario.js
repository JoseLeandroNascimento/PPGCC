let usuario = document.querySelector('.usuario');
let tipoUsuario = document.getElementsByName('tipo_usuario');
let status_usuario = document.getElementsByName('status');
let caixaPermissoes1 = document.querySelector('#caixa-permissoes');
let senha1 = document.querySelector('.senha1');
let senha2 = document.querySelector('.senha2');
let sucesso = document.querySelector('.sucesso');
let erro = document.querySelector('.erro');
let url_destino = document.querySelector('.url_destino');
let form = document.querySelector('.form');


form.addEventListener('submit', (event) => {


    event.preventDefault();


    let campo_usuario = usuario.value;
    let campo_senha1 = senha1.value;
    let campo_senha2 = senha2.value;
    let campo_tipo_usuario;
    let campo_status;


    // Verifica o tipo de usuario senhdo criado
    let tipoUsuario_radio1 = tipoUsuario[0]

    campo_tipo_usuario = tipoUsuario[1].value;

    if (tipoUsuario_radio1.checked) {

        campo_tipo_usuario = tipoUsuario_radio1.value;

    }


    // Verifica o status do usuario para

    let tipoStatus_radio1 = status_usuario[0];


    let valor = status_usuario[1].value;

    if (tipoStatus_radio1.checked) {

        valor = tipoStatus_radio1.value;
    }

    campo_status = valor;

    let listaSecoesPermitidas = [];


    for (let indice = 0; indice < caixaPermissoes1.options.length; indice++) {

        listaSecoesPermitidas.push(caixaPermissoes1.options[indice].value);

    }

    if (senha1.value != senha2.value) {

        erro.style.display = 'block';

        setTimeout(() => {

            erro.style.display = 'none';

        }, 4000)
    } else {


        campo_usuario = usuario.value;
        campo_senha1 = senha1.value;
        campo_senha2 = senha2.value;


        let obj = {

            usuario: campo_usuario,
            status: campo_status,
            tipo_usuario: campo_tipo_usuario,
            senha1: campo_senha1,
            secoes: listaSecoesPermitidas,
            senha2: campo_senha2,
            url_destino: url_destino.value,

        }

        axios.post("../../backend/criarUsuario.php", JSON.stringify(obj)).then(response => {

            console.log(response.data);

        }).catch(err => {

            console.log(err);
        })

    }


})