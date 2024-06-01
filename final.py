################################################################################
#Aikaterini Bleka 4575
#Stavroula Dimitra Koutsikou 4396
################################################################################
import os
import sys

# Pairnoume to onoma tou arxeiou apo command line 
file = open(sys.argv[1], 'r')

##################################################################################################################################################################################
# Ola osa tha xreiastoume:
###################################################################################################################################################################################

#Katastaseis

katastash_zero = 0
katastash_letters = 1
katastash_digits = 2 
katastash_equal = 3
katastash_div = 4
katastash_lessthan = 5
katastash_greaterthan = 6
katastash_exclmark = 7
katastash_hashtag = 8
katastash_comment = 9
katastash_close_comment = 10

#Tokens

identifier_tkn = 70
digits_tkn = 71
EOF_tkn = 72
add_tkn = 73
sub_tkn = 74
equal_tkn = 75
comma_tkn = 76
mult_tkn = 77
div_tkn = 78
mod_tkn = 79
lessthan_tkn = 80
greaterthan_tkn = 81
left_parenthesis_tkn = 82
right_parenthesis_tkn = 83
colon_tkn = 84
open_block_tkn = 85
close_block_tkn = 86
assign_symb_tkn = 87
lessOrequal_tkn = 88
greaterORequal_tkn = 89
different_tkn = 90

#Charakthres

letters = 0
digits = 1
EOF = 2
white_character = 3
add = 4
sub = 5
equal = 6
comma = 7
mult = 8
div = 9
mod = 10
hashtag = 11
excl_mark = 12
less_than = 13
greater_than = 14
left_parenthesis = 15
right_parenthesis = 16
colon = 17
open_block = 18
close_block = 19
not_acceptable_symbol = 20
new_line = 21

#Desmeumenes lekseis

main_tkn = 300
hastag_int_tkn = 301
if_tkn = 302
while_tkn = 303
print_tkn = 304
return_tkn = 305
input_tkn = 306
and_tkn = 307
def_tkn = 308
global_tkn = 309
elif_tkn = 310
int_tkn = 311
or_tkn = 312
hastag_def_tkn = 313
else_tkn = 314
not_tkn = 315

#Errors

ERROR_FIRST_NUMBER_THEN_LETTER = 400 
ERROR_MORE_THAN_30_CHARACTERS = 410
ERROR_NOT_ACCEPTABLE_SYMBOL = 420
ERROR_LEFT_BLOCK_ALONE = 430
ERROR_RIGHT_BLOCK_ALONE = 440
ERROR_DIGIT_OUT_OF_LIMIT = 450
ERROR_EXCLMARK_ALONE = 460
ERROR_SLASH_ALONE = 470
ERROR_HASTAG_ALONE = 480
ERROR_COMMENT_OPENED_WITH_EOF = 490

###########################################################################################################################################################################
# O pinakas metavasewn symfwna me ton opoio dhmiourgeitai to peperasmeno automato thw glwssas cpy
# Exei oses grammes einai oi katastaseis kai oses sthles einai oi charakthres
# Gia kathe katastash elegxoume kathe charakthra pou tha doume gia to an:
# i) dwsei token
# ii) paei se allh katastash apthn opoia epanalambanoume ton elegxo
###########################################################################################################################################################################

pinakas_metavasewn = [
    #---------------------------------------------katastash_zero-------------------------------------------------#
    [katastash_letters,katastash_digits,EOF_tkn,katastash_zero,add_tkn,sub_tkn,katastash_equal,comma_tkn,mult_tkn,
    katastash_div,mod_tkn,katastash_hashtag,katastash_exclmark, katastash_lessthan,katastash_greaterthan,left_parenthesis_tkn,
    right_parenthesis_tkn,colon_tkn,ERROR_LEFT_BLOCK_ALONE,ERROR_RIGHT_BLOCK_ALONE,ERROR_NOT_ACCEPTABLE_SYMBOL,katastash_zero],
        
    #---------------------------------------------katastash_letters---------------------------------------------#
    [katastash_letters,katastash_letters,identifier_tkn,identifier_tkn,identifier_tkn,identifier_tkn,
    identifier_tkn,identifier_tkn,identifier_tkn,identifier_tkn,identifier_tkn,identifier_tkn,identifier_tkn,identifier_tkn,
    identifier_tkn,identifier_tkn,identifier_tkn,identifier_tkn,identifier_tkn, identifier_tkn,ERROR_NOT_ACCEPTABLE_SYMBOL,identifier_tkn],
        
    #---------------------------------------------katastash_digits---------------------------------------------#
    [ERROR_FIRST_NUMBER_THEN_LETTER,katastash_digits,digits_tkn,digits_tkn,digits_tkn,
    digits_tkn,digits_tkn,digits_tkn,digits_tkn,digits_tkn,digits_tkn,digits_tkn,digits_tkn,digits_tkn,digits_tkn,
    digits_tkn,digits_tkn,digits_tkn,digits_tkn,digits_tkn,ERROR_NOT_ACCEPTABLE_SYMBOL,digits_tkn],
        
    #---------------------------------------------katastash_equal---------------------------------------------#
    [assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,equal_tkn,assign_symb_tkn,assign_symb_tkn,
    assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,
    assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,assign_symb_tkn,ERROR_NOT_ACCEPTABLE_SYMBOL,assign_symb_tkn],

    #---------------------------------------------katastash_div---------------------------------------------#
    [ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,
    ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,div_tkn,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,
    ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_SLASH_ALONE,ERROR_NOT_ACCEPTABLE_SYMBOL,ERROR_SLASH_ALONE],

    #---------------------------------------------katastash_lessthan---------------------------------------------
    [lessthan_tkn,lessthan_tkn,lessthan_tkn,lessthan_tkn,lessthan_tkn,lessthan_tkn,lessOrequal_tkn,lessthan_tkn,lessthan_tkn,lessthan_tkn,
    lessthan_tkn,lessthan_tkn,lessthan_tkn,lessthan_tkn,lessthan_tkn,lessthan_tkn,lessthan_tkn,lessthan_tkn,
    lessthan_tkn,lessthan_tkn,ERROR_NOT_ACCEPTABLE_SYMBOL,lessthan_tkn],
        
    #---------------------------------------------katastash_greaterthan---------------------------------------------#
    [greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterORequal_tkn,greaterthan_tkn,
    greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,
    greaterthan_tkn,greaterthan_tkn,greaterthan_tkn,ERROR_NOT_ACCEPTABLE_SYMBOL,greaterthan_tkn],
        
    #---------------------------------------------katastash_exclmark---------------------------------------------#
    [ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,different_tkn,
    ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,
    ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,
    ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,ERROR_EXCLMARK_ALONE,
    ERROR_EXCLMARK_ALONE,ERROR_NOT_ACCEPTABLE_SYMBOL,ERROR_EXCLMARK_ALONE],
        
    #---------------------------------------------katastash_hashtag---------------------------------------------#
    [katastash_letters,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,
    ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,katastash_comment,ERROR_HASTAG_ALONE,
    ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,ERROR_HASTAG_ALONE,open_block_tkn,close_block_tkn,
    ERROR_NOT_ACCEPTABLE_SYMBOL,ERROR_HASTAG_ALONE],
        
    #---------------------------------------------katastash_comment---------------------------------------------#
    [katastash_comment,katastash_comment,ERROR_COMMENT_OPENED_WITH_EOF,katastash_comment,katastash_comment,katastash_comment,katastash_comment,
    katastash_comment,katastash_comment,katastash_comment,katastash_comment,katastash_close_comment,katastash_comment,katastash_comment,
    katastash_comment,katastash_comment,katastash_comment,katastash_comment,katastash_comment,katastash_comment,ERROR_NOT_ACCEPTABLE_SYMBOL,
    katastash_comment],
        
    #---------------------------------------------katastash__close_comment---------------------------------------------# 
    [katastash_comment,katastash_comment,ERROR_COMMENT_OPENED_WITH_EOF,katastash_comment,katastash_comment,katastash_comment,katastash_comment,
    katastash_comment,katastash_comment,katastash_comment,katastash_comment,katastash_zero,katastash_comment,katastash_comment,katastash_comment,
    katastash_comment,katastash_comment,katastash_comment,katastash_comment,katastash_comment,ERROR_NOT_ACCEPTABLE_SYMBOL,katastash_comment]
               
]

