0 alias ls="rm  *" creates an alias of name:ls and value:rm * 
1 echo "hello $(USER)" prints a hello user where the user is the current linux user
2 export PATH=$PATH:/action add action to the PATH. /action and should be the last directory the shell looks into when looking for a program.
3 echo $PATH | tr ":" "\n" | wc -l counts the number of directories in the PATH.
4 'printenv' that lists environment variables
5 'declare' lists all local variables and environment variables and functions
6 'BEST=School' creates a new local variable
7'export BEST="School" creates a new local variable
8 'echo $((128 + $TRUEKNOWLEDGE))' prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line 
9 'echo $(($POWER/$DIVIDE))' prints the result of POWER divided by DIVIDE, followed by a new line
10 'echo $(($BREATH** $LOVE))'  displays the result of BREATH to the power LOVE
11 'echo $((2#$BINARY))' converts a number from base 2 to base 10.
12 'echo {a..z}{a..z} | tr ' ' '\n' | grep -v 'oo'' prints all possible combinations of two letters, except oo
13 'echo printf "%.2f\n" $NUM' prints a number with two decimal places, followed by a new line
14 'echo  printf '%x\n' $DECIMAL' converts a number from base 10 to base 16
15 'echo tr 'A-Za-z' 'N-ZA-Mn-za-m'' encodes and decodes text using the rot13 encryption
16 'echo paste - - | cut -d$'\t' -f1' prints every other line from the input, starting wih the first line
17 'echo printf '%o\n' $(( $((5#$(echo $STIR | tr 'stir.' '01234'))) + $((5#$(echo $WATER | tr 'water' '01234'))) )) | tr '01234567' 'bestchol'' adds the two numbers stored  in the environment variables WATER and STIR and prints the result
~                                                                                                                                                                     
~                                                                                                                                         
o~                          
~                        
