# Day 5 Notes — Issue Reproduction (OWASP ZAP)

## Issue Chosen
- Link: https://github.com/zaproxy/zaproxy/issues/9114
- Summary: Text hidden when switching Look and Feel in Site Details

## Expected Behavior
Text in the Site Details panel should remain fully visible after switching
the Look & Feel.

## Actual Behavior
Some text becomes hidden or clipped after changing the Look & Feel.

## Steps to Reproduce (Logical)
1. Open OWASP ZAP
2. Navigate to Site Details
3. Switch Look & Feel
4. Observe that some text is hidden

## Area Likely Involved
- UI components related to Site Details
- Swing layout code
- Files under src/main/java/org/zaproxy/zap/extension/

## Current Understanding
This appears to be a UI layout issue where components are not resizing
correctly after the Look & Feel change.
