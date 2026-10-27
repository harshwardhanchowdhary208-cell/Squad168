import ProductCard, { Greet } from "./call.jsx";
import { useState } from "react";

function App() {
  const [showMessage, setShowMessage] = useState(true);
  const [count, setCount] = useState(0);
  const [message, setMessage] = useState("");
  const [text, setText] = useState("");


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
  function handleChange(e) {
    setText(e.target.value);
  
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
      <input type="text" value={text} onChange={handleChange}/>
      <h1>{text}</h1>
      {message && <p>{message}</p>}
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
 * Props
  Props in react are used to pass data in component to another component
  Immutable
  <Greet name="Rohit" age={20}/> we can only pass string directly in props else we have to pass in {}
  Attribute
  React is a just a libary not a full framework which can only be used for frontend not backend.
  Component Reusability	Applications are split into small, isolated, and reusable blocks of code. This speeds up development times and makes the codebase easier to maintain.
  High Performance (Virtual DOM)	Instead of updating the browser's slow Real DOM directly, React updates a lightweight "Virtual DOM". It only re-renders the exact elements that changed, ensuring fast user experiences.
  Stable One-Way Data Flow	Data flows strictly from parent components down to child components. This downward data binding ensures that modifying child elements won't accidentally break parent data, making the system predictable and easy to debug.
  SEO Friendliness	Traditional JavaScript apps often face search engine indexing hurdles. Through Server-Side Rendering (SSR) tools like Next.js, React apps can execute on the server and deliver standard HTML to web crawlers.
  React Native for Mobile	Learning React serves as a double investment. The exact same core architectural concepts can be used to build native iOS and Android apps using React Native.
  Vast Ecosystem & Community	Backed by a massive developer network, you gain immediate access to endless third-party packages, custom developer tools, browser extensions, and comprehensive troubleshooting resources.
  In React, rendering is the process where React calls your component function to figure out what the UI should look like based on the current state and props. It is essentially React "thinking" or taking a snapshot of the UI before making any physical changes to the screen
 */
export default App;