import os
def DeleteFile (Filepath):

  if os.path.exist (Filepath):
    os.remove (Filepath)
    print ("Deleted" + Filepath)
  else:
    print ("File dosn't exist")
DeleteFile ('text.txt')