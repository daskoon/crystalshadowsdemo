# Plan: Client Feedback Refactoring (Crystal Shadows)

## Goal
Refactor `index.html` and `style.css` to address specific client feedback regarding visibility, layout, color palette, content, and typography. The aim is to achieve a "Less Ghostly" look, clear facial visibility in the hero section, a Teal-dominant title, and improved readability.

## Inputs
*   `index.html` (Current Site Structure)
*   `style.css` (Current Styles)
*   Client Feedback Points 1-5.

## Tasks

### 1. Visual & Layout Adjustments (`style.css`)
*   **Hero Overlay Visibility**:
    *   Locate `.hero-section`.
    *   Reduce the opacity of the `linear-gradient` overlay (currently `0.6`) to a lower value (e.g., `0.3` or `0.4`) to make the background photo brighter.
*   **Hero Text Placement**:
    *   Target `.hero-content`.
    *   Add significant `padding-top` or `margin-top` (approx. `30vh` or specific pixel value) to push text below the subject's "chin line".
    *   **Responsive Check**: Ensure media queries adjust this spacing for mobile so text remains readable and doesn't push important elements off-screen or overlap awkwardly.
*   **Color Palette Update**:
    *   Define a new CSS variable for Teal (e.g., `--accent-teal: #20B2AA;`).
    *   Update `h1` to use `--accent-teal` instead of `--accent-gold`.
    *   Review other gold usages. "Tone down" gold by thinning borders (`1px` to `0.5px` or similar) or removing gold color from secondary text where it feels "too harsh". Keep gold for subtle highlights only.
*   **Typography & Readability**:
    *   Increase global `body` font size (e.g., from default/16px to `18px` or `1.1rem`).
    *   Increase `font-weight` slightly for better contrast.
    *   **Fix Mobile Overlap**: Increase `line-height` for `h1` and `h2` (e.g., to `1.3` or `1.4`) to prevent lines crashing into each other on small screens.

### 2. Content Updates (`index.html`)
*   **Section Header**:
    *   Search for "Offerings & Investments".
    *   Replace with "Offerings & Rates".

### 3. Review & Verification
*   Verify the "Hero" text sits lower on the screen.
*   Confirm the "Crystal Shadows" title is Teal.
*   Check that "Investments" is removed.
*   Ensure text is larger and legible on both desktop and mobile widths.
*   Verify the booking widget still renders correctly at the bottom.

## Output
*   Updated `style.css`
*   Updated `index.html`
