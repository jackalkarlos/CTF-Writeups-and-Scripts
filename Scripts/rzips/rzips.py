#!/usr/bin/env python3

###############################################################################
###############################################################################
###############################################################################
## RZIPS: Recursive ZIP (Zipper/Unzipper) Suite
###############################################################################

import pyminizip # zipfile can not set password to zip. So, pyminizip here!
import zipfile
import warnings # ...for pyminizip... Compress lines.
import os
import glob
import sys
import time
import shutil # ...for rmtree function (for non empty directory).

###############################################################################

def menu():
    program_ascii_logo_and_menu = """
██████╗░███████╗██╗██████╗░░██████╗
██╔══██╗╚════██║██║██╔══██╗██╔════╝
██████╔╝░░███╔═╝██║██████╔╝╚█████╗░
██╔══██╗██╔══╝░░██║██╔═══╝░░╚═══██╗
██║░░██║███████╗██║██║░░░░░██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░░░░╚═════╝░

[ Nuri ACAR ] [ nuriacar.com ]

[ RZIPS ] [ Recursive ZIP Suite ] [ v0.0.6 : 20201207232323 ]

[ Menu ]
===============================================================================
.
... 1. Recursive Zipper
...... [+] Zips your files, directories recursively.
...... [+] Adds password(s) to your .zip files.

... 2. Recursive Unzipper [ Try one by one! ]
...... [+] Extracts .zip files. If necessary, performs recursively.
...... [+] Performs wordlist attack to password protected .zip files!
.......... You must have at least a wordlist file for wordlist attack!
...... [!] Directory must exists only one zip!
.......... If you have multiple, isolate one of them and unzip it. Then next...
.......... Remember! Try one by one!

... 8. About & Source Code Repository & Version History
... 9. Exit
===============================================================================
"""

    clear_screen()
    print("{}".format(program_ascii_logo_and_menu))

###############################################################################

def swtch_menu_option(): # Python has not switch case.
    print("Select an Option")
    selected_option = get_chck_positive_numeric()

    # Python has not switch case.
    if selected_option == 9:
        clear_screen()
        print("[ 9. Exit ]")
        prnt_seperator()
        prnt_terminated()
        return False # while loop breaker in main.
    elif selected_option == 1:
        clear_screen()
        print("[ 1. Recursive Zipper ]")
        prnt_seperator()
        zipper()
        prnt_hit_enter_to_continue()
    elif selected_option == 2:
        clear_screen()
        print("[ 2. Recursive Unzipper ]")
        prnt_seperator()
        unzipper()
        prnt_hit_enter_to_continue()
    elif selected_option == 8:
        clear_screen()
        print("[ 8. About & Source Code Repository & Version History ]")
        prnt_seperator()
        prnt_about_source_history()
        prnt_hit_enter_to_continue()
    else:
        prnt_out_of_option()
        prnt_hit_enter_to_continue()


###############################################################################

# function v.1

# def clear_screen():
#     if os.name == "nt":
#         os.system("cls")
#     else:
#         os.system("clear")


# function v.2 (shortest version of v.1)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

###############################################################################

def prnt_seperator():
    print("=" * 79)

###############################################################################

def prnt_hit_enter_to_continue():
    yazilanlar = input("\nHit 'Enter' to continue to menu!")
    clear_screen()

###############################################################################

def prnt_newline():
    print("")

###############################################################################

def prnt_terminated():
    print("Terminated!\n") # Double newline! First one is in print() fn!

###############################################################################

def prnt_out_of_option():
    print("\nOut of Option!")

###############################################################################

def prnt_developing_in_progress():
    print("This option developing in progress for now!")

###############################################################################

def prnt_entry_must_be_numeric():
    print("\nEntry must be numeric!")

###############################################################################

def prnt_entry_must_be_positive_number():
    print("\nEntry must be positive number!")

###############################################################################

def prnt_not_found_in_dir():
    print("\nNot found in directory!")

###############################################################################

def prnt_empty_dir_wont_be_zipped():
    print("\nEmpty Directory!.. will not be zipped!")

###############################################################################

def prnt_exit_submenu():
    print("\nAye aye!..")

###############################################################################

