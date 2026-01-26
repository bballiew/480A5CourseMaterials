

print('Checking if installed packages import correctly....')
import numpy; 
import scipy; 
import skimage; 
import Bio; 
import matplotlib; 
import pandas; 
import tifffile; 
import trackpy;
import seaborn;
print('All packages imported correctly.')

try: 
    import torch; 
    import cellpose; 
    print('PyTorch has GPU enabled?')
    print(torch.cuda.is_available())
    print('Cellpose is installed')

except:
	print('torch and cellpose skipped for now')

print('Check that biopython isnt blank:')
from Bio import SeqIO
try:
    SeqIO.parse
    print('Biopython is not blank.')
except:
    print('Biopython is blank, not installed correctly.')
    
print('Check if muscle is available:')
import subprocess
import sys # To check for MUSCLE executable

import os
try:
    muscle_command = ["muscle", "-version"]

    # Run the command, capture output, decode as text, and check for errors
    result = subprocess.run(muscle_command, capture_output=True, text=True, check=True, shell=False)

    # Print the standard output (which contains the version)
    print("Found MUSCLE Version:")
    print(result.stdout.strip()) # .strip() removes leading/trailing whitespace

except FileNotFoundError:
    print(f"Error: 'muscle' command not found.", file=sys.stderr)
    print("Please ensure MUSCLE is installed and in your system's PATH.", file=sys.stderr)
except subprocess.CalledProcessError as e:
    print(f"Error running MUSCLE: {e}", file=sys.stderr)
    print(f"Stderr: {e.stderr.strip()}", file=sys.stderr)
except Exception as e:
    print(f"An unexpected error occurred: {e}", file=sys.stderr)	




