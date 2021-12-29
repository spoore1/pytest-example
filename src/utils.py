import numbers
import pexpect
from pexpect.pxssh import pxssh


def ssh_pexpect(username, password, hostname, encoding='utf-8'):
    """ Setup an ssh connection to remote host """
    ssh = pxssh(options={
        "StrictHostKeyChecking": "no",
        "UserKnownHostsFile": "/dev/null"
        }, encoding=encoding, codec_errors='replace')
    ssh.force_password = True
    ssh.login(hostname, username, password)
    ssh.sendline('echo loggedin')
    ssh.expect('loggedin')
    return ssh


def check_number(number):
    if type(number) !== int:
        raise ValueError(f'value {number} is not an integer!')


def add(num1, num2):
    for num in [num1, num2]:
        check_number(num)
    result = sum([num1, num2])
    return result
