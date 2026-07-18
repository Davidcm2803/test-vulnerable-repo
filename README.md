# Test Vulnerable Repo

Este repo sirve para probar los scanners de tu plataforma
No usar en produccion, tiene vulnerabilidades a proposito

## Que prueba cada archivo

app/auth.py
Prueba Bandit
Tiene password hardcodeada, sql injection, eval, pickle, comandos shell, hash md5

app/main.py
Prueba Bandit
Tiene debug true, ssl sin verificar, random inseguro, bind a 0.0.0.0

routes/search.js
Prueba Semgrep
Tiene xss reflejado, eval con input externo, cors abierto

routes/users.js
Prueba Semgrep
Tiene sql injection y log de credenciales en texto plano

requirements.txt
Prueba osv-scanner
Tiene versiones viejas de fastapi requests pyyaml jinja2 urllib3 con CVEs conocidos

package.json
Prueba osv-scanner
Tiene versiones viejas de express lodash axios minimist con CVEs conocidos

.env.example
Prueba gitleaks
Tiene claves de AWS GitHub y Stripe de ejemplo

utils/payment.py
Prueba gitleaks
Tiene una api key de Stripe embebida en el codigo

Dockerfile
Prueba Checkov
Corre como root, tiene secreto en ENV, expone el puerto 22

docker-compose.yml
Prueba Checkov
Usa privileged true y monta la raiz del host como volumen

## Como usarlo

Subir esta carpeta completa a tu plataforma usando la opcion de upload o pegar la url si lo subis a un repo propio de github

Revisar que el resultado del scan muestre hallazgos con estos detector_source
bandit
semgrep
osv-scanner
gitleaks
checkov

Si alguno de los cinco no aparece en el resultado ese detector no esta funcionando bien
