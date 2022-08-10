# connecting to a server without
file_line { '/etc/ssh/ssh_config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no;    IdentityFile ~/.ssh/holberton',
}