#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const libDir = path.resolve(__dirname, '../libraries');

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log(`
Usage:
  node scripts/update-references.mjs <file.json> <item-json-string-or-file>

Examples:
  node scripts/update-references.mjs components.json '{"id":"new-card","name":"New Card",...}'
`);
  process.exit(0);
}

const targetFile = args[0];
const targetPath = path.join(libDir, targetFile);

if (!fs.existsSync(targetPath)) {
  console.error(`Target file ${targetFile} does not exist in ${libDir}`);
  process.exit(1);
}

try {
  let newItem;
  if (fs.existsSync(args[1])) {
    newItem = JSON.parse(fs.readFileSync(args[1], 'utf8'));
  } else {
    newItem = JSON.parse(args[1]);
  }

  const catalog = JSON.parse(fs.readFileSync(targetPath, 'utf8'));
  if (Array.isArray(catalog)) {
    const existingIdx = catalog.findIndex(i => i.id === newItem.id);
    newItem.verified_at = new Date().toISOString().split('T')[0];
    if (existingIdx >= 0) {
      catalog[existingIdx] = newItem;
      console.log(`Updated existing item: ${newItem.id}`);
    } else {
      catalog.push(newItem);
      console.log(`Added new item: ${newItem.id}`);
    }
    fs.writeFileSync(targetPath, JSON.stringify(catalog, null, 2) + '\n', 'utf8');
    console.log(`Saved catalog to ${targetFile}. Total items: ${catalog.length}`);
  }
} catch (err) {
  console.error('Failed to update references:', err.message);
  process.exit(1);
}
