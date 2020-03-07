/*Esse é a parte back-end do website que se comunica com o server e contra a visualização
dos arquivos HTML. A vulnerabilidade consiste em não haver verificação de autorização para acessar
os arquivos, sendo assim a aplicação é vulnerável a Path Traversal Injection*/

<?php

$page = $_GET['page'] ?? 'home';

echo file_get_contents($page.'.php');

?>
