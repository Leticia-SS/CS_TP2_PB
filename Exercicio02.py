import asyncio
import aiohttp
from typing import List
import time


async def baixar_pagina(session: aiohttp.ClientSession, url: str) -> str:
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            response.raise_for_status()
            conteudo = await response.text()
            print(f"Download concluído: {url} ({len(conteudo)} bytes)")
            return conteudo
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
        return ""


async def processar_pagina(conteudo: str, url: str) -> dict:
    if not conteudo:
        return {"url": url, "status": "erro", "palavras": 0}

    palavras = len(conteudo.split())
    titulo = "Não encontrado"

    if "<title>" in conteudo:
        inicio = conteudo.find("<title>") + 7
        fim = conteudo.find("</title>")
        if fim > inicio:
            titulo = conteudo[inicio:fim].strip()[:50]

    return {
        "url": url,
        "status": "sucesso",
        "palavras": palavras,
        "titulo": titulo
    }


async def baixar_e_processar_urls(urls: List[str]) -> List[dict]:
    async with aiohttp.ClientSession() as session:
        tarefas_download = [baixar_pagina(session, url) for url in urls]
        conteudos = await asyncio.gather(*tarefas_download, return_exceptions=True)

        resultados = []
        for url, conteudo in zip(urls, conteudos):
            if isinstance(conteudo, Exception):
                print(f"Exceção em {url}: {conteudo}")
                resultados.append({"url": url, "status": "erro", "palavras": 0})
            else:
                resultado = await processar_pagina(conteudo, url)
                resultados.append(resultado)

        return resultados

async def main():
    urls = [
        "https://www.gov.br/",
        "https://www.wikipedia.org/",
        "https://stackoverflow.com/"
    ]

    print("Iniciando downloads assíncronos...")
    inicio = time.time()

    resultados = await baixar_e_processar_urls(urls)

    tempo_total = time.time() - inicio
    print(f"\n==== RESULTADOS ====")
    print(f"Tempo total: {tempo_total:.2f} segundos")
    print(f"URLs processadas: {len(urls)}")

    for resultado in resultados:
        print(f"URL: {resultado['url']}")
        print(f"  Status: {resultado['status']}")
        if resultado['status'] == 'sucesso':
            print(f"  Título: {resultado['titulo']}")
            print(f"  Palavras: {resultado['palavras']}")
        print()

if __name__ == "__main__":
    asyncio.run(main())