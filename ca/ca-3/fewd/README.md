

## Problem Statement

A typed function documents itself — get its inputs or output wrong and TypeScript catches you the moment you call it. You're given five small store-helper functions with **no types and no bodies**. Add the correct types and logic so the automated specs pass and the file compiles cleanly.

## Tasks

Edit **only** `starter/src/functions.ts`:

1. `priceWithTax(price, rate = 0.08)` — type `price` as `number`; give `rate` a **default** value `0.08`; return `price + price * rate`; return `number`.
2. `label(name, prefix?)` — `name: string`; make `prefix` an **optional** `string` (`?`); return `"<prefix>: <name>"` with `"Item"` as the fallback; return `string`.
3. `isInStock(qty)` — `qty: number`, return `boolean`, `true` when `qty` is greater than `0`.
4. `format(value)` — `value` is a **union** `string | number`; **narrow** with `typeof`: for a number return `"#" + value`, otherwise return `value.toUpperCase()`; return `string`.
5. `total = (prices) => …` — a typed **arrow function**: param `prices: number[]`, return type `: number` before the `=>`, return the sum of the array (`0` for an empty array).

## Instructions

```bash
npm install
npm run test:serve        # runs vitest once (10 specs)
```


## Submission Guidelines

- Complete all five functions so `npm run test:serve t` reports **10/10 passing**.
- Submit your completed `src/functions.ts` (or the repository link) as directed on the platform.

## What the specs check

- **Behavior (7):** correct results for `priceWithTax` (default and explicit rate), `label` (with and without the optional prefix), `isInStock`, `format` (number and string branches), and `total` (including the empty array).
- **Types (3):** every parameter annotated; at least four explicit return types; one optional (`?`) and one default (`=`) parameter present.
