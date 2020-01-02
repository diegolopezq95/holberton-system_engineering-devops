# Custom HTTP header response (w/ Puppet)

exec {'HTTP_header':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; new_string_header="http {\\n\\tadd_header \"X-Served-By\" \"$HOSTNAME\";" ; sudo sed -i "s/http {/$new_string_header/" /etc/nginx/nginx.conf ; sudo service nginx restart',
  provider => shell,
}