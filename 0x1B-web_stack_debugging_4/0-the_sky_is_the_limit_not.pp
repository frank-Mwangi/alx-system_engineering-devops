# Increase the number of requests web server
# can handle by increasing ulimit

exec { 'add-requests':
  command  => 'sed -i "5s/[0-9]\+$( ulimit -n )/" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
