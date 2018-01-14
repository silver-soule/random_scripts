import subprocess
import os
import sys

FNULL = open(os.devnull, 'w')
    
def run_subprocess(split_cmd):
    retcode = subprocess.call(split_cmd, stdout=FNULL, stderr=subprocess.STDOUT)
    return retcode

def run_cmd(cmd):
    split_cmd = cmd.strip().split(" ")
    return run_subprocess(split_cmd)

def run_for_all_subdirs(directory_path,list_of_cmds):
    list_of_subdirs = os.listdir(directory_path)
    for directory in list_of_subdirs:
        os.chdir(directory)
        run_chain_of_commands_one_dir(directory,list_of_cmds)
        os.chdir("../")


#HOW TO USE: first parameter is the path opf the folder you want to go to
#, after that just type in the command you want to run
# e.g python script.py **path** git pull origin master , mvn clean compile


def run_chain_of_commands_one_dir(dir, list_of_cmds):
    for cmd in list_of_cmds:
        return_code = run_cmd(cmd)
        print(str(return_code) +" : " + cmd + "  " + dir)

def args_to_list_of_commands(args):
    cmds = " ".join(sys.argv[2:])
    list_of_cmds = cmds.split(",")
    return list_of_cmds

if __name__ =='__main__':
    if sys.argv[1]!=None:
        os.chdir(sys.argv[1])

    if sys.argv[2]!=None:
        list_of_cmds = args_to_list_of_commands(sys.argv)
        curr_dir = os.getcwd()
        run_for_all_subdirs(curr_dir,list_of_cmds)
