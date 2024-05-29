import argparse
import os
import random
import shutil


def split_images(args):

    # 创建目标文件夹
    os.makedirs(os.path.join(args.output_folder, 'train_A'), exist_ok=True)
    os.makedirs(os.path.join(args.output_folder, 'train_B'), exist_ok=True)
    os.makedirs(os.path.join(args.output_folder, 'test_A'), exist_ok=True)
    os.makedirs(os.path.join(args.output_folder, 'test_B'), exist_ok=True)

    # 获取文件列表
    files_a = [file for file in os.listdir(args.folder_a) if not file.endswith('.jsonl')]
    files_b = [file for file in os.listdir(args.folder_b) if not file.endswith('.jsonl')]

    # 计算分割数量
    train_count_a = int(len(files_a) * args.train_ratio)
    train_count_b = int(len(files_b) * args.train_ratio)

    # 随机打乱文件列表
    random.shuffle(files_a)
    random.shuffle(files_b)

    # 拷贝文件到训练集和测试集
    for i, filename in enumerate(tqdm(files_a)):
        source_path = os.path.join(args.folder_a, filename)
        if i < train_count_a:
            destination_folder = os.path.join(args.output_folder, 'train_A')
        else:
            destination_folder = os.path.join(args.output_folder, 'test_A')
        destination_path = os.path.join(destination_folder, filename)
        shutil.copyfile(source_path, destination_path)

    for i, filename in enumerate(tqdm(files_b)):
        source_path = os.path.join(args.folder_b, filename)
        if i < train_count_b:
            destination_folder = os.path.join(args.output_folder, 'train_B')
        else:
            destination_folder = os.path.join(args.output_folder, 'test_B')
        destination_path = os.path.join(destination_folder, filename)
        shutil.copyfile(source_path, destination_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split images from folders A and B into train and test sets.')
    parser.add_argument('--folder_a', type=str, help='Path to folder A')
    parser.add_argument('--folder_b', type=str, help='Path to folder B')
    parser.add_argument('--output_folder', type=str, help='Path to output folder')
    parser.add_argument('--train_ratio', type=float, default=0.8,
                        help='Ratio of images to be put into the training set (default: 0.8)')
    args = parser.parse_args()

    # 调用函数进行分割
    split_images(args)
