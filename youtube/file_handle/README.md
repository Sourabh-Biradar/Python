# file handling
# file I/O

1) `open()` : open('file.txt','mode')
2) `read()` : file.read()
3) `write()` : file.write("content")
4) `close()` : file.close()
5) `with keyword` 
6) `readline()` : l1 content , one line gap , l2 content ...
7) `readlines()` : reads as ONE LIST
8) `writelines()` : writes multiple lines 
9) `seek()` : whr to begin from (int)
10) `tell()` : tells whr are we in file (int) ; seek count
11) `truncate()` : resize file to specified bytes


# modes :
- `r` : defalut ; opens file in READ only mode ; throws error if file not found

- `w` : opens file in WRITE only mode ; creates new file if file doesn't exist ; DELETES existing content & writes in it

- `a` : opens file in APPEND only mode ; creates new file if file doesn't exist ; writes at EoF

- `x` : creates a file ; Error if file name already exists

- `t` : for text files ; default 
- `rt` ,`wt` ,`at` ,`xt`

- `b` : for binary files ; image / audio ... 
- `rb` ,`wb` ,`ab` ,`xb`

# with keyword

- auto closes files
