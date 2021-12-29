from utils import ssh_pexpect, add


def test_remote_echo(username, password, hostname):
    """
    Test echo on remote connection over ssh
    """
    rsh = ssh_pexpect(username, password, hostname)
    rsh.sendline('echo test_remote_echo_0x001')
    rsh.expect('test_remote_echo_0x001')
    rsh.close()


def test_remote_whoami(username, password, hostname):
    """
    Test whoami on remote connection over ssh
    """
    rsh = ssh_pexpect(username, password, hostname)
    rsh.sendline('whoami')
    rsh.expect(username)
    rsh.close


def test_add_function():
    """
    Test utils add function
    """
    sum = add(1, 2)
    assert sum == 4

