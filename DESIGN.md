---
name: SCIL Machinery
description: Complete beverage packaging lines, preform to pallet, drawn as a 5S-marked factory floor seen from above.
colors:
  floor: "#cfd3cd"
  floor-deep: "#c1c6bf"
  seam: "rgba(20, 23, 22, 0.075)"
  plate: "#f4f5f1"
  plate-edge: "#d9dcd4"
  ink: "#141716"
  ink-2: "#353b38"
  ink-3: "#4f5652"
  tape: "#f4b400"
  tape-deep: "#d99f00"
  pet: "#1d58a6"
  pet-tint: "#c9d9ee"
  water: "#7fb0e6"
  done: "#11784a"
  done-tint: "#cfe5d6"
  stop: "#c3161c"
  asphalt: "#191c1b"
  asphalt-line: "rgba(244, 245, 241, 0.12)"
  on-asphalt: "#e9ebe6"
  on-asphalt-2: "#b4bab5"
typography:
  display:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(3.4rem, 8.2vw, 6rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: "0.002em"
  headline:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(2.6rem, 5.4vw, 4.6rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: "0.002em"
  title:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(1.9rem, 3.2vw, 2.75rem)"
    fontWeight: 800
    lineHeight: 0.95
  title-small:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(1.35rem, 1.9vw, 1.6rem)"
    fontWeight: 700
    lineHeight: 1
  stencil:
    fontFamily: "Big Shoulders Stencil, Big Shoulders, sans-serif"
    fontWeight: 800
    lineHeight: 0.85
  lede:
    fontFamily: "Overpass, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.125rem, 1.45vw, 1.3rem)"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Overpass, Segoe UI, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Overpass, Segoe UI, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 800
    letterSpacing: "0.06em"
  data:
    fontFamily: "Overpass Mono, ui-monospace, Cascadia Mono, monospace"
    fontSize: "0.75rem"
    fontWeight: 600
    letterSpacing: "-0.01em"
    fontFeature: "tnum"
rounded:
  none: "0px"
spacing:
  gutter: "clamp(16px, 3.2vw, 48px)"
  section: "clamp(88px, 11vw, 168px)"
  section-tight: "clamp(64px, 8vw, 112px)"
  grid-gap: "24px"
  card-gap: "22px"
  slab: "240px"
  tape: "12px"
  max: "1440px"
components:
  button-primary:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.25em 0.75em"
    height: "52px"
  button-primary-hover:
    backgroundColor: "{colors.tape-deep}"
    textColor: "{colors.ink}"
  button-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.plate}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.25em 0.75em"
    height: "52px"
  button-plate:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.25em 0.75em"
    height: "52px"
  button-small:
    padding: "0.6em 0.95em 0.5em"
    height: "42px"
  zone-sign:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "9px 12px 6px"
  zone-sign-active:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.ink}"
  equipment-plate:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "10px 12px 14px"
  figure-plate:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.plate}"
    typography: "{typography.data}"
    rounded: "{rounded.none}"
    padding: "4px 8px 2px"
  finished-goods-zone:
    backgroundColor: "{colors.done}"
    textColor: "{colors.plate}"
    rounded: "{rounded.none}"
    padding: "16px"
  input-field:
    backgroundColor: "#ffffff"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "12px 12px 10px"
    height: "50px"
  chip:
    backgroundColor: "#ffffff"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "9px 14px 7px"
  chip-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.tape}"
  loading-zone:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
---

# Design System: SCIL Machinery

## Overview

**Creative North Star: "Factory Floor Markings"**

The site is a bottling plant seen from above. The ground is sealed, cool-grey epoxy laid on a 240px tile module with faint seam lines and a fine grain; everything that sits on it is painted, taped or stencilled the way a 5S-disciplined floor is. A yellow lane runs through the work, equipment stands inside white L-cornered footprints, numbers are sprayed through stencils, and the navigation hangs from the gantry as zone signs. Nothing is decoration: every mark is a floor-code mark, and the floor code decides what colour a thing may be.

Density is that of a working floor: big, blunt signage headlines in condensed uppercase, plain Overpass text at a comfortable reading measure, and figures set in Overpass Mono on small ink plates like stamped data tags. Surfaces are square-cornered sheet plates with a thin edge lip and a soft fall-off shadow, never rounded cards. The dark "asphalt" ground is the second floor, used for the service shift and the footer, keeping the same tile grid in light seams.

