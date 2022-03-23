function montarBoxDefesas() {

    let dia = document.getElementById('area-dia');
    // let data;

    axios.get('./backend/getDefesas.php').then(response => {


        console.log(JSON.parse(response.data));

    }).catch(err => {

        console.log(err);
    })


}

montarBoxDefesas();