# Pinakas arxikopoihshs twn grammatwn
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Pinakas arxikopoihshs twn arithmwn
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


##########################################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# LEXICAL ANALYSIS STARTS HERE!
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
##########################################################################################################################################################################


#########################################################################################################################################################################
# Synarthseis elegxwn gia eukoloterh organwsh kai diaxeirish ths synarthshs lexical()
# Sygkekrimena, analoga tou ti charakthra tha dei h lexical(), kalei kai tis paraktw antistoixes synarthseis:
#########################################################################################################################################################################

##########################################################
# An h synarthsh lexical() dei gramma h psifio, kalei thn:
##########################################################

def characters(ch):
    if(ch in alphabet):
        ch = letters
    elif(ch in numbers):
        ch = digits
    return ch


##############################################################
# An h synarthsh lexical() dei arithmitiko telesth, kalei thn:
##############################################################

def arithmetic_op(ch):
    if(ch =='+'):
        ch = add
    elif(ch == '-'):
        ch = sub
    elif(ch == '='):
        ch = equal
    elif(ch == '*'):
        ch = mult
    elif(ch == '/'):
        ch = div
    elif(ch == '%'):
        ch = mod
    elif(ch == '<'):
        ch = less_than
    elif(ch == '>'):
        ch = greater_than
    return ch


############################################################################
# An h synarthsh lexical() dei opoiodhpote apta parakatw symbola, kalei thn:
############################################################################

def symbols(ch):
    if(ch == ','):
        ch = comma
    elif(ch == '#'):
        ch = hashtag
    elif(ch == '!'):
        ch = excl_mark
    elif(ch == '('):
        ch = left_parenthesis
    elif(ch == ')'):
        ch = right_parenthesis
    elif(ch == ':'):
        ch = colon
    elif(ch == '{'):
        ch = open_block
    elif(ch == '}'):
        ch = close_block
    return ch


###############################################################################################################################################################################
# Synarthseis elegxwn gia tis desmeymenes lekseis thw glwssas cpy
# Sygkekrimena, analoga me thn kathe leksh poy tha diabastei, epistrefoume to antistoixo token
# H omadopoihsh egine me bash thn genikh leitourgia twn desmeymenwn leksewn, opws blepete:
#############################################################################################################################################################################

################################################
# Gia desmeumenes lekseis gia dhlwsh metavlhtwn:
################################################

def current_tkn_declaration(word):
    if(word == 'main'):
        word = main_tkn
    elif(word == '#int'):
        word = hastag_int_tkn
    elif(word == 'if'):
        word = if_tkn
    elif(word == 'def'):
        word = def_tkn
    elif(word == 'global'):
        word = global_tkn
    elif(word == 'int'):
        word = int_tkn
    elif(word == '#def'):
        word = hastag_def_tkn
    return word


######################################################
# Gia desmeumenes lekseis gia elegxo rohs sthn cpy:
######################################################

def current_tkn_control_flow(word):
    if(word == 'if'):
        word = if_tkn
    elif(word == 'while'):
        word = while_tkn
    elif(word == 'elif'):
        word = elif_tkn
    elif(word == 'else'):
        word = else_tkn
    return word


#################################################################
# Gia desmeumenes lekseis gia In (input), Out (print) and Return:
#################################################################

def current_tkn_IOR(word):
    if(word == 'print'):
        word = print_tkn
    elif(word == 'return'):
        word = return_tkn
    elif(word == 'input'):
        word = input_tkn
    return word


################################################
# Gia desmeumenes lekseis gia logikes prakseis:
################################################

def current_tkn_logical_op(word):
    if(word == 'and'):
        word = and_tkn
    elif(word == 'or'):
        word = or_tkn
    elif(word == 'not'):
        word = not_tkn
    return word


##########################################################################################################################################################################
# Mesw ths generate_char(word, ch, katastash) elegxoume ton periorismo twn 30 prwtwn grammatwn pou anagnwrizontai kai an den upervainei to orio ki den vrisketai 
# se sygkekrimenes katastaseis, epanaliptika prosthetei enan-enan tous charakthres mexri na vrei token
###########################################################################################################################################################################

def generate_char(word, ch, katastash):
    if(len(word)>=30):
        katastash = ERROR_MORE_THAN_30_CHARACTERS
    else:
        if(katastash == katastash_comment or katastash == katastash_close_comment or katastash == katastash_zero):
            word = ''
        else: 
            word = word + ch
    return word, katastash


##########################################################################################################################################################################
# Mesw ths def digit_limit(katastash, word) elegxoume an kapoios arithmos exei upervei to kathorismeno orio [-32767, 32767]
###########################################################################################################################################################################

def digit_limit(katastash, word):
    if(katastash == digits_tkn):
        if(int(word) > 32767 or int(word) < -32767):
            katastash = ERROR_DIGIT_OUT_OF_LIMIT
    return katastash


# Ksekiname na metrame
line = 1

##########################################################################################################################################################################
# Ksekinaei h synarthsh lexical() opou paragontai ta tokens(3ada)
###########################################################################################################################################################################

