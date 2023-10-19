# Unscrambler for teamcity passwords
Compatibility with all versions of TeamCity for the last few years at least

## How to run
Script works only with python2 
```bash
pip2 install -r requirements.txt
python2 decrypt.py <encrypt password>
```

### Run via docker

Build local docker image
```
docker build https://github.com/DmitryevichD/teamcity-password-decryptor.git --tag=teamcity-password-decryptor
```

Unscrambler password
```
docker run teamcity-password-decryptor --rm  zxxb1b64ad3319d8d0ba7e5744b9e50a0fb
```

[Source research](https://www.exfiltrated.com/research/Continuous_Integration_Continous_Compromise_Bsides2017_Wesley_Wineberg.pdf)

[Source script](https://exfiltrated.com/research/teamcity-secret-decrypt.py)
