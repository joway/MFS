from mfs.mfs import MFS

mfs = MFS()
mfs.mkdir('root')
mfs.mkdir('root/xxx')
mfs.ls()
mfs.cd('root')
mfs.ls()

