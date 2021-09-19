from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyotp
import json
import requests
import base64

def load_settings_values():
    print("loading settings..")
    with open("credentials.json", "r") as credentialsFile:
        credentialsData = json.load(credentialsFile)
        netID = credentialsData["netID"]
        password = credentialsData["password"]
        deviceURL = credentialsData["deviceURL"]
        runDaily = credentialsData["runDaily"]
        headless = credentialsData["headless"]
        firstRun = credentialsData["firstRun"]

    return [netID, password, deviceURL, runDaily, headless, firstRun]

def write_settings_values(netID, password, deviceURL, runDaily, headless):
    """Writes settings values to credentials.json"""
    with open("credentials.json", "w") as credentialsFile:

        credentialsData["netID"] = netID
        credentialsData["password"] = password
        credentialsData["deviceURL"] = deviceURL
        credentialsData["runDaily"] = runDaily
        credentialsData["headless"] = headless

        credentialsJson = json.dumps(credentialsData, indent = 4)
        credentialsFile.write(credentialsJson)

# Getting the secret from the confirmation URL (credit to Bye DUO and No DUO Lockout for this)
def generate_secret(deviceURL):
    """Returns an unencoded secret from DUO after activating device"""
    deviceURL = deviceURL.lstrip("https://").split("/")
    domain = deviceURL[0][1:]
    key = deviceURL[-1]
    DUO = f"https://api{domain}/push/v2/activation/{key}?customer_protocol=1"
    try:
        req = json.loads(requests.post(DUO).text)
        hotpSecret = req['response']['hotp_secret']            
        print("Successfully activated device and generated secret!")
        return hotpSecret
    except:
        #print(netID, password, counter, hotpSecret, generateSecret, deviceURL, DUO)
        print("Connection error. Maybe the device is already activated?")
        exit(1)

def automation():
    """Goes through the main page filling out the forms"""
    deviceURL = load_settings_values()[2]
    #deviceURL = "https://m-e4c9863e.duosecurity.com/android/GYXpjzXzE0DKWxxERpB1"

    #Code generation
    if needSecret: # Only runs once per device - Also should say needSecret but changed for testing
        hotpSecret = generate_secret(deviceURL)
        credentialsData["hotpSecret"] = hotpSecret
        credentialsData["needSecret"] = False
    else:
        hotpSecret = credentialsData["hotpSecret"]

    hotpSecretEncode = base64.b32encode(hotpSecret.encode('ascii')).decode('utf-8')
    hotp = pyotp.HOTP(hotpSecretEncode)
    code = hotp.at(counter)
    print("Code generated")

    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    #if (True): #Should say headless but changed for testing
        #option.add_argument("--headless")
        #option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    
    driver = webdriver.Chrome("chromedriver.exe", options=option)
    wait = WebDriverWait(driver, 10)

    # Link to NYU Daily Screener survey to fill out
    driver.get("https://nyu.qualtrics.com/jfe/form/SV_ePNv0eXvGWgCxkq?")
    assert "NYU COVID-19" in driver.title

    # Clicks on Next
    wait.until(expected_conditions.element_to_be_clickable((By.ID, "NextButton"))).click()
    # Selecting yes to 'Do you have a NetID option'
    wait.until(expected_conditions.element_to_be_clickable((By.ID, "QID2-1-label"))).click()
    wait.until(expected_conditions.element_to_be_clickable((By.ID, "NextButton"))).click()
    print("Clicked the next button")

    # Find and fill username/password
    wait.until(expected_conditions.element_to_be_clickable((By.ID, "username")))
    driver.find_element_by_id("username").send_keys(netID)
    wait.until(expected_conditions.element_to_be_clickable((By.ID, "password")))
    driver.find_element_by_id("password").send_keys(password)
    wait.until(expected_conditions.element_to_be_clickable((By.NAME, "_eventId_proceed"))).click()
    print("Filled out the username/password, moving on to the next part")

    # Switch to iFrame for DUO authentication
    time.sleep(1)
    #driver.get_screenshot_as_png()
    wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.ID, "duo_iframe")))
    #Switched iframes
    time.sleep(1) #temporary, remove later

    # Use HOTP passcode to authenticate
    driver.find_element_by_id("passcode").click()
    driver.find_element_by_class_name("passcode-input").send_keys(code)
    wait.until(expected_conditions.element_to_be_clickable((By.ID, "passcode"))).click()
    print("Got to the end")

    # Increment password counter
    with open("credentials.json", "w") as credentialsFile:
        credentialsData["counter"] += 1
        credentialsData["needSecret"] = False
        credentialsData["firstRun"] = False;
        credentialsJson = json.dumps(credentialsData, indent = 4)
        credentialsFile.write(credentialsJson)

def disableFirstRun():
    with open("credentials.json", "w") as credentialsFile:
        credentialsData["firstRun"] = False

# Load user credentials
with open("credentials.json", "r") as credentialsFile:
    credentialsData = json.load(credentialsFile)

    netID = credentialsData["netID"]
    password = credentialsData["password"]
    deviceURL = credentialsData["deviceURL"]
    headless = credentialsData["headless"]
    runDaily = credentialsData["runDaily"]

    counter = credentialsData["counter"] #Dev stuff
    hotpSecret = credentialsData["hotpSecret"]
    needSecret = credentialsData["needSecret"]

automation()