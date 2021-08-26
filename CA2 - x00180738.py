'''
Name: Flavio Vieira
student number/email: x00180738@mytudublin.ie
subject: Software Development Fundamentals - CA1

#inputs
 - Menu option (str)
 - DNA
    - species 1 (str)
    - species 2 (str)
- Hangman
    - letters to guess
#outputs
 - DNA
    - species 1 (added indel)
    - species 2 (added indel)
    - species 1 (delete indel)
    - species 2 (delete indel)
    - mismatch score (score)
    - matching score (score)
- Hangman
    - number of tries
    - letters found

#algorithm
print (options menu)
Input option (user_option)
while option not in [1, 2, 3] Loop through options menu
if user_option == 1:
    loop until only allowed characters are used:
    Insert indel:
        input species_1 (str)
            - input indel location
            - insert indel
        input species_2 (str)
            - input indel location
            - insert indel
    Delete indel:
        input species_1 (str)
            - input indel location
            - delete indel
        input species_2 (str)
            - input indel location
            - delete indel
    Score:
     - add indel on shorter dna sequence
     - upper case on mismatches
     - count mismatches (including indel)
     - count matches

elif option == 2:
    assign random game_word
    insert letter_guess
    if letter_exists in game_word
        replace game_word_blank on the same index as game_word
        print (game_word_blank)

else:
    exit app

'''
import math
import random
user_option = 0
while user_option != '3':
    print('\n')
    print('\t\t**********************************************')
    print('\t\t***************** FV program *****************')
    print('\t\t************ Option 1 - Examine DNA **********')
    print('\t\t************ Option 2 - Play Hangman *********')
    print('\t\t************ Option 3 - Exit *****************')
    print('\t\t**********************************************')
    print('\n')
    user_option = input('Please choose one of the above options: ')
    # print(user_option)
    print('\n')
    options_list = ['1', '2', '3']
    while user_option not in options_list:
        print('Invalid Option - Please select one of the valid options below')
        user_option = input('Please chose a valid option: ')
        # print(user_option)
        print('\n')

    #OPTION 1 - EXAMINE DNA PROGRAM
    if user_option == '1':
        DNA_list = ['A', 'T', 'C', 'G']
        print('EXAMINE DNA PROGRAM')

        dna_1_validation = False
        while not dna_1_validation:
            DNA_1 = input('Please insert species 1 DNA - Biological characters ("A", "T", "C", "G"): ')
            DNA_1 = DNA_1.upper()
            if any(x not in DNA_list for x in DNA_1):
                print('INVALID')
                dna_1_validation = False
            else:
                # print('happy days')
                dna_1_validation = True

        dna_2_validation = False
        while not dna_2_validation:
            DNA_2 = input('Please insert species 2 DNA - Biological characters ("A", "T", "C", "G"): ')
            DNA_2 = DNA_2.upper()
            if any(x not in DNA_list for x in DNA_2):
                print('INVALID')
                dna_2_validation = False
            else:
                dna_2_validation = True
        print('\n')
        print('Species 1 DNA: {}'.format(DNA_1))
        print('Species 2 DNA: {}'.format(DNA_2))


        dna_option = 0
        while dna_option != 'q':
            print('\n')
            print('\t\t Option "a" - Add an indel ')
            print('\t\t Option "d" - Delete an indel ')
            print('\t\t Option "s" - Score the present alignment ')
            print('\t\t Option "q" - Stop the process ')
            print('\n')
            dna_option = input('Choose 1 of the above options: ')
            dna_options_list = ['a', 'd', 's', 'q']

            while dna_option not in dna_options_list:
                print('Invalid Option - Please select one of the valid options below')
                dna_option = input('Choose 1 of the above options: ')

            #ADD AN INDEL
            if dna_option == 'a':
                dna_to_change_list = ['1', '2']
                dna_to_change = 0
                while dna_to_change not in dna_to_change_list:
                    dna_to_change = input('Select DNA species to change (1 or 2): ')
                    if dna_to_change not in dna_to_change_list:
                        print('incorrect DNA species - You can only choose 1 or 2.')
                    else:
                        if dna_to_change == '1':
                            index_of_indel = int(input('Select the Index you wish to have indel inserted: '))
                            while index_of_indel > len(DNA_1):
                                index_of_indel = int(input('Select the Index you wish to have indel inserted wihtin DNA 1 length: '))
                            new_dna_1 = '{}-{}'.format((DNA_1[:index_of_indel]), (DNA_1[index_of_indel:]))
                            DNA_1 = new_dna_1
                            print('\n')
                            print('Species 1 DNA is: {}'.format(DNA_1))
                            print('Species 2 DNA is: {}'.format(DNA_2))
                        else:
                            index_of_indel = int(input('Select the Index you wish to have indel inserted: '))
                            while index_of_indel > len(DNA_2):
                                index_of_indel = int(input('Select the Index you wish to have indel inserted wihtin DNA 2 length: '))
                            new_dna_2 = '{}-{}'.format((DNA_2[:index_of_indel]), (DNA_2[index_of_indel:]))
                            DNA_2 = new_dna_2
                            print('\n')
                            print('Species 1 DNA is: {}'.format(DNA_1))
                            print('Species 2 DNA is: {}'.format(DNA_2))

            # DELETE AN INDEL
            elif dna_option == 'd':
                dna_to_change_list = ['1', '2']
                dna_to_change = 0
                while dna_to_change not in dna_to_change_list:
                    dna_to_change = input('Select DNA species to change (1 or 2): ')
                    if dna_to_change not in dna_to_change_list:
                        print('incorrect DNA species - You can only choose 1 or 2.')
                    else:
                        if dna_to_change == '1':
                            if DNA_1.__contains__('-'):
                                index_of_indel = int(input('Select the Index you wish to have indel deleted: '))
                                while index_of_indel > len(DNA_1) or DNA_1[index_of_indel] != '-':
                                    index_of_indel = int(input('Select the Index you wish to have indel deleted from wihtin DNA 1 length: '))
                                new_dna_1 = DNA_1.replace(DNA_1[index_of_indel], '')
                                DNA_1 = new_dna_1
                                print('\n')
                                print('Species 1 DNA is: {}'.format(DNA_1))
                                print('Species 2 DNA is: {}'.format(DNA_2))
                            else:
                                print('\n')
                                print('DNA 1 species does not contain and indel!')
                        else:
                            if DNA_2.__contains__('-'):
                                index_of_indel = int(input('Select the Index you wish to have indel deleted: '))
                                while (index_of_indel > len(DNA_2)) or (DNA_2[index_of_indel] != '-'):
                                    index_of_indel = int(input('Select the Index you wish to have indel deleted from wihtin DNA 2 length: '))
                                new_dna_2 = DNA_2.replace(DNA_2[index_of_indel], '')
                                DNA_2 = new_dna_2
                                print('\n')
                                print('Species 1 DNA is: {}'.format(DNA_1))
                                print('Species 2 DNA is: {}'.format(DNA_2))
                            else:
                                print('\n')
                                print('DNA 2 species does not contain and indel!')

            # SCORE THE PRESENT ALIGNMENT
            elif dna_option == 's':

                name = DNA_1
                name2 = DNA_2
                name = name.lower()
                name2 = name2.lower()

                if len(name) > len(name2):
                    ind_to_add = len(name) - len(name2)
                    name_2_ind = '-' * ind_to_add
                    name2_plus = '{}{}'.format(name2, name_2_ind)
                    name2 = name2_plus
                elif len(name2) > len(name):
                    ind_to_add = len(name2) - len(name)
                    name_ind = '-' * ind_to_add
                    name_plus = '{}{}'.format(name, name_ind)
                    name = name_plus

                score_mismatch = 0
                for i in range(len(name)):
                    if name[i] != name2[i]:
                        name = '{}{}{}'.format(name[:i], name[i].upper(), name[i + 1:])
                        name2 = '{}{}{}'.format(name2[:i], name2[i].upper(), name2[i + 1:])
                        score_mismatch += 1
                    else:
                        score_mismatch = score_mismatch

                score_match = len(name)-score_mismatch
                print('Number of matches: {}'.format(score_match))
                print('Number of mismatches: {}'.format(score_mismatch))
                print('Species 1 DNA: {}'.format(name))
                print('Species 2 DNA: {}'.format(name2))

            # QUIT THE EXAMINE DNA PROGRAM
            else:
                print('Process stopped - Thank you for using DNA Examine!')
                print('\n')

    #OPTION 2 - HANGMAN PROGRAM
    elif user_option == '2':
        print('you have chosen to Play Hangman - Let the game begin!')
        hangman_words = ['baubles', 'guards', 'boneshaker', 'drudges', 'medicide', 'full-bottom', 'coagulase', 'simmer',
                         'bunnia', 'tremie', 'muttonheads', 'roughneck', 'creds', 'timber-line', 'emberiza',
                         'dominionism', 'sunsets', 'cucujo', 'earthbank', 'streaks', 'extravagate', 'conjuncture',
                         'elongator', 'ology', 'cutworms', 'refusion', 'levitator', 'unbowel', 'keenness', 'droschka',
                         'darnels', 'flammables', 'wildtype', 'gypsy', 'retrainee', 'piaga', 'giddy-head',
                         'rastafarianism', 'selenology', 'hymenoptera', 'wrist-drop', 'triggermen', 'multilingualism',
                         'cloaths', 'hemophobia', 'retrofit', 'commandments', 'unglue', 'inshining', 'nicholas',
                         'hotfoot', 'pubkeeper', 'gas-tank', 'uprun', 'stabler', 'doctrinaires', 'akathisia', 'ribcage',
                         'neurophysicist', 'unappropriate']

        game_word = random.choice(hangman_words)
        game_word_list = list(game_word)
        # print(game_word)
        game_word_blank = '_' * len(game_word)
        lives = int(9)
        completed = False

        while not completed and lives > 0:
            print('The word is {}'.format(game_word_blank))
            letter_guess = input('Enter guess: ')
            # print(letter_guess)
            if game_word.__contains__(letter_guess):
                if game_word_blank.__contains__(letter_guess):
                    print('Letter already guessed!')
                    print('\n')
                    print(game_word_blank)
                else:
                    for index, item in enumerate(game_word_list):
                        if item == letter_guess:
                            game_word_blank = '{}{}{}'.format(game_word_blank[:index], letter_guess, game_word_blank[index + 1:])
                            if game_word_blank.__contains__('_') == False:
                                completed = True
                        else:
                            game_word_blank = game_word_blank
                    print('Well done, the word is {}'.format(game_word_blank))
            else:
                lives -= 1
                print('Wrong, lives: {}'.format(lives))

        if completed:
            print('Good Job!')
        else:
            print('Better luck next time, the word was: {}'.format(game_word))

    #OPTION 3  - EXIT APP
    else:
        print('You have selected to exist the app - See you soon!')
