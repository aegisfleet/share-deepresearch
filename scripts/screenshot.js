const { chromium } = require('playwright');

async function captureScreenshots() {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  // トップページ（ライトモード）
  await page.goto('http://localhost:4000');
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: 'screenshot-light.png', fullPage: true });

  // トップページ（ダークモード）
  await page.evaluate(() => {
    localStorage.setItem('theme', 'dark');
    document.documentElement.setAttribute('data-theme', 'dark');
  });
  await page.reload();
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: 'screenshot-dark.png', fullPage: true });

  // 最新の記事ページ（ダークモード）
  const firstArticle = await page.$('.topic-list li:first-child a');
  if (firstArticle) {
    await firstArticle.click();
    await page.waitForLoadState('networkidle');
    await page.screenshot({ path: 'screenshot-article-dark.png', fullPage: true });
  }

  // 記事ページ（ライトモード）
  await page.evaluate(() => {
    localStorage.setItem('theme', 'light');
    document.documentElement.setAttribute('data-theme', 'light');
  });
  await page.reload();
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: 'screenshot-article-light.png', fullPage: true });

  await browser.close();
}

captureScreenshots().catch(console.error);
