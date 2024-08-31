import './App.css';
import { useState } from 'react';

function App() {
  const [num1, setNum1] = useState("");
  const [num2, setNum2] = useState("");
  const [result, setResult] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  const handleSubmit = (event, operation) => {
    event.preventDefault();
    setIsLoading(true);
    setResult("");
    setErrorMsg("");
    const url = `https://simple-calculator-h60j.onrender.com/${operation}`;
    // const url = `http://127.0.0.1:8000/${operation}`; // gunicorn base:api
    // const url = `http://127.0.0.1:5000/${operation}`; // flask run
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: new URLSearchParams({
        "num1": num1,
        "num2": num2
      })
    }).then((response) => {
      setIsLoading(false);
      // encountered error
      if (!response.ok) {
        return response.json().then((err) => {
          throw new Error(err.error);
        });
      } else {
        return response.json();
      }
    }).then((data) => {
      setResult(data.data.answer);
      console.log(data.data.answer);
    }).catch((err) => {
      setErrorMsg(err.message);
    })
  };

  return (
    <div className="App">
      <form>
        First number:
        <input type="text" name="num1" value={num1} onChange={(e) => setNum1(e.target.value)} /><br />
        Second number:
        <input type="text" name="num2" value={num2} onChange={(e) => setNum2(e.target.value)} /><br />
        <button type="submit" name="operation" onClick={(e) => handleSubmit(e, "add")}>Add</button>
        <button type="submit" name="operation" onClick={(e) => handleSubmit(e, "subtract")}>Subtract</button>
      </form>
      {isLoading ? <p>Loading...</p> : <></>}
      {result || result === 0 ? <p>Result: {result}</p> : <></>}
      {errorMsg ? <p>Error: {errorMsg}</p> : <></>}
    </div>
  );
}

export default App;
