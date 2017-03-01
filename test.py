from mfs.constants import CommandType
from mfs.mfs import MFS

if __name__ == '__main__':
    mfs = MFS()
    mfs.mkdir('/etc/www')
    mfs.mkdir('/etc/aaa/xxx')
    mfs.mkdir('/etc/aaa/asdas')
    mfs.mkdir('/root/xx')
    mfs.mkdir('/root/asda')
    # mfs.ls()
    mfs.cd('/etc')
    mfs.cd('aaa')
    mfs.pwd()
    print(mfs.parent_path('etc/aaa/bbb'))
    # a = mfs.get_root_path()
    # print(a)
    # print(os.path.split('../etc'))
    # mfs.pwd()

    while True:
        command_input = input().split(' ')
        cmd = command_input[0]
        args = command_input[1:] if len(command_input) > 1 else []
        if cmd == CommandType.CD:
            pass
        elif cmd == CommandType.LS:
            pass
        elif cmd == CommandType.MKDIR:
            pass
        elif cmd == CommandType.PWD:
            pass
        elif cmd == CommandType.TREE:
            pass
        print(args)
