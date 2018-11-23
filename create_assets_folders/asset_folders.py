proj_asset_pub_subfolder = ["Chars", "Fx", "Props", "Sets"]


print proj_dir_asset_path[0]
print os.path.isdir(proj_dir_asset_path[0])
if os.path.isdir(proj_dir_asset_path[0]):
    for proj_asset_hierarchy in proj_asset_pub_subfolder:
        asset_folders = os.path.join(proj_dir_asset_path[0], proj_asset_hierarchy)
        os.mkdir(asset_folders)