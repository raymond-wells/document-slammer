BEGIN {
    page = 1;

    # Page 3 accounts for the two lead-in pages, which are not counted as part of the
    # numbering scheme: The Title Page & Table of Contents. Page 1 starts immediately thereafter.
    startPage=3;
}

/^showpage/ {
    if (page % 2 == 0) {pos = 50} else {pos = 550};
    if (page >= startPage) {
        print "/Helvetica findfont 16 scalefont setfont\n" pos " 25 moveto\n(" page - 2 ") show\nshowpage";
    } else {
        print $0;
    }
    page += 1;
}

!/^showpage/ {print $0}