def lexical():
    global katastash, word, reslexical, line
    katastash = katastash_zero          #trexousa katastash
    word = ''                           #edw tha apothikeftei to token
    reslexical = []                     #pinakas me to apotelesma ths synarthshs
    counter_line = line                 #metrhths gia kathe grammh tou arxeiou

    ##########################################################################################################################################################################
    # Oso vriskomaste se katastash (den exoume vrei akoma token) diavase ena charakthra
    ##########################################################################################################################################################################
    while(katastash >= 0 and katastash <= 10):
        ch = file.read(1)

        if(ch in alphabet):
            symbl_tkn = characters(ch)
        elif(ch in numbers):
            symbl_tkn = characters(ch)
        elif(ch == ''):
            symbl_tkn = EOF
        elif(ch == ' ' or ch == '\t'):
            symbl_tkn = white_character
        elif(ch == '+'):
            symbl_tkn = arithmetic_op(ch)
        elif(ch == '-'):
            symbl_tkn = arithmetic_op(ch)
        elif(ch == '='):
            symbl_tkn = arithmetic_op(ch)
        elif(ch == ','):
            symbl_tkn = symbols(ch)
        elif(ch == '*'):
            symbl_tkn = arithmetic_op(ch)
        elif(ch == '/'):
            symbl_tkn = arithmetic_op(ch)
        elif(ch == '%'):
            symbl_tkn = arithmetic_op(ch)
        elif(ch == '#'):
            symbl_tkn = symbols(ch)
        elif(ch == '!'):
            symbl_tkn = symbols(ch)
        elif(ch == '<'):
            symbl_tkn = arithmetic_op(ch)
        elif(ch == '>'):
            symbl_tkn = arithmetic_op(ch)
        elif(ch == '('):
            symbl_tkn = symbols(ch)
        elif(ch == ')'):
            symbl_tkn = symbols(ch)
        elif(ch == ':'):
            symbl_tkn = symbols(ch)
        elif(ch == '{'):
            symbl_tkn = symbols(ch)
        elif(ch == '}'):
            symbl_tkn = symbols(ch)
        elif(ch == '\n'):
            counter_line = counter_line + 1
            symbl_tkn = new_line
        else:
            symbl_tkn = not_acceptable_symbol


        #H trexousa katastash einai katastash or token
        katastash = pinakas_metavasewn[katastash][symbl_tkn]                   


        #Kaloume thn generate_char
        word, katastash = generate_char(word, ch, katastash)

    #Epistrefoume ton teleftaio xarakthra tou arxeiou kai ton afairoume
    if(katastash == digits_tkn or katastash ==  identifier_tkn or katastash == assign_symb_tkn or katastash == lessthan_tkn or katastash == greaterthan_tkn):
        if(ch == '\n'):
            counter_line = counter_line - 1
        file.seek(file.tell()-1, 0)
        word = word[:-1]
        
    ##########################################################################################################################################################################
    # Efoson eimaste sthn katastash 'identifier_tkn' elegxoume an anhkei se desmevmenh leksh
    ##########################################################################################################################################################################
    if(katastash == identifier_tkn):
        if(word == 'main'):
            katastash = current_tkn_declaration(word)
        elif(word == '#int'):
            katastash = current_tkn_declaration(word)
        elif(word == 'if'):
            katastash = current_tkn_control_flow(word)
        elif(word == 'while'):
            katastash = current_tkn_control_flow(word)
        elif(word == 'print'):
            katastash = current_tkn_IOR(word)
        elif(word == 'return'):
            katastash = current_tkn_IOR(word)
        elif(word == 'input'):
            katastash = current_tkn_IOR(word)
        elif(word == 'and'):
            katastash = current_tkn_logical_op(word)
        elif(word == 'def'):
            katastash = current_tkn_declaration(word)
        elif(word == 'global'):
            katastash = current_tkn_declaration(word)
        elif(word == 'elif'):
            katastash = current_tkn_control_flow(word)
        elif(word == 'int'):
            katastash = current_tkn_declaration(word)
        elif(word == 'or'):
            katastash = current_tkn_logical_op(word)
        elif(word == '#def'):
            katastash = current_tkn_declaration(word)
        elif(word == 'else'):
            katastash = current_tkn_control_flow(word)
        elif(word == 'not'):
            katastash = current_tkn_logical_op(word)

    #Kaloume thn digit_limit
    katastash = digit_limit(katastash, word)

    
    ##########################################################################################################################################################################
    # Elegxos se periptwsh pou vrethoume stis katstaseis pou antiproswpevoun errors kai kanoume ta analoga print() gia kathe periptwsh
    ##########################################################################################################################################################################
    if(katastash == ERROR_FIRST_NUMBER_THEN_LETTER):
        print("ERROR -- Letter detected after a number")
    elif(katastash == ERROR_MORE_THAN_30_CHARACTERS):
        print("ERROR -- Appearance of a word with more than 30 characters")
    elif(katastash == ERROR_NOT_ACCEPTABLE_SYMBOL):
        print("ERROR -- Not acceptable symbol")
    elif(katastash == ERROR_LEFT_BLOCK_ALONE):
        print("ERROR -- Appearance of { symbol alone")
    elif(katastash == ERROR_RIGHT_BLOCK_ALONE):
        print("ERROR -- Appearance of } symbol alone")
    elif(katastash == ERROR_DIGIT_OUT_OF_LIMIT):
        print("ERROR -- Number detected out if the (-32767, 32767) limit")
    elif(katastash == ERROR_EXCLMARK_ALONE):
        print("ERROR -- Appearance of ! symbol alone")
    elif(katastash == ERROR_SLASH_ALONE):
        print("ERROR -- Appearence of / symbol alone")
    elif(katastash == ERROR_HASTAG_ALONE):
        print("ERROR -- Apearance of # symbol alone")
    elif(katastash == ERROR_COMMENT_OPENED_WITH_EOF):
        print("ERROR -- Opening of the comment was succesful but no closing of it was detected at the end of the file ")

    #Prosthetoume sth lista me ta apotelesmata thn 1)grammh tou arxeiou, 2)to token kai 3)thn katstash
    reslexical.insert(0, counter_line)
    reslexical.insert(1, word)
    reslexical.insert(2, katastash)
    
    line = counter_line
    print(reslexical)       ##print the results of reslexical
    return reslexical


##########################################################################################################################################################################
# Klhsh ths lexical() wste na emfanistoune ola ta tokens sthn othonh kai elegxos oti h lexixal() doulevei swsta
##########################################################################################################################################################################
##while(1):
    ##reslexic = lexical()
    ##if(reslexic[2] == EOF_tkn):
        ##break
    ##print(reslexic)



##########################################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# SYNTAX ANALYSIS STARTS HERE!
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
##########################################################################################################################################################################


