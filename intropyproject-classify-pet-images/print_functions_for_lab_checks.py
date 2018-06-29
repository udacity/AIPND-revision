#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/print_functions_for_lab_checks.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 05/14/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE:  This set of functions can be used to check your code after programming 
#           each function. The top section of each part of the lab contains
#           the section labeled 'Checking your code'. When directed within this
#           section of the lab one can use these functions to more easily check 
#           your code. See the docstrings below each function for details on how
#           to use the function within your code.
#
##

# Functions below defined to help with "Checking your code", specifically
# running these functions with the appropriate input arguments within the
# main() funtion will print out what's needed for "Checking your code"
#
def check_command_line_arguments(in_arg):
    """
    For Lab: Classifying Images - 7. Command Line Arguments
    Prints each of the command line arguments passed in as parameter in_arg, 
    assumes you defined all three command line arguments as outlined in 
    '7. Command Line Arguments'
    Parameters:
     in_arg -data structure that stores the command line arguments object
    Returns:
     Nothing - just prints to console  
    """
    if in_arg is None:
        print("* Doesn't Check the Command Line Arguments because 'get_input_args' hasn't been defined.")
    else:
        # prints command line agrs
        print("Command Line Arguments:\n     dir =", in_arg.dir, 
              "\n    arch =", in_arg.arch, "\n dogfile =", in_arg.dogfile)

def check_creating_pet_image_labels(results_dic):
    """    For Lab: Classifying Images - 9/10. Creating Pet Image Labels
    Prints first 10 key-value pairs and makes sure there are 40 key-value 
    pairs in your results_dic dictionary. Assumes you defined the results_dic
    dictionary as was outlined in 
    '9/10. Creating Pet Image Labels'
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
    Returns:
     Nothing - just prints to console  
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'get_pet_labels' hasn't been defined.")
    else:
        # Code to print 10 key-value pairs (or fewer if less than 10 images)
        # & makes sure there are 40 pairs, one for each file in pet_images/
        stop_point = len(results_dic)
        if stop_point > 10:
            stop_point = 10
        print("\nPet Image Label Dictionary has", len(results_dic),
              "key-value pairs.\nBelow are", stop_point, "of them:")
    
        # counter - to count how many labels have been printed
        n = 0
    
        # for loop to iterate through the dictionary
        for key in results_dic:
 
            # prints only first 10 labels
            if n < stop_point:
                print("{:2d} key: {:>30}  label: {:>26}".format(n+1, key,
                      results_dic[key][0]) )

                # Increments counter
                n += 1
            
            # If past first 10 (or fewer) labels the breaks out of loop
            else:
                break


def check_classifying_images(results_dic):
    """    For Lab: Classifying Images - 11/12. Classifying Images
    Prints Pet Image Label and Classifier Label for ALL Matches followed by ALL 
    NOT matches. Next prints out the total number of images followed by how 
    many were matches and how many were not-matches to check all 40 images are
    processed. Assumes you defined the results_dic dictionary as was 
    outlined in '11/12. Classifying Images'
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and 
                    classifer labels and 0 = no match between labels
    Returns:
     Nothing - just prints to console  

    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    elif len(results_dic[next(iter(results_dic))]) < 2:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    else:
        # Code for checking classify_images -
        # Checks matches and not matches are classified correctly
        # Checks that all 40 images are classified as a Match or Not-a Match
    
        # Sets counters for matches & NOT-matches
        n_match = 0
        n_notmatch = 0
    
        # Prints all Matches first
        print("\n     MATCH:")
        for key in results_dic:

            # Prints only if a Match Index 2 == 1
            if results_dic[key][2] == 1:

                # Increments Match counter
                n_match += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}".format(key, 
                      results_dic[key][0], results_dic[key][1]))

        # Prints all NOT-Matches next
        print("\n NOT A MATCH:")
        for key in results_dic:
        
            # Prints only if NOT-a-Match Index 2 == 0 
            if results_dic[key][2] == 0:
 
                # Increments Not-a-Match counter
                n_notmatch += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}".format(key,
                      results_dic[key][0], results_dic[key][1]))

        # Prints Total Number of Images - expects 40 from pet_images folder
        print("\n# Total Images",n_match + n_notmatch, "# Matches:",n_match ,
              "# NOT Matches:",n_notmatch)

 
