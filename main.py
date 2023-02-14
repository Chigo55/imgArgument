import os, shutil
import cv2
import numpy as np

file_cnt = 33000
output_path = './argument'

def addtionData(file_name):
    try:
        global file_cnt
        txt_file_name = file_name[:-4] + ".txt"

        img = cv2.imread(file_name)
        flip = cv2.flip(img, 1)

        cv2.imwrite(output_path + str(file_cnt).zfill(6) + '.jpg', flip)
        flip_txt_name = output_path + str(file_cnt).zfill(6) + '.txt'
        file_cnt += 1

        # flip 일때
        modified = []
        with open(txt_file_name, 'r', encoding='utf-8') as fr:
            data = fr.readlines()
            for i in data:
                data_list = i.split(" ")
                data_list[1] = str(1 - float(data_list[1]))
                modified.append(" ".join(data_list))

        with open(flip_txt_name, 'w', encoding='utf-8') as fw:
            fw.writelines(modified)

        # 반전 없이 명암조절만 할 때
        for i in range(1, 5):
            val = 25 * i
            array = np.full(img.shape, (val, val, val), dtype=np.uint8)

            add = cv2.add(img, array)
            cv2.imwrite(output_path + str(file_cnt).zfill(6) + '.jpg', add)
            shutil.copy(txt_file_name, output_path + str(file_cnt).zfill(6) + '.txt')
            file_cnt += 1

            sub = cv2.subtract(img, array)
            cv2.imwrite(output_path + str(file_cnt).zfill(6) + '.jpg', sub)
            shutil.copy(txt_file_name, output_path + str(file_cnt).zfill(6) + '.txt')
            file_cnt += 1

        for i in range(1, 5):
            val = 25 * i
            array = np.full(flip.shape, (val, val, val), dtype=np.uint8)

            add = cv2.add(flip, array)
            cv2.imwrite(output_path + str(file_cnt).zfill(6) + '.jpg', add)
            shutil.copy(flip_txt_name, output_path + str(file_cnt).zfill(6) + '.txt')
            file_cnt += 1

            sub = cv2.subtract(flip, array)
            cv2.imwrite(output_path + str(file_cnt).zfill(6) + '.jpg', sub)
            shutil.copy(flip_txt_name, output_path + str(file_cnt).zfill(6) + '.txt')
            file_cnt += 1
    except FileNotFoundError:
        return


if __name__ == "__main__":
    path = "" # to save argument file derectory
    file_list = os.listdir(path)
    for file_path in file_list:
        if 'jpg' in file_path:
            addtionData(path + file_path)
    print('완료')