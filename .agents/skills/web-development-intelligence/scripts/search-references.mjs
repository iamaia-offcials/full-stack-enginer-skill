#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const libDir = path.resolve(__dirname, '../libraries');

function readJson(filename) {
  const filePath = path.join(libDir, filename);
  if (!fs.existsSync(filePath)) return [];
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (e) {
    console.error(`Error reading ${filename}:`, e.message);
    return [];
  }
}

const components = readJson('components.json');
const animations = readJson('animations.json');
const layouts = readJson('layouts.json');
const websites = readJson('websites.json');
const sources = readJson('sources.json');

const args = process.argv.slice(2);
const params = {};

for (let i = 0; i < args.length; i++) {
  if (args[i].startsWith('--')) {
    const key = args[i].slice(2);
    const value = args[i + 1] && !args[i + 1].startsWith('--') ? args[++i] : true;
    params[key] = value;
  }
}

if (args.length === 0 || params.help) {
  console.log(`
Web Development Intelligence - Reference Search Utility
Usage:
  node scripts/search-references.mjs [options]

Options:
  --query <text>       Free-text keyword search across all catalogs
  --category <cat>     Filter by category (e.g. Hero, Cards, Scroll Animations, Gestures)
  --industry <ind>     Filter by industry (e.g. tourism, restaurant, ecommerce, real-estate, esim)
  --complexity <lvl>   Filter by complexity (low, medium, high)
  --source <src>       Filter by library source (Aceternity, Magic UI, React Bits, GSAP, etc.)
  --type <type>        Filter by record type (components, animations, layouts, websites)
  --help               Show this help message

Examples:
  node scripts/search-references.mjs --industry tourism --category hero
  node scripts/search-references.mjs --query "sticky scroll"
  node scripts/search-references.mjs --complexity low --category cards
`);
  process.exit(0);
}

const query = (params.query || '').toLowerCase();
const category = (params.category || '').toLowerCase();
const industry = (params.industry || '').toLowerCase();
const complexity = (params.complexity || '').toLowerCase();
const source = (params.source || '').toLowerCase();

function matchesItem(item) {
  const text = JSON.stringify(item).toLowerCase();
  if (query && !text.includes(query)) return false;
  if (category && !(item.category && item.category.toLowerCase().includes(category))) return false;
  if (complexity && !(item.implementation_complexity && item.implementation_complexity.toLowerCase() === complexity)) return false;
  if (source && !(item.source && item.source.toLowerCase().includes(source))) return false;
  if (industry) {
    const indMatch = text.includes(industry) || 
      (item.suitable_use_cases && item.suitable_use_cases.some(u => u.toLowerCase().includes(industry))) ||
      (item.suitable_industries && item.suitable_industries.some(u => u.toLowerCase().includes(industry)));
    if (!indMatch) return false;
  }
  return true;
}

const matchedComponents = components.filter(matchesItem);
const matchedAnimations = animations.filter(matchesItem);
const matchedLayouts = layouts.filter(matchesItem);
const matchedWebsites = websites.filter(matchesItem);

console.log('\n=== Search Results ===');
console.log(`Found: ${matchedComponents.length} components, ${matchedAnimations.length} animations, ${matchedLayouts.length} layouts, ${matchedWebsites.length} websites.\n`);

if (matchedComponents.length > 0) {
  console.log('--- Components ---');
  matchedComponents.forEach(c => {
    console.log(`• [${c.id}] ${c.name} (${c.source}) - ${c.category}`);
    console.log(`  Description: ${c.description}`);
    console.log(`  Install: ${c.source_code_url || c.documentation_url}`);
    console.log(`  Mobile: ${c.mobile_behavior}\n`);
  });
}

if (matchedAnimations.length > 0) {
  console.log('--- Animations ---');
  matchedAnimations.forEach(a => {
    console.log(`• [${a.id}] ${a.name} (${a.source})`);
    console.log(`  Pattern: ${a.implementation_pattern || a.description}`);
    console.log(`  Mobile adaptation: ${a.mobile_adaptation}\n`);
  });
}

if (matchedLayouts.length > 0) {
  console.log('--- Layouts ---');
  matchedLayouts.forEach(l => {
    console.log(`• [${l.id}] ${l.name} - ${l.category}`);
    console.log(`  Characteristics: ${l.characteristics}`);
    console.log(`  Industries: ${(l.suitable_industries || []).join(', ')}\n`);
  });
}

if (matchedWebsites.length > 0) {
  console.log('--- Case Study Websites ---');
  matchedWebsites.forEach(w => {
    console.log(`• ${w.name} (${w.industry}) - ${w.url}`);
    console.log(`  Key Takeaway: ${w.key_takeaway}\n`);
  });
}
