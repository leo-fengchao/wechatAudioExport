"""
这个文件的作用是：
"""
import re
import shutil
import sqlite3
import os
from pprint import pprint

import argparse
import ffmpeg


def get_files_from_manifest(manifest_database_path, ouput_path, directory, file_name_pattern):
    file_list = []

    # 连接到 manifest 数据库
    conn = sqlite3.connect(manifest_database_path)
    cursor = conn.cursor()

    # 执行查询
    cursor.execute(
        f'SELECT * FROM "Files" WHERE "domain" = "AppDomain-com.tencent.xin" AND "relativePath" LIKE "{file_name_pattern}" AND "flags" = 1 ORDER BY relativePath'
    )
    # pprint(cursor.fetchall())

    # 处理查询结果
    for row in cursor.fetchall():
        manifest_file_name = row[0]
        file_full_name = row[2]
        if not file_full_name.endswith('.aud'):
            continue
        chat_id = re.findall(r'Audio/(.+?)/\d*.aud', file_full_name)[0]
        file_name = os.path.basename(file_full_name)

        folder_path = os.path.join(ouput_path, chat_id.strip())
        os.makedirs(folder_path, exist_ok=True)
        save_file_path = os.path.join(folder_path, file_name)

        if not manifest_file_name:
            continue

        file_prefix = manifest_file_name[:2]
        file_path = os.path.join(directory, file_prefix, manifest_file_name)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                with open(save_file_path, 'wb') as output_file:
                    shutil.copyfileobj(file, output_file)

    # 关闭数据库连接
    conn.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='从 iOS 非加密备份数据库中提取微信语音文件，备份文件夹需要先移动至非系统目录，如下载文件夹')

    parser.add_argument('--backup_path', '-i', type=str, required=True, help='Manifest.db文件的路径')
    parser.add_argument('--output_path', '-o', type=str, required=True, help='存储语音文件的目录路径')
    args = parser.parse_args()

    backup_path = args.backup_path
    manifest_database_path = os.path.join(backup_path, "Manifest.db")
    file_name_pattern = '%/Audio/%'  # 指定导出的是微信语音音频文件
    output_path = args.output_path

    get_files_from_manifest(manifest_database_path, output_path, backup_path, file_name_pattern)


