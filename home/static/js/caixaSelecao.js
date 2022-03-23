let caixaSecoes = document.getElementById('caixa-secoes');
let caixaPermissao = document.getElementById('caixa-permissoes');
let btnAdd = document.querySelector('.btn-add');
let btnRemove = document.querySelector('.btn-remove');
let listaOculta = document.querySelector('.lista-oculta');

let selecionados = [];


function carregarSelecionados() {


    btnAdd.click();
}


function listar() {

    for (let i = 0; i < caixaPermissao.options.length; i++) {


        let texto = caixaPermissao.options[i].text;
        let valor = caixaPermissao.options[i].value;
        selecionados.push({ texto, valor });
    }

    renderizarPermisoes();
}

function limparSelect() {

    for (let i = 0; i < caixaSecoes.options.length; i++) {

        caixaSecoes.options[i].selected = false;

    }
}

btnAdd.addEventListener('click', (event) => {

    event.preventDefault();
    push(caixaSecoes);
    renderizarPermisoes()

});



btnRemove.addEventListener('click', (event) => {

    event.preventDefault();
    pop(caixaPermissao);
    renderizarPermisoes()
});



function pop(elemento) {

    let aux = []
    for (let i = 0; i < elemento.options.length; i++) {


        if (!elemento.options[i].selected) {

            let texto = elemento.options[i].text;
            let valor = elemento.options[i].value;
            aux.push({ texto, valor });

        }

    }

    selecionados = aux;


}


function push(elemento) {

    for (let i = 0; i < elemento.options.length; i++) {

        // Coloca na lista de selecionados somente se não foi listado anteriormente

        let valido = true;

        for (let j = 0; j < selecionados.length; j++) {


            if (selecionados[j].texto == elemento.options[i].text && selecionados[j].valor == elemento.options[i].value) {

                valido = false;
                break;

            }

        }


        if (elemento.options[i].selected && valido) {

            let texto = elemento.options[i].text;
            let valor = elemento.options[i].value;
            selecionados.push({ texto, valor });

        }

    }


}


function renderizarPermisoes() {


    caixaPermissao.innerHTML = '';
    listaOculta.innerHTML = '';

    for (let i = 0; i < selecionados.length; i++) {


        let option = document.createElement('option');
        let hidden = document.createElement('input');

        hidden.value = selecionados[i].valor;
        hidden.setAttribute('name', "lista[]");
        hidden.setAttribute('type', 'hidden');

        option.value = selecionados[i].valor;
        option.classList.add("border");
        option.classList.add("mb-2");
        option.classList.add("borde-top-0");
        option.classList.add("border-left-0");
        option.classList.add("border-right-0");

        option.innerHTML = selecionados[i].texto;

        listaOculta.appendChild(hidden)
        caixaPermissao.appendChild(option);

    }


}