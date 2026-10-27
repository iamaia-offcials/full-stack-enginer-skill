# Workflow: Multi-Viewport Quality Assurance

Final verification protocol before releasing code to production.

## Verification Protocol

1. **Viewport Matrix Testing:**
   - Mobile: 360px & 390px (Check for horizontal scroll, input font >= 16px, touch targets >= 44px).
   - Tablet: 768px (Check grid collapse and drawer navigation).
   - Desktop: 1024px & 1440px (Check max container bounds and visual balance).
2. **Keyboard Operability Walk:**
   - Tab through all interactive elements; confirm logical reading order and visible focus rings.
3. **Form Resilience Check:**
   - Test empty submission, invalid email, oversized text input, and async in-flight state.
4. **Performance & Build Check:**
   - Confirm clean build without TypeScript errors, verify image aspect ratios, and test reduced motion.
