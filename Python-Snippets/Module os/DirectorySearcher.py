"""Script that recursively searches for a given directory name in a structure and prints paths"""

import os

class DirectorySearcher:
    """Finds given directory name in path, returns None"""
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # Doesn't process a file that isn't a directory.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")
