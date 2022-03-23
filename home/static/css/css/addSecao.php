<?php

include "../../backend/isLogado.php";

include "../../backend/conexao.php";
include "../../backend/SecaoModel.php";

$usuario_logado = $_SESSION['usuario'];

$novaSecao = true;

$secaoModel = new SecaoModel($cnx);
$icons = [
    'Android' => 'fab fa-android',
    'Apple' => 'fab fa-apple',
    'Aranha' => 'fas fa-spider',
    'Ampulheta' => 'fas fa-hourglass-half',
    'Alinhado ao centro' => 'fas fa-align-center',
    'Alfinete' => 'fas fa-thumbtack',
    'Justificado' => 'fas fa-align-justify',
    'Alinhado à esquerda' => 'fas fa-align-left',
    'Alinhado à direita' => 'fas fa-align-right',
    'Âncora' => 'fas fa-anchor',
    'Asterísco' => 'fas fa-asterisk',
    'Arroba' => 'fas fa-at',
    'Avião' => 'fas fa-plane',
    'Bandeira' => 'fas fa-flag',
    'Balança Justiça' => 'fas fa-balance-scale',
    'Balão de comentário' => 'far fa-comment',
    'Bateria' => 'fas fa-battery-three-quarters',
    'Bíblia' => 'fas fa-bible',
    'Binóculo' => 'fas fa-binoculars',
    'Bolo de aniversário' => 'fas fa-birthday-cake',
    'Bitcoin' => 'fab fa-bitcoin',
    'Bloco de notas' => 'fas fa-sticky-note',
    'Bluetooth' => 'fab fa-bluetooth',
    'Bomba' => 'fas fa-bomb',
    'Cachorro' => 'fas fa-dog',
    'Cadeado' => 'fas fa-lock',
    'Cadeira de rodas' => 'fab fa-accessible-icon',
    'Caixa registradora' => 'fas fa-cash-register',
    'Calculadora' => 'fas fa-calculator',
    'Calendário' => 'far fa-calendar-alt',
    'Caneta' => 'fas fa-marker',
    'Câmera' => 'fas fa-camera',
    'Caminhão' => 'fas fa-truck',
    'Capa de livro com pessoa' => 'fas fa-address-book',
    'Cartão com pessoa' => 'fas fa-address-card',
    'Carro' => 'fas fa-car',
    'Cartão SD' => 'fas fa-sd-card',
    'Cavalo' => 'fas fa-horse',
    'Carrinho de bebê' => 'fas fa-baby-carriage',
    'Carrinho de compras' => 'fas fa-shopping-cart',
    'Cérebro' => 'fas fa-brain',
    'Casa' => 'fas fa-home',
    'Chapéu de formatura' => 'fas fa-graduation-cap',
    'Chave' => 'fas fa-key',
    'Chuveiro' => 'fas fa-shower',
    'Cifrão' => 'fas fa-dollar-sign',
    'Clipe' => 'fas fa-paperclip',
    'Código de Barras' => 'fas fa-barcode',
    'Compartilhar' => 'fas fa-share-alt-square',
    'Curativo' => 'fas fa-band-aid',
    'Dados' => 'fas fa-dice',
    'Dente' => 'fas fa-tooth',
    'Diagrama' => 'fas fa-sitemap',
    'Documento' => 'fas fa-file-alt',
    'Escudo' => 'fas fa-shield-alt',
    'Estrela' => 'fas fa-star',
    'Facebook' => 'fab fa-facebook-square',
    'Feminino' => 'fas fa-female',
    'Ferramentas' => 'fas fa-tools',
    'Floco de neve' => 'fas fa-snowflake',
    'Fone de ouvido' => 'fas fa-headphones',
    'Funil' => 'fas fa-filter',
    'Engrenagem' => 'fas fa-cog',
    'Envelope' => 'fas fa-envelope',
    'Estetoscópio' => 'fas fa-stethoscope',
    'Garfo e faca' => 'fas fa-utensils',
    'Gato' => 'fas fa-cat',
    'Globo terrestre' => 'fas fa-globe-americas',
    'Google' => 'fab fa-google',
    'Google Drive' => 'fab fa-google-drive',
    'Google Play Store' => 'fab fa-google-play',
    'Gota' => 'fas fa-tint',
    'Guarda-chuva' => 'fas fa-umbrella',
    'Hashtag' => 'fas fa-hashtag',
    'Helicóptero' => 'fas fa-helicopter',
    'Hipopótamo' => 'fas fa-hippo',
    'HD' => 'fas fa-hdd',
    'Ícone de informação' => 'fas fa-info-circle',
    'Ímã' => 'fas fa-magnet',
    'Instagram' => 'fab fa-instagram',
    'Impressora' => 'fas fa-print',
    'Lâmpada' => 'fas fa-lightbulb',
    'Lápis' => 'fas fa-pencil-alt',
    'Linguagem de sinais' => 'fas fa-sign-language',
    'Linkedin' => 'fab fa-linkedin',
    'Livro fechado' => 'fas fa-book',
    'Livro aberto' => 'fas fa-book-open',
    'Lixeira' => 'fas fa-trash',
    'Lua' => 'fas fa-moon',
    'Lupa' => 'fas fa-search',
    'Martelo' => 'fas fa-hammer',
    'Mapa' => 'fas fa-map-marked-alt',
    'Masculino' => 'fas fa-male',
    'Medalha' => 'fas fa-medal',
    'Messenger' => 'fab fa-facebook-messenger',
    'Microfone' => 'fas fa-microphone-alt',
    'Monitor de computador' => 'fas fa-desktop',
    'Nota musical' => 'fas fa-music',
    'Notebook' => 'fas fa-laptop',
    'Óculos' => 'fas fa-glasses',
    'Ônibus' => 'fas fa-bus-alt',
    'Osso' => 'fas fa-bone',
    'Passáro' => 'fas fa-dove',
    'Pasta' => 'fas fa-folder-open',
    'Pena' => 'fas fa-feather-alt',
    'Peixe' => 'fas fa-fish',
    'Pincel' => 'fas fa-paint-brush',
    'Pinterest' => 'fab fa-pinterest',
    'Pizza' => 'fas fa-pizza-slice',
    'Play' => 'fas fa-play-circle',
    'Prédio' => 'fas fa-building',
    'Proibido fumar' => 'fas fa-smoking-ban',
    'Raio' => 'fas fa-bolt',
    'Reciclagem' => 'fas fa-recycle',
    'Régua' => 'fas fa-ruler-horizontal',
    'Rôbo' => 'fas fa-robot',
    'Sapo' => 'fas fa-frog',
    'Sino' => 'fas fa-bell',
    'Sinal de internet' => 'fas fa-signal',
    'Snapchat' => 'fab fa-snapchat',
    'Skype' => 'fab fa-skype',
    'Steam' => 'fab fa-steam-square',
    'Tag' => 'fas fa-tag',
    'Teclado' => 'fas fa-keyboard',
    'Telefone' => 'fas fa-phone-alt',
    'Telegram' => 'fab fa-telegram',
    'Termômetro' => 'fas fa-thermometer-quarter',
    'Tomada' => 'fas fa-plug',
    'Trello' => 'fab fa-trello',
    'Troféu' => 'fas fa-trophy',
    'Twitch' => 'fab fa-twitch',
    'Twitter' => 'fab fa-twitter',
    'Violão' => 'fas fa-guitar',
    'USB' => 'fab fa-usb',
    'Usuário' => 'fas fa-user-alt',
    'Usuário formatura' => 'fas fa-user-graduate',
    'Vaso sanitário' => 'fas fa-toilet',
    'Vídeo' => 'fas fa-video',
    'Vírus' => 'fas fa-virus',
    'Volume desligado' => 'fas fa-volume-mute',
    'Volume ligado' => 'fas fa-volume-up',
    'Whatsapp' => 'fab fa-whatsapp',
    'Windows' => 'fab fa-windows',
    'Wi-Fi' => 'fas fa-rss',
    'Wikipedia' => 'fab fa-wikipedia-w',
    'Xícara' => 'fas fa-coffee',
    'Yin e Yang' => 'fas fa-yin-yang',
    'Youtube' => 'fab fa-youtube',

];

