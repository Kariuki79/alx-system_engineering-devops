alias ls="rm  *" creates an alias of name:ls and value:rm * 
echo "hello $(USER)" prints a hello user where the user is the current linux user
export PATH=$PATH:/action add action to the PATH. /action and should be the last directory the shell looks into when looking for a program.
echo $PATH | tr ":" "\n" | wc -l counts the number of directories in the PATH.
printenv that lists environment variables
declare lists all local variables and environment variables and functions
