# 0x0F. Load balancer

0- Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
The name of the custom HTTP header must be X-Served-By
The value of the custom HTTP header must be the hostname of the server Nginx is running on

1-Install and configure HAproxy with version equal or greater than 1.5 so that it send traffic to web-01 and web-02
Distribute requests using a roundrobin algorithm
Make sure that HAproxy can be managed via an init script
Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02. If not, follow this tutorial.

2- Creating a custom HTTP header response, but with Puppet.
The name of the custom HTTP header must be X-Served-By
The value of the custom HTTP header must be the hostname of the server Nginx is running on