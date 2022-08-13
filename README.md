### README.md 👋
# B1k1
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Xeroxxhah/B1k1)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![Contribution](https://img.shields.io/badge/Contributions-Welcome-<brightgreen>)
[![Active](http://img.shields.io/badge/Status-Active-green.svg)](https://github.com/Xeroxxhah)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![semver](https://badgen.net/badge/Semantic-Version/0.1.1/purple)

A python utility for taking backups and with the option to upload to Google Drive.

# Installation & Usage:

# Follow these steps: 
- 1st: ```git clone https://github.com/Xeroxxhah/B1k1.git```
- 2nd: ```cd B1k1```
- 3rd: ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```
- 4th: ```Configure config.json```
- 5th  ```python3 main.py```

### Configuring config.json
- "paths" = "Pths which you want to take backup of" i.e "/home/username/"

- "backup_path" = "path where you want to store backup" i.e "/home/username/"

- "gd_sk_path" = "Path of Creddentails.json, which was obtained from the authentication process"


### Authentication for Google Drive
please follow the steps in following document:[Authentication Guide](https://1drv.ms/b/s!Aumu-6oUf5yPkxJgMYXNqfdkitQw?e=9462B2) 

### Bug report
Found any bug!
Report it to me at xeroxxhah@pm.me
or open an [issue](https://github.com/Xeroxxhah/B1k1/issues)

### Updates:
schedule jobs for linux and windows.

### Contributions:
All contributions are welcomed.fork this repo,improve it and [pull requests](https://github.com/Xeroxxhah/B1k1/pulls)
### License
Distributed under GPLV3.0
