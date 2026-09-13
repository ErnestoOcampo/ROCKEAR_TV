# ROCKEAR TV

## Que hay en este repo

- `index.html` — **sitio actual en produccion**. Se publica en la raiz de GitHub Pages.
- `new/` — **version nueva, en prueba**. Se publica en `/new/` sin reemplazar el sitio actual.
  Lleva `noindex` para que Google no la tome mientras se revisa.
- `.github/workflows/static.yml` — deploy automatico a GitHub Pages con cada push a `main`.

## La version nueva (`new/`)

- `new/index.html` — sitio completo: HTML, CSS y JS en un solo archivo, sin build ni dependencias.
- `new/assets/` — emblema y logo en WebP.
- `new/assets/marco/` — kit del marco de afiche: 4 esquinas (decoracion unica, nunca se repiten),
  4 tiras de borde (se repiten en un solo eje) y la textura grunge central.

Cuando la nueva reemplace a la actual: mover `new/index.html` y `new/assets/` a la raiz,
sacarle el `noindex` y corregir `canonical` y `og:url`.

## Archivos fuente

Los PNG originales sin optimizar estan **fuera del repo**, en `../ROCKEAR_TV_originales/`,
para que no se suban en cada deploy.
