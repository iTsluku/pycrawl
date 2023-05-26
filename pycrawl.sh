#!/bin/bash

pycrawl_directory="$HOME/repos/pycrawl/"

cd "$pycrawl_directory" || exit
python -m pycrawl "$@"

#### GUIDE ####
# 1. Set directory (line 3)
#    pycrawl_directory="$HOME/repos/pycrawl/"
# 2. Copy symbolic link to directory listed in the PATH variable
#    ln -s "$(pwd)/pycrawl.sh" "$HOME/bin"
# 3. Make script executable
#    chmod +x "$HOME/bin/pycrawl.sh"
# 4. Run the script from any directory with input arguments.
#    pycrawl.sh arg1 arg2 arg3
#### GUIDE ####