def prnt_about_source_history():
    about_source_history = """[ About ]  http://nuriacar.com/cevizlab/2020/10/12/rzips.html

[ Source ] https://github.com/nuriacar/rzips

[ Version History ]
===============================================================================

20200407131313 :        : Coding with Python 3 started.
20200409012105 : v0.0.1 : Zip/unzip done in seperate files. Time to mix.
20200410055835 : v0.0.2 : Zipper fixed. Unzip added.
20200411043803 : v0.0.3 : Zipper and unzipper refactored and beautified.
20200411052611 : v0.0.3 : Name changed.
20200412082257 : v0.0.4 : Wordlist attack option added.
20200412234321 : v0.0.4 : Unzipper refactored, beautified, commented.
20200415001835 : v0.0.5 : Zipper refactored, beautified, commented.
20201207232323 : v0.0.6 : Workflow changed.

[ TODO List ]
===============================================================================

+ File or directory name autocompete
+ Packaging"""

    print("{}".format(about_source_history))

###############################################################################

def get_chck_positive_numeric():
    # Returns only positive number. If entry not numeric, 0 or negative, 
    # calls itself till entry become positive.
    str_numeric_entry = input("\n>>> ") # ...reads user entry.

    try:
        int_numeric_entry = int(str_numeric_entry) # If entry is integer,
        if int_numeric_entry > 0: # and positive (must)...
            return int_numeric_entry
        else: # Else, so not positive...
            prnt_entry_must_be_positive_number()

            # Because of function recall inside itself, value become None.
            # So, return is important below!
            # Returns proper value of function call n to function call 1!
            return get_chck_positive_numeric()
    except ValueError: # Else, so entry is not integer.
        prnt_entry_must_be_numeric()

        # Because of function recall inside itself, value become None.
        # So, return is important below!
        # Returns proper value of function call n to function call 1!
        return get_chck_positive_numeric()

###############################################################################

def prnt_classified_file_or_dir(classified_elements_list):
    print("{}".format(os.getcwd())) # Prints current working directory.
    prnt_newline()

    # classified_elements_list[0] includes file elements.
    for file_element in classified_elements_list[0]:
        print(".. [f]", file_element)
    
    # classified_elements_list[1] includes directory elements.
    # If there is no element in classified_elements_list[1]
    # Actually .zip format is a file format. So, there is any .zip file in
    # directory.
    if len(classified_elements_list[1]) == 0:
        pass
    else: # If exists...
        prnt_newline()
        for dir_element in classified_elements_list[1]:
            print(".. [d]", dir_element)

###############################################################################

def clssfr_file_or_dir(directory_content_list):

    file_elements_list = list()
    dir_elements_list = list()

    # Adds file and directory content to seperate lists.
    for element in directory_content_list:
        if os.path.isfile(element):
            file_elements_list.append(element)
        elif os.path.isdir(element):
            dir_elements_list.append(element)
        else:
            pass

    # list of lists
    classified_elements_list = list()
    # classified_elements_list[0] = file_elements_list
    classified_elements_list.append(file_elements_list)
    #classified_elements_list[1] = dir_elements_list
    classified_elements_list.append(dir_elements_list)

    return classified_elements_list

###############################################################################

def lstr_dir_content():
    directory_content_list = os.listdir() # Gets directory content to list.
    directory_content_list.sort() # Sorts list elements.

    return directory_content_list

###############################################################################

def qry_is_file_or_dir_exist(zip_cand_name, directory_content_list):
    if zip_cand_name in directory_content_list:
        return True
    else:
        return False

##############################################################################

# def is_dir_empty(zip_cand_name):
#     if len(os.listdir(zip_cand_name)) == 0:
#         return True
#     else:
#         return False

###############################################################################

