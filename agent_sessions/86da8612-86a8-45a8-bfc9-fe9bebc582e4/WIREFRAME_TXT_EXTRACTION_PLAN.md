# Wireframe & TXT Export Extraction Plan

**Date**: 2025-11-30  
**Purpose**: Extract full wireframe details and TXT exports from all hierarchical projects  
**Status**: Partial - need complete extraction

---

## Requirements

For each of the 3 hierarchical projects, we need:

1. ✅ **Sitemap** (structure) - DONE via DOM
2. ⏳ **Wireframe** (detailed copy/specs) - PARTIAL
3. ⏳ **TXT Export** (official Relume export) - NOT DONE

---

## What We've Captured So Far

### MezTal Information Architecture
- ✅ Sitemap: Complete (~27 pages)
- ⏳ Wireframe: Partial extraction showing detailed specs
- ❌ TXT Export: Not captured yet

**Partial Wireframe Content Captured:**
The browser subagent extracted initial wireframe content showing:
- Detailed Hero section specs: "Fix Your Margins. Scale Your Care."
- Interactive Talent Search filter
- 3-step process visuals
- City-specific content (Guadalajara, CDMX, Monterrey, Colima)
- Immersion Trips agenda details

### MezTa 8
- ✅ Sitemap: Complete (~30-35 pages)
- ⏳ Wireframe: Browser saw "WORLD STAFFING SOLUTIONS" and verbatim testimonials in DOM
- ❌ TXT Export: Not captured yet

**Key Finding:** The DOM showed detailed content that suggests this was generated from our documented prompts!

### MezTal 5
- ✅ Sitemap: Complete (~25-30 pages)
- ❌ Wireframe: Extraction timed out
- ❌ TXT Export: Not captured yet

---

## Next Steps - Manual Extraction Needed

Since browser automation hit tool call limits, I recommend **manual extraction** by you:

### For Each Project (MezTal IA, MezTa 8, MezTal 5):

1. Open project in Relume
2. Click "Export" button (top right)
3. Select "Copy Text" in the export modal
4. Paste the full TXT export here in chat
5. Label each with project name

This will give us:
- Complete wireframe specifications
- Exact component copy
- All page details
- Comparison with documented prompts

---

## What We'll Compare

Once we have all TXT exports:

### 1. Content Match Analysis
- Which project uses "Fix Your Margins. Scale Your Care."?
- Which has "Staffing like you've never seen"?
- Which has "We manage the messy stuff. You get world-class talent."?
- Which mentions "YOURSOURCED" model?

### 2. Testimonial Verification
- Scott testimonial (Atlas Senior Living)
- Isaac testimonial (Anthem)
- Any verbatim quotes we documented

### 3. Industry/Solution Coverage
- Which has all 8 industries?
- Which has all Solutions we specified?
- Which includes geographic depth (Why Guadalajara)?

### 4. Prompt Alignment
Compare against:
- `MEZTAL_RELUME_PROMPT_FINAL.md`
- `MezTal copy_1.csv` (20 "Ogilvy" pages)
- `novel_meztal_insights.md`

---

## Expected Outcome

**Hypothesis:** One of these projects (likely **MezTa 8** or **MezTal IA**) was generated using the documented prompts and content.

**Evidence so far:**
- MezTa 8 DOM showed "WORLD STAFFING SOLUTIONS" (not in other projects)
- MezTal IA has most complete structure matching our specifications
- MezTal 5 has verified 16/20 "Ogilvy" content match

---

## Alternative: Automated TXT Export

If you'd prefer automated extraction, I can try:

**Option A:** Use browser automation to:
1. Click each project
2. Click "Export" button
3. Click "Copy Text"
4. Read clipboard content
5. Save to file

**Option B:** Direct API call to Relume (if API access available)

**Recommendation:** Manual paste is fastest and most reliable at this point.

---

## Ready When You Are

Please paste the TXT exports from:
1. MezTal Information Architecture
2. MezTa 8
3. MezTal 5

And I'll create a comprehensive comparison showing which matches our documented content!
