<?php
header("Content-type:text/html;charset=utf8");
$config = [
    'host'=>'127.0.0.1:3308',
    'user'=>'root',
    'password'=>'Zyf646130..',
    'database'=>'atguigudb',
    'charset'=>'utf8'
];
$dsn = sprintf(
    "mysql:host=%s;dbname=%s;charset=%s", 
    $config['host'],
    $config['database'],
    $config['charset']
);
try{
    $pdo = new PDO($dsn, $config['user'], $config['password'],
    [PDO::ATTR_ERRMODE=>PDO::ERRMODE_WARNING]);
    $query = $pdo->query("SELECT * FROM testphp WHERE id=1");
    $rows = $query->fetchAll();
    print_r($rows);
}catch (PDOExecption $e){
    die($e->getMessage());
}
?>