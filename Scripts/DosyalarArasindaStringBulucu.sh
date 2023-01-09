find . type f -exec strings {} \; 2>/dev/null | grep --text "stmctf"
