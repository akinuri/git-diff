import os

def is_git_project(value):
    result = False
    cwd = os.getcwd()
    if not os.path.isdir(value):
        return result
    os.chdir(value)
    result = os.path.isdir(".git")
    os.chdir(cwd)
    return result