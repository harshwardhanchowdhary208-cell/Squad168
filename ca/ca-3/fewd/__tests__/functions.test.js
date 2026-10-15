import { describe, it, expect } from 'vitest'
import { readFileSync } from 'node:fs'
import { priceWithTax, label, isInStock, format, total } from '../src/functions.ts'

// Read the TypeScript source as text so we can confirm the type annotations are
// actually written (types are erased at runtime). Done lazily, inside the tests,
// and tolerant of the working directory, so it can never crash test collection.
function readSource() {
  const candidates = [
    'src/functions.ts',
    '../src/functions.ts',
    './src/functions.ts',
    'functions.ts',
  ]
  for (const p of candidates) {
    try {
      return readFileSync(p, 'utf8')
    } catch {
      /* try the next candidate */
    }
  }
  return ''
}

describe('Typed Store Kit — behavior', () => {
  it('priceWithTax() uses the default rate of 0.08 when none is given (default parameter)', () => {
    expect(priceWithTax(100)).toBeCloseTo(108)
    expect(priceWithTax(0)).toBeCloseTo(0)
  })

  it('priceWithTax() uses the rate you pass in', () => {
    expect(priceWithTax(200, 0.25)).toBeCloseTo(250)
  })

  it('label() uses "Item" when the prefix is left out (optional parameter)', () => {
    expect(label('Pen')).toBe('Item: Pen')
  })

  it('label() uses the prefix you pass in', () => {
    expect(label('Pen', 'Sale')).toBe('Sale: Pen')
  })

  it('isInStock() returns a boolean', () => {
    expect(isInStock(3)).toBe(true)
    expect(isInStock(0)).toBe(false)
  })

  it('format() narrows a string | number union with typeof', () => {
    expect(format(42)).toBe('#42')
    expect(format('abc')).toBe('ABC')
  })

  it('total() (arrow function) sums the array, 0 when empty', () => {
    expect(total([10, 20, 30])).toBe(60)
    expect(total([])).toBe(0)
  })
})

describe('Typed Store Kit — types', () => {
  it('every function parameter is annotated with a type', () => {
    const src = readSource()
    expect(src).toMatch(/price\s*:\s*number/)
    expect(src).toMatch(/rate\s*:\s*number/)
    expect(src).toMatch(/name\s*:\s*string/)
    expect(src).toMatch(/qty\s*:\s*number/)
    expect(src).toMatch(/value\s*:\s*string\s*\|\s*number/)
    expect(src).toMatch(/prices\s*:\s*number\s*\[\s*\]/)
  })

  it('declares an explicit return type on at least four functions', () => {
    const src = readSource()
    const returns = src.match(/\)\s*:\s*(number|string|boolean)/g) || []
    expect(returns.length).toBeGreaterThanOrEqual(4)
  })

  it('uses one optional parameter (?) and one default parameter (=)', () => {
    const src = readSource()
    expect(src).toMatch(/prefix\s*\?\s*:/)                   // optional param
    expect(src).toMatch(/rate\s*:\s*number\s*=\s*0?\.0?8/)   // default value 0.08
  })
})
