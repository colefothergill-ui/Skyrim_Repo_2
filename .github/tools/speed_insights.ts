/**
 * Vercel Speed Insights Integration Module
 * 
 * This module provides centralized exports for Vercel Speed Insights components
 * and utilities, making it easy to integrate performance monitoring across
 * different frameworks supported by @vercel/speed-insights.
 * 
 * Usage:
 * - Next.js: import { SpeedInsights } from '@vercel/speed-insights/next'
 * - React: import { SpeedInsights } from '@vercel/speed-insights/react'
 * - Remix: import { SpeedInsights } from '@vercel/speed-insights/remix'
 * - SvelteKit: import { injectSpeedInsights } from '@vercel/speed-insights/sveltekit'
 * - Vue/Nuxt: import { SpeedInsights } from '@vercel/speed-insights/vue'
 * - Astro: import SpeedInsights from '@vercel/speed-insights/astro'
 * - Generic: import { injectSpeedInsights } from '@vercel/speed-insights'
 */

// Re-export Next.js component for convenience
export { SpeedInsights } from "@vercel/speed-insights/next";

// Note: For other frameworks, import directly from @vercel/speed-insights
// using the appropriate subpath as shown in SPEED_INSIGHTS_GUIDE.md
