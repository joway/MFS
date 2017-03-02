from mfs.constants import CommandType, CommandHelp
from mfs.exceptions import MFSException
from mfs.mfs import MFS

if __name__ == '__main__':
    mfs = MFS()
    help_text = """
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
    
Input your command :

    """

    print(help_text)

    while True:
        command_input = input().split(' ')
        cmd = command_input[0]
        args = command_input[1:] if len(command_input) > 1 else []
        try:
            if cmd == CommandType.CD:
                mfs.cd(args[0])
            elif cmd == CommandType.LS:
                if not args:
                    args = ['.']
                mfs.ls(args[0])
            elif cmd == CommandType.MKDIR:
                mfs.mkdir(args[0])
            elif cmd == CommandType.TOUCH:
                if len(args) == 1:
                    mfs.touch(args[0])
                else:
                    mfs.touch(args[0], args[1])
            elif cmd == CommandType.PWD:
                mfs.pwd()
            elif cmd == CommandType.TREE:
                if not args:
                    mfs.tree()
                else:
                    mfs.tree(args[0])
            elif cmd == CommandType.CP:
                if len(args) == 2:
                    mfs.cp_dir(source_path=args[0], target_path=args[1])
                else:
                    mfs.cp_file(source_path=args[0], source_filename=args[1],
                                target_path=args[2], target_filename=args[3])
            elif cmd == CommandType.FREAD:
                ret = mfs.read_file(args[0])
                print(ret)
            elif cmd == CommandType.FWRITE:
                mfs.write_file(file_path=args[0], data=args[1])
            elif cmd == CommandType.EXIT:
                print('Good bye !')
                break
            elif cmd == CommandType.HELP:
                print(help_text)
            else:
                print('Unknown command')
            mfs.tree('.')
        except MFSException as me:
            print(str(me))
            print(CommandHelp[cmd])
        except Exception as me:
            print(CommandHelp[cmd])
