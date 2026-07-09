from playwright.sync_api import Page

def test_buka_halaman(page: Page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()

def test_cek_heading(page: Page):
    page.goto("https://example.com")
    heading = page.locator("h1").text_content()
    assert heading == "Example Domain"

def test_search_google(page: Page):
    page.goto("https://playwright.dev")
    page.get_by_role("link", name="Get started").click()
    page.wait_for_load_state("networkidle")
    assert "Installation" in page.content()

def test_isi_form(page: Page):
    page.goto("https://demoqa.com/text-box")
    
    # Isi form
    page.locator("#userName").fill("Budi Santoso")
    page.locator("#userEmail").fill("budi@gmail.com")
    page.locator("#currentAddress").fill("Jl. Merdeka No. 1, Jakarta")
    
    # Klik submit
    page.locator("#submit").click()
    
    # Verifikasi output muncul
    assert "Budi Santoso" in page.locator("#output").text_content()
    assert "budi@gmail.com" in page.locator("#output").text_content()

def test_isi_automation_practice_form(page: Page):
    
    page.goto("https://demoqa.com/automation-practice-form")
    #isi form
    page.locator("#firstName").fill("tata")
    page.locator("#lastName").fill("tata")
    page.locator("#userEmail").fill("tata@gmail.com")
    
    # click label gender
    page.locator("label[for='gender-radio-1']").click()
    
    page.locator("#userNumber").fill("645212154512")
    
     # Isi alamat
    page.locator("#currentAddress").fill("Jl. Patumbak No. 1")

    # Klik submit
    page.locator("#submit").click()

    # Verifikasi modal konfirmasi muncul
    assert page.locator("#example-modal-sizes-title-lg").is_visible()
    assert "Thanks for submitting the form" in page.locator("#example-modal-sizes-title-lg").text_content()