Motion is mechanical and purposeful: the lane draws itself in, equipment plates settle onto their footprints, a container token travels the lane and changes state at each station, gauges fill once. All of it collapses under reduced motion.

**Key Characteristics:**
- Colour is law: hue is assigned by the 5S floor code, never by taste.
- Square corners everywhere; the only radii are physical details (a punched hole, a badge slot).
- Condensed uppercase signage for headings, Overpass for reading, Overpass Mono for figures.
- Depth is a sheet plate lying on the floor: edge lip plus soft fall-off, nothing floats.
- The lane (12px tape) is the recurring structural device: hero plan, walk-the-line rail, return-customer path, mobile menu and footer edges.

## Colors

A cool concrete neutral field carrying a strict, coded set of safety hues.

### Primary
- **Floor Tape Yellow** (tape): the route. Reserved for the lane and its derivatives (progress fills, past-station segments, the selector underline), primary CTA plates, the active zone sign, the enquiry loading zone, the focus halo and text selection. Its deeper press (tape-deep) is the primary plate's hover and the link-hover underline.

### Secondary
- **Finished-Goods Green** (done): output and results. The finished-goods zone at the end of the lane, the running-output bar in the proof gauge, testimonial tag bands, checklist ticks and the form's sent confirmation (done-tint background).
- **PET Blue** (pet) with **Preform Tint** (pet-tint) and **Water Blue** (water): raw material. Used inside the container-token drawings for preforms, caps, label print and water fill.

### Tertiary
- **Stop Red** (stop): stop and breakdown only. The breakdown step in the service loop and invalid form fields.

### Neutral
- **Sealed Epoxy Floor** (floor, with floor-deep for scroll tracks): the page ground, tiled at the slab module with seam lines.
- **Equipment Plate** (plate, edged by plate-edge): the white of footprints and sheet plates, secondary sign buttons, zone signs, and light text on dark grounds.
- **Stencil Ink** (ink, ink-2, ink-3): headings and borders in ink; body copy in ink-2; meta, captions and placeholders' neighbours in ink-3.
- **Asphalt** (asphalt, asphalt-line, on-asphalt, on-asphalt-2): the dark floor for the service shift and footer, with light seam lines and two light text levels.

### Named Rules
**The Colour Is Law Rule.** Every hue has one floor-code meaning: yellow = route and primary action, white = equipment footprint, blue = raw material, green = finished goods and results, red = stop or breakdown, black = stencil ink. A hue never appears outside its meaning.

**The Red Means Stop Rule.** Stop Red is never used for emphasis, sale, urgency or brand. If nothing has stopped or failed, there is no red on the screen.

**The One Lane Rule.** Yellow is a lane or a plate, not a highlighter on arbitrary content. When yellow appears it either marks the route, the primary action, the active location or the loading zone.

## Typography

**Display Font:** Big Shoulders (with Arial Narrow), plus Big Shoulders Stencil for numbers
**Body Font:** Overpass (with Segoe UI, system-ui)
**Label/Mono Font:** Overpass Mono (with ui-monospace, Cascadia Mono)

**Character:** Big Shoulders is signage: condensed, heavy, uppercase, set tight like painted zone lettering. Overpass, itself derived from highway signage, carries reading text plainly; Overpass Mono stamps the numbers.

### Hierarchy
- **Display** (800, clamp(3.4rem, 8.2vw, 6rem), 0.9, uppercase): page and hero headlines. The home hero tightens to clamp(3.4rem, 7.4vw, 6rem) at 0.86 line-height.
- **Headline** (800, clamp(2.6rem, 5.4vw, 4.6rem), 0.9, uppercase): section heads.
- **Title** (800, clamp(1.9rem, 3.2vw, 2.75rem), 0.95, uppercase): sub-section and block heads; station and card names run 1.5–2rem at line-height 1.
- **Title Small** (700, clamp(1.35rem, 1.9vw, 1.6rem), 1, uppercase): zone labels and small sign heads.
- **Stencil** (Big Shoulders Stencil 800, 0.85): station numbers 01–06, step numerals, Q-numbers, return-customer years as display numerals.
- **Lede** (400, clamp(1.125rem, 1.45vw, 1.3rem), 1.5, ink-2, max 46ch): the sentence under a headline.
- **Body** (400, 1.0625rem, 1.6): reading text; prose blocks max 68ch in ink-2, strong in ink.
- **Label** (800, 0.8125–0.9375rem, 0.05–0.06em, uppercase, Overpass): button text, zone signs, form labels, text links with arrows, table heads.
- **Data** (Overpass Mono 400–600, 0.6875–0.875rem, tabular numerals): BPH figures, spec values, phone numbers, years, gauge ticks, prices' units.

