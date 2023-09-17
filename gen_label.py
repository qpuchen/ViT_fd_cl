import os

if __name__ == '__main__':

    # 定义文件夹路径和CCC.txt文件路径
    folder_path = r'./xfdata/叶片病害识别挑战赛训练集-复赛/'
    output_file = r'./xfdata/datasets/leaf_disease_new/anno/label.txt'

    i = 0
    # 遍历文件夹folder_path下的所有文件
    with open(output_file, 'w') as f:
        test=os.listdir(folder_path)
        for subfolder_name in os.listdir(folder_path):
            i += 1
            subfolder_path = os.path.join(folder_path, subfolder_name)
            if os.path.isdir(subfolder_path):
                label = i
                for file_name in os.listdir(subfolder_path):
                    file_path = os.path.join(subfolder_path, file_name)
                    f.write(f'{file_name} {label}\n')

    print('文件名和标签已写入label.txt文件中。')

