#! /usr/bin/env python3
""" The goal is to take photos and evaluate
them with openface to have action unit"""

import os
import sys

import yaml
import json

import pygame
import pygame.camera


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
    call_openface and return emotions of the person"""
    json_data=open(au_file)
    data = json.load(json_data)
    #print(data)

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
    # call_openface(prog_file, picture_location, output_informations)

    # We extract emotions
    #interpretation_AU(config["openface"]["output_file_relative_path"])
