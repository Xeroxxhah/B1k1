from pathlib import *
from .misc import Misc
import zipfile
import datetime
import hashlib
import os
import shutil


class File:
    def __init__(self, file_path):
        self.path = Path(file_path)
        self.file_path = file_path if self.path.exists() else None
        self.file_name = self.path.name
        self.file_type = self.file_name.split('.')[-1] if len(self.file_name.split('.')) > 0 else None
        self.file_size = self.path.stat().st_size
        self.file_checksum = self.getCheckSum()

    def getCheckSum(self):
        if self.file_path is not None:
            with open(self.file_path,'rb') as reader:
                data = reader.read()
                return hashlib.md5(data).hexdigest()
        return None
    
    def __str__(self):
        return f'''
        File Path: {self.file_path}
        File Name: {self.file_name}
        File Type: {self.file_type}
        File Size: {self.file_size}
        File Checksum: {self.file_checksum}
        '''

class Handler:

    def __init__(self,root_path, dest_path):
        self.path = Path(root_path)
        self.dpath = Path(dest_path)
        self.root_path = root_path if self.path.exists() else None
        self.backup_dir_name = f'backup_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}'
        self.dest_path = self.dpath.joinpath(self.backup_dir_name) if self.dpath.exists() else None
        

    
    def compressData(self):
        path = Path(self.root_path)
        zip_name = f'{path.name}{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.zip'
        destination_path = Path(self.dest_path)
        if not destination_path.exists():
            destination_path.mkdir(parents=True)
        with zipfile.ZipFile(destination_path.joinpath(zip_name), mode="w") as archive:
            for file_path in path.rglob('*'):
                archive.write(
                    file_path,
                    arcname=file_path.relative_to(path)
                )
    
    def fileFactory(self):
        fileslist = []
        for r,d,f in os.walk(self.root_path):
            for files in f:
                file = File(os.path.join(r,files))
                fileslist.append(file)
        return fileslist
    
    def logFileInfo(self,files):
        file_name = f'log_{self.path.name}_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.log'
        destination_path = Path(self.dest_path)
        with open(destination_path.joinpath(file_name),'w') as logger:
            for file in files:
                logger.write(str(file))
        logger.close()

    def finalZip(self):
        zip_name = f'{self.dest_path.name}.zip'
        with zipfile.ZipFile(self.dest_path.parent.joinpath(zip_name), mode="w") as archive:
            for file_path in self.dest_path.rglob('*'):
                archive.write(
                    file_path,
                    arcname=file_path.relative_to(self.dest_path)
                )
            shutil.rmtree(self.dest_path)