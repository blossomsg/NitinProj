import os
import sys


def create_structure(path):
    """ It will create a proj structure when provided path of a folder.
    This is a command line module

    how to run in command line if not set in env var
    1]cd\
    2]<enter drive name where you have saved the script>:  (d:)
    3]cd <enter path where you have saved the script>
    4]python create_structure.py <arg: path for where you want to create the structures>

    Args:
        path: ["D:\\All_Projs\\TestProjForGit\\test_folder\\"]

    Returns: ["Assetbuildpubs", "References", "Shotdev", "Shotpubs"]
    path/Prod/<with_the_folder_names_from_the_above_mentioned_list>

    """

    # ALERT : Check how to add the directory to environment var so directly calling the file with python creates the folders
    # CAVEAT : Kindly give the dir path
    proj_dir = [path]

    # CAVEAT : Project path lists
    proj_folder = ["Prod"]
    proj_subfolder = ["Assetbuildpubs", "References", "Shotdev", "Shotpubs"]

    # CAVEAT : Joining dir path and folder path
    proj_dir_path = os.path.join(proj_dir[0], proj_folder[0])
    # print proj_dir_path
    os.mkdir(proj_dir_path)

    # CAVEAT : List of all the sub-folders in Proj path(folder)
    proj_dir_asset_path = []

    for proj_hierarchy in proj_subfolder:
        hierarchy_paths = os.path.join(proj_dir_path, proj_hierarchy)
        # print hierarchy_paths
        proj_dir_asset_path.append(hierarchy_paths)
        os.mkdir(hierarchy_paths)

    # CAVEAT : Returning sub-folder paths list
    # return proj_dir_asset_path


if __name__ == '__main__':
    print "This is my main function"
    # create_structure(sys.argv[1:])
    create_structure("D:\\All_Projs\\TestProjForGit\\test_folder\\")
# HOWTO : create_structure("D:\\All_Projs\\TestProjForGit\\test_folder\\")