def backup_zip_files(unzip_cand_filepath_list):
    # New dir name must be r string!
    backup_dir_name = r"zip_backup"
    backup_dir_path = os.path.join(os.getcwd(), backup_dir_name)
    if not os.path.exists(backup_dir_path):
        os.mkdir(backup_dir_path)
        prnt_newline()
        print("'{}' directory created!".format(backup_dir_name))
        print("Backups will be moved in '{}'!".format(backup_dir_name))
    elif os.path.exists(backup_dir_path):
        prnt_newline()
        print("'{}' directory already exists!".format(backup_dir_name)) 
        print("Backups will be moved in '{}'!".format(backup_dir_name))
    else:
        pass
    
    for unzip_candidate in unzip_cand_filepath_list:
        source_file_basename = os.path.basename(unzip_candidate)
        destination_file_path = \
            os.path.join(backup_dir_path, source_file_basename)
        # unzip_candidate is a path element in unzip_cand_filepath_list
        shutil.copy2(unzip_candidate, destination_file_path)

# ┌──────────────────┬────────┬───────────┬───────┬────────────────┐
# │     Function     │ Copies │   Copies  │Can use│   Destination  │
# │                  │metadata│permissions│buffer │may be directory│
# ├──────────────────┼────────┼───────────┼───────┼────────────────┤
# │shutil.copy       │   No   │    Yes    │   No  │      Yes       │
# │shutil.copyfile   │   No   │     No    │   No  │       No       │
# │shutil.copy2      │  Yes   │    Yes    │   No  │      Yes       │
# │shutil.copyfileobj│   No   │     No    │  Yes  │       No       │
# └──────────────────┴────────┴───────────┴───────┴────────────────┘

###############################################################################

def prnt_default_value_assign(value):
    if value == "do_not_delete_originals":
        prnt_out_of_option()
        print("Default value assigned!")
        print("Original [f]ile(s) or [d]ir(s) will NOT remove!")
    elif value == "do_not_set_password":
        prnt_out_of_option()
        print("Default value assigned!")
        print("File(s) will be password unprotected!")
    elif value == "just_default_value_assigned":
        prnt_newline()
        print("Default value assigned!")
    else:
        pass

###############################################################################

def pwlist_pwgen_neither():
    passwd_list_or_passwd_generator_text = \
    """\nSome of .zip [f]iles may be password protected!
Select one of them below to be used if necessary!

1. I think, the .zip file is not password protected. [ Default ]
2. A wordlist is necessary. Let me select a wordlist file."""
    print(passwd_list_or_passwd_generator_text)

    selected_option = get_chck_positive_numeric()

    if selected_option == 1: # I think, the .zip file is not pass protected.
        prnt_default_value_assign("just_default_value_assigned")
        return "1"
    elif selected_option == 2: # Let me select a wordlist file.
        # Returns directory content for file existence check.
        directory_content_list = lstr_dir_content()
        
        while True:
            prnt_newline()

            passwd_list_filename = \
                input("Type the name of the password list file: ")

            # Checks user entered name really exists in directory.
            if qry_is_file_or_dir_exist\
                (passwd_list_filename, directory_content_list): # Exists..
                
                prnt_newline()
                print("File found! ... will be used if necessary!")
                return passwd_list_filename
            else:
                prnt_not_found_in_dir() # and, asks again next loop in while.
    else:
        prnt_default_value_assign("just_default_value_assigned")
        return "1"

###############################################################################

def sttr_zip_password(zip_count):
    explanation_and_graph = """\nYou can set password for your first and final .zip [f]ile!

    + ==> [f]ile or [d]ir want to .zip
    |
    v
    + >>> First .zip [ password protected ]
    +
    +
    .
    .
    + >>> Final .zip [ password protected ]

Do you want to set password?"""
    print(explanation_and_graph)

    set_pass_yes_no = input("[y]es | [n]o: ").lower()

    if set_pass_yes_no == "y" or set_pass_yes_no == "yes":
        first_zip_pass = None
        final_zip_pass = None

        if zip_count == 1:
            prnt_newline()
            print("You want just one .zip! So, you can set just one password!")
            first_zip_pass = input("First and Only .zip Password >>> ")
            # tuple return (immutable)
            return (True, first_zip_pass, False)
        else:
            prnt_newline()
            first_zip_pass = input("First .zip Password >>> ")
            final_zip_pass = input("Final .zip Password >>> ")
            # tuple return (immutable)
            return (True, first_zip_pass, final_zip_pass)
            
    elif set_pass_yes_no == "n" or set_pass_yes_no == "no":
        return (False, False, False) # tuple return (immutable)
    else:
        prnt_default_value_assign("do_not_set_password")
        return (False, False, False) # tuple return (immutable)

