from pathlib import *
import platform
import json
from pathlib import Path

class Misc:
    if platform.system() == 'Windows':
        config_path = PureWindowsPath(PureWindowsPath('.').parent).joinpath('config.json')
    elif platform.system() == 'Linux':
        config_path = PurePosixPath(PurePosixPath('.').parent).joinpath('config.json')
    else:
        config_path = None
    
    backup_path = ''
    paths = ''
    gd_sk_path = ''
    timeout = ''
    
    
    def LoadConfig():
        with open(Misc.config_path, 'r') as config:
            config_content = config.read()
            config_settings = json.loads(config_content)
            for key ,value in config_settings.items():
                if config_settings.get(key) == '':
                    print(f'{key} is not set.')
                    quit()
            if len(config_settings.get('paths')) > 1:
                for path in config_settings.get('paths'):
                    temp_path = Path(path)
                    if not temp_path.exists():
                        print('Please provide valid path')
                        quit()
            temp_backup_path = Path(config_settings.get('backup_path'))
            temp_paths = Path(config_settings.get('paths')[0])
            temp_gd_sk_path = Path(config_settings.get('gd_sk_path'))
            if temp_backup_path.exists() and temp_paths.exists() and temp_gd_sk_path.exists():            
                Misc.backup_path = config_settings.get('backup_path')
                Misc.paths = config_settings.get('paths')
                Misc.gd_sk_path = config_settings.get('gd_sk_path')
                Misc.timeout = config_settings.get('timeout')
            else:
                Misc.backup_path = ''
                Misc.timeout = ''
                Misc.paths = ''
                Misc.gd_sk_path = ''
                print('Please provide valid paths...')
                quit()


                    