def syntax():                   # H kiria sinartisi pou ksekina tin analisi tou programmatos kai kalei tous katallilous kanones.
    global line, reslexic

    def startRule():            # Arxikopoiei to main scope kai ksekina tin analisi diloseon, sinartiseon
                                # kai tin klisi tis kirias sinartisis.
        makeScope('main')

        declarations()
        def_functions_declaration_part() 
        call_main_part()

    def def_functions_declaration_part():   # Anagnorizei kai epeksergazetai tis diloseis sinartiseon mesa sto programma.
        global reslexic
        while(reslexic[2] == def_tkn):
             def_function()
            
    def def_function():                     # Analyei ti sintaksi mias sinartisis, epivevaionontas oti periexei ta aparetita stoixeia
        global line, reslexic               # (onoma, parametrous, soma).
        if(reslexic[2] == def_tkn):
            reslexic = lexical()
            line = reslexic[0]

            if(reslexic[2] == identifier_tkn):
                name = reslexic[1]
                reslexic = lexical()
                line = reslexic[0]

                if(reslexic[2] == left_parenthesis_tkn):
                    reslexic = lexical()
                    line = reslexic[0]

                    ent = Entity()
                    ent.type = 'FUNC'
                    ent.name = name
                    ent.function.type = 'Function'
                    makeEntity(ent)

                    id_list(0)

                    if(reslexic[2] == right_parenthesis_tkn):
                        reslexic = lexical()
                        line = reslexic[0]

                        if(reslexic[2] == colon_tkn):
                            reslexic = lexical()
                            line = reslexic[0]

                            if(reslexic[2] == open_block_tkn):
                                reslexic = lexical()
                                line = reslexic[0]

                                makeScope(name)
                                addParam()

                                declarations()

                                while(reslexic[2] == def_tkn):
                                    def_function()

                                global_decl()

                                calcStartQuad()
                                genquad('begin_block', name, '_', '_')
                                statements()
                                calcFrameLength()
                                genquad('end_block', name, '_', '_')
                                printSymbTable()
                                
                                deleteScope()

                                if(reslexic[2] == close_block_tkn):
                                    reslexic = lexical()
                                    line = reslexic[0]
                                else:
                                    print("ERROR -- Missing '#}' after function's statements in line", line)
                                    exit(1)

                            else:
                                print("ERROR -- Missing '#{' before function's declarations in line", line)
                                exit(1)

                        else:
                            print("ERROR -- Missing ':' after '()'  of the function's name in line", line)
                            exit(1)

                    else:
                        print("ERROR -- Missing right parenthesis ')' after the function's name in line", line)
                        exit(1)

                else:
                    print("ERROR -- Missing left parenthesis '(' after the function's name in line", line)
                    exit(1)

            else:
                print("ERROR -- Missing function's name in line", line)
                exit(1)

        else:
            print("ERROR -- Missing 'def' at the start of the program in line", line)
            exit(1)
    
    def declarations():            # Epeksergazetai tis diloseis metabliton.
        global reslexic
        
        while(reslexic[2] == hastag_int_tkn):
            declaration_line()

    def declaration_line():         # Analyei ti syntaxi mias grammis dilosis metablitis.
        global reslexic, line

        if(reslexic[2] == hastag_int_tkn):
            reslexic = lexical()
            line = reslexic[0]

            id_list(1)

    def global_decl():              # Epeksergazetai tis diloseis katholikon metabliton
        global reslexic

        while(reslexic[2] == global_tkn):
            global_decl_line()

    def global_decl_line():         # Analyei ti syntaxi mias grammis dilosis katholikis metablitis.
        global reslexic, line

        if(reslexic[2] == global_tkn):
            reslexic = lexical()
            line = reslexic[0]

            id_list(2)

    def statement():                # Anagnorizei kai epeksergazetai mia entoli 
        global reslexic, line

        if(reslexic[2] == identifier_tkn or reslexic[2] == print_tkn or reslexic[2] == return_tkn):
            simple_statement()
        elif(reslexic[2] == while_tkn or reslexic[2] == if_tkn):
            structured_statement()
        else:
            print("ERROR -- Incorrect statement given in line", line)
            exit(1)

    def statements():               # Analyei mia akolouthia entolon.
        global reslexic

        statement()

        while(reslexic[2] == identifier_tkn or reslexic[2] == print_tkn or reslexic[2] ==return_tkn or reslexic[2] ==while_tkn or reslexic[2] == if_tkn ):
            statement()
        
    def simple_statement():         # Epeksergazetai aples entoles
        global reslexic

        if(reslexic[2] == identifier_tkn):
            assignment_stat()
        elif(reslexic[2] == return_tkn):
            return_stat()
        elif(reslexic[2] == print_tkn):
            print_stat()

    def structured_statement():     # Epeksergazetai domimenes entoles opos epanalipseis kai synthikes.
        global reslexic

        if(reslexic[2] == while_tkn):
            while_stat()
        elif(reslexic[2] == if_tkn):
            if_stat()

    def assignment_stat():          # Analyei entoles anathesis timwn se metablites.
        global reslexic, line

        if(reslexic[2] == identifier_tkn):
            identfr = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

            if(reslexic[2] == assign_symb_tkn):
                reslexic = lexical()
                line = reslexic[0]

                ####### S -> input(id){P1} #######
                if(reslexic[2] == int_tkn):
                    reslexic = lexical()
                    line = reslexic[0]

                    #{P1}
                    genquad('inp', identfr, '_', '_')

                    if(reslexic[2] == left_parenthesis_tkn):
                        reslexic = lexical()
                        line = reslexic[0]

                        if(reslexic[2] == input_tkn):
                            reslexic = lexical()
                            line = reslexic[0]

                            if(reslexic[2] == left_parenthesis_tkn):
                                reslexic = lexical()
                                line = reslexic[0]
                                
                                if(reslexic[2] == right_parenthesis_tkn):
                                    reslexic = lexical()
                                    line = reslexic[0]

                                    if(reslexic[2] == right_parenthesis_tkn):
                                        reslexic = lexical()
                                        line = reslexic[0]

                                    else:
                                        print("ERROR -- Missing ')' in line", line)
                                        exit(1)
                                    
                                else:
                                    print("ERROR -- Missing ')' in line", line)
                                    exit(1)

                            else:
                                print("ERROR -- Missing input in line", line)
                                exit(1)

                        else:
                            print("ERROR -- Missing '(' in line", line)
                            exit(1)

                    else:
                        print("ERROR -- Missing '( in line", line)
                        exit(1)

                ####### S -> id:=E{P1}; #######
                else:
                    #{P1}
                    Eplace = expression()
                    genquad(':=', Eplace, '_', identfr)

            else:
                print("ERROR -- Missing '=' after identifier in line", line)
                exit(1)

        else:
            print("ERROR -- Missing identifier in line", line)
            exit(1)

    def print_stat():               # Analyei entoles ektyposis timhs.
        ####### S -> print(E){P2} ####### 
        global line, reslexic

        if(reslexic[2] == print_tkn):
            reslexic = lexical()
            line = reslexic[0]

            if(reslexic[2] == left_parenthesis_tkn):
                reslexic = lexical()
                line = reslexic[0]

                #{P2}
                Eplace = expression()
                genquad('out', Eplace, '_', '_')

                if(reslexic[2] == right_parenthesis_tkn):
                    reslexic = lexical()
                    line = reslexic[0]

                else:
                    print("ERROR -- Missing ')' in 'print' statement in line", line)
                    exit(1)

            else:
                print("ERROR -- Missing '(' in 'print' statement in line", line)
                exit(1)

        else:
            print("ERROR -- Missing 'print' statement in line", line)
            exit(1)

    def return_stat():              # Analyei entoles epistrofis timhs apo sinartisi.
        ####### S -> return(E){P1} #######
        global reslexic, line

        if(reslexic[2] == return_tkn):
            reslexic = lexical()
            line = reslexic[0]

            #{P1}
            Eplace = expression()
            genquad('retv', Eplace, '_', '_')

        else:
            print("ERROR -- Missing 'return' statement in line", line)
            exit(1)

    def if_stat():              # Analyei synthikes if-elif-else kai ta somata ton entolon tous.
        ####### S -> if B then {P1} S1 {P2} TAIL {P3} #######

        global reslexic, line

        if(reslexic[2] == if_tkn):
            reslexic = lexical()
            line = reslexic[0]

            tempList = emptylist()

            B = condition()

            #{P1}
            backpatch(B[0], nextquad())

            if(reslexic[2] == colon_tkn):
                reslexic = lexical()
                line = reslexic[0]

                if(reslexic[2] == open_block_tkn):
                    reslexic = lexical()
                    line = reslexic[0] 

                    statements()

                    #{P2}
                    ifList = makelist(nextquad())
                    genquad('jump', '_', '_', '_')
                    tempList = merge(tempList, ifList)
                    backpatch(B[1], nextquad())

                    if(reslexic[2] == close_block_tkn):
                        reslexic = lexical() 
                        line =  reslexic[0]

                    else:
                        print("ERROR -- Missing '#}' after 'if' statements in line", line)
                        exit(1)

                else:
                    statement()
                    
                    #{P2}
                    ifList = makelist(nextquad())
                    genquad('jump', '_', '_', '_')
                    tempList = merge(tempList, ifList)
                    backpatch(B[1], nextquad())

                while(reslexic[2] == elif_tkn):
                    reslexic = lexical()
                    line = reslexic[0]

                    B = condition()

                    #{P1}
                    backpatch(B[0], nextquad())

                    if(reslexic[2] == colon_tkn):
                        reslexic = lexical()
                        line = reslexic[0]

                        if(reslexic[2] == open_block_tkn):
                            reslexic = lexical()
                            line = reslexic[0]

                            statements()

                            #{P2}
                            ifList = makelist(nextquad())
                            genquad('jump', '_', '_', '_')
                            tempList = merge(tempList, ifList)
                            backpatch(B[1], nextquad())

                            if(reslexic[2] == close_block_tkn):
                                reslexic = lexical()
                                line = reslexic[0]

                            else:
                                print("ERROR -- Missing '#} after 'elif' statements in line", line)
                                exit(1)

                        else:
                            statement()

                            #{P2}
                            ifList = makelist(nextquad())
                            genquad('jump', '_', '_', '_')
                            tempList = merge(tempList, ifList)
                            backpatch(B[1], nextquad())
                    else:
                        print("ERROR -- Missing ':' after 'elif' condition in line", line)
                        exit(1)
                        
                if(reslexic[2] == else_tkn):
                    ####### TAIL -> else S2 | TAIL -> ε #######
                    reslexic = lexical()
                    line = reslexic[0]

                    if(reslexic[2] == colon_tkn):
                        reslexic = lexical()
                        line = reslexic[0]

                        if(reslexic[2] == open_block_tkn):
                            reslexic = lexical()
                            line = reslexic[0]

                            statements()
                            
                            #{P3}
                            backpatch(tempList, nextquad())

                            if(reslexic[2] == close_block_tkn):
                                reslexic = lexical()
                                line = reslexic[0]

                            else:
                                print("ERROR -- Missing '#}' after 'if' statements in line", line)
                                exit(1)
                            
                        else:
                            statement()

                            #{P3}
                            backpatch(tempList, nextquad())

                    else:
                        print("ERROR -- Missing ':' after 'else' condition in line", line)
                        exit(1)
                else:
                    #{P3}
                    backpatch(tempList, nextquad())

            else:
                print("ERROR -- Missing ':' after 'if' condition in line", line)
                exit(1)
                
        else:
            print("ERROR --  Missing 'if' condition in line", line)
            exit(1)

    def while_stat():           #Analyei entoles epanalipsis while kai to soma ton entolon tous.
        ####### S -> while {P1} B do {P2} S1 {P3}

        global line, reslexic

        if(reslexic[2] == while_tkn):
            reslexic = lexical()
            line = reslexic[0]

            #{P1}
            Bquad = nextquad()
            B = condition()
            #{P2}
            backpatch(B[0], nextquad())

            if(reslexic[2] == colon_tkn):
                reslexic = lexical()
                line = reslexic[0]

                if(reslexic[2] == open_block_tkn):
                    reslexic = lexical()
                    line = reslexic[0]

                    statements()
                    #{P3}
                    genquad('jump', '_','_', Bquad)
                    backpatch(B[1], nextquad())

                    if(reslexic[2] == close_block_tkn):
                        reslexic = lexical()
                        line = reslexic[0]
                    else:
                        print("ERROR -- Missing '#}' after 'while' condition in line", line)
                        exit(1)

                else:
                    statement()
                    #{P3}
                    genquad('jump', '_','_', Bquad)
                    backpatch(B[1], nextquad())
                
            else:
                print("ERROR -- Missing':' after 'while' condition in line", line)
                exit(1)
        
        else:
            print("ERROR -- Missing 'while' condition in line", line)
            exit(1)

    def id_list(flag):      # Anagnorizei kai epeksergazetai mia lista apo id (onomata metablitwn h parametrwn).
        global line, reslexic

        if(reslexic[2] == identifier_tkn):
            name = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

            if(flag == 1):
                ent = Entity()
                ent.type = 'VAR'
                ent.name = name
                ent.variable.offset = calcOffset()
                makeEntity(ent)
            elif(flag == 0):
                arg = Argument()
                arg.name = name
                arg.parMode = 'CV'
                makeArgument(arg)

            while(reslexic[2] == comma_tkn):
                reslexic = lexical()
                line = reslexic[0]
                
                if(reslexic[2] == identifier_tkn):
                    reslexic = lexical()
                    line = reslexic[0]

                else:
                    print("ERROR -- No identification token after comma in line",line)
                    exit(1)

    def expression():       # Analyei kai aksiologei ekfraseis arithmitikes h logikes.
        ####### E -> T1(+- T2 {P1})* {P2} #######
        global reslexic,line

        optional_sign()
        T1place = term()

        while(reslexic[2] == add_tkn or reslexic[2] == sub_tkn):
            addOrSub = ADD_OP()
            T2place = term()

            #{P1}
            w = newTemp()
            genquad(addOrSub, T1place, T2place, w)
            T1place = w
        #{P2}
        Eplace = T1place
        return Eplace
    
    def ADD_OP():           # Anagnorizei kai epistrefei to symvolo tis prostheisis h afairesis.
        global line, reslexic

        if(reslexic[2] == add_tkn):
            opAdd = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]
        
        elif(reslexic[2] == sub_tkn):
            opAdd = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        return opAdd


    def MUL_OP():           # Anagnorizei kai epistrefei to symvolo tou pollaplasiasmou, tis diairesis h tou ypoloipou.
        global line, reslexic

        if(reslexic[2] == mult_tkn):
            opMulOrDiv = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]
        
        elif(reslexic[2] == div_tkn):
            opMulOrDiv = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        elif(reslexic[2] == mod_tkn):
            opMulOrDiv = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        return opMulOrDiv

    def term():             # Analyei kai axiologei ena arithmitiko oro, o opoios mporei na periexei pollaplasiasmo i diairesi
        ####### T -> F1(X F2 {P1})* {P2} #######
        global reslexic,line

        F1place = factor()

        while(reslexic[2] == mult_tkn or reslexic[2] == div_tkn or reslexic[2] == mod_tkn):
            multOrDivsn = MUL_OP()
            F2place = factor()

            #{P1}
            w = newTemp()
            genquad(multOrDivsn, F1place, F2place, w)
            F1place = w
        
        #{P2}
        Tplace = F1place
        return Tplace

    def factor():       # Analyei kai axiologei enan paragonta, o opoios mporei na einai arithmos, ekfrasi se parenthesi h id/taftotitis.
        global reslexic, line

        ####### F -> (E){P1} #######
        if(reslexic[2] == digits_tkn):
            factr = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        elif(reslexic[2] == left_parenthesis_tkn):
            reslexic = lexical()
            line = reslexic[0]

            #{P1}
            Eplace = expression()
            factr = Eplace

            if(reslexic[2] == right_parenthesis_tkn):
                reslexic = lexical()
                line = reslexic[0]

            else:
                print("ERROR -- Missing right parenthesis ')' in line", line)
                exit(1)

        ####### F -> id{P1} #######
        elif(reslexic[2] == identifier_tkn):
            #{P1}
            fact_temp = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

            factr = idtail(fact_temp)

        else:
            print("ERROR -- Missing Expression or Variable or Constant in line", line)
            exit(1)
        
        return factr

    def idtail(assign_idtail):
        global line, reslexic

        if(reslexic[2] == left_parenthesis_tkn):
            reslexic = lexical()
            line = reslexic[0]

            actual_par_list()
            w = newTemp()
            genquad('par', w, 'RET', '_')
            genquad('call', assign_idtail, '_', '_')

            if(reslexic[2] == right_parenthesis_tkn):
                reslexic = lexical()
                line = reslexic[0]
                return w

            else:
                print("ERROR -- Missing right parenthesis ')' in line", line)
                exit(1)

        else:
            return assign_idtail

    def actual_par_list():      # Anagnorizei kai epeksergazetai ti lista parametron kata tin klisi mias sinartisis
        global line, reslexic

        if(reslexic[2] == digits_tkn or reslexic[2] == left_parenthesis_tkn or reslexic[2] == identifier_tkn):

            assign_expression = expression()
            genquad('par', assign_expression, 'CV', '_')

            while(reslexic[2] == comma_tkn):
                reslexic = lexical()
                line = reslexic[0]

                assign_expression = expression()
                genquad('par', assign_expression, 'CV', '_')

    def optional_sign():          # Anagnorizei proairetiko prosimo (thetiko i arnitiko) brosta apo arithmo i ekfrasi.
        global reslexic

        if(reslexic[2] == add_tkn or reslexic[2] == sub_tkn):
            ADD_OP()

    def condition():            # Analyei kai axiologei logikes synthikes
        ####### B -> Q1{P1}(or{P2}Q2{P3})* #######
        
        global line, reslexic

        #{P1}
        BTrue = []
        BFalse = []

        Q1 = bool_term()

        BTrue = Q1[0]
        BFalse = Q1[1]

        while(reslexic[2] == or_tkn):
            reslexic = lexical()
            line = reslexic[0]

            #{P2}
            backpatch(BFalse, nextquad())

            Q2 = bool_term()

            #{P3}
            BTrue = merge(BTrue, Q2[0])
            BFalse = Q2[1]
        
        return BTrue, BFalse

    def bool_term():        # Analyei kai axiologei logikous orous pou syndyazontai me to AND.
        global line, reslexic

        QTrue = []
        QFalse = []

        R1 = bool_factor()

        QTrue = R1[0]
        QFalse = R1[1]

        while(reslexic[2] == and_tkn):
            reslexic = lexical()
            line = reslexic[0]

            backpatch(QTrue, nextquad())

            R2 = bool_factor()

            
            QFalse = merge(QFalse, R2[1])
            QTrue = R2[0]
            
        return QTrue, QFalse

    def bool_factor():      # Analyei kai axiologei logikous paragontes.
        global line, reslexic

        RTrue = []
        RFalse = []

        if(reslexic[2] == not_tkn):
        ####### R -> (B){P1} #######
            
            reslexic = lexical()
            line = reslexic[0]

            B = condition()
            #{P1}
            RTrue = B[1]
            RFalse = B[0]
        
        else:
        ####### R -> E1 relop E2 {P1} #######   
            E1Place = expression()
            relop = REL_OP()
            E2Place = expression()

            #{P1}
            RTrue = makelist(nextquad())
            genquad(relop, E1Place, E2Place, '_')
            RFalse = makelist(nextquad())
            genquad('jump', '_', '_', '_')

        return RTrue, RFalse
    

    def REL_OP():           # Anagnorizei kai epistrefei to symvolo logikis sigkrisis (p.x., <, >, =).
        global line, reslexic

        if(reslexic[2] == equal_tkn):
            relop = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        elif(reslexic[2] == lessthan_tkn):
            relop = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        elif(reslexic[2] == lessOrequal_tkn):
            relop = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        elif(reslexic[2] == different_tkn):
            relop = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        elif(reslexic[2] == greaterthan_tkn):
            relop = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        elif(reslexic[2] == greaterORequal_tkn):
            relop = reslexic[1]
            reslexic = lexical()
            line = reslexic[0]

        else:
            print("ERROR -- Some of the following symbols is/are missing: <, >, <=, <>, >=  in line", line)
            exit(1)

        return relop

    def call_main_part():       # Analyei kai epeksergazetai tin klisi tis kyrias sinartisis (main) tou programmatos.
        global line, reslexic

        if(reslexic[2] == hastag_def_tkn):
            reslexic = lexical()
            line = reslexic[0]

            if(reslexic[2] == main_tkn):
                reslexic = lexical()
                line = reslexic[0]

                declarations()

                genquad('begin_block', 'main', '_', '_')
                statements()
                genquad('halt', '_', '_', '_')
                genquad('end_block', 'main', '_', '_')

                printSymbTable()
                
                deleteScope()

            else:
                print("ERROR -- Missing main in line", line)
                exit(1)

        else:
            print("ERROR -- Missing '#def' in line", line)
            exit(1)

    reslexic = lexical()
    line = reslexic[0]

    startRule()

