import discord
from discord.ext import commands
import asyncio
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
token = os.getenv("TOKEN")

def get_filtered_list(all_num, l2):
    for index, i in enumerate(all_num):
        if i == l2[0]:
            newlist = all_num[index:]
            if l2[:len(newlist)] == newlist:
                l2 = l2[len(newlist):]
                break
    return l2

def remove_consecutive_duplicates(lst):
    if not lst:
        return []
    
    result = []
    last_seen = None
    
    for num in lst:
        if num != last_seen:
            result.append(num)
        last_seen = num
    
    return result
    
async def get_instagram_reel_views(reel_url):
    driver = await webdriver.Chrome()
    total_views = 0
    try:
        await driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        await asyncio.sleep(3)
        
        username = await driver.find_element(By.NAME, "username")
        await username.send_keys(username)
        password = await driver.find_element(By.NAME, "password")
        await password.send_keys(password)
        xpath_query = f"//div[contains(text(), 'Log in')]"
        submit = await driver.find_element(By.XPATH, xpath_query)
        await submit.click()
        await asyncio.sleep(8)

        await driver.get(reel_url)
        await asyncio.sleep(15)
        
        all_numbers = []
        counter = 0
        
        while True:
            script = """
            let aajyDivs = document.querySelectorAll('div._aajy');

            if (!aajyDivs) {
                return [];
            }

            let numbers = [];

            aajyDivs.forEach((aajyDiv) => {
                let spanElement = aajyDiv.querySelector('span.html-span');
                let text = spanElement.innerText.trim();

                let match = text.match(/^([\\d,]+(?:\\.\\d+)?)([KkMm]?)$/);
                
                if (match) {
                    let num = match[1].replace(",", "");
                    let suffix = match[2];
                    
                    // Convert based on suffix
                    if (suffix.toLowerCase() === "k") {
                        num = parseFloat(num) * 1000;
                    } else if (suffix.toLowerCase() === "m") {
                        num = parseFloat(num) * 1000000;
                    }
                    
                    numbers.push(parseInt(num)); 
                }
            });

            return numbers;
            """
            numbers = await driver.execute_script(script)

            new_numbers = []
            for num in numbers:
                if isinstance(num, int):
                    new_numbers.append(num)
                else:
                    try:
                        num = int(num)
                        new_numbers.append(num)
                    except:
                        continue
            new_numbers = remove_consecutive_duplicates(new_numbers)
            new_numbers = get_filtered_list(all_numbers, new_numbers)
            all_numbers.extend(new_numbers)
            if new_numbers:
                counter = 0
            else:
                if counter > 2:
                    break
                counter += 1
            await driver.execute_script("window.scrollBy(0, 950);")
            await asyncio.sleep(5)

        total_views = sum(all_numbers)
    finally:
        await driver.quit()

    return total_views


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print("BOT IS ONLINE")

@bot.command()
async def views(ctx, reel_url):
    await ctx.send("Fetching reel views...")

    try:
        total_views = await get_instagram_reel_views(reel_url)
        
        await ctx.send(f"Total Views: {total_views}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


bot.run(token)
