<?php
foreach ($_POST as $key => $value) {
    echo $key."=".htmlspecialchars($value)."<hr/>";
}

for ($i = 0, $count = count($_POST); $i < $count; $i++)
{
    echo key($_POST)."=".htmlspecialchars($_POST[key($_POST)])."<hr/>";
    next($_POST);
}
?>