$subsecao_atual = -1;
$secao_atual = -1;


?>


<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Admin - adicionar Seção</title>

    <!-- Google Font: Source Sans Pro -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="../../assets/plugins/fontawesome-free/css/all.min.css">
    <!-- Ionicons -->
    <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
    <!-- Tempusdominus Bootstrap 4 -->
    <link rel="stylesheet" href="../../assets/plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css">
    <!-- iCheck -->
    <link rel="stylesheet" href="../../assets/plugins/icheck-bootstrap/icheck-bootstrap.min.css">
    <!-- JQVMap -->
    <link rel="stylesheet" href="../../assets/plugins/jqvmap/jqvmap.min.css">
    <!-- Theme style -->
    <link rel="stylesheet" href="../../assets/dist/css/adminlte.min.css">
    <!-- overlayScrollbars -->
    <link rel="stylesheet" href="../../assets/plugins/overlayScrollbars/css/OverlayScrollbars.min.css">
    <!-- Daterange picker -->
    <link rel="stylesheet" href="../../assets/plugins/daterangepicker/daterangepicker.css">
    <link rel="stylesheet" href="../../assets/dist/css/style-admin.css">


    <style>
        iframe {
            max-width: 100%;
            height: 360px;
        }
    </style>


</head>

<body class="hold-transition sidebar-mini layout-fixed">
    <div class="wrapper">

        <!-- Preloader -->
        <div class="preloader flex-column justify-content-center align-items-center">
            <img class="animation__shake" src="../../assets/dist/img/ufac-logo.png" alt="AdminLTELogo" height="auto" width="80">
        </div>

        <!-- Navbar -->


        <!-- Navbar -->
        <?php

        include "./partial/menu.php";
        ?>
        <!-- /.sidebar-menu -->
    </div>
    <!-- /.sidebar -->

    <!-- Content Wrapper. Contains page content -->
    <div class="content-wrapper">
        <!-- Content Header (Page header) -->
        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">

                    </div><!-- /.col -->
                    <div class="col-sm-6 text-right">

                    </div><!-- /.col -->
                </div><!-- /.row -->
            </div><!-- /.container-fluid -->
        </div>
        <!-- /.content-header -->

        <!-- Main content -->

        <section class="content">


            <div class="container">


                <div class="card">
                    <div class="card-header">


                        <h3> <i class="nav-icon fas fa-plus-circle icon-menu"></i> Nova Seção</h3>
                    </div>

                    <div class="card-body">

                        <form action="../../backend/criaSecao.php" method="post">

                            <div class="row p-0 mb-3">
                                <div class="col-8">
                                    <label for="titulo">Titulo</label>
                                    <input type="text" maxlength="30" name="titulo" autocomplete="off" id="titulo" class="form-control" placeholder="ex: Introdução" required>


                                </div>
                                <div class="col-4">
                                    <?php


                                    $res = $secaoModel->getSecaoAll();

                                    $quantidade_secao = $res->num_rows + 1;


                                    ?>

                                    <label for="ordem">Ordem</label>
                                    <select name="ordem" id="ordem" class="form-control">
                                        <?php for ($ordem = 1; $ordem <= $quantidade_secao; $ordem++) { ?>

                                            <?php if ($ordem == $quantidade_secao) { ?>

                                                <option value="<?= $ordem ?>" selected>


                                                    <?= $ordem ?>

                                                </option>

                                            <?php } else { ?>


                                                <option value="<?= $ordem ?>" selected>


                                                    <?= $ordem ?>

                                                </option>


                                            <?php } ?>
                                        <?php } ?>
                                    </select>
                                </div>
                            </div>


                            <div class="row">

                                <div class="col">

                                    <label for="icon">Ícone da Seção</label>
                                </div>
                                <div class="col text-center">

                                    <label>Visibilidade da Página</label>
                                </div>
                            </div>

                            <div class="row">

                                <div class="col-3">

                                    <select name="icon" id="icon" class="form-control mb-3" size="7" onchange="pegarIcon(this)">

                                        <?php foreach ($icons as $nome => $valor) { ?>

                                            <option value="<?= $valor ?>"><?= $nome ?> </option>

                                        <?php } ?>
                                    </select>

                                </div>
                                <div class="col-5">

                                    <p style="display: inline;">
                                        <i class="nav-icon fas fa-plus-circle icon-menu" style='font-size:30px;'></i>

                                    </p>
                                </div>
                                <div class="col pl-3">
                                    <div class="form-check">
                                        <label class="form-check-label">
                                            <input type="radio" value="1" class="form-check-input" name="ativada" checked>Ativada
                                        </label>
                                    </div>
                                    <div class="form-check mb-4">
                                        <label class="form-check-label">
                                            <input type="radio" value="0" class="form-check-input" name="ativada">Desativada
                                        </label>
                                    </div>

                                </div>
                            </div>

                            <input type="hidden" name="url_destino" value="../pages/admin/addSecao.php">
                            <input type="hidden" name="id_usuario" value="<?= $usuario_logado['id'] ?>">
                            <div class="text-center">

                                <button type="submit" class="btn btn-success mt-3">
                                    <i class="fas fa-plus"></i>
                                    Criar Seção
                                </button>

                                <a href="index.php" class="btn btn-danger mt-3">
                                    <i class="fas fa-ban"></i>
                                    Cancelar
                                </a>

                            </div>

                        </form>
                    </div>
                </div>

            </div>



        </section>


        <?php

        include "./partial/modelSair.php";

        ?>

        <!-- /.content -->
    </div>
    <!-- /.content-wrapper -->
    <?php include "footer.php"; ?>


    <!-- Control Sidebar -->
    <aside class="control-sidebar control-sidebar-dark">
        <!-- Control sidebar content goes here -->
    </aside>
    <!-- /.control-sidebar -->
    </div>
    <!-- ./wrapper -->

    <script>
        const inputTitulo = document.querySelector('#titulo');
        const label = document.querySelector('#label-icon');
        const icon = document.querySelectorAll('.icon-menu');

        let titulo = '';
        inputTitulo.addEventListener('input', (event) => {


            label.innerHTML = inputTitulo.value;

        });

        function pegarIcon(ele) {

            let classes = (ele.value + "").split(' ');

            classes.forEach((valor) => {

                icon.forEach((ic) => {

                    ic.classList.remove(ic.classList[1]);
                    ic.classList.remove(ic.classList[2]);
                    ic.classList.add(valor);

                })


            })

        }
    </script>


