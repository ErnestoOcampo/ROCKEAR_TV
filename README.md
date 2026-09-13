# ROCKEAR TV

## Que hay en este repo

- `index.html` — **sitio actual en produccion**, en la raiz de GitHub Pages. Intacto.
- `new/` — **sitio nuevo, multipagina, en prueba**. Se publica en `/new/` con `noindex`
  y `robots.txt` bloqueado mientras se revisa.
- `.github/workflows/static.yml` — deploy automatico con cada push a `main`.

## Estructura del sitio nuevo

```
new/
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
  _build/           generador de paginas (no se publica como pagina)
```

## Como editar

El header, el footer y el `<head>` son **uno solo** para las 9 paginas: viven en
`_build/build.py`. El contenido de cada seccion vive en `_build/parts/*.html`.

Despues de tocar cualquiera de los dos, regenerar las paginas:

```bash
cd new && python3 _build/build.py
```

Estilos y scripts compartidos: `assets/css/main.css` y `assets/js/main.js`.

## Para reemplazar al sitio actual

Mover el contenido de `new/` a la raiz, sacar el `noindex` de `_build/build.py`,
poner `Allow: /` en `robots.txt` y actualizar `SITE` en el generador.

## Archivos fuente

Los PNG originales sin optimizar estan fuera del repo, en `../ROCKEAR_TV_originales/`.
