from core.filehandler import File, Handler
from core.misc import Misc
from core.threadmanager import ThreadManager
from core.cloudhelper import GoogleDrive
from core.version import Version
from pathlib import Path
import datetime


config = Misc()
config.LoadConfig()
root_paths = config.paths
backup_path = config.backup_path
gd_sk_path = config.gd_sk_path
timeout = config.timeout


version = Version()
print('*'*20)
print(f'Current version: {version.currentVersion}')
if not version.IsUpdated():
    if version.updatedVersion is None:
        pass
    else:
        print(f'Update available: {version.updatedVersion}')
print('*'*20)
print(f'Start time: {datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}')
print('*'*20)
print('Following Paths are being backed up...')
for path in root_paths:
    print(path)
print('*'*20)
print(f'Backup Path: {backup_path}')
print('*'*20)

def driver(path_list, backup_path):
    for path in path_list:
        handler = Handler(path[0],backup_path)
        handler.compressData()
        file_list = handler.fileFactory()
        handler.logFileInfo(file_list)
        handler.finalZip()


thread_manager = ThreadManager()
thread_manager.CalculateThreads(len(root_paths))
path_iter = thread_manager.Slice(root_paths, thread_manager.calculated_threads)
thread_list = thread_manager.ThreadFactory(path_iter,backup_path,driver)

print('*'*20)
print(f'Total Threads: {thread_manager.calculated_threads}')
print('*'*20)

def main():
    for thread in thread_list:
        thread.start()
        thread.join()
    path = Path(backup_path)
    for x in path.iterdir():
        if x.name.startswith('backup') and x.name.endswith('.zip'):
            print(x.name)
    print('Upload to Google Drive\nCtrl + c to cancel')
    try:
        z = input('Enter file name:')
        z = path.joinpath(z)
        google_drive = GoogleDrive(gd_sk_path,timeout)
        google_drive.authHandler()
        google_drive.uploadFile(z)
    except KeyboardInterrupt:
        print('\nBye...')
        quit()




main()
