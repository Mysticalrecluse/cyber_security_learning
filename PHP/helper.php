<?php
function upload() {
    if(is_uploaded_file($_FILES['up']['tmp_name'])) {
        $to = 'upload/'.$F_ILES['up']['name'];
        if (move_uploaded_file($_FILES['up']['tmp_name'], $to)) {
            return $to;
        } 
    }

}
?>