###############################################################################

def qry_delete_originals():
    print("\nDo you want to delete original [f]ile(s) or [d]ir(s)?")
    
    remove_yes_no = input("[y]es | [n]o: ").lower()

    if remove_yes_no == "y" or remove_yes_no == "yes":
        return "y"
    elif remove_yes_no == "n" or remove_yes_no == "no":
        return "n"
    else: # This block becomes default option for delete.
        prnt_default_value_assign("do_not_delete_originals")
        return None

###############################################################################

def zipper():
    # Returns directory content.
    directory_content_list = lstr_dir_content()

    # Classifies the elements.
    # classified_elements_list is list of lists
    classified_elements_list = \
        clssfr_file_or_dir(directory_content_list)
    
    # ...after classification, prints sorted and classified directory elements.
    prnt_classified_file_or_dir(classified_elements_list)
    
    # Gets .zip candidate name from user.
    print("\nType the name of the [f]ile or [d]ir you want to .zip")
    zip_cand_name = input("or [q]uit: ")

    if zip_cand_name == "q" or zip_cand_name == "quit": # I want to quit.
        prnt_exit_submenu()
        return # Exit me this submenu without do anything to main menu.
    
    # Checks user entered name really exists in directory.
    if qry_is_file_or_dir_exist(zip_cand_name, directory_content_list):

        print("\nHow many times want you zip?")

        zip_count = get_chck_positive_numeric() # Gets .zip count.

        # Multiple return function call.
        set_pass_yes_no, first_zip_pass, final_zip_pass = \
            sttr_zip_password(zip_count)

        remove_yes_no = qry_delete_originals()

        ####################
        
        # At the begining we have two diff. situations: file or directory.
        # If zip_cand_name is directory, packs directory content in a zip.
        # Directory become a file. Then we have a file!
        if os.path.isdir(zip_cand_name):
            temp_zip_dirname = "temp_zip_dirname.zip"

            # Zipped dir name construction.
            zipped_dir_name = zip_cand_name + ".zip"

            # Temporary .zip dir name for .zip creation.
            temp_zip_cand_name = zip_cand_name
            
            # Creates first .zip file object. This is directory packing!
            with zipfile.ZipFile(temp_zip_dirname, "w") as new_zip_candidate:

                # Iterates over all the files in directory.
                for dirname, subdirs, filenames in \
                    os.walk(temp_zip_cand_name):
                    
                    for filename in filenames:
                        # Create complete filepath of file
                        # in directory.
                        filepath = os.path.join(dirname, filename)
                        temp_zip_cand_name = filepath
                        # Adds file to zip.
                        new_zip_candidate.write(temp_zip_cand_name)
            
            # Renames the brand new zip.
            os.rename(temp_zip_dirname, zipped_dir_name)

            # Retargeting the program.
            zip_cand_name = zipped_dir_name

            del subdirs # Not necessary but vs code warns "unused variable".
            
            # Packing done.
            # Now we have a .zip file evolved from a directory.
        
        ####################

        # Till now, all operations same! Because, we have just files!
        temp_zip_filename = "temp_zip_filename.zip"

        # Gets file basename without extension.
        zip_cand_base_name = os.path.splitext(zip_cand_name)[0]

        # Zipped file name construction.
        zipped_file_name = zip_cand_base_name + ".zip"

        # Temporary .zip file name for .zip creation.
        temp_zip_cand_name = zip_cand_name
        
        if set_pass_yes_no: # True
            if zip_count == 1:
                # Zipper
                pyminizip.compress\
                    ("{}".format(temp_zip_cand_name), \
                        "", \
                            "{}".format(temp_zip_filename), \
                                "{}".format(first_zip_pass), 1)
                

                # Renames the brand new .zip file.
                os.rename(temp_zip_filename, zipped_file_name)

            else:
                for i in range(zip_count):
                    if i == 0: # First_zip_pass locks.
                        # Zipper
                        pyminizip.compress\
                            ("{}".format(temp_zip_cand_name), \
                                "", \
                                    "{}".format(temp_zip_filename), \
                                        "{}".format(first_zip_pass), 1)
                    elif i == (zip_count - 1): # final_zip_pass locks
                        # Zipper
                        pyminizip.compress\
                            ("{}".format(temp_zip_cand_name), \
                                "", \
                                    "{}".format(temp_zip_filename), \
                                        "{}".format(final_zip_pass), 1)
                    else: # There is no lock for between first and final zips.
                        # Zipper
                        pyminizip.compress\
                            ("{}".format(temp_zip_cand_name), \
                                "", \
                                    "{}".format(temp_zip_filename), \
                                        "", 1)

                    # Renames the brand new .zip file.
                    os.rename(temp_zip_filename, zipped_file_name)

                    # Assigns zipped_file_name to .zip candidate for recursion.
                    temp_zip_cand_name = zipped_file_name
                    

        else: # Password unprotected .zips.
            # Recursion count times...
            for i in range(zip_count):
                # zipper
                pyminizip.compress\
                    ("{}".format(temp_zip_cand_name), \
                        "", \
                            "{}".format(temp_zip_filename), \
                                "", 1)
                
                # Renames the brand new .zip file.
                os.rename(temp_zip_filename, zipped_file_name)

                # Assigns zipped_file_name to .zip candidate for recursion.
                temp_zip_cand_name = zipped_file_name
            
            del i # Not necessary but vs code warns "unused variable".
        
        # All operations done!
        # Time to remove original [f]ile(s) or [d]ir(s) if wanted.
        if remove_yes_no == "y":
            # Removes temporary .zip candidate.
            if os.path.isfile(zip_cand_name):
                os.remove(zip_cand_name)
            elif os.path.isdir(zip_cand_name):
                try:
                    # Removes .zip candidate non empty directory.
                    shutil.rmtree(zip_cand_name)
                except FileNotFoundError:
                    pass
            else:
                pass
        elif remove_yes_no == "n":
            pass
        else:
            pass # Done in qry_delete_originals()
            
    else:
        prnt_not_found_in_dir()

