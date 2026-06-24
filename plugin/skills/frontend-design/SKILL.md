---
name: frontend-design
description: Impeccable frontend craft. Enforces the polish bar on any UI work so output never looks templated or default — deliberate type and spacing, real hierarchy, every component state, responsive behavior, restrained motion, and accessibility. Use whenever a task creates or changes a user interface (component, page, dashboard, form, email, layout, styling), even if the user didn't say "make it nice."
---

# Frontend Design

Craft, not brand. The job is to make UI that looks deliberately designed, not generated. (Brand specifics — palette, fonts, components — belong in a project-local brand skill, not here.)

Hold this bar on every UI task:

- **Type & rhythm** — a real type scale, consistent spacing units, generous and consistent whitespace. No arbitrary pixel values scattered around.
- **Hierarchy** — the eye should land where it should. Size, weight, color, and spacing earn attention deliberately; one clear primary action per view.
- **Every state** — design and implement hover, focus, active, disabled, loading, empty, and error — not just the happy populated state. Empty and error states are where most UIs feel cheap.
- **Responsive** — define behavior across breakpoints; don't let layouts break or overflow on small screens.
- **Motion** — restrained and purposeful; transitions that clarify, never decorate. Respect reduced-motion.
- **Accessibility** — sufficient contrast, visible focus rings, keyboard operability, semantic markup, labels and ARIA where needed, alt text. Non-negotiable (Ponytail never minimizes this away).
- **Consistency** — reuse tokens and components; match the patterns already in the codebase.

Before calling a UI task done: does it look intentional, work on mobile, handle empty/error, and pass keyboard + contrast? If not, it's not done.
