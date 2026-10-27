#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const target = process.argv[2] || '.';
let errorCount = 0;
let warningCount = 0;

console.log(`Scanning target for design and hardening defects: ${target}\n`);

function scanFile(filePath) {
  const ext = path.extname(filePath);
  if (!['.css', '.html', '.jsx', '.tsx', '.vue', '.svelte'].includes(ext)) return;
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');

  lines.forEach((line, idx) => {
    const lineNum = idx + 1;

    // 1. Viewport scaling lock (WCAG 1.4.4)
    if (line.includes('user-scalable=no') || line.includes('maximum-scale=1')) {
      console.error(`❌ [${filePath}:${lineNum}] WCAG 1.4.4 Violation: user-scalable=no or maximum-scale=1 locks viewport zoom.`);
      errorCount++;
    }

    // 2. Input font size < 16px (iOS zoom trap)
    const fontMatch = line.match(/(?:input|select|textarea)[^{]*\{[^}]*font-size:\s*([0-9]+)px/);
    if (fontMatch && parseInt(fontMatch[1], 10) < 16) {
      console.error(`❌ [${filePath}:${lineNum}] Mobile Zoom Trap: Form input font-size is ${fontMatch[1]}px (< 16px). Triggers iOS Safari zoom.`);
      errorCount++;
    }

    // 3. Ease-in on entrance animation
    if (line.includes('ease-in') && (line.includes('enter') || line.includes('modal') || line.includes('dialog') || line.includes('fade-in'))) {
      console.warn(`⚠️ [${filePath}:${lineNum}] Motion Defect: ease-in detected on entrance animation. Entrances must use ease-out for instant feedback.`);
      warningCount++;
    }

    // 4. Flex container without min-width: 0
    if ((line.includes('flex') || line.includes('grid')) && line.includes('truncate') && !content.includes('min-w-0') && !content.includes('min-width: 0')) {
      console.warn(`⚠️ [${filePath}:${lineNum}] Layout Risk: Truncated text inside flex/grid without min-width: 0 may cause overflow blowout.`);
      warningCount++;
    }

    // 5. Disabled button during submit
    if (line.includes('disabled={isSubmitting}') || line.includes('disabled={loading}')) {
      console.warn(`⚠️ [${filePath}:${lineNum}] Accessibility Warning: Directly setting disabled on in-flight submit button drops keyboard focus. Use aria-busy="true" instead.`);
      warningCount++;
    }
  });
}

function walk(dir) {
  if (!fs.existsSync(dir)) return;
  const stat = fs.statSync(dir);
  if (stat.isFile()) {
    scanFile(dir);
    return;
  }
  const files = fs.readdirSync(dir);
  for (const f of files) {
    if (f === 'node_modules' || f === '.git' || f === 'dist') continue;
    const full = path.join(dir, f);
    if (fs.statSync(full).isDirectory()) {
      walk(full);
    } else {
      scanFile(full);
    }
  }
}

walk(target);

console.log(`\nScan Complete: ${errorCount} errors, ${warningCount} warnings.`);
if (errorCount > 0) process.exit(1);
