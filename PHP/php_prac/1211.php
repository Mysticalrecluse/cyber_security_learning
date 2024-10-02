<?php
function printCount(int $count): void
{
    $i = 0;
    while (++$i) {
        echo "Outer\n";
        while (1) {
            echo "Middle\n";
            while (1) {
                echo "Inner\n";
                if ($i == $count) {
                    break 3;
                }
                continue 3;
                
            }
            echo "This never gets output.\n";
        }
        echo "Neither does this.\n";
    }
}

printCount(4);