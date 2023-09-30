<?php
foreach ($_GET as $key => $value) {
    echo $key."=".htmlspecialchars($value)."<hr/>";
}

for ($i = 0, $count = count($_GET); $i < $count; $i++)
{
    echo key($_GET)."=".htmlspecialchars($_GET[key($_GET)])."<hr/>";
    next($_GET);
}
?>