### Named Rules
**The Mono Means Measured Rule.** Overpass Mono sets figures and data only: outputs, specs, phone numbers, years, counts. It is not a label or caption voice.

**The Signage Is Uppercase Rule.** Big Shoulders is always uppercase and heavy (700–800). Overpass is never set as a display face.

## Layout

The page is a 1440px max container with a fluid gutter (clamp(16px, 3.2vw, 48px)). Composition runs on a 12-column grid with 24px column gaps; heads typically split 7 / 5 (heading left, lede right), detail pages split 7 / 5 media / info with sticky media. Card grids use auto-fill tracks (210–290px minimums) with 22px gaps. Sections breathe at clamp(88px, 11vw, 168px) vertical padding, tight sections at clamp(64px, 8vw, 112px).

The floor tile module (240px) sizes the seam grid behind everything, on both the epoxy and asphalt grounds. The 12px tape width is a layout unit: lanes, progress rails and dark-panel edges all use it.

Responsive behaviour: the hero floor plan keeps a 1180px minimum and becomes a horizontal snap-scroller with a hint below 1100px; the walk-the-line sticky rail becomes a sticky progress strip below 960px; machine rows turn into horizontal snap carousels below 700px; 12-column splits collapse to a single column at 900px; the nav collapses to a menu at 960px.

## Elevation & Depth

Depth is physical and shallow: a plate lies on the floor. Surfaces sit flat on the epoxy with a thin vertical edge lip and a soft, pulled-in fall-off below. Sticky bars use a translucent floor tint with backdrop blur. Hover lifts a plate a few pixels and lengthens its fall-off; press pushes a button plate down onto the floor.

### Shadow Vocabulary
- **Plate rest** (`box-shadow: 0 2px 0 rgba(20,23,22,.1), 0 12px 16px -12px rgba(20,23,22,.4)`): equipment plates, testimonial tags, team badges.
- **Plate lifted** (`box-shadow: 0 2px 0 rgba(20,23,22,.1), 0 18px 20px -12px rgba(20,23,22,.45)`): hovered equipment plate, with translateY(-3 to -4px).
- **Sign plate** (`box-shadow: 0 2px 0 rgba(20,23,22,.35), 0 10px 18px -12px rgba(20,23,22,.55)`): buttons at rest; pressed collapses to `0 0 0 rgba(20,23,22,.35), 0 4px 10px -8px rgba(20,23,22,.5)` with translateY(2px).
- **Hanging sign** (`box-shadow: 0 6px 8px -6px rgba(20,23,22,.45)`): zone signs in the nav.

### Named Rules
**The Lying-Flat Rule.** Shadows describe a sheet resting on the floor: a vertical lip of at most a few pixels plus a soft blurred fall-off. No sideways offsets, no solid ink drop shadows, no floating glows.

## Shapes

Square-cornered everywhere (0px radius) on buttons, plates, inputs, chips, tables and panels; the only radii are literal objects: the punched hole in a testimonial tag and the lanyard slot on a team badge. Borders are 2px ink on interactive plates and inputs, 3px ink for heavy rules (legend band, vision columns), 1px translucent ink for dividers. Equipment footprints are drawn with four L-shaped corner tapes (24px arms, 6px thick) in plate white, in yellow for route items, or in ink. Hazard edges (ink and yellow 46px stripes, 18px tall) bound the enquiry loading zone. Dashed lines mean loops and empty bays: an 8px dashed plate line for the service loop, a 3px dashed ink border for an empty catalogue bay. Icons are 24px-grid strokes at 2px with square caps and mitred joins.

## Components