##########################################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# SYNARTHSEIS GIA TON ENDIAMESO KWDIKA
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
##########################################################################################################################################################################   
global listOfQuads      
listOfQuads = []        ##periexei oles tis tetrades
quadCounter = 1         ##metrhths gia ton arithmo twn tetradwn
listOfQuadsFinal = []

def nextquad():         ## epistrefei ton arithmo ths epomenhs tetradas
    global quadCounter
    x = quadCounter

    return x

def genquad(op, x, y, z):       ##paragei tetrada
    global quadCounter, listOfQuads, listOfQuadsFinal
    list = []

    list = [nextquad()]
    list.extend([op, x, y, z])
    
    listOfQuads += [list]
    quadCounter = quadCounter + 1
    listOfQuadsFinal += [list]

    return list

i = 1
tempVarList = []        ##lista me tis proswrines metavlhtes

def newTemp():      ##dhmiourgei nea proswrinh metavlhth
    global i
    global tempVarList

    varTemp = 'T_' + str(i)
    i = i + 1

    tempVarList += [varTemp]

    ent = Entity()
    ent.type = 'TEMP'
    ent.name = varTemp
    ent.temp_var.offset = calcOffset()
    makeEntity(ent)
    
    return varTemp


def emptylist():
    
    listEmpty = []
    return listEmpty