###############################################################################

def unzipper():
    # Returns directory content.
    directory_content_list = lstr_dir_content()

    # Classifies the elements.
    # classified_elements_list is list of lists
    classified_elements_list = \
        clssfr_file_or_dir(directory_content_list)
    
    # ...after classification, prints sorted and classified directory elements.
    prnt_classified_file_or_dir(classified_elements_list)
    
    prnt_newline()

    unzip_cand_filepath_list = list()
    # glob searches all .zip file inside current working directory
    # then adds paths of them to list.
    unzip_cand_filepath_list = glob.glob(os.path.join(os.getcwd(), "*.zip"))

    if len(unzip_cand_filepath_list) == 0: # If there is no .zip file in dir...
        print("There is no .zip [f]ile(s) in directory!")
        return # ...exits function.
    elif len(unzip_cand_filepath_list) >= 2: # if there is 1+ .zip files.
        print("Directory exists more then one .zip [f]ile(s)!")
        print("Try one by one! Extraction will terminate!")
        return # ...exits function.
    else:
        unzip_cand_file_basename_list = list()

        # Converts added paths to base names, then adds the base name list.
        for file_path in unzip_cand_filepath_list:
            unzip_cand_file_basename_list.append(os.path.basename(file_path))

        unzip_cand_file_basename_list.sort()

        unzip_cand_filename_list_for_print = list()
        # prnt_classified_file_or_dir works with list_of_lists.
        # unzip_cand_filename_list_for_print[0] = unzip_cand_filepath_list
        unzip_cand_filename_list_for_print.\
            append(unzip_cand_file_basename_list)
        # unzip_cand_filename_list_for_print[1] = [] # Blank list.
        unzip_cand_filename_list_for_print.append([])

        prnt_classified_file_or_dir(unzip_cand_filename_list_for_print)

        print("\n... will be extracted!")

        # Returns one of these : "1" or passwd_list_filename
        # Password protected .zip files rises RuntimeError when extracting.
        # If returns 1 (means there is no wordlist necessary), so
        # wordlist attacker do not runs.
        # If returns a wordlist name, when the error rise, wordlist attack
        # will involve the pass cracking.
        one_or_wordlist = pwlist_pwgen_neither()

        remove_yes_no = qry_delete_originals()
        # Will be used on out of y - n deletion option.

        # Time to remove files or directories.
        if remove_yes_no == "y" or remove_yes_no == "yes":
            pass
        elif remove_yes_no == "n" or remove_yes_no == "no":
            backup_zip_files(unzip_cand_filepath_list)
        else: # This block becomes default option for delete
            prnt_default_value_assign("do_not_delete_originals")
            backup_zip_files(unzip_cand_filepath_list)

        # Recursive Unzipper
        while True:
            try:
                unzip_cand_filepath_list = list()
                # glob searches all .zip file inside current working directory
                # then adds to list.
                unzip_cand_filepath_list = \
                    glob.glob(os.path.join(os.getcwd(), "*.zip"))

                # If there is no .zip file in dir,
                if len(unzip_cand_filepath_list) == 0:
                    break
                else:
                    # Every unzip candidate renamed to this below.
                    temp_zip_filename = "temp_zip_filename.zip"

                    # Gets the basename of file from path.
                    founded_zip_filename = \
                        os.path.basename(unzip_cand_filepath_list[0])
                    # Renames the file.
                    os.rename(founded_zip_filename, temp_zip_filename)
                    unzip_cand_f_name = temp_zip_filename

                    # Time to unzip.
                    with zipfile.ZipFile(unzip_cand_f_name, "r") as \
                        new_unzip_candidate:
                        
                        # Extracts working directory.
                        new_unzip_candidate.extractall()
                    
                    # If extraction success, removes.
                    os.remove(temp_zip_filename)
            
            # If unzip candidate protected with password, raises Runtime Error,
            # then runs codes below.
            except RuntimeError:
                # If value int, occurs below.
                # ValueError: invalid literal for int() with base 10: 
                # 'rockyou.txt'
                
                # So value must be str
                
                # If unnecessary option selected in
                # pwlist_pwgen_neither and unzip candidate
                # is actually a password protected .zip:
                if one_or_wordlist == "1":
                    prnt_newline()
                    print(".zip is actually a password protected one!")
                    print("Please, select '2' in next extraction try!")
                    return # Exits in function..
                else: # Wordlist attacker runs.
                    unzip_cand_filepath_list = list()
                    # glob searches all .zip file inside current working 
                    # directory, then adds to list
                    unzip_cand_filepath_list = \
                        glob.glob(os.path.join(os.getcwd(), "*.zip"))

                    # If there is no .zip file in dir,
                    if len(unzip_cand_filepath_list) == 0:
                        break
                    else:

                        # Will be used in extraction.
                        password = None

                        # Every unzip candidate renamed to this below.
                        temp_zip_filename = "temp_zip_filename.zip"

                        # Gets the basename of file from path.
                        founded_zip_filename = \
                            os.path.basename(unzip_cand_filepath_list[0])
                        # Renames the file.
                        os.rename(founded_zip_filename, temp_zip_filename)
                        unzip_cand_f_name = temp_zip_filename

                        # If password not found in wordlist,
                        # terminates the trying. Else, program never stops.
                        list_end_counter = 0

                        # Time to unzip.
                        with zipfile.ZipFile(unzip_cand_f_name, "r") as \
                            new_unzip_candidate:
                            with open(one_or_wordlist, "r") as wlf:
                                wordlist_list = wlf.readlines()
                                # for loop below, must be break
                                # when password found! There is no need to
                                # try other passwords in list.
                                for line in wordlist_list:
                                    password = line.strip("\n")
                                    try:
                                        # (pwd=bytes(password, 'utf-8')) is
                                        # very important. It got my 6 hours.
                                        # Without this, throws encoding error!
                                        # Also password variable data must be
                                        # byte string! Important!

                                        # Extracts working directory.
                                        new_unzip_candidate.\
                                            extractall\
                                                (pwd=bytes(password, 'utf-8'))
                                        
                                        prnt_newline()
                                        print("[+] Password Found: {}".\
                                            format(password))
                                        
                                        os.remove(unzip_cand_f_name)

                                        # break below is important!
                                        # When password founded in wordlist
                                        # breakes the for loop.
                                        # So, other words in wordlist
                                        # will not tried!
                                        break
                                    except:
                                        # Counts one by one for every wrong
                                        # password in given wordlist.
                                        # If passwords ends, terminates the
                                        # trying. Without return, trying never
                                        # ends.
                                        list_end_counter += 1
                                        if list_end_counter == \
                                            len(wordlist_list):
                                            
                                            prnt_newline()
                                            print("[-] Password not found \
in wordlist!")
                                            return # Exits in function.
                                        else:
                                            pass
        
        # Extraction trying done. Lets check the changes.
        # Which [f]ile(s) or [d]ir(s) is/are new?
        dir_content_list_after_extraction = lstr_dir_content()

        new_files_or_dirs = list()
        
        # Finds new [f]ile(s) or [d]ir(s) and adds the list.
        for element in dir_content_list_after_extraction:
            if element not in directory_content_list:
                new_files_or_dirs.append(element)
        
        new_files_or_dirs.sort()

        prnt_newline()
        print("new [f]ile(s) or [d]ir(s) in ...")

        # Classifies the new ones...
        # classified_new_elements_list is list of lists
        classified_new_elements_list = \
            clssfr_file_or_dir(new_files_or_dirs)
        
        # After classification, prints...
        prnt_classified_file_or_dir(classified_new_elements_list)