### Buttons
Floor-sign plates: square, ink-edged, uppercase, sitting on the floor.
- **Shape:** square corners (0px), 2px ink border, 52px minimum height (42px small).
- **Primary:** Floor Tape Yellow plate with ink label, 800 weight 0.9375rem uppercase at 0.06em, padding 0.85em 1.25em 0.75em, icon gap 0.7em.
- **Hover / Focus:** hover deepens to tape-deep and nudges the trailing arrow 4px right; press drops the plate 2px and flattens its shadow; focus is a 3px ink outline offset 3px with a 6px yellow halo.
- **Ink plate:** ink with plate-white text, hover #2b302e. **Plate:** equipment white with ink text, hover pure white, for secondary actions such as WhatsApp.
- **Text link with arrow:** uppercase 800 label, 2px ink underline at 6px offset; hover swaps to a 4px yellow underline.

### Chips
- **Style:** white field, 2px ink-3 border, square, 600 weight 0.9375rem, padding 9px 14px 7px; used as product radio choices in the enquiry form.
- **State:** hover inks the border; selected is an ink plate with yellow text; keyboard focus adds the yellow 4px halo.

### Cards / Containers
- **Corner Style:** square (0px).
- **Background:** equipment plate white on the epoxy floor, framed by footprint corner tapes.
- **Shadow Strategy:** plate rest, plate lifted on hover (see Elevation & Depth).
- **Border:** none on plates; the footprint corners do the framing.
- **Internal Padding:** 10–14px; the footprint frame sits 12px outside the plate. A figure plate (ink tag with Overpass Mono output, e.g. "to 22,000 BPH") pins to each machine card.

### Inputs / Fields
- **Style:** white field, 2px ink-3 border, square, 50px min height, padding 12px 12px 10px, blue caret; uppercase 800 labels at 0.8125rem.
- **Focus:** border goes to ink with a 4px yellow halo, no outline.
- **Error / Disabled:** invalid fields take a Stop Red border and a bold red message; disabled buttons drop to 50% opacity.

### Navigation
Hanging zone signs on a gantry. The header is sticky with a 6px ink top beam and a translucent blurred floor tint. Each nav item is a plate-white sign with a 2px ink border, hung from the beam by two short ink drop-rods; hover swings it 1.5deg on a pivot above the sign and whitens it; the current page's sign is yellow. Below 960px a square ink menu button opens a full-width asphalt panel with large Big Shoulders entries, a yellow current item and a 12px yellow tape edge.

### Floor Plan and Lane (signature)
A full-width top-down plan: a 12px yellow lane with a thinner edge lane and faint chevrons runs left to right through six numbered equipment footprints (stencil 01–06, machine photo, name, figure plate) and ends in a solid green finished-goods zone. On load the lane draws itself in (scaleX over 1.6s) and plates settle onto their footprints in a staggered sequence.

### Walk the Line (signature)
A sticky rail on the left carries a 12px lane that fills with scroll, numbered tick squares that ink in as stations pass, and a container token that travels down the rail changing state: preform, bottle, filled, labelled, pack, pallet. Station numbers on the right are outlined stencils that fill yellow when active.

### Loading Zone (enquiry)
A full-bleed yellow band bounded top and bottom by ink-and-yellow hazard stripes, holding the enquiry form as an ink-bordered white plate.

## Do's and Don'ts

### Do:
- **Do** assign every colour by the floor code: yellow for route and primary action, white for equipment footprints, blue for raw material, green for finished goods and results, red only for stop or breakdown, ink for stencil.
- **Do** frame equipment as a white plate inside four L-shaped corner tapes (24px arms, 6px thick).
- **Do** set figures (BPH, specs, phone numbers, years, counts) in Overpass Mono with tabular numerals, usually on a small ink plate.
- **Do** keep every corner square (0px) and every interactive plate edged in 2px ink.
- **Do** use the 12px yellow lane as the connective device between steps, stations and sequences.
- **Do** use the yellow halo (4–6px) plus ink outline for focus, and honour prefers-reduced-motion for every draw-in, settle, swing and fill.

### Don't:
- **Don't** use red for anything except stop, breakdown or error.
- **Don't** use yellow as a decorative accent or background tint outside the lane, primary plates, active state and loading zone.
- **Don't** set labels, captions or words in Overpass Mono; mono is for measured values.
- **Don't** round corners, add sideways or solid ink drop shadows, or float plates with glows.
- **Don't** put small uppercase eyebrow or kicker labels above headlines; the headline is the sign.
- **Don't** use unicode glyphs as icons; icons are 2px square-capped strokes on a 24px grid.