def makelist(x):

    return [x]

def merge(list1, list2):
    lista = []
    lista += list1 + list2
    return lista

def backpatch(list, z):         ##episkeptetai terades pou den exoun symplhrwmeno to 4o teloumeno kai to antikathistoun me z
    global listOfQuads

    for index in list:
        for quad in listOfQuads:
            if index == quad[0] and quad[4] == '_':
                quad[4] = z
                break
    return

##########################################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# SYMBOLS TABLE STARTS HERE!
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
##########################################################################################################################################################################

listScp = []

class Entity():         # antiprosopeuei ena stoixeio ston pinaka symbolon.
    def __init__(self):
        self.name = ''
        self.type = ''

        self.function = self.Function()
        self.variable = self.Variable()
        self.temp_var = self.VarTemp()
        self.parameter = self.Parameter()
        

    class Function:     # antiprosopeuei mia synarthsh ston pinaka symbolon.
        def __init__(self):
            self.startQuad = 0
            self.argument = []
            self.framelength = 0

    class Variable:     # antiprosopeuei mia metavlhth ston pinaka symbolon.
        def __init__(self):
            self.offset = 0
    
    class VarTemp:      # antiprosopeuei mia prosorinh metavlhth ston pinaka symbolon.
        def __init__(self):
            self.offset = 0

    class Parameter:    # antiprosopeuei mia parametro ston pinaka symbolon.
        def __init__(self):
            self.offset = 0

