FROM nginx:1.19.6

EXPOSE 5000
EXPOSE 80

COPY key.key /etc/nginx/certs/host.key
COPY cert.crt /etc/nginx/certs/host.crt

RUN chmod 600 /etc/nginx/certs/host.key
RUN chmod 600 /etc/nginx/certs/host.crt

COPY nginx.conf /etc/nginx/     
COPY default.conf /etc/nginx/conf.d