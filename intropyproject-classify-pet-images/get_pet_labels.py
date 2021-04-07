#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Lorenzo Hernandez
# DATE CREATED: 03/27/2021                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(pet_images):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    img_pth = listdir("pet_images/")
    results_dic = dict()
    
    # iterating through the img directory
    for indx in range(0, len(img_pth), 1):
        pet_label = ""
        
        # makes pet_labels lowercase and splits the words
        pet_labels = img_pth[indx].lower().split("_")  
        
        '''
        for each label within pet_labels, if label starts with anything other than a letter it gets removed
        and word pet_label gets updated with the label
        '''
        
        for label in pet_labels:
            if label.isalpha():
                pet_label += label + " "
                
        # removes any leading and ending spaces        
        pet_label = pet_label.strip()
        
        # if item in directory doesn't exist in results_dic, item gets added as the key and pet_label is added as the value
        if img_pth[indx] not in results_dic:
            results_dic[img_pth[indx]] = [pet_label]
            
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
