import ProductCard, { Greet }from './call.jsx'
import { useState } from "react";

function App() {
  const [count, setCount] = useState(true);
  function handleSubmit(){
    setCount(!count)
  }
  return (
    <div>
      <h1>Hi, Harsshwadhan</h1>
      <ProductCard title="Wireless Headphones" price={99} />
      <ProductCard title="Mechanical Keyboard" price={149} />
      <ProductCard title="Ergonomic Mouse" price={45} />
      <Greet name="Harsshwardhan Chowdhary" squad={168} />
      <Greet name="Naman" squad={169} />

       <h1>{count}</h1>
      {count && <h1>Sorry</h1>}
      <button onClick={handleSubmit}>{count ? "remove" : "show"}</button>
    </div>
  )
}
/**
 * Hooks - To use React feature we have to use hooks
 * 1.  useState - when state change then react tirgger re-render.
 * 2 . useState return a array of two values
 * 3. first refers a current value second value is for update the state.
 */
export default App
