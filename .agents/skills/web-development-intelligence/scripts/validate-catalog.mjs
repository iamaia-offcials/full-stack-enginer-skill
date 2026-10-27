#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const libDir = path.resolve(__dirname, '../libraries');

const requiredFiles = ['sources.json', 'components.json', 'animations.json', 'layouts.json', 'websites.json'];
let errorCount = 0;

console.log('Validating registry catalog in:', libDir);

for (const file of requiredFiles) {
  const filePath = path.join(libDir, file);
  if (!fs.existsSync(filePath)) {
    console.error(`❌ Missing catalog file: ${file}`);
    errorCount++;
    continue;
  }
  try {
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    console.log(`✓ Valid JSON: ${file} (${Array.isArray(data) ? data.length + ' items' : 'object'})`);
    
    if (file === 'components.json') {
      data.forEach((c, idx) => {
        const requiredFields = ['id', 'name', 'category', 'source', 'license', 'access_type', 'description', 'suitable_use_cases', 'desktop_behavior', 'mobile_behavior'];
        for (const f of requiredFields) {
          if (!c[f]) {
            console.error(`❌ [components.json #${idx}] Missing field '${f}' in component ${c.id || 'unknown'}`);
            errorCount++;
          }
        }
      });
    }
  } catch (err) {
    console.error(`❌ Syntax error in ${file}:`, err.message);
    errorCount++;
  }
}

if (errorCount === 0) {
  console.log('\n✅ PASS: Catalog integrity verified (0 errors).');
  process.exit(0);
} else {
  console.error(`\n❌ FAIL: Found ${errorCount} catalog errors.`);
  process.exit(1);
}
