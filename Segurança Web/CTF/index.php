<?php

$page = $_GET['page'] ?? 'home';

echo file_get_contents($page.'.php');

?>
