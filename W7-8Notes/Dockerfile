FROM php:8.2-apache

COPY app.php /var/www/html

COPY ./000-default.conf /etc/apache2/sites-available/000-default.conf

EXPOSE 80

CMD ["apache2-foreground"]