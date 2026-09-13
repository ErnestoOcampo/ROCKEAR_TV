# ROCKEAR TV

Sitio oficial de **ROCKEAR TV** — creado por Ernesto Ocampo, producido por Rockeart.produce.
Se publica en GitHub Pages con cada push a `main`.

## Estructura

```
index.html        Home
el-medio/         Que es ROCKEAR TV + redes
agenda/           Proxima fecha + archivo
produce/          Rockeart.produce
ernesto/          El creador (bio)
libro/            La musica, mi religion
sponsors/         Nos acompanan
contacto/         Contacto
legal/            Aviso legal
sitemap.xml       9 URLs
robots.txt
assets/           css, js, imagenes, marco, sponsors, eventos
_build/           generador de paginas
```

## Como editar

El header, el footer y el `<head>` son **uno solo** para las 9 paginas: viven en
`_build/build.py`. El contenido de cada seccion vive en `_build/parts/*.html`.
Despues de tocar cualquiera de los dos hay que regenerar:

```bash
python3 _build/build.py
```

Estilos y scripts compartidos: `assets/css/main.css` y `assets/js/main.js`.
Si se agrega o saca una pagina, actualizar tambien `sitemap.xml`.

## Archivos fuente

Los PNG originales sin optimizar estan fuera del repo, en `../ROCKEAR_TV_originales/`.
