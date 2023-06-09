import pystyle
import time
import os

import modules.title as title

title.start()

import modules.watermark

def search(name):
    if name == '':
        print(f"    {pystyle.Colors.light_red}Votre recherche est vide\n")
        return
    
    files = os.listdir("data")

    total_lines = 0
    lines = 0
    output = ''

    for i in range(len(files)):
        if os.path.isdir(os.path.join('data', files[i])):
            print(f'    {pystyle.Colors.StaticRGB(50, 50, 255)}{str(files[i])}')
            files_dir = os.listdir(f'data/{files[i]}')
            for i2 in range(len(files_dir)):
                with open(f'data/{files[i]}/{files_dir[i2]}', encoding='latin-1') as f:
                    file = open(f'data/{files[i]}/{files_dir[i2]}')
                    for line in f:
                        if name in line:
                            total_lines += 1
                            lines += 1

                            espaces = ' ' * (6 - len(str(lines)))
                            output += f'     {pystyle.Colors.turquoise}{lines}{espaces}{pystyle.Colors.cyan}{line}'
                    if output != '':
                        print(f'     {pystyle.Colors.light_blue}{str(files_dir[i2])} ({lines})\n{str(output)}')
                lines = 0
                output = ''
            
            if len(files) == 0:
                print()

        else:
            with open(f'data/{files[i]}', encoding='latin-1') as f:
                file = open(f'data/{files[i]}')
                for line in f:
                    if name in line:
                        total_lines += 1
                        lines += 1

                        espaces = ' ' * (6 - len(str(lines)))
                        output += f'    {pystyle.Colors.turquoise}{lines}{espaces}{pystyle.Colors.cyan}{line}'
                if output != '':
                    print(f'    {pystyle.Colors.light_blue}{str(files[i])} ({lines})\n{str(output)}')
            lines = 0
            output = ''
        
    if total_lines == 0:
        print(f"    {pystyle.Colors.orange}Aucun résultat trouvé\n")

while True:
    search(input(f'  {pystyle.Colors.dark_green}Recherche : {pystyle.Colors.light_green}'))