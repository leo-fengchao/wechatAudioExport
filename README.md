# wechatAudioExport
将 iOS 备份中的微信语音文件导出至本地。

通过对 [ph-my-wechat](https://github.com/chclt/oh-my-wechat) 项目的研究，实现了一个从 iOS 备份文件中的导出微信语音文件的功能。

## 使用方法

### 将备份文件转移至非系统文件夹

Mac 下默认的备份路径：~/Library/Application Support/MobileSync/Backup，我们需要将文件夹是 xxxxxxxx-xxxxxxxxxxxxxxxx 格式并且是希望提取文件的那个备份复制粘贴到非系统路径下，如 `Downloads/下载` 文件夹。

### 运行

```
python3 export_wechat_voice_files_from_backup.py \
--backup_path /path/to/xxxxxxxx-xxxxxxxxxxxxxxxx \
--output_path /path/to/output_folder
```

或

```
python3 export_wechat_voice_files_from_backup.py \
--i /path/to/xxxxxxxx-xxxxxxxxxxxxxxxx \
--o /path/to/output_folder
```

#### 参数说明

--backup_path 或 -i：复制到非系统路径下的备份文件夹路径（名称为 xxxxxxxx-xxxxxxxxxxxxxxxx 格式）

--output_path 或 -o：存储语音文件的文件夹路径