</body>


<!-- jQuery -->
<script src="../../assets/plugins/jquery/jquery.min.js"></script>
<!-- jQuery UI 1.11.4 -->
<script src="../../assets/plugins/jquery-ui/jquery-ui.min.js"></script>
<!-- Resolve conflict in jQuery UI tooltip with Bootstrap tooltip -->
<script>
    $.widget.bridge('uibutton', $.ui.button)
</script>
<!-- Bootstrap 4 -->
<script src="../../assets/plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
<!-- ChartJS -->
<script src="../../assets/plugins/chart.js/Chart.min.js"></script>
<!-- Sparkline -->
<script src="../../assets/plugins/sparklines/sparkline.js"></script>
<!-- JQVMap -->
<script src="../../assets/plugins/jqvmap/jquery.vmap.min.js"></script>
<script src="../../assets/plugins/jqvmap/maps/jquery.vmap.usa.js"></script>
<!-- jQuery Knob Chart -->
<script src="../../assets/plugins/jquery-knob/jquery.knob.min.js"></script>
<!-- daterangepicker -->
<script src="../../assets/plugins/moment/moment.min.js"></script>
<script src="../../assets/plugins/daterangepicker/daterangepicker.js"></script>
<!-- Tempusdominus Bootstrap 4 -->
<script src="../../assets/plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script>
<!-- Summernote -->
<script src="../../assets/plugins/summernote/summernote-bs4.min.js"></script>
<!-- overlayScrollbars -->
<script src="../../assets/plugins/overlayScrollbars/js/jquery.overlayScrollbars.min.js"></script>
<!-- AdminLTE App -->
<script src="../../assets/dist/js/adminlte.js"></script>
<!-- AdminLTE for demo purposes -->
<!-- <script src="../../../../assets/dist/js/demo.js"></script> -->
<!-- AdminLTE dashboard demo (This is only for demo purposes) -->
<script src="../../assets/dist/js/pages/dashboard.js"></script>

<script src="../../assets/plugins/summernote/summernote-bs4.min.js"></script>

<script src="../../plugins/summernote/summernote-bs4.min.js"></script>
<!-- CodeMirror -->
<script src="../../plugins/codemirror/codemirror.js"></script>
<script src="../../plugins/codemirror/mode/css/css.js"></script>
<script src="../../plugins/codemirror/mode/xml/xml.js"></script>
<script src="../../plugins/codemirror/mode/htmlmixed/htmlmixed.js"></script>
<!-- AdminLTE for demo purposes -->
<!-- <script src="../../../../assets/dist/js/demo.js"></script> -->
<!-- Page specific script -->

</html>