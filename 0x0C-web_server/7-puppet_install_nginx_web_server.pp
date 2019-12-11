# Install Nginx web server (w/ Puppet)

exec {'nginx_install':
  command  => 'sudo apt update && sudo apt -y install nginx && echo "Holberton School" | sudo tee /var/www/html/index.html',
  provider => shell,
}
exec {'nginx_full':
  command  => 'new_string="server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;" && sudo sed -i "s/server_name _;/$new_string/" /etc/nginx/sites-available/default && sudo service nginx restart',
  provider => shell,
}