class Argument():       # antiprosopeuei mia parametro ston pinaka symbolon
      def __init__(self):
          self.name = ''


class Scope():          # antiprosopeuei ena pedio embeleias ston pinaka symbolon
    def __init__(self):
        self.entity = []
        self.name = ''
        self.nestingLevel = 0



def makeArgument(object):                       # Synarthsh pou dimiourgei mia parametro sto pedio emveleias.
    global listScp, arg

    arg = listScp[-1].entity[-1].function       # Apothikevei to trexon pedio emveleias stin metavlith arg.
    arg.argument.append(object)                 # Prostethei to antikeimeno object sti lista ton orismaton tis synartisis i diadikasias.


def makeEntity(object):                         # Synartisi pou dimiourgei mia ontotita sto pedio emveleias.
    global listScp, ent

    ent = listScp[-1].entity                    # Apothikevei to trexon pedio emveleias stin metavlith ent.
    ent.append(object)                          # Prostethei to antikeimeno object sto pedio emveleias.


def makeScope(name):                            # Synartisi pou dimiourgei ena neo pedio emveleias.
    global listScp

    nextSc = Scope()                            # Dimiourgei ena neo pedio emveleias.

    if listScp:                                 # An yparxei idi pedio emveleias, afksanei to epipedo emveleias kata ena.

        nextSc.nestingLevel = listScp[-1].nestingLevel + 1      # Orizei to onoma tou pediou emveleias. 
    else:                                                       # Prosthetei to neo pedio emveleias sti lista pedion emveleias.
        nextSc.nestingLevel = 0

    nextSc.name = name
    listScp.append(nextSc)

def deleteScope():                              # Synartisi pou diagrafi to trexon pedio emveleias.
    global listScp

    delScope = listScp.pop() 
    del delScope

def calcOffset():                               # Synartisi pou ypologizei to offset gia metavlites, parametrous kai prosorines metavlites.
    global listScp, w

    counter = 0
    w = listScp[-1].entity

    if(w is not []):                            # An to pedio emveleias den einai keno.
        for ent in (listScp[-1].entity):
            if(ent.type == 'TEMP' or ent.type == 'PARAM' or ent.type == 'VAR'): 
                counter += 1                    # An i ontotita einai prosorini metavliti, parametro h genika metavliti, afksanei ton counter.

    offset =(4 * counter) + 12                  # Ypologizei to offset.

    return offset

def calcStartQuad():                           # Synartisi pou ypologizei tin arxiki dieuthinsi tis tetrapletas gia ti synartisi.
    global listScp, y

    y = listScp[-2].entity[-1]                 # Orizei tin arxiki dieuthinsi tis tetrapletas gia tin teleutaia synartisi sto proigoumeno pedio emveleias.
    y.function.startQuad = nextquad()

def calcFrameLength():                         # Synartisi pou ypologizei to mikos tou plaisiou (frame length) gia ti synartisi.
    global listScp, x

    x = listScp[-2].entity[-1]                 # Ypologizei to mikos tou plaisiou gia tin teleutaia synartisi sto proigoumeno pedio emveleias.
    x.function.framelength = calcOffset()

