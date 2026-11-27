# Validação da aplicação

Execute `python -m tests.smoke` após instalar as dependências. O teste verifica 26.640 observações, 834.398 ocorrências, 185 códigos territoriais, filtro anual, retorno do callback, HTTP 200 e associação geográfica global e individual. Não reproduz o treinamento dos modelos nem substitui inspeção visual.

A execução automatizada está em [GitHub Actions](../.github/workflows/dashboard-smoke.yml).

