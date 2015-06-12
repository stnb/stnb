INSERT INTO comptes_usuari (id, password, last_login, is_superuser, email, nom, cognoms, is_staff, is_active, date_joined) SELECT a.id, a.password, a.last_login, a.is_superuser, a.email, a.first_name, a.last_name, a.is_staff, a.is_active, a.date_joined from auth_user a;

