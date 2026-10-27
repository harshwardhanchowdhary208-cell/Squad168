import ProductCard, { Greet } from "./call.jsx";
import { useState } from "react";

function App() {
  const [showMessage, setShowMessage] = useState(true);
  const [count, setCount] = useState(0);
  const [message, setMessage] = useState("");

  function handleToggle() {
    setShowMessage((prev) => !prev);
  }

  function handleIncrement() {
    if ((count+1)%5!=0){
      setCount((prev) => prev + 1);
      setMessage("");
    } else {
      setCount((prev) => prev + 2);
      setMessage("Skipped multiple of 5");
    }
  }

  function handleDecrement() {
    if ((count-1)%5!=0){
      setCount((prev) => prev - 1);
      setMessage("");
    } else {
      setCount((prev) => prev - 2);
      setMessage("Skipped multiple of 5");
    }
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
      {message && <p role="status">{message}</p>}
      {showMessage && <h1>Sorry</h1>}
      <button onClick={handleToggle}>{showMessage ? "Remove" : "Show"}</button>
      <button onClick={handleIncrement}>Increment</button>
      <button onClick={handleDecrement}>Decrement</button>
    </div>
  );
}
/**
 * Hooks - To use React feature we have to use hooks
 * 1.  useState - when state change then react tirgger re-render.
 * 2 . useState return a array of two values
 * 3. first refers a current value second value is for update the state.
 */
export default App;