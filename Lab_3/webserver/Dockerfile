FROM nginx:latest
RUN apt-get update && apt-get install -y curl
COPY . /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]