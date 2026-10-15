import fs from 'fs';
import path from 'path';

beforeEach(() => {
  const htmlPath = path.resolve(__dirname, './index.html');
  const cssPath = path.resolve(__dirname, './main.css');

  const html = fs.readFileSync(htmlPath, 'utf-8');
  const css = fs.readFileSync(cssPath, 'utf-8');

  document.documentElement.innerHTML = html;

  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);
});

afterEach(() => {
  document.documentElement.innerHTML = '';
});
