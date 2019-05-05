import glob
import pandas as pd
from zipfile import ZipFile

class mytask:

    def __init__(self, dirpath,files_format,out_put_file,zipped_file):
        self.dirpath = dirpath
        self.files_format=files_format
        self.out_put_file=out_put_file
        self.zipped_file=zipped_file

    def unzip_this(self,file_name):
        with ZipFile('Task.zip', 'r') as zipObj:
            zipObj.extractall()
        return True

    def read_and_sort_by_date(self):
        all_files = glob.glob(self.dirpath + self.files_format)
        all_files.sort()
        return all_files
        # return __init__.dirpath

    def get_date_and_time(self,string):
        item=string.split('-')
        fixer1=item[3].split('_')
        fixer2=item[4].split('.')
        datee=item[1]+'/'+item[2]+'/'+fixer1[0]
        time=fixer1[1]+':'+fixer2[0]
        item_date_time=datee+' '+time
        return item_date_time

    def read_this_csv(self,string):
        mydf=pd.read_csv(string, skiprows=1,header=None, sep=";")
        return mydf

    def mix_and_save(self,myfull_frame,out_put_file):
        frame = pd.concat(myfull_frame, axis=0, ignore_index=False)
        export_csv = frame.to_csv (self.out_put_file, index = None, header=True)
        return frame

    def do_this_now(self,zipped_file):
        self.unzip_this(zipped_file)
        all_files=self.read_and_sort_by_date()
        i=0
        myfull_frame=[]
        for string in all_files:
            item_date_time=self.get_date_and_time(string)
            mydf=self.read_this_csv(string)
            mydf.insert(0, 'date_time', item_date_time)
            mydf.columns = ['date_time','Color','Some Event','Some Name','Count']
            myfull_frame.append(mydf)
            self.mix_and_save(myfull_frame,self.out_put_file)
        # print(myfull_frame)
        print('Done')
