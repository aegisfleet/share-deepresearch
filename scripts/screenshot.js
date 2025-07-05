const { chromium } = require('playwright');

async function captureScreenshots() {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  // トップページ（ライトモード）
  await page.goto('http://localhost:4000');
  await page.waitForSelector('.topic-list');
  await page.screenshot({ path: 'screenshot-light.png', fullPage: true });

  // トップページ（ダークモード）
  await page.evaluate(() => {
    localStorage.setItem('theme', 'dark');
    document.documentElement.setAttribute('data-theme', 'dark');
  });
  // DOMの更新を待つ
  await page.waitForTimeout(500);
  await page.screenshot({ path: 'screenshot-dark.png', fullPage: true });

  // 最新の記事ページ（ダークモード）
  const firstArticle = await page.$('.topic-list li:first-child a');
  if (firstArticle) {
    await Promise.all([
      page.waitForNavigation(),
      firstArticle.click()
    ]);
    await page.waitForSelector('article');
    await page.screenshot({ path: 'screenshot-article-dark.png', fullPage: true });
  }

  // 記事ページ（ライトモード）
  await page.evaluate(() => {
    localStorage.setItem('theme', 'light');
    document.documentElement.setAttribute('data-theme', 'light');
  });
  // DOMの更新を待つ
  await page.waitForTimeout(500);
  await page.screenshot({ path: 'screenshot-article-light.png', fullPage: true });

  await browser.close();
}

captureScreenshots().catch(console.error);
