import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 

class TestBuscarcita:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_buscarcita(self):
        # Retrieve sensitive data from environment variables
        id_citado = os.getenv("ID_CITADO")  # Fetch from GitHub Secrets
        des_citado = os.getenv("DES_CITADO")  # Fetch from GitHub Secrets

        self.driver.get("https://sede.administracionespublicas.gob.es/icpplustiej/citar?org=JUS-RC&locale=es")
        self.driver.find_element(By.ID,"cookie_action_close_header").click()
        self.driver.find_element(By.ID, "provincia").click()
        dropdown = self.driver.find_element(By.ID, "provincia")
        dropdown.find_element(By.XPATH, "//option[. = 'Las Palmas']").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(22)").click()
        dropdown = self.driver.find_element(By.ID, "sede")
        dropdown.find_element(By.XPATH, "//option[. = 'Oficina General del Registro Civil de Las Palmas de Gran Canaria, Málaga, 2, Las Palmas de Gran Canaria']").click()
        self.driver.find_element(By.CSS_SELECTOR, "optgroup > option:nth-child(3)").click()
        dropdown = self.driver.find_element(By.ID, "tramiteGrupo[4]")
        dropdown.find_element(By.XPATH, "//option[. = 'EXPEDIENTE DE MATRIMONIO CIVIL Y CAPACIDAD MATRIMONIAL']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#tramiteGrupo\\[4\\] > option:nth-child(2)").click()
        btn_aceptar = self.driver.find_element(By.ID, "btnAceptar")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn_aceptar)
        btn_aceptar.click()
        self.driver.find_element(By.CSS_SELECTOR, "#btnEntrar span").click()
        self.driver.find_element(By.ID, "txtIdCitado").click()
        self.driver.find_element(By.ID, "txtIdCitado").send_keys(id_citado)  # Use secret value
        self.driver.find_element(By.ID, "txtDesCitado").click()
        self.driver.find_element(By.ID, "txtDesCitado").send_keys(des_citado)  # Use secret value
        self.driver.find_element(By.ID, "btnEnviar").click()
        self.driver.find_element(By.ID, "btnEnviar").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".mf-msg__info").text == "Información: En este momento no hay citas disponibles"