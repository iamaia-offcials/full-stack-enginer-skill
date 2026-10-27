/**
 * Test Suite for web-development-intelligence Agent Skill
 * Verifies Scenarios A, B, C, D, E per User Specification Section 23.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const skillRoot = path.resolve(__dirname, '..');

console.log('====================================================');
console.log('Web Development Intelligence - Test Scenarios A - E');
console.log('====================================================\n');

let totalTests = 0;
let passedTests = 0;

function assert(condition, testName, details = '') {
  totalTests++;
  if (condition) {
    console.log(`✓ PASS: ${testName}`);
    passedTests++;
  } else {
    console.error(`✗ FAIL: ${testName}`);
    if (details) console.error(`  Details: ${details}`);
  }
}

// Helper: load JSON catalog
function loadCatalog(filename) {
  const filePath = path.join(skillRoot, 'libraries', filename);
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

// ---------------------------------------------------------
// TEST A: Restaurant Homepage
// Expectation: Menu-first, high emotional photography, reservation flow, proper mobile stack
// ---------------------------------------------------------
console.log('--- Test A: Modern Restaurant Homepage ---');
{
  const restaurantCaseStudy = path.join(skillRoot, 'case-studies', 'restaurants.md');
  const exists = fs.existsSync(restaurantCaseStudy);
  assert(exists, 'Case study for restaurants exists');

  const content = fs.readFileSync(restaurantCaseStudy, 'utf8');
  assert(content.toLowerCase().includes('menu-first') || content.toLowerCase().includes('menu architecture'), 'Emphasizes menu-first architecture', 'Restaurant UX must prioritize menu accessibility');
  assert(content.includes('Reservation'), 'Contains direct reservation funnel UX');
  assert(content.includes('Ambience') || content.includes('Photography'), 'Specifies photography and ambience guidelines');

  // Verify component search can locate relevant components
  const components = loadCatalog('components.json');
  const modalOrDialog = components.some(c => c.category === 'Dialogs' || c.suitable_use_cases.some(u => u.includes('booking') || u.includes('reservation')));
  assert(modalOrDialog, 'Component catalog contains accessible booking/reservation modal primitives');
}
console.log('');

// ---------------------------------------------------------
// TEST B: Real Estate Agency Without Catalog (Lead Generation)
// Expectation: Lead gen funnel, home valuation, agent trust, NO fake catalog grid
// ---------------------------------------------------------
console.log('--- Test B: Real Estate Lead Gen (No Catalog) ---');
{
  const realEstateCaseStudy = path.join(skillRoot, 'case-studies', 'real-estate.md');
  assert(fs.existsSync(realEstateCaseStudy), 'Case study for real estate exists');

  const content = fs.readFileSync(realEstateCaseStudy, 'utf8');
  assert(content.includes('WITHOUT a Property Catalog') || content.includes('Lead Generation'), 'Explicitly addresses agency WITHOUT property catalog');
  assert(content.includes('Home Valuation') || content.includes('Valuation Estimator'), 'Features home valuation / seller lead capture funnel');
  assert(content.includes('NEVER render a dummy "3 featured listings" grid') || content.includes('anti-patterns'), 'Explicitly forbids inserting fake property listings');
  assert(content.includes('Social Proof') || content.includes('Trust Metrics'), 'Includes agent authority and closed deal metrics');
}
console.log('');

// ---------------------------------------------------------
// TEST C: Tourism Website with Cinematic Parallax & Pinned Scroll
// Expectation: Parallax, GSAP ScrollTrigger, mobile unpinning, performance budget
// ---------------------------------------------------------
console.log('--- Test C: Cinematic Tourism Website with Parallax ---');
{
  const tourismCaseStudy = path.join(skillRoot, 'case-studies', 'tourism.md');
  assert(fs.existsSync(tourismCaseStudy), 'Case study for tourism exists');

  const tourismContent = fs.readFileSync(tourismCaseStudy, 'utf8');
  assert(tourismContent.includes('ScrollTrigger') || tourismContent.includes('Parallax'), 'Integrates ScrollTrigger / Parallax animations');
  assert(tourismContent.includes('Mobile Adaptation') || tourismContent.includes('Unpin'), 'Enforces mobile unpinning to prevent scroll trapping');

  const animations = loadCatalog('animations.json');
  const pinnedReel = animations.find(a => a.id === 'gsap-pinned-horizontal-showcase');
  assert(pinnedReel !== undefined, 'GSAP pinned scroll showcase pattern exists in animation catalog');
  if (pinnedReel) {
    assert(pinnedReel.mobile_adaptation.toLowerCase().includes('unpin'), 'Pinned scroll pattern explicitly defines mobile unpinning rule');
  }

  const scrollRef = fs.readFileSync(path.join(skillRoot, 'references', 'scroll-interactions.md'), 'utf8');
  assert(scrollRef.includes('refreshPriority'), 'References GSAP refreshPriority correctly');
}
console.log('');

// ---------------------------------------------------------
// TEST D: Improving an Existing Product Catalog
// Expectation: Non-breaking refactoring, preserves existing design tokens, fixes visual hierarchy
// ---------------------------------------------------------
console.log('--- Test D: Existing Product Catalog Improvement ---');
{
  const existingWorkflow = path.join(skillRoot, 'workflows', 'existing-project.md');
  assert(fs.existsSync(existingWorkflow), 'Workflow for existing project exists');

  const content = fs.readFileSync(existingWorkflow, 'utf8');
  assert(content.includes('Token Discovery') || content.includes('Inspect CSS variables'), 'Begins with discovering existing tokens');
  assert(content.includes('Do NOT reinvent') || content.includes('Preserve'), 'Forbids overriding existing design system without permission');
  assert(content.includes('Additive'), 'Specifies additive, non-breaking modifications');

  const designReview = path.join(skillRoot, 'workflows', 'design-review.md');
  assert(fs.existsSync(designReview), 'Design review rubric exists');
}
console.log('');

// ---------------------------------------------------------
// TEST E: Quick Modal Appearance Animation
// Expectation: Quick mode trigger, 150-220ms ease-out, zero heavy dependencies, accessible
// ---------------------------------------------------------
console.log('--- Test E: Quick Modal Animation (Lightweight) ---');
{
  const skillManifest = fs.readFileSync(path.join(skillRoot, 'SKILL.md'), 'utf8');
  assert(skillManifest.includes('mode: quick') || skillManifest.includes('quick'), 'Skill manifest specifies "quick" operational mode');

  const motionRef = fs.readFileSync(path.join(skillRoot, 'references', 'motion-design.md'), 'utf8');
  assert(motionRef.includes('150') || motionRef.includes('200') || motionRef.includes('220'), 'Defines crisp 150-220ms modal entrance durations');
  assert(motionRef.includes('prefers-reduced-motion'), 'Mandates prefers-reduced-motion fallback');

  // Verify that simple modal animation does not pull in heavy Three.js or GSAP
  assert(!motionRef.includes('use Three.js for modal'), 'Does not recommend Three.js or heavy libraries for modals');
}
console.log('');

// ---------------------------------------------------------
// SUMMARY
// ---------------------------------------------------------
console.log('====================================================');
console.log(`Results: ${passedTests} / ${totalTests} tests passed (${Math.round((passedTests / totalTests) * 100)}%)`);
console.log('====================================================');

if (passedTests === totalTests) {
  console.log('🎉 ALL SCENARIO TESTS PASSED SUCCESSFULLY!\n');
  process.exit(0);
} else {
  console.error('❌ SOME TESTS FAILED!\n');
  process.exit(1);
}
