import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user_test1_exits(host):
    """
    Unit test for the presence of the local user test1
    :param host: instance under test
    :return: None
    """

    assert host.ansible(
        "win_user",
        "name='test1' Ensure='Present'"
        )["changed"] is False


def test_default(host):
    """
    Default unit test that always passes
    :param host: instance under test
    :return: None
    """
    assert 1 == 1


def test_temp_directory_exits(host):
    """
    Unit test for the presence of the Windows temp directory
    :param host: instance under test
    :return: None
    """
    assert host.ansible(
        "win_file",
        "path='C:\\temp3' state=directory"
        )["changed"] is False
