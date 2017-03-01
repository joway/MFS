from mfs.constants import CommandType, CommandHelp
from mfs.mfs import MFS

if __name__ == '__main__':
    mfs = MFS()

    while True:
        command_input = input().split(' ')
        cmd = command_input[0]
        args = command_input[1:] if len(command_input) > 1 else []
        try:
            if cmd == CommandType.CD:
                mfs.cd(args[0])
            elif cmd == CommandType.LS:
                mfs.ls(args[0])
            elif cmd == CommandType.MKDIR:
                mfs.mkdir(args[0])
            elif cmd == CommandType.PWD:
                mfs.pwd()
            elif cmd == CommandType.TREE:
                mfs.tree(args[0])
            else:
                print('Unknown command')
        except Exception as e:
            print(CommandHelp[cmd])
