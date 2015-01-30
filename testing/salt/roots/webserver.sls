apache2:                # ID declaration
  pkg:                  # state declaration
    - installed         # function declaration
  service:
    - running
    - enable: True
    - order: last
    - watch:
      - file: /etc/apache2/sites-available/personalsite
      - file: /etc/apache2/sites-enabled/000-personalsite

python3:
  pkg:
    - installed

libapache2-mod-wsgi-py3:
  pkg:
    - installed

repo-wheezy-backports:
  pkgrepo.managed:
    - humanname: Wheezy Backports Repository
    - name: deb http://http.debian.net/debian/ wheezy-backports main
    - dist: wheezy-backports
    - comps: main,contrib,non-free
    - consolidate: True
    - require:
      - pkg: python-apt
    - require_in:
      - pkg: python3-django

python-apt:
  pkg:
    - installed

python3-django:
  pkg:
    - installed

python3-markdown:
  pkg:
    - installed

/etc/apache2/sites-available/personalsite:
  file.managed:
    - name: /etc/apache2/sites-available/personalsite
    - source: salt://apache2/sites-available/personalsite
    - user: root
    - group: root
    - mode: 644
    - require:
      - pkg: apache2

/etc/apache2/mods-enabled/rewrite.load:
  file.symlink:
    - target: /etc/apache2/mods-available/rewrite.load
    - require:
      - pkg: apache2

/etc/apache2/mods-enabled/ssl.load:
  file.symlink:
    - target: /etc/apache2/mods-available/ssl.load
    - require:
      - pkg: apache2

/etc/apache2/mods-enabled/ssl.conf:
  file.symlink:
    - target: /etc/apache2/mods-available/ssl.conf
    - require:
      - pkg: apache2

/etc/apache2/ssl/server.crt:
  file.managed:
    - source: salt://ssl/server.crt
    - user: root
    - group: root
    - mode: 400
    - makedirs: True
    - require:
      - pkg: apache2

/etc/apache2/ssl/server.key:
  file.managed:
    - source: salt://ssl/server.key
    - user: root
    - group: root
    - mode: 400
    - makedirs: True
    - require:
      - pkg: apache2

/etc/apache2/sites-enabled/000-personalsite:
  file.symlink:
    - target: /etc/apache2/sites-available/personalsite
    - require:
      - file: /etc/apache2/sites-available/personalsite

/etc/apache2/sites-enabled/000-default:
  file:
    - absent
    - require:
      - pkg: apache2

www:
  user.present:
    - home: /home/www
    - groups:
      - www-data

www-data:
  user.present:
    - groups:
      - www
    - remove_groups: False
    - require:
      - pkg: apache2

/home/www/static:
  file.directory:
    - user: www
    - group: www
    - mode: 755
    - require:
      - user: www

/home/www/personalsite:
  file.recurse:
    - source: salt://personalsite/
    - user: www
    - group: www
    - file_mode: 774
    - dir_mode: 775
    - require:
      - user: www

/var/www/html:
  file.directory:
    - user: root
    - group: root
    - makedirs: True

/etc/personalsite/personalsite.sqlite3:
  file.managed:
    - source: salt://personalsite_conf/personalsite.sqlite3
    - replace: False
    - makedirs: True
    - user: root
    - group: www-data
    - mode: 664

/etc/personalsite/lastfm_api_key.txt:
  file.managed:
    - source: salt://personalsite_conf/lastfm_api_key.txt
    - makedirs: True
    - user: root
    - group: root
    - mode: 664

/etc/personalsite/django_secret_key.txt:
  file.managed:
    - source: salt://personalsite_conf/django_secret_key.txt
    - makedirs: True
    - user: root
    - group: root
    - mode: 664

/home/www/static/bootstrap_custom.css:
  file.managed:
    - source: salt://personalsite_static/bootstrap_custom.css
    - user: www
    - group: www
    - mode: 774
    - require:
      - user: www

sudo su - www -c "python3 /home/www/personalsite/manage.py collectstatic -v0 --noinput":
  cmd.run:
    - require:
      - pkg: python3-django
      - file: /home/www/static
      - file: /home/www/personalsite
      - user: www
