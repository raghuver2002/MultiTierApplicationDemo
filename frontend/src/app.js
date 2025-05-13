import React, { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://<PUBLIC-IP>:5000/")
      .then((res) => res.text())
      .then((data) => setMessage(data));
  }, []);

  return (
    <div>
      <h1>Frontend Connected to Backend</h1>
      <p>Backend says: {message}</p>
    </div>
  );
}

export default App;
