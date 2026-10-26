function ProductCard({ title, price }) {
  return <h1>{title} is at price {price}</h1>
}

export function Greet({ name, squad }) {
  return <h2>{name} is from squad {squad}</h2>
}

export default ProductCard