class CommandType(object):
    LS = 'ls'
    MKDIR = 'mkdir'
    PWD = 'pwd'
    TREE = 'tree'
    CD = 'cd'
    TOUCH = 'touch'
    CP = 'cp'
    HELP = 'help'
    FREAD = 'fread'
    FWRITE = 'fwrite'
    EXIT = 'exit'


CommandHelp = {
    CommandType.LS: "eg: ls /root ; ls ../  ; ls ./",
    CommandType.MKDIR: "eg: mkdir /root ; mkdir /etc/www",
    CommandType.PWD: "eg: pwd",
    CommandType.TREE: "eg: tree ; tree . ; tree /root",
    CommandType.CD: "eg: cd /root ; cd ../",
    CommandType.CP: "eg: cp /root/s.txt /etc/t.txt",
    CommandType.TOUCH: "eg: touch x.c ; touch /root/x.c ",
    CommandType.FREAD: "eg: fread x.c ; fread /root/x.c",
    CommandType.FWRITE: "eg: fwrite x.c \"dataxxx\"",
}
