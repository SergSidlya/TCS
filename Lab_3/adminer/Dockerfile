FROM php:apache
MAINTAINER Your Name <youremail@domain.com>

RUN apt-get update && \
    apt-get install -y wget && \
    rm -rf /var/lib/apt/lists/* && \
    wget -O /usr/local/bin/adminer.php https://github.com/vrana/adminer/releases/download/v4.7.7/adminer-4.7.7.php && \
    echo "Alias /adminer.php /usr/local/bin/adminer.php" >> /etc/apache2/apache2.conf && \
    echo "Alias /adminer /usr/local/bin/adminer.php" >> /etc/apache2/apache2.conf

EXPOSE 80
CMD ["apache2-foreground"]
