# MFS

Memory File System

## Dependency

- Python3.5/3.6

## Run

    python main.py


## Tests

    python tests.py


## Usage

    Help:
    /---------------------------------------------------------\\
    |  CMD  |      Usage      |            Example           |
    ----------------------------------------------------------
    |  ls   |   ls [path]     |  ls /root ; ls ../  ; ls ./  |
    | mkdir |   mkdir [path]  | mkdir /root ; mkdir /etc/www |
    |  pwd  |      pwd        |              pwd             |
    | touch |    touch name   |  touch x.c ; touch /root/x.c |
    | tree  |   tree [path]   |   tree ; tree . ; tree /root |
    |  cd   |   cd [path]     |   cd /root ; cd ../          |
    | fread | fread file_path |   fread x.c ; fread /root/x.c|
    | fwrite| fwrite file_path|   fwrite x.c "dataxxx"       |
    |  cp   |cp s_name t_name |   cp /root/s.txt /etc/t.txt  |
    |  help |      help       |             help             |
    |  exit |      exit       |             exit             |
    \---------------------------------------------------------/

## Summary

由于纯粹基于内存进行快速随机存储 , 且对文件夹中内容无排序需求, 树深度(目录层级)一般情况不会过深, 故而简单地采用一棵的自由树来组织目录结构。

每个子节点有两种类型 : Directory 和 File , 根节点自身是一个 Directory。
