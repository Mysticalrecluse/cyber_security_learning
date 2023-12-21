<?php
session_name('mystical');
session_start();

echo session_name();
echo "<br>";
echo session_id();
session_destroy();
?>