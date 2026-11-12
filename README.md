# publicar_facturaap

Repositorio publicado con GitHub Pages en `https://diegomesav.github.io/publicar_facturaap/`.
Cada `git push` a `main` se publica en 1 o 2 minutos.

## Políticas de las apps de Google Play (`/politicas`)

Base de las URL: `https://diegomesav.github.io/publicar_facturaap/politicas/`

| Archivo | App | Uso en Play Console |
|---|---|---|
| [`PoliticaPrivacidadFacturaap.html`](politicas/PoliticaPrivacidadFacturaap.html) | Facturaap | Contenido de la aplicación > Política de privacidad |
| [`TerminosFacturaap.html`](politicas/TerminosFacturaap.html) | Facturaap | Contenido de la aplicación > Estado de operador a nivel de aplicación y términos del servicio |
| [`PoliticaPrivacidadAnalista.html`](politicas/PoliticaPrivacidadAnalista.html) | Analista | Contenido de la aplicación > Política de privacidad |
| [`TerminosAnalista.html`](politicas/TerminosAnalista.html) | Analista | Contenido de la aplicación > Estado de operador a nivel de aplicación y términos del servicio |
| `politica-de-privacidad-boomerang-digital.html` | Boomerang Digital | Otro negocio, con su propio correo (`fpboomerang2@gmail.com`). No hace parte de estas apps. |
| `eliminacion-de-datos.html` | Boomerang Digital | Igual que la anterior. |

Correo de contacto en todas las páginas de Facturaap y Analista: `diegomesav0130@gmail.com`.

## Configuración en Play Console (actualizada el 11 de noviembre de 2026)

### Cuenta de desarrollador

- **Estado de operador:** declarada como **operador** (Gestionar cuenta > Información de la cuenta > Información sobre ti).
  - Motivo: las dos apps tienen anuncios de AdMob y se distribuyen en 178 países, incluidos el EEE y el Reino Unido.
    Google considera las apps con publicidad como actividad comercial.
  - El plazo para declarar era el 1 de febrero de 2027 y ya está cumplido.
  - Desde el 1 de marzo de 2027, Google Play muestra en el perfil público el nombre legal, la dirección,
    el correo y el teléfono del desarrollador. El nombre y la dirección vienen del perfil de pagos de Google.
- **Correo público del desarrollador:** `diegomesav0130@gmail.com`.
- **Teléfono del desarrollador:** verificado por SMS y visible públicamente.
- Referencia: <https://support.google.com/googleplay/android-developer/answer/17594752>

### Facturaap (`com.cdp.facturaap`) y Analista (`com.myapp.analista`)

Las dos apps tienen la misma configuración:

| Sección | Valor declarado |
|---|---|
| Estado de operador de la app | Sí, el estado de operador se aplica a esta aplicación |
| Términos del servicio | `TerminosFacturaap.html` / `TerminosAnalista.html` |
| Política de privacidad | `PoliticaPrivacidadFacturaap.html` / `PoliticaPrivacidadAnalista.html` |
| Anuncios | Sí, contiene anuncios (Google AdMob) |
| ID de publicidad | Sí, se usa para publicidad o marketing |
| Distribución | 178 países o regiones |

**Seguridad de los datos.** Se declara lo que recoge el SDK de anuncios de Google, según la
[guía oficial de AdMob](https://developers.google.com/admob/android/privacy/play-data-disclosure):

| Tipo de dato | Recogido | Compartido | Temporal | Obligatorio | Fines |
|---|---|---|---|---|---|
| Ubicación aproximada (IP) | Sí | Sí | No | Sí | Analíticas, publicidad, prevención de fraude |
| Interacciones con la aplicación | Sí | Sí | No | Sí | Analíticas, publicidad, prevención de fraude |
| Diagnósticos | Sí | Sí | No | Sí | Analíticas, publicidad, prevención de fraude |
| IDs de dispositivo o de otro tipo | Sí | Sí | No | Sí | Analíticas, publicidad, prevención de fraude |

Otras respuestas del formulario de seguridad de los datos:

- Los datos se cifran en tránsito.
- La app no permite crear cuentas ni iniciar sesión con cuentas externas.
- No se ofrece solicitar la eliminación de datos.

Lo que el usuario escribe en las apps (gastos en Facturaap; ingresos, montos y plazos en Analista)
**se queda solo en el teléfono** y no se envía a ningún servidor.

### Historial de envíos a revisión

| Fecha | App | Cambios |
|---|---|---|
| 2026-11-11 | Facturaap | Estado de operador y términos del servicio (ya aprobado y publicado) |
| 2026-11-11 | Facturaap | Seguridad de los datos con los datos de AdMob |
| 2026-11-11 | Analista | Declaración de anuncios (antes decía "no contiene anuncios"), seguridad de los datos con los datos de AdMob, estado de operador y términos del servicio |

## Mantenimiento

Antes de cambiar algo, revisa estas reglas para que las páginas y Play Console no se contradigan:

- **Las páginas y Play Console deben decir lo mismo.** La política de privacidad, los términos y la
  sección Seguridad de los datos deben coincidir. Si cambia algo, actualiza las tres cosas y vuelve a
  enviar a revisión en Play Console (Resumen de publicación).
  Algunos ejemplos de cambios que obligan a actualizar:
  - un SDK nuevo, como Firebase o Analytics;
  - datos que empiecen a salir del teléfono;
  - compras dentro de la app;
  - inicio de sesión.
- **Fecha de modificación.** Al editar una página, actualiza la fecha de "Última modificación".
- **Revisiones en curso.** Si envías un cambio mientras hay una revisión en curso, Google la reinicia.
- **Teléfono de Facturaap.** El teléfono de contacto de la ficha de Facturaap (Configuración de la tienda)
  es distinto del teléfono verificado en la cuenta. Si se quiere unificar, se cambia en esa sección.
