from utils import ssh_pexpect


def test_remote_echo(username, password, hostname):
    """
    Test echo on remote connection over ssh
    """
    rsh = ssh_pexpect(username, password, hostname)
    rsh.sendline('echo test_remote_echo_0x001')
    rsh.expect('test_remote_echo_0x001')
    rsh.close()