###############################################################################

def main():
    ##########
    # Gets time now for elapsed time calculation.
    start_time = time.time() # Returns float.
    ##########
    clear_screen()
    
    # pyminizip.compress lines gets warning like below when first call!
    # DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats.
    # This code below blocs all warnings.
    warnings.filterwarnings("ignore")

    # ctrl + c termination and input error handler
    try:
        while True:
            menu()
            while_breaker = swtch_menu_option()
            if while_breaker == False:
                break
    except KeyboardInterrupt: # If ctrl + c pressed while code is running
        prnt_newline()
        prnt_newline()
        print("Keyboard Interrupt Termination!")
        prnt_newline()
    except EOFError: # Input error handler
        prnt_newline()
        prnt_newline()
        print("Input Error Termination!")
        prnt_newline()
    
    ##########
    # Gets duration time from time 0 till now.
    duration = time.time() - start_time # Returns float, so convert to int.
    
    hours = int(duration / 3600)
    minutes = int((duration / 60) % 60)
    seconds = int(duration % 60)

    prnt_seperator

    if hours > 0:
        print("[ Done! ] ====> {0} h. {1} m. {2} s."\
            .format(hours, minutes, seconds))
    elif minutes > 0:
        print("[ Done! ] ====> {0} m. {1} s."\
            .format(minutes, seconds))
    else:
        print("[ Done! ] ====> {0} s."\
            .format(seconds))
    
    prnt_seperator
    ##########

