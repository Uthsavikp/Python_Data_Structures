'''
* @Author: Uthsavi KP
* @Date: 2020-01-06 14:58:52 
* @Last Modified by: Uthsavi KP
* @Last Modified time: 2020-01-06 14:58:52
* @Title : To  find files and skip directories of a given directory.
'''


class FindFiles:
    def find_files_skip_directory(self):
        """
        finding files and skiping directory
        """
        import os
        print([f for f in os.listdir(r'C:\Users\uthsa\week-2_data_structures') if os.path.isfile(os.path.join(r'C:\Users\uthsa\week-2_data_structures', f))])


if __name__ == "__main__":
    fnd_files = FindFiles()
    fnd_files.find_files_skip_directory()