def addParam():                                        # Prostethei parametrous se mia synartisi pou vrisketai sto proigoumeno pedio emveleias
    global listScp, par

    par = listScp[-2].entity[-1]                       # Anakta tin teleutaia synartisi sto proigoumeno pedio emveleias

    for arg in par.function.argument:                  # Gia kathe parametro tis synartisis
        ent = Entity()                                 # Dimiourgei mia nea ontotita
        ent.type = 'PARAM'                             # Orizei tin ontotita os parametro
        ent.name = arg.name                            # Anathetei to onoma tis parametrou stin ontotita
        ent.parameter.offset = calcOffset()            # Ypologizei kai anathetei to offset tis parametrou
        makeEntity(ent)                                # Prostethei tin ontotita sti lista ontotiton tou trexontos pediou emveleias
        ent.parameter.parMode = 'CV'                   # Orizei ti methodo perasmatos parametrou os Call by Value (CV)



##########################################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# SYNARTISEIS GIA TELIKO KWDIKA
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
##########################################################################################################################################################################
#ascF = open('asc-file.asm', 'w')                   # Anoigei to arxeio 'asc-file.asm' gia eggrafh
#ascF.write('         \n\n\n')

#def loadvr(v, r):                                  # Synarthsh gia fortwsh mias metavlhths ston kataxwrhth
    #global listScp, ascF

    #if v.isdigit():                               
        #ascF.write('li t%d, %s\n' % (r, v))
    #else:
        ###else if v is variable                    

#def storerv(r, v):                                 # Synarthsh gia apothikeush ths timhw apo ton kataxwrhth se mia metavlhth
    #global listScp, ascF

#line = -1

#def prod_final():                                  # Synarthsh gia paragwgh tou telikou kwdika apo tis tetrades 
    #global listScp, line, listOfQuads, ascF
    
    #relop = {                                     
        #'>' : 'bgt',
        #'<' : 'blt',
        #'==' : 'beq',
        #'!=' : 'bne',
        #'<=' : 'ble',
        #'>=' : 'bge'
    #}

    #op = {                                         
        #'+' : 'add',
        #'-' : 'sub',
        #'*' : 'mul',
        #'//' : 'div',
        #'%' : 'rem'
    #}

    #in_out = {                                      
    #}

    #for i in range(len(listOfQuads)):              # Prospelash twn mexri stigmhs tetradwn kai elegxos tis kathe tetradas gia tin paragwgh telikou kwdika
        #ascF.write('L' + str(listOfQuads[i][0]) + ': \n')  # 
        
        #if(listOfQuads[i][1] in relop):            
            #loadvr(listOfQuads[i][2], 1)          
            #loadvr(listOfQuads[i][3], 2)
            #ascF.write(relop[listOfQuads[i][1]] + ', t1, t2, L' + str(listOfQuads[i][4]) + '\n')  
        
        #elif(listOfQuads[i][1] == 'jump'):        
            #ascF.write('b L' + str(listOfQuads[i][4]) + '\n')
        
        #elif(listOfQuads[i][1] in op):             
            #loadvr(listOfQuads[i][2], 1)           
            #loadvr(listOfQuads[i][3], 2)
            #ascF.write(op[listOfQuads[i][1]] + ', t1, t1, t2\n')  
            #storerv(1, listOfQuads[i][4])          
        
        #elif(listOfQuads[i][1] == ':='):    
            #loadvr(listOfQuads[i][2], 1)  
            #storerv(1, listOfQuads[i][3]) 
        
        #elif (listOfQuads[i][1] == 'retv'):        
            #loadvr(listOfQuads[i][2], 1)           
            #ascF.write('lw t0,-8(sp)\n')           
            #ascF.write('sw t1,(t0)\n')
        
        #elif (listOfQuads[i][1] == 'inp'):        
            #ascF.write('li a7, 5\n')
            #ascF.write('ecall\n')
            #ascF.write('mv t1, a0\n')
        
        #elif (listOfQuads[i][1] == 'out'):        
            #loadvr(listOfQuads[i][2], 1)
            #ascF.write('li a7, 1\n')
            #ascF.write('ecall\n')
        
        #elif (listOfQuads[i][1] == 'begin_block' and listScp[-1].nestingLevel != 0): 
            #ascF.write('sw ra,(sp)\n') 
        
        #elif (listOfQuads[i][1] == 'end_block' and listScp[-1].nestingLevel != 0): 
            #ascF.write('lw ra,(sp)\n') 
            #ascF.write('jr ra\n')
        
        #elif (listOfQuads[i][1] == 'halt'): 
            #ascF.write('li a0, 0\n')
            #ascF.write('li a7, 93\n')
            #ascF.write('ecall\n')

    #listOfQuads = []  

        
        
##########################################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# SYNARTHSEIS GIA GRAPSIMO SE ARXEIA .int KAI .sym
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
##########################################################################################################################################################################

def printSymbTable():               # Typwnei ton pinaka symbolwn se ena arxeio .sym
    global listScp, symFile

    for scp in reversed(listScp):
        symFile.write("Scope: name: " + scp.name + " | nestingLevel: " + str(scp.nestingLevel) + "\n")
        symFile.write("\tEntities:\n")

        for ent in scp.entity:
            if ent.type == 'VAR':
                symFile.write("\t- Variable: name: " + ent.name + " | Type: " + ent.type + " | Offset: " + str(ent.variable.offset) + "\n")
            
            elif ent.type == 'FUNC':
                symFile.write("\t- Function: name: " + ent.name + " | Type: " + ent.type + " | Function type: " + ent.function.type + " | StartQuad: " + str(ent.function.startQuad) + " | FrameLength: " + str(ent.function.framelength) + "\n")
                symFile.write("\t\tArguments:\n")
				
                for arg in ent.function.argument:
                    symFile.write("\t\t- Argument: name: " + arg.name + " | Parameter Mode: " + arg.parMode + "\n")
            
            elif ent.type == 'TEMP':
                symFile.write("\t- Temporary Variable: name: " + ent.name + " | Type: " + ent.type + " | Offset: " + str(ent.temp_var.offset) + "\n")

            elif ent.type == 'PARAM':
                symFile.write("\t- Parameter: name: " + ent.name + " | Type: " + ent.type + " | Mode: " + ent.parameter.parMode + " | Offset: " + str(ent.parameter.offset) + "\n")

def intC(intFile):
    for i in range(len(listOfQuadsFinal)):
        q = listOfQuadsFinal[i]
        intFile.write(str(q[0]))
        intFile.write(":  ")
        intFile.write(str(q[1]))
        intFile.write("  ")
        intFile.write(str(q[2]))
        intFile.write("  ")
        intFile.write(str(q[3]))
        intFile.write("  ")
        intFile.write(str(q[4]))
        intFile.write("\n")

intF = open('intFile.int', 'w')
symFile = open('symFile.sym', 'w')
syntax()
print("THE SYNTAX ANALYSIS HAS ENDED SUCCESSFULLY!")
symFile.close()
intC(intF)
intF.close()









                        


        


            