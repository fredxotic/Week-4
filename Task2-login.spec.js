import { test, expect } from '@playwright/test';

test('login test with valid and invalid credentials', async ({ page }) => {
  // Go to login page
  await page.goto('https://the-internet.herokuapp.com/login');
  
  // Test valid login
  await page.getByRole('textbox', { name: 'Username' }).fill('tomsmith');
  await page.getByRole('textbox', { name: 'Password' }).fill('SuperSecretPassword!');
  await page.getByRole('button', { name: ' Login' }).click();
  
  // Verify successful login
  await expect(page.locator('text=You logged into a secure area!')).toBeVisible();
  
  // Logout
  await page.getByRole('link', { name: 'Logout' }).click();
  
  // Test invalid login
  await page.getByRole('textbox', { name: 'Username' }).fill('wronguser');
  await page.getByRole('textbox', { name: 'Password' }).fill('wrongpass');
  await page.getByRole('button', { name: ' Login' }).click();
  
  // Verify error message for invalid login
  await expect(page.locator('text=Your username is invalid!')).toBeVisible();
});