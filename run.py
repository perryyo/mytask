import os
from task import mytask

zipped_file='Task.zip'
dirpath=os.getcwd()+'/Task' # get current dir and add csv's dir name to end of it
files_format="/*.csv"
out_put_file="SampleOutput.csv" # define output file name

do_this=mytask(dirpath,files_format,out_put_file,zipped_file)
do_this.do_this_now(zipped_file)