def check_classifying_labels_as_dogs(results_dic):
    """    For Lab: Classifying Images - 13. Classifying Labels as Dogs
    Prints Pet Image Label, Classifier Label, whether Pet Label is-a-dog(1=Yes,
    0=No), and whether Classifier Label is-a-dog(1=Yes, 0=No) for ALL Matches 
    followed by ALL NOT matches. Next prints out the total number of images 
    followed by how many were matches and how many were not-matches to check 
    all 40 images are processed. Assumes you defined the results_dic dictionary
    as was outlined in '13. Classifying Labels as Dogs'
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and 
                    classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     Nothing - just prints to console  

    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")
    elif len(results_dic[next(iter(results_dic))]) < 4 :
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")

    else:
        # Code for checking adjust_results4_isadog -
        # Checks matches and not matches are classified correctly as "dogs" and
        # "not-dogs" Checks that all 40 images are classified as a Match or Not-a 
        # Match
    
        # Sets counters for matches & NOT-matches
        n_match = 0
        n_notmatch = 0
    
        # Prints all Matches first
        print("\n     MATCH:")
        for key in results_dic:

            # Prints only if a Match Index 2 == 1
            if results_dic[key][2] == 1:

                # Increments Match counter
                n_match += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(key,
                      results_dic[key][0], results_dic[key][1], results_dic[key][3], 
                      results_dic[key][4]))

        # Prints all NOT-Matches next
        print("\n NOT A MATCH:")
        for key in results_dic:
        
            # Prints only if NOT-a-Match Index 2 == 0 
            if results_dic[key][2] == 0:
 
                # Increments Not-a-Match counter
                n_notmatch += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(key,
                      results_dic[key][0], results_dic[key][1], results_dic[key][3], 
                      results_dic[key][4]))

        # Prints Total Number of Images - expects 40 from pet_images folder
        print("\n# Total Images",n_match + n_notmatch, "# Matches:",n_match ,
              "# NOT Matches:",n_notmatch)



def check_calculating_results(results_dic, results_stats_dic):
    """    For Lab: Classifying Images - 14. Calculating Results
    Prints First statistics from the results stats dictionary (that was created
    by the calculates_results_stats() function), then prints the same statistics
    that were calculated in this function using the results dictionary.
    Assumes you defined the results_stats dictionary and the statistics 
    as was outlined in '14. Calculating Results '
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and 
                    classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     results_stats_dic - Dictionary that contains the results statistics (either
                     a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
    Returns:
     Nothing - just prints to console  

    """
    if results_stats_dic is None:
        print("* Doesn't Check the Results Dictionary because 'calculates_results_stats' hasn't been defined.")
    else:
        # Code for checking results_stats_dic -
        # Checks calculations of counts & percentages BY using results_dic
        # to re-calculate the values and then compare to the values
        # in results_stats_dic
    
        # Initialize counters to zero and number of images total
        n_images = len(results_dic)
        n_pet_dog = 0
        n_class_cdog = 0
        n_class_cnotd = 0
        n_match_breed = 0
    
        # Interates through results_dic dictionary to recompute the statistics
        # outside of the calculates_results_stats() function
        for key in results_dic:

            # match (if dog then breed match)
            if results_dic[key][2] == 1:

                # isa dog (pet label) & breed match
                if results_dic[key][3] == 1:
                    n_pet_dog += 1

                    # isa dog (classifier label) & breed match
                    if results_dic[key][4] == 1:
                        n_class_cdog += 1
                        n_match_breed += 1

                # NOT dog (pet_label)
                else:

                    # NOT dog (classifier label)
                    if results_dic[key][4] == 0:
                        n_class_cnotd += 1

            # NOT - match (not a breed match if a dog)
            else:
 
                # NOT - match
                # isa dog (pet label) 
                if results_dic[key][3] == 1:
                    n_pet_dog += 1

                    # isa dog (classifier label)
                    if results_dic[key][4] == 1:
                        n_class_cdog += 1

                # NOT dog (pet_label)
                else:

                    # NOT dog (classifier label)
                    if results_dic[key][4] == 0:
                        n_class_cnotd += 1

                    
        # calculates statistics based upon counters from above
        n_pet_notd = n_images - n_pet_dog
        pct_corr_dog = ( n_class_cdog / n_pet_dog )*100
        pct_corr_notdog = ( n_class_cnotd / n_pet_notd )*100
        pct_corr_breed = ( n_match_breed / n_pet_dog )*100
    
        # prints calculated statistics
        print("\n ** Statistics from calculates_results_stats() function:")
        print("N Images: {:2d}  N Dog Images: {:2d}  N NotDog Images: {:2d} \nPct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              results_stats_dic['n_images'], results_stats_dic['n_dogs_img'],
              results_stats_dic['n_notdogs_img'], results_stats_dic['pct_correct_dogs'],
              results_stats_dic['pct_correct_notdogs'],
              results_stats_dic['pct_correct_breed']))
        print("\n ** Check Statistics - calculated from this function as a check:")
        print("N Images: {:2d}  N Dog Images: {:2d}  N NotDog Images: {:2d} \nPct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              n_images, n_pet_dog, n_pet_notd, pct_corr_dog, pct_corr_notdog,
              pct_corr_breed))
