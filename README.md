# MascotApp - Proyecto final TPDI

> MascotApp es una red social dedicada a las mascotas que brinda múltiples servicios como ayudar a encontrar las mascotas perdidas, realizar adopciones y/o tránsito. Además brinda información sobre castraciones y campañas de vacunación gratuitas.

## Grupo 01
- Bálsamo, Verónica 
- Carbone, Paula
- Perez, Leonor

## Configuración inicial
```
pip install -r requirements.txt
```

## Iniciar aplicación localmente
```
python main.py
```

## Heroku

### Configuración inicial
1. Instalar [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)
2. Ejecutar `heroku login`
3. Ejecutar `heroku git:remote -a mascot-app-dev`

### Subir nueva versión
```
git push heroku main
```

### Abrir aplicación
https://mascot-app-dev.herokuapp.com/