const {Builder, By, Key, util} = require("selenium-webdriver");

async function example() {
    let driver = await new Builder().forBrowser("firefox").build();
    try {
    await driver.get("http://suninjuly.github.io/find_xpath_form");
    await driver.findElement(By.name("first_name")).sendKeys("Ivan");
    await driver.findElement(By.name("last_name")).sendKeys("Smirnov");
    await driver.findElement(By.className("city")).sendKeys("Kemerovo");
    await driver.findElement(By.id("country")).sendKeys("Rus");
    await driver.findElement(By.xpath('//button[@type="submit"]')).click();
    }
    finally{ 
        driver.sleep(15000).then(function() {
        driver.quit();
    });
}

}
example();

