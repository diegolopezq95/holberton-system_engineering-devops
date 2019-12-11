# Install Nginx web server (w/ Puppet)

package { 'nginx':
  ensure => 'present',
}
exec { 'display':
  path    => ['/usr/bin', '/bin'],
  command => 'echo "Holberton School" | sudo tee /var/www/html/index.html',
}
exec { 'change':
  path    => ['/usr/bin', '/bin'],
  command => 'sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.google.com\/ permanent;/" /etc/nginx/sites-available/default',
}
exec { 'start_nginx':
  path    => ['/usr/bin', '/bin'],
  command => 'sudo service nginx start',
}