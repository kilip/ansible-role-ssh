"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/home/toni/.ssh/id_rsa")

    assert f.exists
    assert f.user == "toni"
    assert f.group == "toni"
