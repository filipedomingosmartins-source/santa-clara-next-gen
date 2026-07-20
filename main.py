from playwright.sync_api import sync_playwright

URL = "https://resultados.fpf.pt/Competition/Details?competitionId=29536&seasonId=106"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    print(page.title())

    with open("pagina.html", "w", encoding="utf-8") as f:
        f.write(page.content())

    browser.close()

print("Página descarregada com sucesso!")
