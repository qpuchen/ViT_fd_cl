import os


if __name__ == '__main__':
    import os

    dataset_path = r'./xfdata/叶片病害识别挑战赛训练集_new/'

    # 遍历文件夹下的所有文件
    for folder_name in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path + folder_name)

        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                new_filename = "pre_" + filename
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
                print(f'Renamed: {filename} to {new_filename}')



