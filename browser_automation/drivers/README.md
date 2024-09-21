# Browser Drivers Directory

The `drivers` directory contains the essential browser drivers required for the PokerAI’s automation functionality. Browser drivers enable the automation scripts to interact with web browsers like Chrome and Firefox via Selenium. These drivers bridge the gap between the automation scripts and the actual browser, allowing the AI to play poker on real-world platforms without direct human involvement.

## Directory Structure

- **`chrome_driver.exe`**: This is the Chrome WebDriver binary for controlling Chrome-based browsers. It is used by the Selenium scripts to simulate human-like actions such as clicking, navigating, and reading data from the webpage.
  
- **`firefox_driver.exe`**: This is the GeckoDriver binary required to automate Firefox. It serves the same purpose as ChromeDriver but is specifically for Firefox browsers.

## Purpose of Browser Drivers

Browser drivers are a crucial component for web automation. They allow the AI system to:
- **Simulate user interactions**: Perform actions like clicking buttons, entering text, and navigating different parts of the poker platform.
- **Retrieve game states**: Scrape information from the poker platform, including current cards, player actions, and pot sizes.
- **Execute AI decisions**: Based on the AI’s strategy and reinforcement learning models, browser drivers allow the AI to interact with the poker game by placing bets, folding, raising, or chatting.

## Supported Browsers

Currently, this directory contains drivers for two widely used browsers:
1. **Chrome**: Supported through `chrome_driver.exe`.
2. **Firefox**: Supported through `firefox_driver.exe`.

The drivers allow the PokerAI to operate on these browsers, ensuring flexibility based on user preference or system requirements.

### How to Install Drivers

To use the drivers in this directory, follow these steps:

1. **Download the correct driver for your browser**:
   - **ChromeDriver**: Download from the official [ChromeDriver site](https://sites.google.com/a/chromium.org/chromedriver/). Make sure the driver version matches your installed Chrome browser version.
   - **GeckoDriver (for Firefox)**: Download from the official [GeckoDriver site](https://github.com/mozilla/geckodriver/releases).

2. **Place the driver in the `drivers` directory**:
   - Ensure the driver matches your system’s architecture (e.g., 32-bit or 64-bit) and operating system (Windows, macOS, or Linux).
   - The file names should be `chrome_driver.exe` or `firefox_driver.exe` depending on the browser.

3. **Set the driver path in your environment**:
   - If needed, update your environment variables to include the path to the driver.
   - Alternatively, modify the browser automation scripts to use the relative path:  
     ```python
     driver = webdriver.Chrome(executable_path='./drivers/chrome_driver.exe')
     ```

### Headless Mode Support

Both ChromeDriver and GeckoDriver support **headless mode**, allowing the browser to run without a graphical interface. This is useful for running the PokerAI in server or cloud environments where no GUI is available.

To enable headless mode, modify the automation script as follows:
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='./drivers/chrome_driver.exe', options=chrome_options)
```

### Keeping Drivers Updated

It's important to keep the browser drivers up-to-date to avoid compatibility issues with newer versions of Chrome or Firefox:
- **ChromeDriver**: Ensure you update the driver when your Chrome browser updates, as mismatched versions may cause errors.
- **GeckoDriver**: Similarly, update GeckoDriver with Firefox updates.

### Cross-Browser Compatibility

The PokerAI browser automation is designed to work seamlessly across Chrome and Firefox. While the system defaults to Chrome, users can configure their preference by modifying the environment configuration file (`env_config.yaml`). For instance:
```yaml
browser: chrome   # or 'firefox'
```

### Common Issues

- **Driver version mismatch**: Ensure the driver version matches the browser version installed on your system.
- **Path issues**: Verify that the driver’s executable path is correctly set either via environment variables or in the automation script.
- **Permissions**: On Linux or macOS, you may need to grant execution permissions to the driver using `chmod +x chrome_driver`.

## Future Improvements

1. **Support for Additional Browsers**: Adding support for other browsers like Safari and Edge to expand platform compatibility.
2. **Dynamic Driver Management**: Automating driver updates and compatibility checks to ensure that the latest driver is always being used.
3. **Mobile Browser Support**: Integrating mobile browser drivers (e.g., Chrome for Android, Safari for iOS) to allow PokerAI to interact with mobile-optimized poker platforms.
4. **Parallel Browser Sessions**: Extending the capability to run multiple browser instances in parallel for multi-table poker play.
5. **Driver Health Checks**: Adding health checks to verify the integrity and responsiveness of the browser drivers before initiating an automation session.

---

This `drivers` directory is a critical component of the browser automation system, enabling seamless interaction with poker platforms through web browsers. By keeping the drivers updated and ensuring proper configuration, the PokerAI can perform reliably and efficiently.
