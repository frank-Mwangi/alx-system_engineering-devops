#Creates a custom HTTP header using Puppet

exec { 'update':
  command => 'apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line { 'redirect':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
  require =>  Package['nginx'],
}

file_line { 'addHeader':
  ensure  =>  'present',
  path    =>  '/etc/nginx/sites-available/default',
  after   =>  'listen 80 default_server;'
  line    =>  'add_header X-Served-By $HOSTNAME;',
  require =>  Package['nginx'],
}

file { '/var/www/html/index.html':
  content  => 'Hello World!",
  require  =>  Package['nginx'],
}

service { 'nginx':
  ensure   =>  running,
  require  =>  Package['nginx'],
}

