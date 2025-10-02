#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:55:41 2023

@author: marik
"""

import argparse


def nacti_soubor(file="../translator_template.md"):
    with open(file) as f:
        lines = f.readlines()
    return(lines)

def remove_yaml(data):
    temp = [i for i,j in enumerate(data) if j=="---\n"]
    return data[temp[1]+1:]

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--initialize", 
                           help="The name of the directory where translations have to be initialized.", 
                           action="store", 
                           dest='dirname', 
                           default="../00002_pyramid_game/"
                           )
    
    args = argParser.parse_args()
    dirname = args.dirname
    template = "".join(nacti_soubor())
    cs = nacti_soubor(file=f'{dirname}/cs_article.md')
    #en = nacti_soubor(file=f'{dirname}/en_article.md')
    cs = remove_yaml(cs)
    #en = remove_yaml(en)
    template = template.replace("<cs_article>","".join(cs))
    #template = template.replace("<en_article>","".join(en))
    for lang in ["es","sk","pl"]:
        with open(f"{dirname}/{lang}_article.md", "w") as f:
            f.write(template)
    

if __name__ == '__main__':
    main()
        
