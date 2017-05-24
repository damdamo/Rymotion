#! /usr/bin/env python3
""" The goal is to take photos and evaluate
them with openface to have action unit"""

import os
import sys

import yaml
import json

import pygame
import pygame.camera

import pandas as pd


def take_photos(folder_name, file_name):
    """Juste to take photos with webcam"""
    pygame.camera.init()
    # Camera detected or not
    list_camera = pygame.camera.list_cameras()

    if len(list_camera) == 0:
        print("Aucune camera détecté sur votre ordinateur")
        return -1

    # If a camera exists, we take the first in the list_camera
    cam = pygame.camera.Camera(list_camera[0], (1280, 720))
    cam.start()
    img = cam.get_image()

    output_name = "{}/{}".format(folder_name, file_name)
    pygame.image.save(img, output_name)


def call_openface(prog_file, picture_location, output_informations):
    """Call openface application, take a picture and extract informations
    about it, we want AU for analysis"""
    exec_line = "{} -f {} -of {}".format(prog_file,
                                         picture_location, output_informations)
    os.system(exec_line)


def interpretation_AU(au_file):
    """Extract informations in the return file of
    call_openface and return emotions of the person

    What does AU mean:
    Happiness: AU06 + AU12
    Sadness: AUO1 + AU04 + AU15
    Anger: AU04 + AU05 + AU07 + AU23
    Surprise: AU01 + AU02 + AU5 + AU26
    """

    # Dictionnary with actions units
    dic_au = {}
    with open(au_file, 'r') as au_file_streaming:
        for ligne in au_file_streaming:
            ligne_split = ligne.split()
            if "AU" in ligne_split[0]:
                if ligne_split[1] == "0" or ligne_split[1] == "1":
                    dic_au[ligne_split[0]] = ligne_split[1]

    # On regarde dans quel état est la personne
    if dic_au["AU06"] == 1 and dic_au["AU12"] == 1:
        return "happy"

    else if dic_au["AU04"] == 1 or (dic_au["AU05"] == 1 and dic_au["AU07"] == 1 and dic_au["AU23"] == 1):
        return "angry"

    else:
        return "neutral"


if __name__ == '__main__':

    config_file = sys.argv[1]

    with open(config_file, 'r') as config_stream:
        config = yaml.safe_load(config_stream)

    prog_file = config["openface"]["bin_file"]
    picture_location = "{}/{}".format(config["pictures"]["folder_name"],
                                      config["pictures"]["file_name"])
    output_informations = config["openface"]["output_extract_informations"]["output_file_full_path"]

    # We take a photo
    take_photos(config["pictures"]["folder_name"],
                config["pictures"]["file_name"])

    # We call openface
    call_openface(prog_file, picture_location, output_informations)

    # We extract emotions
    interpretation_AU(
        config["openface"]["output_extract_informations"]["output_file_relative_path"])
