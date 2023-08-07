Shell, I/O Redirections and filters
0 echo 'Hello World' prints out Hello World
1 echo "(Ôo)'prints out (Ôo)
2 cat /etc/passwd displays the content of the /etc/passwd file 
3 cat /etc/passwd /etc/hosts displays the content of /etc/passwd and /etc/hosts
4 tail /etc/passwd displays the last 10 lines of /etc/passwd file
5 head /etc/passwd displays the first 10 lines of /etc/passwd file
6 head -n 3 iacta | tail -n 1 displays the the third line of the file iacta
7 echo 'Best School' > \\*\\'"Best School"\'\\\*$\\?\\*\\*\\*\\*\\*:\), a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) conta ining the text Best School ending by a new line.
8 s -la > ls_cwd_content  a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
9 tail -n 1 >> iacta a script that duplicates the last line of the file iacta
10 find . -type f -name "*.js" -exec rm {} a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders
11 find . -type d | wc -l 
12 