###############################################################################

if __name__ == "__main__":
    main()

###############################################################################
## Notes for future.

# #!/usr/bin/python
# import zipfile
# import argparse

# def extractFile(zFile, password):
# 	try:
# 		zFile.extractall(pwd=password)
# 		print "[+] Found password = " + password
# 		return True
# 	except:
# 		return False

# def main():
# 	parser = argparse.ArgumentParser("%prog -f <zipfile> -d <dictionary>")
# 	parser.add_argument("-f", dest="zname", help="specify .zip file")
# 	parser.add_argument("-d", dest="dname", help="specify dictionary file")
# 	args = parser.parse_args()

# 	if (args.zname == None):
# 		print parser.usage
# 		exit(0)
# 	elif (args.dname == None):
# 		zname = args.zname
# 		dname = 'passwords.txt'
# 	else:
# 		zname = args.zname
# 		dname = args.dname

# 	zFile = zipfile.ZipFile(zname)
# 	passFile = open(dname)

# 	for line in passFile.readlines():
# 		password = line.strip("\n")
# 		found = extractFile(zFile, password)
# 		# Exit if password found
# 		if found == True:
# 			exit(0)

# 	# If it makes it here password has not been found...
# 	print '[-] Password not found'

# if __name__ == "__main__":
# 	main()

##############################################################################

# pyminizip.compress("1.sh", "zipizip", "1.zip", "p", 5)

##############################################################################