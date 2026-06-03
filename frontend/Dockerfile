FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
COPY cytoscape.min.js /usr/share/nginx/html/cytoscape.min.js

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000