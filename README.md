# SortDir

A cli tool to organize a specified directory into specific categories.

___
# About
______

By running `sortdir`, your current working directories loose files, will be sorted into 
5 folders. **IMAGES, VIDEO, DOCUMENTS, COMPRESSED, PROGRAMS**

There is a fairly comprehensive list of filetypes, however if there is a program specific filetype you work with often, you can add it to the `filetypes.py` dictionary. 
_____

# SETUP
______

run the following commands in order to setup:

1. Clone the Repository:

`git clone https://github.com/willn-dev/sort.git`


 2. Make the program executable
    cd into the program folder, then run:
    `chmod -x dl-sort.py`

3. Create the ~/.local/bin directory if it doesn't exist:
    `mkdir -p ~/.local/bin`

4. Create a symlink in order to add the program to your PATH:
    `ln -s $(pwd)/dl-sort.py ~/.local/bin/sortdir`
    (by default this will be called using *sortdir*, however, you can change
    this name to anything you would like.)

5. Add ~/.local/bin to your PATH if it's not already there:
   
   First, check which shell you're using, if you dont already know:
   `echo $SHELL`
   
   **For Bash:**

   `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc`

   reload your shell:
   `source ~/.bashrc`

   
   **For Zsh (macOS default):**

   `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc`
   reload your shell:
   `source ~/.zshrc`

You are now set up, and ready to sort!
**NOTE: DO NOT RUN THIS PROGRAM IN A DIRECTORY IN WHICH YOU DO NOT WANT LOOSE FILES MOVED**

# USAGE

Simply cd into the directory you would like to run the program on.
execute `sortdir` (or whatever name you set in step 4).


