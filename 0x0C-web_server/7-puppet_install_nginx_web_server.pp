# Install Nginx web server (w/ Puppet)

$my_string = '\"server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;\"'

package { 'nginx':
  ensure => installed,
}
exec { 'display':
  path    => ['/usr/bin', '/bin'],
  command => 'echo "Holberton School" | sudo tee /var/www/html/index.html',
}
exec { 'change':
  path    => ['/usr/bin', '/bin'],
  command => 'sed -i "s/server_name _;/$my_string/" /etc/nginx/sites-available/default',
}
exec { 'start_nginx':
  path    => ['/usr/bin', '/bin'],
  command => 'sudo service nginx restart',
}