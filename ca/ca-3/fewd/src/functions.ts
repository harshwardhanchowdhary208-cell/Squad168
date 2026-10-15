// Typed Store Kit — STARTER
// Right now these functions have NO types and NO bodies, so every spec is red.
// Your job: add the types AND the logic described in each TODO, then run `npm test`.

// Explanation: Both inputs and the output are numbers; the default rate applies 8% tax when omitted.
export function priceWithTax(price:number, rate:number=0.08):number {
  // TODO 1: type `price` as `number`. Give `rate` a DEFAULT value of 0.08 (a number).
  //         Return price plus price * rate. The return type is `number`.
  return price + price * rate;
}

// Explanation: The prefix is optional; use "Item" as a fallback to keep labels consistent.
export function label(name:string, prefix?:string):string {
  return `${prefix ?? "Item"}: ${name}`
  // TODO 2: type `name` as `string`. Make `prefix` an OPTIONAL string (use `?`).
  //         Return "<prefix>: <name>", but fall back to "Item" when prefix is
  //         left out. The return type is `string`.
}

// Explanation: An item is in stock only when its quantity is greater than zero.
export function isInStock(qty:number):boolean {
  return qty>0
  // TODO 3: type `qty` as `number`, give the function a `boolean` return type,
  //         and return true when qty is greater than 0.
}

// Explanation: Narrow the union with typeof so numbers and strings can be formatted differently.
export function format(value:string | number):string {
if( typeof value === "number"){
  return "#" + value
}else{  
return value.toUpperCase()
}

  // TODO 4: type `value` as the UNION `string | number`. NARROW with typeof:
  //         if it is a number return "#" + value, otherwise return
  //         value.toUpperCase(). The return type is `string`.
}

// Explanation: A loop adds each price to the total; starting at 0 handles an empty list correctly.
export const total = (prices: number[]): number => {
  let sum = 0;
  for (const price of prices) {
    sum += price;
  }
  return sum;
  // TODO 5: type the parameter `prices` as `number[]` and the arrow's return as
  //         `number` (the return type goes right before the =>); return the sum
  //         of the array (0 for an empty array).
};
